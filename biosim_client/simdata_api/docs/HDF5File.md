# HDF5File

## Properties

| Name         | Type                                | Description | Notes |
| ------------ | ----------------------------------- | ----------- | ----- |
| **filename** | **str**                             |             |
| **id**       | **str**                             |             |
| **uri**      | **str**                             |             |
| **groups**   | [**List[HDF5Group]**](HDF5Group.md) |             |

## Example

```python
from biosim_client.simdata_api.models.hdf5_file import HDF5File

# TODO update the JSON string below
json = "{}"
# create an instance of HDF5File from a JSON string
hdf5_file_instance = HDF5File.from_json(json)
# print the JSON string representation of the object
print(HDF5File.to_json())

# convert the object into a dict
hdf5_file_dict = hdf5_file_instance.to_dict()
# create an instance of HDF5File from a dict
hdf5_file_from_dict = HDF5File.from_dict(hdf5_file_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
