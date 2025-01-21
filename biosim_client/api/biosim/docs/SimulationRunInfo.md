# SimulationRunInfo

## Properties

| Name               | Type                                              | Description | Notes |
| ------------------ | ------------------------------------------------- | ----------- | ----- |
| **biosim_sim_run** | [**BiosimSimulationRun**](BiosimSimulationRun.md) |             |
| **hdf5_file**      | [**HDF5File**](HDF5File.md)                       |             |

## Example

```python
from biosim_client.api.biosim.models.simulation_run_info import SimulationRunInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SimulationRunInfo from a JSON string
simulation_run_info_instance = SimulationRunInfo.from_json(json)
# print the JSON string representation of the object
print(SimulationRunInfo.to_json())

# convert the object into a dict
simulation_run_info_dict = simulation_run_info_instance.to_dict()
# create an instance of SimulationRunInfo from a dict
simulation_run_info_from_dict = SimulationRunInfo.from_dict(simulation_run_info_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
