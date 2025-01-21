from datetime import datetime, timedelta
from time import sleep

from biosim_client.api.biosim.api.default_api import DefaultApi as BiosimDefaultApi
from biosim_client.api.biosim.api.verification_api import VerificationApi
from biosim_client.api.biosim.api_client import ApiClient as BiosimApiClient
from biosim_client.api.biosim.configuration import Configuration as BiosimConfiguration
from biosim_client.api.biosim.models.runs_verify_workflow_output import RunsVerifyWorkflowOutput
from biosim_client.api.biosim.models.runs_verify_workflow_status import RunsVerifyWorkflowStatus
from biosim_client.api.simdata.api_client import ApiClient as SimdataApiClient
from biosim_client.api.simdata.configuration import Configuration as SimdataConfiguration
from biosim_client.api.simdata.models.hdf5_file import HDF5File as SimDataHDF5File
from biosim_client.sim_data import SimData

simdata_configuration = SimdataConfiguration(host="https://simdata.api.biosimulations.org")
biosim_configuration = BiosimConfiguration(host="https://biosim.biosimulations.org")


class VerifyResults:
    run_verify_results: RunsVerifyWorkflowOutput
    run_ids: list[str]

    def __init__(self, run_ids: list[str], run_verify_results: RunsVerifyWorkflowOutput) -> None:
        self.run_verify_results = run_verify_results
        self.run_ids = run_ids

    def _update(self) -> None:
        with BiosimApiClient(biosim_configuration) as biosim_api_client:
            api_instance = VerificationApi(biosim_api_client)
            self.run_verify_results = api_instance.get_verify_runs(workflow_id=self.run_verify_results.workflow_id)

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
        ]

    def get_simdata(self) -> list[SimData]:
        sim_data_list: list[SimData] = []
        if self.run_verify_results.workflow_results is None:
            return sim_data_list
        with SimdataApiClient(simdata_configuration) as simdata_api_client:
            api_instance = simdata_api_client.DefaultApi(simdata_api_client)
            for sim_run_info in self.run_verify_results.workflow_results.sims_run_info:
                simdata_hdf5_file: SimDataHDF5File = api_instance.get_metadata(sim_run_info.biosim_sim_run.id)
                sim_data_list.append(SimData(run_id=sim_run_info.biosim_sim_run.id, hdf5_file=simdata_hdf5_file))
        return sim_data_list


class BiosimClient:
    def get_root(self) -> str:
        with BiosimApiClient(biosim_configuration) as biosim_api_client:
            api_instance = BiosimDefaultApi(biosim_api_client)
            api_response: dict[str, str] = api_instance.root_get()
            return str(api_response)

    def compare_runs(self, run_ids: list[str]) -> VerifyResults:
        with BiosimApiClient(biosim_configuration) as biosim_api_client:
            api_instance = VerificationApi(biosim_api_client)
            output: RunsVerifyWorkflowOutput = api_instance.start_verify_runs(
                workflow_id_prefix="my_runs", biosimulations_run_ids=run_ids
            )
            return VerifyResults(run_ids=run_ids, run_verify_results=output)
