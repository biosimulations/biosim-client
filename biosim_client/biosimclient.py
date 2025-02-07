from datetime import datetime, timedelta
from time import sleep

import numpy as np
from pydantic import BaseModel

from biosim_client.api.biosim.api.default_api import DefaultApi as BiosimDefaultApi
from biosim_client.api.biosim.api.verification_api import VerificationApi
from biosim_client.api.biosim.api_client import ApiClient as BiosimApiClient
from biosim_client.api.biosim.api_response import ApiResponse
from biosim_client.api.biosim.configuration import Configuration as BiosimConfiguration
from biosim_client.api.biosim.models.comparison_statistics import ComparisonStatistics
from biosim_client.api.biosim.models.hdf5_attribute import HDF5Attribute as BiosimHDF5Attribute
from biosim_client.api.biosim.models.hdf5_file import HDF5File as BiosimHDF5File
from biosim_client.api.biosim.models.runs_verify_workflow_output import RunsVerifyWorkflowOutput
from biosim_client.api.biosim.models.runs_verify_workflow_status import RunsVerifyWorkflowStatus
from biosim_client.api.biosim.models.simulation_run_info import SimulationRunInfo
from biosim_client.api.simdata.api.default_api import DefaultApi as SimdataDefaultApi
from biosim_client.api.simdata.api_client import ApiClient as SimdataApiClient
from biosim_client.api.simdata.configuration import Configuration as SimdataConfiguration
from biosim_client.api.simdata.models.hdf5_attribute import HDF5Attribute as SimDataHDF5Attribute
from biosim_client.api.simdata.models.hdf5_file import HDF5File as SimDataHDF5File
from biosim_client.sim_data import SimData

simdata_configuration = SimdataConfiguration(host="https://simdata.api.biosimulations.org")
biosim_configuration = BiosimConfiguration(host="https://biosim.biosimulations.org")

type NDArray3D = np.ndarray[tuple[int, int, int], np.dtype[np.float64]]


class DatasetComparison:
    dataset_name: str
    var_names: list[str]
    run_ids: list[str]
    dataset_score: NDArray3D  # shape=(len(var_names), len(run_ids), len(run_ids))

    def __init__(
        self, dataset_name: str, var_names: list[str], run_ids: list[str], stats_list: list[list[ComparisonStatistics]]
    ) -> None:
        self.dataset_name = dataset_name
        self.var_names = var_names
        self.run_ids = run_ids
        self.dataset_score = self.parse_stats(stats_list=stats_list)

    def parse_stats(self, stats_list: list[list[ComparisonStatistics]]) -> NDArray3D:
        shape: tuple[int, int, int] = (len(self.var_names), len(self.run_ids), len(self.run_ids))
        array: NDArray3D = np.full(dtype=np.float64, shape=shape, fill_value=np.inf)
        for i in range(len(self.run_ids)):
            for j in range(len(self.run_ids)):
                stats: ComparisonStatistics = stats_list[i][j]
                if stats is not None and stats.score is not None:
                    array[:, i, j] = [float(score) for score in stats.score]
        return array

    def __str__(self) -> str:
        return f"DatasetComparison(dataset_name={self.dataset_name}, var_names={self.var_names}, run_ids={self.run_ids}, score={self.dataset_score})"


