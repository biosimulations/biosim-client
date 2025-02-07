# BiosimulatorVersion

## Properties

| Name             | Type    | Description | Notes |
| ---------------- | ------- | ----------- | ----- |
| **id**           | **str** |             |
| **name**         | **str** |             |
| **version**      | **str** |             |
| **image_url**    | **str** |             |
| **image_digest** | **str** |             |
| **created**      | **str** |             |
| **updated**      | **str** |             |

## Example

```python
from biosim_client.api.biosim.models.biosimulator_version import BiosimulatorVersion

# TODO update the JSON string below
json = "{}"
# create an instance of BiosimulatorVersion from a JSON string
biosimulator_version_instance = BiosimulatorVersion.from_json(json)
# print the JSON string representation of the object
print(BiosimulatorVersion.to_json())

# convert the object into a dict
biosimulator_version_dict = biosimulator_version_instance.to_dict()
# create an instance of BiosimulatorVersion from a dict
biosimulator_version_from_dict = BiosimulatorVersion.from_dict(biosimulator_version_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
