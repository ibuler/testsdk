# swagger_client.OpsCommandExecutionsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ops_v1_command_executions_create**](OpsCommandExecutionsApi.md#ops_v1_command_executions_create) | **POST** /ops/v1/command-executions/ | 
[**ops_v1_command_executions_delete**](OpsCommandExecutionsApi.md#ops_v1_command_executions_delete) | **DELETE** /ops/v1/command-executions/{id}/ | 
[**ops_v1_command_executions_list**](OpsCommandExecutionsApi.md#ops_v1_command_executions_list) | **GET** /ops/v1/command-executions/ | 
[**ops_v1_command_executions_partial_update**](OpsCommandExecutionsApi.md#ops_v1_command_executions_partial_update) | **PATCH** /ops/v1/command-executions/{id}/ | 
[**ops_v1_command_executions_read**](OpsCommandExecutionsApi.md#ops_v1_command_executions_read) | **GET** /ops/v1/command-executions/{id}/ | 
[**ops_v1_command_executions_update**](OpsCommandExecutionsApi.md#ops_v1_command_executions_update) | **PUT** /ops/v1/command-executions/{id}/ | 


# **ops_v1_command_executions_create**
> CommandExecution ops_v1_command_executions_create(data)





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
api_instance = swagger_client.OpsCommandExecutionsApi(swagger_client.ApiClient(configuration))
data = swagger_client.CommandExecution() # CommandExecution | 

try:
    api_response = api_instance.ops_v1_command_executions_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsCommandExecutionsApi->ops_v1_command_executions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CommandExecution**](CommandExecution.md)|  | 

### Return type

[**CommandExecution**](CommandExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_command_executions_delete**
> ops_v1_command_executions_delete(id)





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
api_instance = swagger_client.OpsCommandExecutionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.ops_v1_command_executions_delete(id)
except ApiException as e:
    print("Exception when calling OpsCommandExecutionsApi->ops_v1_command_executions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_command_executions_list**
> list[CommandExecution] ops_v1_command_executions_list(search=search, order=order)





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
api_instance = swagger_client.OpsCommandExecutionsApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.ops_v1_command_executions_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsCommandExecutionsApi->ops_v1_command_executions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[CommandExecution]**](CommandExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_command_executions_partial_update**
> CommandExecution ops_v1_command_executions_partial_update(id, data)





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
api_instance = swagger_client.OpsCommandExecutionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
data = swagger_client.CommandExecution() # CommandExecution | 

try:
    api_response = api_instance.ops_v1_command_executions_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsCommandExecutionsApi->ops_v1_command_executions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**CommandExecution**](CommandExecution.md)|  | 

### Return type

[**CommandExecution**](CommandExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_command_executions_read**
> CommandExecution ops_v1_command_executions_read(id)





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
api_instance = swagger_client.OpsCommandExecutionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.ops_v1_command_executions_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsCommandExecutionsApi->ops_v1_command_executions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CommandExecution**](CommandExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_command_executions_update**
> CommandExecution ops_v1_command_executions_update(id, data)





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
api_instance = swagger_client.OpsCommandExecutionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
data = swagger_client.CommandExecution() # CommandExecution | 

try:
    api_response = api_instance.ops_v1_command_executions_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsCommandExecutionsApi->ops_v1_command_executions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**CommandExecution**](CommandExecution.md)|  | 

### Return type

[**CommandExecution**](CommandExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

