# RunsVerifyWorkflowOutput

## Properties

| Name                  | Type                                                        | Description | Notes      |
| --------------------- | ----------------------------------------------------------- | ----------- | ---------- |
| **workflow_id**       | **str**                                                     |             |
| **workflow_input**    | [**RunsVerifyWorkflowInput**](RunsVerifyWorkflowInput.md)   |             |
| **workflow_status**   | [**RunsVerifyWorkflowStatus**](RunsVerifyWorkflowStatus.md) |             |
| **timestamp**         | **str**                                                     |             |
| **workflow_error**    | **str**                                                     |             | [optional] |
| **actual_simulators** | [**List[BiosimSimulatorSpec]**](BiosimSimulatorSpec.md)     |             | [optional] |
| **workflow_run_id**   | **str**                                                     |             | [optional] |
| **workflow_results**  | [**GenerateStatisticsOutput**](GenerateStatisticsOutput.md) |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.runs_verify_workflow_output import RunsVerifyWorkflowOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RunsVerifyWorkflowOutput from a JSON string
runs_verify_workflow_output_instance = RunsVerifyWorkflowOutput.from_json(json)
# print the JSON string representation of the object
print(RunsVerifyWorkflowOutput.to_json())

# convert the object into a dict
runs_verify_workflow_output_dict = runs_verify_workflow_output_instance.to_dict()
# create an instance of RunsVerifyWorkflowOutput from a dict
runs_verify_workflow_output_from_dict = RunsVerifyWorkflowOutput.from_dict(runs_verify_workflow_output_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
