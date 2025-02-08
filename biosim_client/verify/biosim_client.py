from datetime import datetime, timedelta
from pathlib import Path
from time import sleep

from biosim_client.api.biosim.api.default_api import DefaultApi as BiosimDefaultApi
from biosim_client.api.biosim.api.verification_api import VerificationApi
from biosim_client.api.biosim.api_client import ApiClient as BiosimApiClient
from biosim_client.api.biosim.api_response import ApiResponse
from biosim_client.api.biosim.configuration import Configuration as BiosimConfiguration
from biosim_client.api.biosim.models.verify_workflow_output import VerifyWorkflowOutput
from biosim_client.api.biosim.models.verify_workflow_status import VerifyWorkflowStatus
from biosim_client.verify.models import VerifyResults

biosim_configuration = BiosimConfiguration(host="https://biosim.biosimulations.org")


class BiosimClient:
    def get_api_version(self) -> str:
        with BiosimApiClient(biosim_configuration) as biosim_api_client:
            api_instance = BiosimDefaultApi(biosim_api_client)
            api_response: str = api_instance.get_version_version_get()
            return api_response

    def compare_runs(
        self, run_ids: list[str], wait_interval_s: int = 5, timeout_s: timedelta = timedelta(minutes=10)
    ) -> VerifyResults:
        """
        :param run_ids:  list of biosimulations run IDs to compare simulation results
        :param wait_interval_s:  optional interval in seconds to wait between polling for verification results
        :param timeout_s:  optional timeout in seconds to wait for verification results
        :return: VerifyResults:  The results of the verification
        """
        with BiosimApiClient(biosim_configuration) as biosim_api_client:
            api_instance = VerificationApi(biosim_api_client)
            response: ApiResponse[VerifyWorkflowOutput] = api_instance.verify_runs_with_http_info(
                workflow_id_prefix="client_runs", biosimulations_run_ids=run_ids
            )
            if response.status_code != 200:
                raise ValueError(f"Failed to start run verification workflow: {response}")

            verify_workflow_output = response.data
            start_time = datetime.now()
            while verify_workflow_output.workflow_status not in [
                VerifyWorkflowStatus.COMPLETED,
                VerifyWorkflowStatus.FAILED,
                VerifyWorkflowStatus.RUN_ID_NOT_FOUND,
            ]:
                if datetime.now() - start_time > timeout_s:
                    raise TimeoutError(f"Timed out waiting for verification results: {verify_workflow_output}")
                sleep(wait_interval_s)
                response = api_instance.get_verify_output_with_http_info(workflow_id=verify_workflow_output.workflow_id)
                if response.status_code != 200:
                    raise ValueError(f"Failed to retrieve verification results: {response}")

                verify_workflow_output = response.data

            if (
                verify_workflow_output.workflow_status == VerifyWorkflowStatus.RUN_ID_NOT_FOUND
                or verify_workflow_output.workflow_status == VerifyWorkflowStatus.FAILED
            ):
                raise ValueError(f"Failed to retrieve verification results: {verify_workflow_output.workflow_error}")
            if verify_workflow_output is None:
                raise ValueError(f"Failed to retrieve verification results: {response}")

            return VerifyResults(run_verify_results=verify_workflow_output)

    def compare_omex(
        self,
        omex_path: Path,
        simulators: list[str],
        cache_buster: str = "",
        wait_interval_s: int = 5,
        timeout_s: timedelta = timedelta(minutes=10),
    ) -> VerifyResults:
        """
        :param omex_path:  path to the omex file to verify against the simulators
        :param simulators:  list of simulator_name[:simulator_version] to compare simulation results
        :param cache_buster:  optional cache buster to use for the verification - unique values will force a new verification
        :param wait_interval_s:  optional interval in seconds to wait between polling for verification results
        :param timeout_s:  optional timeout in seconds to wait for verification results
        :return: VerifyResults:  The results of the verification
        """
        with open(omex_path, "rb") as file:
            omex_bytes = file.read()
        filename = omex_path.name
        with BiosimApiClient(biosim_configuration) as biosim_api_client:
            api_instance = VerificationApi(biosim_api_client)
            response: ApiResponse[VerifyWorkflowOutput] = api_instance.verify_omex_with_http_info(
                workflow_id_prefix="client_omex_",
                uploaded_file=(filename, omex_bytes),
                simulators=simulators,
                cache_buster=cache_buster,
            )
            if response.status_code != 200:
                raise ValueError(f"Failed to start run verification workflow: {response}")

            verify_workflow_output = response.data
            start_time = datetime.now()
            while verify_workflow_output.workflow_status not in [
                VerifyWorkflowStatus.COMPLETED,
                VerifyWorkflowStatus.FAILED,
                VerifyWorkflowStatus.RUN_ID_NOT_FOUND,
            ]:
                if datetime.now() - start_time > timeout_s:
                    raise TimeoutError(f"Timed out waiting for verification results: {verify_workflow_output}")
                sleep(wait_interval_s)
                response = api_instance.get_verify_output_with_http_info(workflow_id=verify_workflow_output.workflow_id)
                if response.status_code != 200:
                    raise ValueError(f"Failed to retrieve verification results: {response}")

                verify_workflow_output = response.data

            if (
                verify_workflow_output.workflow_status == VerifyWorkflowStatus.RUN_ID_NOT_FOUND
                or verify_workflow_output.workflow_status == VerifyWorkflowStatus.FAILED
            ):
                raise ValueError(f"Failed to retrieve verification results: {verify_workflow_output.workflow_error}")
            if verify_workflow_output is None:
                raise ValueError(f"Failed to retrieve verification results: {response}")

            return VerifyResults(run_verify_results=verify_workflow_output)
