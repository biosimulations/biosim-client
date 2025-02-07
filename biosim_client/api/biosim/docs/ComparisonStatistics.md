# ComparisonStatistics

## Properties

| Name                    | Type            | Description | Notes      |
| ----------------------- | --------------- | ----------- | ---------- |
| **dataset_name**        | **str**         |             |
| **simulator_version_i** | **str**         |             |
| **simulator_version_j** | **str**         |             |
| **var_names**           | **List[str]**   |             |
| **score**               | **List[float]** |             | [optional] |
| **is_close**            | **List[bool]**  |             | [optional] |
| **error_message**       | **str**         |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.comparison_statistics import ComparisonStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ComparisonStatistics from a JSON string
comparison_statistics_instance = ComparisonStatistics.from_json(json)
# print the JSON string representation of the object
print(ComparisonStatistics.to_json())

# convert the object into a dict
comparison_statistics_dict = comparison_statistics_instance.to_dict()
# create an instance of ComparisonStatistics from a dict
comparison_statistics_from_dict = ComparisonStatistics.from_dict(comparison_statistics_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
