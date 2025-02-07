# biosim_client.api.biosim.VerificationApi

All URIs are relative to _http://localhost_

| Method                                                        | HTTP request                       | Description                                           |
| ------------------------------------------------------------- | ---------------------------------- | ----------------------------------------------------- |
| [**get_verify_omex**](VerificationApi.md#get_verify_omex)     | **GET** /verify_omex/{workflow_id} | Retrieve verification report for OMEX/COMBINE archive |
| [**get_verify_runs**](VerificationApi.md#get_verify_runs)     | **GET** /verify_runs/{workflow_id} | Get verification report for biosimulation runs        |
| [**start_verify_omex**](VerificationApi.md#start_verify_omex) | **POST** /verify_omex              | Request verification report for OMEX/COMBINE archive  |
| [**start_verify_runs**](VerificationApi.md#start_verify_runs) | **POST** /verify_runs              | Request verification report for biosimulation runs    |

# **get_verify_omex**

> OmexVerifyWorkflowOutput get_verify_omex(workflow_id)

Retrieve verification report for OMEX/COMBINE archive

### Example

```python
import biosim_client.api.biosim
from biosim_client.api.biosim.models.omex_verify_workflow_output import OmexVerifyWorkflowOutput
from biosim_client.api.biosim.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biosim_client.api.biosim.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biosim_client.api.biosim.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biosim_client.api.biosim.VerificationApi(api_client)
    workflow_id = 'workflow_id_example' # str |

    try:
        # Retrieve verification report for OMEX/COMBINE archive
        api_response = api_instance.get_verify_omex(workflow_id)
        print("The response of VerificationApi->get_verify_omex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->get_verify_omex: %s\n" % e)
```

### Parameters

| Name            | Type    | Description | Notes |
| --------------- | ------- | ----------- | ----- |
| **workflow_id** | **str** |             |

### Return type

[**OmexVerifyWorkflowOutput**](OmexVerifyWorkflowOutput.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verify_runs**

> RunsVerifyWorkflowOutput get_verify_runs(workflow_id)

Get verification report for biosimulation runs

### Example

```python
import biosim_client.api.biosim
from biosim_client.api.biosim.models.runs_verify_workflow_output import RunsVerifyWorkflowOutput
from biosim_client.api.biosim.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biosim_client.api.biosim.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biosim_client.api.biosim.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biosim_client.api.biosim.VerificationApi(api_client)
    workflow_id = 'workflow_id_example' # str |

    try:
        # Get verification report for biosimulation runs
        api_response = api_instance.get_verify_runs(workflow_id)
        print("The response of VerificationApi->get_verify_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->get_verify_runs: %s\n" % e)
```

### Parameters

| Name            | Type    | Description | Notes |
| --------------- | ------- | ----------- | ----- |
| **workflow_id** | **str** |             |

### Return type

[**RunsVerifyWorkflowOutput**](RunsVerifyWorkflowOutput.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_verify_omex**

> OmexVerifyWorkflowOutput start_verify_omex(uploaded_file, workflow_id_prefix=workflow_id_prefix, simulators=simulators, include_outputs=include_outputs, user_description=user_description, rel_tol=rel_tol, abs_tol_min=abs_tol_min, abs_tol_scale=abs_tol_scale, cache_buster=cache_buster, observables=observables)

Request verification report for OMEX/COMBINE archive

### Example

```python
import biosim_client.api.biosim
from biosim_client.api.biosim.models.omex_verify_workflow_output import OmexVerifyWorkflowOutput
from biosim_client.api.biosim.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biosim_client.api.biosim.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biosim_client.api.biosim.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biosim_client.api.biosim.VerificationApi(api_client)
    uploaded_file = None # bytearray | OMEX/COMBINE archive containing a deterministic SBML model
    workflow_id_prefix = 'omex-verification-' # str | Prefix for the workflow id. (optional) (default to 'omex-verification-')
    simulators = ["amici","copasi","pysces","tellurium","vcell"] # List[str] | List of simulators 'name' or 'name:version' to compare. (optional) (default to ["amici","copasi","pysces","tellurium","vcell"])
    include_outputs = False # bool | Whether to include the output data on which the comparison is based. (optional) (default to False)
    user_description = 'my-omex-compare' # str | User description of the verification run. (optional) (default to 'my-omex-compare')
    rel_tol = 0.00010 # float | Relative tolerance for proximity comparison. (optional) (default to 0.00010)
    abs_tol_min = 0.001 # float | Min absolute tolerance, where atol = max(atol_min, max(arr1,arr2)*atol_scale. (optional) (default to 0.001)
    abs_tol_scale = 0.000010 # float | Scale for absolute tolerance, where atol = max(atol_min, max(arr1,arr2)*atol_scale. (optional) (default to 0.000010)
    cache_buster = '0' # str | Optional unique id for cache busting (unique string to force new simulation runs). (optional) (default to '0')
    observables = ['observables_example'] # List[str] | List of observables to include in the return data. (optional)

    try:
        # Request verification report for OMEX/COMBINE archive
        api_response = api_instance.start_verify_omex(uploaded_file, workflow_id_prefix=workflow_id_prefix, simulators=simulators, include_outputs=include_outputs, user_description=user_description, rel_tol=rel_tol, abs_tol_min=abs_tol_min, abs_tol_scale=abs_tol_scale, cache_buster=cache_buster, observables=observables)
        print("The response of VerificationApi->start_verify_omex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->start_verify_omex: %s\n" % e)
```

### Parameters

| Name                   | Type                    | Description                                                                               | Notes                                                                                                                     |
| ---------------------- | ----------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **uploaded_file**      | **bytearray**           | OMEX/COMBINE archive containing a deterministic SBML model                                |
| **workflow_id_prefix** | **str**                 | Prefix for the workflow id.                                                               | [optional] [default to &#39;omex-verification-&#39;]                                                                      |
| **simulators**         | [**List[str]**](str.md) | List of simulators &#39;name&#39; or &#39;name:version&#39; to compare.                   | [optional] [default to [&quot;amici&quot;,&quot;copasi&quot;,&quot;pysces&quot;,&quot;tellurium&quot;,&quot;vcell&quot;]] |
| **include_outputs**    | **bool**                | Whether to include the output data on which the comparison is based.                      | [optional] [default to False]                                                                                             |
| **user_description**   | **str**                 | User description of the verification run.                                                 | [optional] [default to &#39;my-omex-compare&#39;]                                                                         |
| **rel_tol**            | **float**               | Relative tolerance for proximity comparison.                                              | [optional] [default to 0.00010]                                                                                           |
| **abs_tol_min**        | **float**               | Min absolute tolerance, where atol &#x3D; max(atol_min, max(arr1,arr2)\*atol_scale.       | [optional] [default to 0.001]                                                                                             |
| **abs_tol_scale**      | **float**               | Scale for absolute tolerance, where atol &#x3D; max(atol_min, max(arr1,arr2)\*atol_scale. | [optional] [default to 0.000010]                                                                                          |
| **cache_buster**       | **str**                 | Optional unique id for cache busting (unique string to force new simulation runs).        | [optional] [default to &#39;0&#39;]                                                                                       |
| **observables**        | [**List[str]**](str.md) | List of observables to include in the return data.                                        | [optional]                                                                                                                |

### Return type

[**OmexVerifyWorkflowOutput**](OmexVerifyWorkflowOutput.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_verify_runs**

> RunsVerifyWorkflowOutput start_verify_runs(workflow_id_prefix=workflow_id_prefix, biosimulations_run_ids=biosimulations_run_ids, include_outputs=include_outputs, user_description=user_description, rel_tol=rel_tol, abs_tol_min=abs_tol_min, abs_tol_scale=abs_tol_scale, observables=observables)

Request verification report for biosimulation runs

### Example

```python
import biosim_client.api.biosim
from biosim_client.api.biosim.models.runs_verify_workflow_output import RunsVerifyWorkflowOutput
from biosim_client.api.biosim.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biosim_client.api.biosim.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with biosim_client.api.biosim.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biosim_client.api.biosim.VerificationApi(api_client)
    workflow_id_prefix = 'runs-verification-' # str | Prefix for the workflow id. (optional) (default to 'runs-verification-')
    biosimulations_run_ids = ["67817a2e1f52f47f628af971","67817a2eba5a3f02b9f2938d"] # List[str] | List of biosimulations run IDs to compare. (optional) (default to ["67817a2e1f52f47f628af971","67817a2eba5a3f02b9f2938d"])
    include_outputs = False # bool | Whether to include the output data on which the comparison is based. (optional) (default to False)
    user_description = 'my-verify-job' # str | User description of the verification run. (optional) (default to 'my-verify-job')
    rel_tol = 1.0E-4 # float | Relative tolerance for proximity comparison. (optional) (default to 1.0E-4)
    abs_tol_min = 0.001 # float | Min absolute tolerance, where atol = max(atol_min, max(arr1,arr2)*atol_scale. (optional) (default to 0.001)
    abs_tol_scale = 1.0E-5 # float | Scale for absolute tolerance, where atol = max(atol_min, max(arr1,arr2)*atol_scale. (optional) (default to 1.0E-5)
    observables = ['observables_example'] # List[str] | List of observables to include in the return data. (optional)

    try:
        # Request verification report for biosimulation runs
        api_response = api_instance.start_verify_runs(workflow_id_prefix=workflow_id_prefix, biosimulations_run_ids=biosimulations_run_ids, include_outputs=include_outputs, user_description=user_description, rel_tol=rel_tol, abs_tol_min=abs_tol_min, abs_tol_scale=abs_tol_scale, observables=observables)
        print("The response of VerificationApi->start_verify_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->start_verify_runs: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                               | Notes                                                                                               |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **workflow_id_prefix**     | **str**                 | Prefix for the workflow id.                                                               | [optional] [default to &#39;runs-verification-&#39;]                                                |
| **biosimulations_run_ids** | [**List[str]**](str.md) | List of biosimulations run IDs to compare.                                                | [optional] [default to [&quot;67817a2e1f52f47f628af971&quot;,&quot;67817a2eba5a3f02b9f2938d&quot;]] |
| **include_outputs**        | **bool**                | Whether to include the output data on which the comparison is based.                      | [optional] [default to False]                                                                       |
| **user_description**       | **str**                 | User description of the verification run.                                                 | [optional] [default to &#39;my-verify-job&#39;]                                                     |
| **rel_tol**                | **float**               | Relative tolerance for proximity comparison.                                              | [optional] [default to 1.0E-4]                                                                      |
| **abs_tol_min**            | **float**               | Min absolute tolerance, where atol &#x3D; max(atol_min, max(arr1,arr2)\*atol_scale.       | [optional] [default to 0.001]                                                                       |
| **abs_tol_scale**          | **float**               | Scale for absolute tolerance, where atol &#x3D; max(atol_min, max(arr1,arr2)\*atol_scale. | [optional] [default to 1.0E-5]                                                                      |
| **observables**            | [**List[str]**](str.md) | List of observables to include in the return data.                                        | [optional]                                                                                          |

### Return type

[**RunsVerifyWorkflowOutput**](RunsVerifyWorkflowOutput.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
