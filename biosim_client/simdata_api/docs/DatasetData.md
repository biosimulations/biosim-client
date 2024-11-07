# DatasetData

## Properties

| Name       | Type            | Description | Notes |
| ---------- | --------------- | ----------- | ----- |
| **shape**  | **List[int]**   |             |
| **values** | **List[float]** |             |

## Example

```python
from biosim_client.simdata_api.models.dataset_data import DatasetData

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetData from a JSON string
dataset_data_instance = DatasetData.from_json(json)
# print the JSON string representation of the object
print(DatasetData.to_json())

# convert the object into a dict
dataset_data_dict = dataset_data_instance.to_dict()
# create an instance of DatasetData from a dict
dataset_data_from_dict = DatasetData.from_dict(dataset_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
