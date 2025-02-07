# BiosimSimulatorSpec

## Properties

| Name          | Type    | Description | Notes      |
| ------------- | ------- | ----------- | ---------- |
| **simulator** | **str** |             |
| **version**   | **str** |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.biosim_simulator_spec import BiosimSimulatorSpec

# TODO update the JSON string below
json = "{}"
# create an instance of BiosimSimulatorSpec from a JSON string
biosim_simulator_spec_instance = BiosimSimulatorSpec.from_json(json)
# print the JSON string representation of the object
print(BiosimSimulatorSpec.to_json())

# convert the object into a dict
biosim_simulator_spec_dict = biosim_simulator_spec_instance.to_dict()
# create an instance of BiosimSimulatorSpec from a dict
biosim_simulator_spec_from_dict = BiosimSimulatorSpec.from_dict(biosim_simulator_spec_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
