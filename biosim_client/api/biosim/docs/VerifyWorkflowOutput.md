# VerifyWorkflowOutput

## Properties

| Name                 | Type                                                                        | Description | Notes      |
| -------------------- | --------------------------------------------------------------------------- | ----------- | ---------- |
| **workflow_id**      | **str**                                                                     |             |
| **compare_settings** | [**CompareSettings**](CompareSettings.md)                                   |             |
| **workflow_status**  | [**VerifyWorkflowStatus**](VerifyWorkflowStatus.md)                         |             |
| **timestamp**        | **str**                                                                     |             |
| **workflow_run_id**  | **str**                                                                     |             | [optional] |
| **workflow_error**   | **str**                                                                     |             | [optional] |
| **workflow_results** | [**GenerateStatisticsActivityOutput**](GenerateStatisticsActivityOutput.md) |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.verify_workflow_output import VerifyWorkflowOutput

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWorkflowOutput from a JSON string
verify_workflow_output_instance = VerifyWorkflowOutput.from_json(json)
# print the JSON string representation of the object
print(VerifyWorkflowOutput.to_json())

# convert the object into a dict
verify_workflow_output_dict = verify_workflow_output_instance.to_dict()
# create an instance of VerifyWorkflowOutput from a dict
verify_workflow_output_from_dict = VerifyWorkflowOutput.from_dict(verify_workflow_output_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
