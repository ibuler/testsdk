# swagger_client.OpsTasksApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ops_v1_tasks_create**](OpsTasksApi.md#ops_v1_tasks_create) | **POST** /ops/v1/tasks/ | 
[**ops_v1_tasks_delete**](OpsTasksApi.md#ops_v1_tasks_delete) | **DELETE** /ops/v1/tasks/{id}/ | 
[**ops_v1_tasks_list**](OpsTasksApi.md#ops_v1_tasks_list) | **GET** /ops/v1/tasks/ | 
[**ops_v1_tasks_partial_update**](OpsTasksApi.md#ops_v1_tasks_partial_update) | **PATCH** /ops/v1/tasks/{id}/ | 
[**ops_v1_tasks_read**](OpsTasksApi.md#ops_v1_tasks_read) | **GET** /ops/v1/tasks/{id}/ | 
[**ops_v1_tasks_run_read**](OpsTasksApi.md#ops_v1_tasks_run_read) | **GET** /ops/v1/tasks/{id}/run/ | 
[**ops_v1_tasks_update**](OpsTasksApi.md#ops_v1_tasks_update) | **PUT** /ops/v1/tasks/{id}/ | 


# **ops_v1_tasks_create**
> Task ops_v1_tasks_create(data)





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
api_instance = swagger_client.OpsTasksApi(swagger_client.ApiClient(configuration))
data = swagger_client.Task() # Task | 

try:
    api_response = api_instance.ops_v1_tasks_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsTasksApi->ops_v1_tasks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_tasks_delete**
> ops_v1_tasks_delete(id)





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
api_instance = swagger_client.OpsTasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this task.

try:
    api_instance.ops_v1_tasks_delete(id)
except ApiException as e:
    print("Exception when calling OpsTasksApi->ops_v1_tasks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_tasks_list**
> list[Task] ops_v1_tasks_list(search=search, order=order)





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
api_instance = swagger_client.OpsTasksApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.ops_v1_tasks_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsTasksApi->ops_v1_tasks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Task]**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_tasks_partial_update**
> Task ops_v1_tasks_partial_update(id, data)





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
api_instance = swagger_client.OpsTasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this task.
data = swagger_client.Task() # Task | 

try:
    api_response = api_instance.ops_v1_tasks_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsTasksApi->ops_v1_tasks_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_tasks_read**
> Task ops_v1_tasks_read(id)





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
api_instance = swagger_client.OpsTasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this task.

try:
    api_response = api_instance.ops_v1_tasks_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsTasksApi->ops_v1_tasks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_tasks_run_read**
> CeleryTask ops_v1_tasks_run_read(id)





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
api_instance = swagger_client.OpsTasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this task.

try:
    api_response = api_instance.ops_v1_tasks_run_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsTasksApi->ops_v1_tasks_run_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 

### Return type

[**CeleryTask**](CeleryTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_tasks_update**
> Task ops_v1_tasks_update(id, data)





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
api_instance = swagger_client.OpsTasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this task.
data = swagger_client.Task() # Task | 

try:
    api_response = api_instance.ops_v1_tasks_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsTasksApi->ops_v1_tasks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

