import biosim_client.simdata_api as simdata_client
from biosim_client.sim_data import SimData
from biosim_client.simdata_api import HDF5File, StatusResponse
from biosim_client.simdata_api.configuration import Configuration


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
