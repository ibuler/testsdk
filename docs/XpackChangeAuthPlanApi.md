# swagger_client.XpackChangeAuthPlanApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**xpack_v1_change_auth_plan_plan_asset_add_partial_update**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_asset_add_partial_update) | **PATCH** /xpack/v1/change_auth_plan/plan/{id}/asset/add/ | 
[**xpack_v1_change_auth_plan_plan_asset_add_read**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_asset_add_read) | **GET** /xpack/v1/change_auth_plan/plan/{id}/asset/add/ | 
[**xpack_v1_change_auth_plan_plan_asset_add_update**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_asset_add_update) | **PUT** /xpack/v1/change_auth_plan/plan/{id}/asset/add/ | 
[**xpack_v1_change_auth_plan_plan_asset_remove_partial_update**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_asset_remove_partial_update) | **PATCH** /xpack/v1/change_auth_plan/plan/{id}/asset/remove/ | 
[**xpack_v1_change_auth_plan_plan_asset_remove_read**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_asset_remove_read) | **GET** /xpack/v1/change_auth_plan/plan/{id}/asset/remove/ | 
[**xpack_v1_change_auth_plan_plan_asset_remove_update**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_asset_remove_update) | **PUT** /xpack/v1/change_auth_plan/plan/{id}/asset/remove/ | 
[**xpack_v1_change_auth_plan_plan_create**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_create) | **POST** /xpack/v1/change_auth_plan/plan/ | 
[**xpack_v1_change_auth_plan_plan_delete**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_delete) | **DELETE** /xpack/v1/change_auth_plan/plan/ | 
[**xpack_v1_change_auth_plan_plan_delete_0**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_delete_0) | **DELETE** /xpack/v1/change_auth_plan/plan/{id}/ | 
[**xpack_v1_change_auth_plan_plan_execution_create**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_execution_create) | **POST** /xpack/v1/change_auth_plan/plan-execution/ | 
[**xpack_v1_change_auth_plan_plan_execution_list**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_execution_list) | **GET** /xpack/v1/change_auth_plan/plan-execution/ | 
[**xpack_v1_change_auth_plan_plan_execution_subtask_list**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_execution_subtask_list) | **GET** /xpack/v1/change_auth_plan/plan-execution-subtask/ | 
[**xpack_v1_change_auth_plan_plan_execution_subtask_partial_update**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_execution_subtask_partial_update) | **PATCH** /xpack/v1/change_auth_plan/plan-execution-subtask/{id}/ | 
[**xpack_v1_change_auth_plan_plan_execution_subtask_update**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_execution_subtask_update) | **PUT** /xpack/v1/change_auth_plan/plan-execution-subtask/{id}/ | 
[**xpack_v1_change_auth_plan_plan_list**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_list) | **GET** /xpack/v1/change_auth_plan/plan/ | 
[**xpack_v1_change_auth_plan_plan_partial_update**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_partial_update) | **PATCH** /xpack/v1/change_auth_plan/plan/ | 
[**xpack_v1_change_auth_plan_plan_partial_update_0**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_partial_update_0) | **PATCH** /xpack/v1/change_auth_plan/plan/{id}/ | 
[**xpack_v1_change_auth_plan_plan_read**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_read) | **GET** /xpack/v1/change_auth_plan/plan/{id}/ | 
[**xpack_v1_change_auth_plan_plan_update**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_update) | **PUT** /xpack/v1/change_auth_plan/plan/ | 
[**xpack_v1_change_auth_plan_plan_update_0**](XpackChangeAuthPlanApi.md#xpack_v1_change_auth_plan_plan_update_0) | **PUT** /xpack/v1/change_auth_plan/plan/{id}/ | 


# **xpack_v1_change_auth_plan_plan_asset_add_partial_update**
> PlanUpdateAsset xpack_v1_change_auth_plan_plan_asset_add_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划.
data = swagger_client.PlanUpdateAsset() # PlanUpdateAsset | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_asset_add_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_asset_add_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划. | 
 **data** | [**PlanUpdateAsset**](PlanUpdateAsset.md)|  | 

### Return type

[**PlanUpdateAsset**](PlanUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_asset_add_read**
> PlanUpdateAsset xpack_v1_change_auth_plan_plan_asset_add_read(id)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划.

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_asset_add_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_asset_add_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划. | 

### Return type

[**PlanUpdateAsset**](PlanUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_asset_add_update**
> PlanUpdateAsset xpack_v1_change_auth_plan_plan_asset_add_update(id, data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划.
data = swagger_client.PlanUpdateAsset() # PlanUpdateAsset | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_asset_add_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_asset_add_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划. | 
 **data** | [**PlanUpdateAsset**](PlanUpdateAsset.md)|  | 

### Return type

[**PlanUpdateAsset**](PlanUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_asset_remove_partial_update**
> PlanUpdateAsset xpack_v1_change_auth_plan_plan_asset_remove_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划.
data = swagger_client.PlanUpdateAsset() # PlanUpdateAsset | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_asset_remove_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_asset_remove_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划. | 
 **data** | [**PlanUpdateAsset**](PlanUpdateAsset.md)|  | 

### Return type

[**PlanUpdateAsset**](PlanUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_asset_remove_read**
> PlanUpdateAsset xpack_v1_change_auth_plan_plan_asset_remove_read(id)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划.

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_asset_remove_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_asset_remove_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划. | 

### Return type

[**PlanUpdateAsset**](PlanUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_asset_remove_update**
> PlanUpdateAsset xpack_v1_change_auth_plan_plan_asset_remove_update(id, data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划.
data = swagger_client.PlanUpdateAsset() # PlanUpdateAsset | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_asset_remove_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_asset_remove_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划. | 
 **data** | [**PlanUpdateAsset**](PlanUpdateAsset.md)|  | 

### Return type

[**PlanUpdateAsset**](PlanUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_create**
> Plan xpack_v1_change_auth_plan_plan_create(data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
data = swagger_client.Plan() # Plan | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Plan**](Plan.md)|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_delete**
> xpack_v1_change_auth_plan_plan_delete(name=name, search=search, order=order)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.xpack_v1_change_auth_plan_plan_delete(name=name, search=search, order=order)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_delete_0**
> xpack_v1_change_auth_plan_plan_delete_0(id)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划.

try:
    api_instance.xpack_v1_change_auth_plan_plan_delete_0(id)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_execution_create**
> PlanExecution xpack_v1_change_auth_plan_plan_execution_create(data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
data = swagger_client.PlanExecution() # PlanExecution | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_execution_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_execution_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PlanExecution**](PlanExecution.md)|  | 

### Return type

[**PlanExecution**](PlanExecution.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_execution_list**
> InlineResponse20024 xpack_v1_change_auth_plan_plan_execution_list(search=search, order=order, limit=limit, offset=offset)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_execution_list(search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_execution_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_execution_subtask_list**
> InlineResponse20023 xpack_v1_change_auth_plan_plan_execution_subtask_list(search=search, order=order, limit=limit, offset=offset)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_execution_subtask_list(search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_execution_subtask_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_execution_subtask_partial_update**
> PlanExecutionSubtask xpack_v1_change_auth_plan_plan_execution_subtask_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划执行子任务.
data = swagger_client.PlanExecutionSubtask() # PlanExecutionSubtask | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_execution_subtask_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_execution_subtask_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划执行子任务. | 
 **data** | [**PlanExecutionSubtask**](PlanExecutionSubtask.md)|  | 

### Return type

[**PlanExecutionSubtask**](PlanExecutionSubtask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_execution_subtask_update**
> PlanExecutionSubtask xpack_v1_change_auth_plan_plan_execution_subtask_update(id, data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划执行子任务.
data = swagger_client.PlanExecutionSubtask() # PlanExecutionSubtask | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_execution_subtask_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_execution_subtask_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划执行子任务. | 
 **data** | [**PlanExecutionSubtask**](PlanExecutionSubtask.md)|  | 

### Return type

[**PlanExecutionSubtask**](PlanExecutionSubtask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_list**
> InlineResponse20025 xpack_v1_change_auth_plan_plan_list(name=name, search=search, order=order, limit=limit, offset=offset)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_list(name=name, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_partial_update**
> Plan xpack_v1_change_auth_plan_plan_partial_update(data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
data = swagger_client.Plan() # Plan | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Plan**](Plan.md)|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_partial_update_0**
> Plan xpack_v1_change_auth_plan_plan_partial_update_0(id, data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划.
data = swagger_client.Plan() # Plan | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划. | 
 **data** | [**Plan**](Plan.md)|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_read**
> Plan xpack_v1_change_auth_plan_plan_read(id)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划.

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划. | 

### Return type

[**Plan**](Plan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_update**
> Plan xpack_v1_change_auth_plan_plan_update(data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
data = swagger_client.Plan() # Plan | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Plan**](Plan.md)|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_change_auth_plan_plan_update_0**
> Plan xpack_v1_change_auth_plan_plan_update_0(id, data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.XpackChangeAuthPlanApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 改密计划.
data = swagger_client.Plan() # Plan | 

try:
    api_response = api_instance.xpack_v1_change_auth_plan_plan_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackChangeAuthPlanApi->xpack_v1_change_auth_plan_plan_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 改密计划. | 
 **data** | [**Plan**](Plan.md)|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