class VerifyResults(BaseModel):
    run_ids: list[str]
    run_verify_results: RunsVerifyWorkflowOutput

    def _update(self) -> None:
        with BiosimApiClient(biosim_configuration) as biosim_api_client:
            api_instance = VerificationApi(biosim_api_client)
            response: ApiResponse[RunsVerifyWorkflowOutput] = api_instance.get_verify_runs_with_http_info(
                workflow_id=self.run_verify_results.workflow_id
            )
            if response.status_code == 200:
                self.run_verify_results = response.data
            else:
                raise ValueError(f"Failed to retrieve run verification results: {response}")

    def wait_for_done(self, wait_interval_s: int = 5, timeout_s: timedelta = timedelta(minutes=10)) -> bool:
        # pool with _update and check status until done or timeout, sleeping wait_interval_s between each check
        start_time = datetime.now()
        while not self.is_done():
            if datetime.now() - start_time > timeout_s:
                return False
            sleep(wait_interval_s)
            self._update()
        return self.is_done()

    def is_done(self) -> bool:
        return self.run_verify_results.workflow_status in [
            RunsVerifyWorkflowStatus.COMPLETED,
            RunsVerifyWorkflowStatus.FAILED,
            RunsVerifyWorkflowStatus.RUN_ID_NOT_FOUND,
        ]

    def get_simdata(self) -> list[SimData]:
        sim_data_list: list[SimData] = []
        if self.run_verify_results.workflow_results is None:
            return sim_data_list
        with SimdataApiClient(simdata_configuration) as simdata_api_client:
            api_instance = SimdataDefaultApi(simdata_api_client)
            for sim_run_info in self.run_verify_results.workflow_results.sims_run_info:
                simdata_hdf5_file: SimDataHDF5File = api_instance.get_metadata(sim_run_info.biosim_sim_run.id)
                sim_data_list.append(SimData(run_id=sim_run_info.biosim_sim_run.id, hdf5_file=simdata_hdf5_file))
        return sim_data_list

    def get_dataset_comparison(self, dataset_name: str) -> DatasetComparison | None:
        if self.run_verify_results.workflow_results is None:
            return None
        first_sim_run_info: SimulationRunInfo | None = None
        if self.run_verify_results.workflow_results.sims_run_info is not None:
            for sim_run_info in self.run_verify_results.workflow_results.sims_run_info:
                if sim_run_info is not None:
                    first_sim_run_info = sim_run_info
                    break
        if first_sim_run_info is None:
            return None  # no data to compare
        for stat_dataset_name, stats_list in self.run_verify_results.workflow_results.comparison_statistics.items():
            if stat_dataset_name == dataset_name:
                var_names: list[str] = self.get_var_names(dataset_name)
                return DatasetComparison(
                    dataset_name=dataset_name, var_names=var_names, run_ids=self.run_ids, stats_list=stats_list
                )
        return None

    def get_dataset_names(self) -> list[str]:
        if self.run_verify_results.workflow_results is None:
            raise ValueError("No workflow results")
        return list(self.run_verify_results.workflow_results.comparison_statistics.keys())

    def get_var_names(self, dataset_name: str) -> list[str]:
        if (
            self.run_verify_results.workflow_results is None
            or self.run_verify_results.workflow_results.sims_run_info is None
            or len(self.run_verify_results.workflow_results.sims_run_info) == 0
        ):
            return []

        # get var names from HDF5 labels attribute of dataset from first sim run
        hdf5_file: BiosimHDF5File = self.run_verify_results.workflow_results.sims_run_info[0].hdf5_file
        attr = extract_dataset_attr(dataset_name=dataset_name, hdf5_file=hdf5_file, attr_key="sedmlDataSetLabels")
        if attr is None:
            return []
        else:
            value: list[str] = attr.model_dump()["value"]["actual_instance"]
            return value


def extract_dataset_attr(
    dataset_name: str, attr_key: str, hdf5_file: BiosimHDF5File | SimDataHDF5File
) -> BiosimHDF5Attribute | SimDataHDF5Attribute | None:
    for group in hdf5_file.groups:
        for dataset in group.datasets:
            if dataset.name == dataset_name:
                for attr in dataset.attributes:
                    if attr.key == attr_key:
                        return attr
    return None


class BiosimClient:
    def get_root(self) -> str:
        with BiosimApiClient(biosim_configuration) as biosim_api_client:
            api_instance = BiosimDefaultApi(biosim_api_client)
            api_response: dict[str, str] = api_instance.root_get()
            return str(api_response)

    def compare_runs(self, run_ids: list[str]) -> VerifyResults:
        with BiosimApiClient(biosim_configuration) as biosim_api_client:
            api_instance = VerificationApi(biosim_api_client)
            response: ApiResponse[RunsVerifyWorkflowOutput] = api_instance.start_verify_runs_with_http_info(
                workflow_id_prefix="my_runs", biosimulations_run_ids=run_ids
            )
            if response.status_code != 200:
                raise ValueError(f"Failed to start run verification workflow: {response}")
            return VerifyResults(run_ids=run_ids, run_verify_results=response.data)
