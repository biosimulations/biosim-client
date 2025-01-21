# GenerateStatisticsOutput

## Properties

| Name                      | Type                                                | Description | Notes      |
| ------------------------- | --------------------------------------------------- | ----------- | ---------- |
| **sims_run_info**         | [**List[SimulationRunInfo]**](SimulationRunInfo.md) |             |
| **all_dataset_vars**      | [**List[DatasetVar]**](DatasetVar.md)               |             |
| **comparison_statistics** | **Dict[str, List[List[ComparisonStatistics]]]**     |             |
| **sim_run_data**          | [**List[RunData]**](RunData.md)                     |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.generate_statistics_output import GenerateStatisticsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateStatisticsOutput from a JSON string
generate_statistics_output_instance = GenerateStatisticsOutput.from_json(json)
# print the JSON string representation of the object
print(GenerateStatisticsOutput.to_json())

# convert the object into a dict
generate_statistics_output_dict = generate_statistics_output_instance.to_dict()
# create an instance of GenerateStatisticsOutput from a dict
generate_statistics_output_from_dict = GenerateStatisticsOutput.from_dict(generate_statistics_output_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
