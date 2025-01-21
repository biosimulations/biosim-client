# SourceOmex

## Properties

| Name             | Type    | Description | Notes |
| ---------------- | ------- | ----------- | ----- |
| **name**         | **str** |             |
| **omex_s3_file** | **str** |             |

## Example

```python
from biosim_client.api.biosim.models.source_omex import SourceOmex

# TODO update the JSON string below
json = "{}"
# create an instance of SourceOmex from a JSON string
source_omex_instance = SourceOmex.from_json(json)
# print the JSON string representation of the object
print(SourceOmex.to_json())

# convert the object into a dict
source_omex_dict = source_omex_instance.to_dict()
# create an instance of SourceOmex from a dict
source_omex_from_dict = SourceOmex.from_dict(source_omex_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
