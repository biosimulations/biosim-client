# RunsVerifyWorkflowInput

## Properties

| Name                       | Type          | Description | Notes      |
| -------------------------- | ------------- | ----------- | ---------- |
| **user_description**       | **str**       |             |
| **biosimulations_run_ids** | **List[str]** |             |
| **include_outputs**        | **bool**      |             |
| **rel_tol**                | **float**     |             |
| **abs_tol**                | **float**     |             |
| **observables**            | **List[str]** |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.runs_verify_workflow_input import RunsVerifyWorkflowInput

# TODO update the JSON string below
json = "{}"
# create an instance of RunsVerifyWorkflowInput from a JSON string
runs_verify_workflow_input_instance = RunsVerifyWorkflowInput.from_json(json)
# print the JSON string representation of the object
print(RunsVerifyWorkflowInput.to_json())

# convert the object into a dict
runs_verify_workflow_input_dict = runs_verify_workflow_input_instance.to_dict()
# create an instance of RunsVerifyWorkflowInput from a dict
runs_verify_workflow_input_from_dict = RunsVerifyWorkflowInput.from_dict(runs_verify_workflow_input_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
