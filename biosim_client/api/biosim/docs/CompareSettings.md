# CompareSettings

## Properties

| Name                 | Type          | Description | Notes      |
| -------------------- | ------------- | ----------- | ---------- |
| **user_description** | **str**       |             |
| **include_outputs**  | **bool**      |             |
| **rel_tol**          | **float**     |             |
| **abs_tol_min**      | **float**     |             |
| **abs_tol_scale**    | **float**     |             |
| **observables**      | **List[str]** |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.compare_settings import CompareSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CompareSettings from a JSON string
compare_settings_instance = CompareSettings.from_json(json)
# print the JSON string representation of the object
print(CompareSettings.to_json())

# convert the object into a dict
compare_settings_dict = compare_settings_instance.to_dict()
# create an instance of CompareSettings from a dict
compare_settings_from_dict = CompareSettings.from_dict(compare_settings_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
