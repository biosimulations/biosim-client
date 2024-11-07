from typing import Optional, get_args

import biosim_client.simdata_api as simdata_client
from biosim_client.dataset import AttributeValueTypes, Dataset
from biosim_client.simdata_api import Configuration, DatasetData, HDF5Attribute, HDF5Dataset, HDF5File

attribute_value_types = get_args(AttributeValueTypes)


class SimData:
    configuration: Configuration
    run_id: str
    hdf5_file: HDF5File
    datasets: dict[str, Dataset]

    def __init__(self, configuration: Configuration, run_id: str, hdf5_file: HDF5File):
        self.configuration = configuration
        self.run_id = run_id
        self.hdf5_file = hdf5_file
        self.datasets = {}

    def dataset_names(self) -> list[str]:
        return [dataset.name for group in self.hdf5_file.groups for dataset in group.datasets]

    def dataset_uris(self) -> list[str]:
        return [
            attr.to_dict()["value"]
            for group in self.hdf5_file.groups
            for dataset in group.datasets
            for attr in dataset.attributes
            if attr.to_dict()["key"] == "uri"
        ]

    def get_dataset(self, name: str) -> Dataset:
        if name in self.datasets:
            # print("cache hit, returning cached dataset")
            return self.datasets[name]

        dataset_uri = None
        hdf5_dataset: Optional[HDF5Dataset] = None
        hdf5_attribute: HDF5Attribute
        for hdf5_group in self.hdf5_file.groups:
            for hdf5_dataset in hdf5_group.datasets:
                if hdf5_dataset.name == name:
                    for hdf5_attribute in hdf5_dataset.attributes:
                        if hdf5_attribute.to_dict()["key"] == "uri":
                            dataset_uri = hdf5_attribute.to_dict()["value"]
                    break

        if dataset_uri is None:
            raise ValueError(f"Dataset '{name}' not found")
        if hdf5_dataset is None:
            raise ValueError(f"Dataset '{name}' not found")

        with simdata_client.api_client.ApiClient(self.configuration) as api_client:
            api_instance = simdata_client.DefaultApi(api_client)
            dataset_data: DatasetData = api_instance.read_dataset(run_id=self.run_id, dataset_name=dataset_uri)
            dataset = Dataset.from_api(data=dataset_data, hdf5_dataset=hdf5_dataset)
            self.datasets[name] = dataset
            return dataset

    def __str__(self) -> str:
        return f"SimResults(run_id='{self.run_id}', dataset_names={self.dataset_names()})"
