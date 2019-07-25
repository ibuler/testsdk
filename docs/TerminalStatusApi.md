# swagger_client.TerminalStatusApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terminal_v1_status_create**](TerminalStatusApi.md#terminal_v1_status_create) | **POST** /terminal/v1/status/ | 
[**terminal_v1_status_delete**](TerminalStatusApi.md#terminal_v1_status_delete) | **DELETE** /terminal/v1/status/{id}/ | 
[**terminal_v1_status_list**](TerminalStatusApi.md#terminal_v1_status_list) | **GET** /terminal/v1/status/ | 
[**terminal_v1_status_partial_update**](TerminalStatusApi.md#terminal_v1_status_partial_update) | **PATCH** /terminal/v1/status/{id}/ | 
[**terminal_v1_status_read**](TerminalStatusApi.md#terminal_v1_status_read) | **GET** /terminal/v1/status/{id}/ | 
[**terminal_v1_status_update**](TerminalStatusApi.md#terminal_v1_status_update) | **PUT** /terminal/v1/status/{id}/ | 


# **terminal_v1_status_create**
> Status terminal_v1_status_create(data)





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
api_instance = swagger_client.TerminalStatusApi(swagger_client.ApiClient(configuration))
data = swagger_client.Status() # Status | 

try:
    api_response = api_instance.terminal_v1_status_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalStatusApi->terminal_v1_status_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Status**](Status.md)|  | 

### Return type

[**Status**](Status.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_status_delete**
> terminal_v1_status_delete(id)





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
api_instance = swagger_client.TerminalStatusApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this status.

try:
    api_instance.terminal_v1_status_delete(id)
except ApiException as e:
    print("Exception when calling TerminalStatusApi->terminal_v1_status_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this status. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_status_list**
> list[Status] terminal_v1_status_list(search=search, order=order)





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
api_instance = swagger_client.TerminalStatusApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.terminal_v1_status_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalStatusApi->terminal_v1_status_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Status]**](Status.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_status_partial_update**
> Status terminal_v1_status_partial_update(id, data)





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
api_instance = swagger_client.TerminalStatusApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this status.
data = swagger_client.Status() # Status | 

try:
    api_response = api_instance.terminal_v1_status_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalStatusApi->terminal_v1_status_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this status. | 
 **data** | [**Status**](Status.md)|  | 

### Return type

[**Status**](Status.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_status_read**
> Status terminal_v1_status_read(id)





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
api_instance = swagger_client.TerminalStatusApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this status.

try:
    api_response = api_instance.terminal_v1_status_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalStatusApi->terminal_v1_status_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this status. | 

### Return type

[**Status**](Status.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_status_update**
> Status terminal_v1_status_update(id, data)





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
api_instance = swagger_client.TerminalStatusApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this status.
data = swagger_client.Status() # Status | 

try:
    api_response = api_instance.terminal_v1_status_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalStatusApi->terminal_v1_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this status. | 
 **data** | [**Status**](Status.md)|  | 

### Return type

[**Status**](Status.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

