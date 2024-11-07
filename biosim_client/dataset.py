from typing import Any, Optional

import numpy as np
import pandas as pd

from biosim_client.simdata_api.models.dataset_data import DatasetData
from biosim_client.simdata_api.models.hdf5_dataset import HDF5Dataset

AttributeValueTypes = list[bool] | list[float] | list[int] | list[str] | bool | float | int | str
DatasetValueTypes = float | int


class Dataset:
    shape: list[int]
    values: list[DatasetValueTypes]
    column_names: Optional[list[str]]
    attributes: Optional[dict[str, Any]]

    def __init__(
        self,
        values: list[DatasetValueTypes],
        shape: Optional[list[int]] = None,
        column_names: Optional[list[str]] = None,
        attributes: Optional[dict[str, Any]] = None,
    ):
        if shape is None:
            shape = [len(values)]
        if attributes is None:
            attributes = {}
        self.values = values
        self.shape = shape
        self.column_names = column_names
        self.attributes = attributes

    def to_numpy(self) -> np.ndarray:
        # print(f"in to_numpy(), len(self.values)={len(self.values)}, self.shape={self.shape}")
        return np.array(self.values).reshape(self.shape)

    def to_pandas(self) -> pd.DataFrame:
        dataframe = pd.DataFrame(self.to_numpy().transpose())
        if self.column_names is not None:
            dataframe.columns = self.column_names  # type: ignore
        return dataframe

    @classmethod
    def from_api(cls, data: DatasetData, hdf5_dataset: HDF5Dataset) -> "Dataset":
        values = data.to_dict()["values"]
        shape = hdf5_dataset.shape

        attributes: dict[str, Any] = {}
        column_names: Optional[list[str]] = None
        for attr in hdf5_dataset.attributes:
            attr_dict = attr.to_dict()
            if attr_dict["key"] == "sedmlDataSetLabels":
                column_names = attr_dict["value"]
            attributes[attr_dict["key"]] = attr_dict["value"]

        return Dataset(values=values, shape=shape, column_names=column_names, attributes=attributes)
