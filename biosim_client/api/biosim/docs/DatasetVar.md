# DatasetVar

## Properties

| Name             | Type    | Description | Notes |
| ---------------- | ------- | ----------- | ----- |
| **dataset_name** | **str** |             |
| **var_name**     | **str** |             |

## Example

```python
from biosim_client.api.biosim.models.dataset_var import DatasetVar

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetVar from a JSON string
dataset_var_instance = DatasetVar.from_json(json)
# print the JSON string representation of the object
print(DatasetVar.to_json())

# convert the object into a dict
dataset_var_dict = dataset_var_instance.to_dict()
# create an instance of DatasetVar from a dict
dataset_var_from_dict = DatasetVar.from_dict(dataset_var_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
