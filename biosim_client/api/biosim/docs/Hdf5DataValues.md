# Hdf5DataValues

## Properties

| Name       | Type            | Description | Notes |
| ---------- | --------------- | ----------- | ----- |
| **shape**  | **List[int]**   |             |
| **values** | **List[float]** |             |

## Example

```python
from biosim_client.api.biosim.models.hdf5_data_values import Hdf5DataValues

# TODO update the JSON string below
json = "{}"
# create an instance of Hdf5DataValues from a JSON string
hdf5_data_values_instance = Hdf5DataValues.from_json(json)
# print the JSON string representation of the object
print(Hdf5DataValues.to_json())

# convert the object into a dict
hdf5_data_values_dict = hdf5_data_values_instance.to_dict()
# create an instance of Hdf5DataValues from a dict
hdf5_data_values_from_dict = Hdf5DataValues.from_dict(hdf5_data_values_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
