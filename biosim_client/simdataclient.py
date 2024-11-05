import biosim_client.api_clients.simdata.openapi_client as simdata_client
from biosim_client.api_clients.simdata.openapi_client import StatusResponse, HDF5File
from biosim_client.api_clients.simdata.openapi_client.configuration import Configuration
from biosim_client.sim_data import SimData


class SimdataClient:

    def __init__(self) -> None:
        self.configuration = Configuration(host="https://simdata.api.biosimulations.org")

    def get_health(self) -> str:
        with simdata_client.api_client.ApiClient(self.configuration) as api_client:
            api_instance = simdata_client.DefaultApi(api_client)
            api_response: StatusResponse = api_instance.get_health()
            return api_response.to_str()

    def get_simdata(self, run_id: str) -> SimData:
        with simdata_client.api_client.ApiClient(self.configuration) as api_client:
            api_instance = simdata_client.DefaultApi(api_client)
            hdf5_file: HDF5File = api_instance.get_metadata(run_id)
            return SimData(configuration=self.configuration, run_id=run_id, hdf5_file=hdf5_file)
