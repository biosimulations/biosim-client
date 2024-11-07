# HDF5Attribute

## Properties

| Name      | Type                  | Description | Notes |
| --------- | --------------------- | ----------- | ----- |
| **key**   | **str**               |             |
| **value** | [**Value**](Value.md) |             |

## Example

```python
from biosim_client.simdata_api.models.hdf5_attribute import HDF5Attribute

# TODO update the JSON string below
json = "{}"
# create an instance of HDF5Attribute from a JSON string
hdf5_attribute_instance = HDF5Attribute.from_json(json)
# print the JSON string representation of the object
print(HDF5Attribute.to_json())

# convert the object into a dict
hdf5_attribute_dict = hdf5_attribute_instance.to_dict()
# create an instance of HDF5Attribute from a dict
hdf5_attribute_from_dict = HDF5Attribute.from_dict(hdf5_attribute_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
