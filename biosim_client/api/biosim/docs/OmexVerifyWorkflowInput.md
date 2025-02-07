# OmexVerifyWorkflowInput

## Properties

| Name                     | Type                                                    | Description | Notes      |
| ------------------------ | ------------------------------------------------------- | ----------- | ---------- |
| **source_omex**          | [**SourceOmex**](SourceOmex.md)                         |             |
| **user_description**     | **str**                                                 |             |
| **requested_simulators** | [**List[BiosimSimulatorSpec]**](BiosimSimulatorSpec.md) |             |
| **include_outputs**      | **bool**                                                |             |
| **rel_tol**              | **float**                                               |             |
| **abs_tol**              | **float**                                               |             |
| **observables**          | **List[str]**                                           |             | [optional] |

## Example

```python
from biosim_client.api.biosim.models.omex_verify_workflow_input import OmexVerifyWorkflowInput

# TODO update the JSON string below
json = "{}"
# create an instance of OmexVerifyWorkflowInput from a JSON string
omex_verify_workflow_input_instance = OmexVerifyWorkflowInput.from_json(json)
# print the JSON string representation of the object
print(OmexVerifyWorkflowInput.to_json())

# convert the object into a dict
omex_verify_workflow_input_dict = omex_verify_workflow_input_instance.to_dict()
# create an instance of OmexVerifyWorkflowInput from a dict
omex_verify_workflow_input_from_dict = OmexVerifyWorkflowInput.from_dict(omex_verify_workflow_input_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
