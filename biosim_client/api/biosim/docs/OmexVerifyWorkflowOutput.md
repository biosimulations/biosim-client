# OmexVerifyWorkflowOutput

## Properties

| Name                 | Type                                                                        | Description | Notes      |
| -------------------- | --------------------------------------------------------------------------- | ----------- | ---------- |
| **workflow_id**      | **str**                                                                     |             |
| **compare_settings** | [**CompareSettings**](CompareSettings.md)                                   |             |
| **workflow_status**  | [**OmexVerifyWorkflowStatus**](OmexVerifyWorkflowStatus.md)                 |             |
| **timestamp**        | **str**                                                                     |             |
| **workflow_run_id**  | **str**                                                                     |             | [optional] |
| **workflow_error**   | **str**                                                                     |             | [optional] |
| **workflow_results** | [**GenerateStatisticsActivityOutput**](GenerateStatisticsActivityOutput.md) |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.omex_verify_workflow_output import OmexVerifyWorkflowOutput

# TODO update the JSON string below
json = "{}"
# create an instance of OmexVerifyWorkflowOutput from a JSON string
omex_verify_workflow_output_instance = OmexVerifyWorkflowOutput.from_json(json)
# print the JSON string representation of the object
print(OmexVerifyWorkflowOutput.to_json())

# convert the object into a dict
omex_verify_workflow_output_dict = omex_verify_workflow_output_instance.to_dict()
# create an instance of OmexVerifyWorkflowOutput from a dict
omex_verify_workflow_output_from_dict = OmexVerifyWorkflowOutput.from_dict(omex_verify_workflow_output_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
