from biosim_client.api.simdata.api.default_api import DefaultApi
from biosim_client.api.simdata.api_client import ApiClient
from biosim_client.api.simdata.configuration import Configuration
from biosim_client.api.simdata.models.hdf5_file import HDF5File
from biosim_client.api.simdata.models.status_response import StatusResponse
from biosim_client.sim_data import SimData


class SimdataClient:
    def __init__(self) -> None:
        self.configuration = Configuration(host="https://simdata.api.biosimulations.org")

    def get_health(self) -> str:
        with ApiClient(self.configuration) as api_client:
            api_instance = DefaultApi(api_client)
            api_response: StatusResponse = api_instance.get_health()
            return api_response.to_str()

    def get_simdata(self, run_id: str) -> SimData:
        with ApiClient(self.configuration) as api_client:
            api_instance = DefaultApi(api_client)
            hdf5_file: HDF5File = api_instance.get_metadata(run_id)
            return SimData(run_id=run_id, hdf5_file=hdf5_file)
