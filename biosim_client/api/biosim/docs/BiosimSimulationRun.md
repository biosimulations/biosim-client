# BiosimSimulationRun

data returned by api.biosimulations.org/runs/{run_id}

## Properties

| Name                  | Type                                                          | Description | Notes      |
| --------------------- | ------------------------------------------------------------- | ----------- | ---------- |
| **id**                | **str**                                                       |             |
| **name**              | **str**                                                       |             |
| **simulator_version** | [**BiosimulatorVersion**](BiosimulatorVersion.md)             |             |
| **status**            | [**BiosimSimulationRunStatus**](BiosimSimulationRunStatus.md) |             |
| **error_message**     | **str**                                                       |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.biosim_simulation_run import BiosimSimulationRun

# TODO update the JSON string below
json = "{}"
# create an instance of BiosimSimulationRun from a JSON string
biosim_simulation_run_instance = BiosimSimulationRun.from_json(json)
# print the JSON string representation of the object
print(BiosimSimulationRun.to_json())

# convert the object into a dict
biosim_simulation_run_dict = biosim_simulation_run_instance.to_dict()
# create an instance of BiosimSimulationRun from a dict
biosim_simulation_run_from_dict = BiosimSimulationRun.from_dict(biosim_simulation_run_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
