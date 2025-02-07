# GenerateStatisticsActivityOutput

## Properties

| Name                      | Type                                                | Description | Notes      |
| ------------------------- | --------------------------------------------------- | ----------- | ---------- |
| **sims_run_info**         | [**List[SimulationRunInfo]**](SimulationRunInfo.md) |             |
| **comparison_statistics** | **Dict[str, List[List[ComparisonStatistics]]]**     |             |
| **sim_run_data**          | [**List[RunData]**](RunData.md)                     |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.generate_statistics_activity_output import GenerateStatisticsActivityOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateStatisticsActivityOutput from a JSON string
generate_statistics_activity_output_instance = GenerateStatisticsActivityOutput.from_json(json)
# print the JSON string representation of the object
print(GenerateStatisticsActivityOutput.to_json())

# convert the object into a dict
generate_statistics_activity_output_dict = generate_statistics_activity_output_instance.to_dict()
# create an instance of GenerateStatisticsActivityOutput from a dict
generate_statistics_activity_output_from_dict = GenerateStatisticsActivityOutput.from_dict(generate_statistics_activity_output_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
