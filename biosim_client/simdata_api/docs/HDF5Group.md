# HDF5Group

## Properties

| Name           | Type                                        | Description | Notes |
| -------------- | ------------------------------------------- | ----------- | ----- |
| **name**       | **str**                                     |             |
| **attributes** | [**List[HDF5Attribute]**](HDF5Attribute.md) |             |
| **datasets**   | [**List[HDF5Dataset]**](HDF5Dataset.md)     |             |

## Example

```python
from biosim_client.simdata_api.models.hdf5_group import HDF5Group

# TODO update the JSON string below
json = "{}"
# create an instance of HDF5Group from a JSON string
hdf5_group_instance = HDF5Group.from_json(json)
# print the JSON string representation of the object
print(HDF5Group.to_json())

# convert the object into a dict
hdf5_group_dict = hdf5_group_instance.to_dict()
# create an instance of HDF5Group from a dict
hdf5_group_from_dict = HDF5Group.from_dict(hdf5_group_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
