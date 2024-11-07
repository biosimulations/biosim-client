# HDF5Dataset

## Properties

| Name           | Type                                        | Description | Notes |
| -------------- | ------------------------------------------- | ----------- | ----- |
| **name**       | **str**                                     |             |
| **shape**      | **List[int]**                               |             |
| **attributes** | [**List[HDF5Attribute]**](HDF5Attribute.md) |             |

## Example

```python
from biosim_client.simdata_api.models.hdf5_dataset import HDF5Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of HDF5Dataset from a JSON string
hdf5_dataset_instance = HDF5Dataset.from_json(json)
# print the JSON string representation of the object
print(HDF5Dataset.to_json())

# convert the object into a dict
hdf5_dataset_dict = hdf5_dataset_instance.to_dict()
# create an instance of HDF5Dataset from a dict
hdf5_dataset_from_dict = HDF5Dataset.from_dict(hdf5_dataset_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
