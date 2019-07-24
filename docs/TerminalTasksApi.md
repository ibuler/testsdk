# swagger_client.TerminalTasksApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terminal_v1_tasks_create**](TerminalTasksApi.md#terminal_v1_tasks_create) | **POST** /terminal/v1/tasks/ | 
[**terminal_v1_tasks_delete**](TerminalTasksApi.md#terminal_v1_tasks_delete) | **DELETE** /terminal/v1/tasks/ | 
[**terminal_v1_tasks_delete_0**](TerminalTasksApi.md#terminal_v1_tasks_delete_0) | **DELETE** /terminal/v1/tasks/{id}/ | 
[**terminal_v1_tasks_kill_session_create**](TerminalTasksApi.md#terminal_v1_tasks_kill_session_create) | **POST** /terminal/v1/tasks/kill-session/ | 
[**terminal_v1_tasks_list**](TerminalTasksApi.md#terminal_v1_tasks_list) | **GET** /terminal/v1/tasks/ | 
[**terminal_v1_tasks_partial_update**](TerminalTasksApi.md#terminal_v1_tasks_partial_update) | **PATCH** /terminal/v1/tasks/ | 
[**terminal_v1_tasks_partial_update_0**](TerminalTasksApi.md#terminal_v1_tasks_partial_update_0) | **PATCH** /terminal/v1/tasks/{id}/ | 
[**terminal_v1_tasks_read**](TerminalTasksApi.md#terminal_v1_tasks_read) | **GET** /terminal/v1/tasks/{id}/ | 
[**terminal_v1_tasks_update**](TerminalTasksApi.md#terminal_v1_tasks_update) | **PUT** /terminal/v1/tasks/ | 
[**terminal_v1_tasks_update_0**](TerminalTasksApi.md#terminal_v1_tasks_update_0) | **PUT** /terminal/v1/tasks/{id}/ | 


# **terminal_v1_tasks_create**
> Task terminal_v1_tasks_create(data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TerminalTasksApi(swagger_client.ApiClient(configuration))
data = swagger_client.Task() # Task | 

try:
    api_response = api_instance.terminal_v1_tasks_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTasksApi->terminal_v1_tasks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_tasks_delete**
> terminal_v1_tasks_delete(search=search, order=order)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TerminalTasksApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.terminal_v1_tasks_delete(search=search, order=order)
except ApiException as e:
    print("Exception when calling TerminalTasksApi->terminal_v1_tasks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_tasks_delete_0**
> terminal_v1_tasks_delete_0(id)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TerminalTasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this task.

try:
    api_instance.terminal_v1_tasks_delete_0(id)
except ApiException as e:
    print("Exception when calling TerminalTasksApi->terminal_v1_tasks_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_tasks_kill_session_create**
> terminal_v1_tasks_kill_session_create()





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TerminalTasksApi(swagger_client.ApiClient(configuration))

try:
    api_instance.terminal_v1_tasks_kill_session_create()
except ApiException as e:
    print("Exception when calling TerminalTasksApi->terminal_v1_tasks_kill_session_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_tasks_list**
> list[Task] terminal_v1_tasks_list(search=search, order=order)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TerminalTasksApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.terminal_v1_tasks_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTasksApi->terminal_v1_tasks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Task]**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_tasks_partial_update**
> Task terminal_v1_tasks_partial_update(data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TerminalTasksApi(swagger_client.ApiClient(configuration))
data = swagger_client.Task() # Task | 

try:
    api_response = api_instance.terminal_v1_tasks_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTasksApi->terminal_v1_tasks_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_tasks_partial_update_0**
> Task terminal_v1_tasks_partial_update_0(id, data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TerminalTasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this task.
data = swagger_client.Task() # Task | 

try:
    api_response = api_instance.terminal_v1_tasks_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTasksApi->terminal_v1_tasks_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_tasks_read**
> Task terminal_v1_tasks_read(id)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TerminalTasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this task.

try:
    api_response = api_instance.terminal_v1_tasks_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTasksApi->terminal_v1_tasks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 

### Return type

[**Task**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_tasks_update**
> Task terminal_v1_tasks_update(data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TerminalTasksApi(swagger_client.ApiClient(configuration))
data = swagger_client.Task() # Task | 

try:
    api_response = api_instance.terminal_v1_tasks_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTasksApi->terminal_v1_tasks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_tasks_update_0**
> Task terminal_v1_tasks_update_0(id, data)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TerminalTasksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this task.
data = swagger_client.Task() # Task | 

try:
    api_response = api_instance.terminal_v1_tasks_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTasksApi->terminal_v1_tasks_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this task. | 
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

