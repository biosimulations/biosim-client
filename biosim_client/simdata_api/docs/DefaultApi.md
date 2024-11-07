# biosim_client.simdata_api.DefaultApi

All URIs are relative to _http://localhost_

| Method                                         | HTTP request                        | Description        |
| ---------------------------------------------- | ----------------------------------- | ------------------ |
| [**get_health**](DefaultApi.md#get_health)     | **GET** /health                     | Health             |
| [**get_metadata**](DefaultApi.md#get_metadata) | **GET** /datasets/{run_id}/metadata | Hdf5 File Metadata |
| [**get_modified**](DefaultApi.md#get_modified) | **GET** /datasets/{run_id}/modified | Modified Datetime  |
| [**read_dataset**](DefaultApi.md#read_dataset) | **GET** /datasets/{run_id}/data     | Read Dataset       |
| [**root_get**](DefaultApi.md#root_get)         | **GET** /                           | Root               |

# **get_health**

> StatusResponse get_health()

Health

### Example

```python
import biosim_client.simdata_api
from biosim_client.simdata_api.models.status_response import StatusResponse
from biosim_client.simdata_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biosim_client.simdata_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biosim_client.simdata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biosim_client.simdata_api.DefaultApi(api_client)

    try:
        # Health
        api_response = api_instance.get_health()
        print("The response of DefaultApi->get_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_health: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**

> HDF5File get_metadata(run_id)

Hdf5 File Metadata

### Example

```python
import biosim_client.simdata_api
from biosim_client.simdata_api.models.hdf5_file import HDF5File
from biosim_client.simdata_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biosim_client.simdata_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biosim_client.simdata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biosim_client.simdata_api.DefaultApi(api_client)
    run_id = 'run_id_example' # str |

    try:
        # Hdf5 File Metadata
        api_response = api_instance.get_metadata(run_id)
        print("The response of DefaultApi->get_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_metadata: %s\n" % e)
```

### Parameters

| Name       | Type    | Description | Notes |
| ---------- | ------- | ----------- | ----- |
| **run_id** | **str** |             |

### Return type

[**HDF5File**](HDF5File.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **404**     | Dataset not found   | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_modified**

> datetime get_modified(run_id)

Modified Datetime

### Example

```python
import biosim_client.simdata_api
from biosim_client.simdata_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biosim_client.simdata_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biosim_client.simdata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biosim_client.simdata_api.DefaultApi(api_client)
    run_id = 'run_id_example' # str |

    try:
        # Modified Datetime
        api_response = api_instance.get_modified(run_id)
        print("The response of DefaultApi->get_modified:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_modified: %s\n" % e)
```

### Parameters

| Name       | Type    | Description | Notes |
| ---------- | ------- | ----------- | ----- |
| **run_id** | **str** |             |

### Return type

**datetime**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **404**     | Dataset not found   | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_dataset**

> DatasetData read_dataset(run_id, dataset_name)

Read Dataset

### Example

```python
import biosim_client.simdata_api
from biosim_client.simdata_api.models.dataset_data import DatasetData
from biosim_client.simdata_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biosim_client.simdata_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biosim_client.simdata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biosim_client.simdata_api.DefaultApi(api_client)
    run_id = 'run_id_example' # str |
    dataset_name = 'dataset_name_example' # str |

    try:
        # Read Dataset
        api_response = api_instance.read_dataset(run_id, dataset_name)
        print("The response of DefaultApi->read_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->read_dataset: %s\n" % e)
```

### Parameters

| Name             | Type    | Description | Notes |
| ---------------- | ------- | ----------- | ----- |
| **run_id**       | **str** |             |
| **dataset_name** | **str** |             |

### Return type

[**DatasetData**](DatasetData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **404**     | Dataset not found   | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**

> object root_get()

Root

### Example

```python
import biosim_client.simdata_api
from biosim_client.simdata_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biosim_client.simdata_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biosim_client.simdata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biosim_client.simdata_api.DefaultApi(api_client)

    try:
        # Root
        api_response = api_instance.root_get()
        print("The response of DefaultApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
