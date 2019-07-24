# swagger_client.OpsHistoryApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ops_v1_history_create**](OpsHistoryApi.md#ops_v1_history_create) | **POST** /ops/v1/history/ | 
[**ops_v1_history_delete**](OpsHistoryApi.md#ops_v1_history_delete) | **DELETE** /ops/v1/history/{id}/ | 
[**ops_v1_history_list**](OpsHistoryApi.md#ops_v1_history_list) | **GET** /ops/v1/history/ | 
[**ops_v1_history_partial_update**](OpsHistoryApi.md#ops_v1_history_partial_update) | **PATCH** /ops/v1/history/{id}/ | 
[**ops_v1_history_read**](OpsHistoryApi.md#ops_v1_history_read) | **GET** /ops/v1/history/{id}/ | 
[**ops_v1_history_update**](OpsHistoryApi.md#ops_v1_history_update) | **PUT** /ops/v1/history/{id}/ | 


# **ops_v1_history_create**
> AdHocRunHistory ops_v1_history_create(data)





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
api_instance = swagger_client.OpsHistoryApi(swagger_client.ApiClient(configuration))
data = swagger_client.AdHocRunHistory() # AdHocRunHistory | 

try:
    api_response = api_instance.ops_v1_history_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsHistoryApi->ops_v1_history_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AdHocRunHistory**](AdHocRunHistory.md)|  | 

### Return type

[**AdHocRunHistory**](AdHocRunHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_history_delete**
> ops_v1_history_delete(id)





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
api_instance = swagger_client.OpsHistoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ad hoc run history.

try:
    api_instance.ops_v1_history_delete(id)
except ApiException as e:
    print("Exception when calling OpsHistoryApi->ops_v1_history_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ad hoc run history. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_history_list**
> list[AdHocRunHistory] ops_v1_history_list(search=search, order=order)





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
api_instance = swagger_client.OpsHistoryApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.ops_v1_history_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsHistoryApi->ops_v1_history_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[AdHocRunHistory]**](AdHocRunHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_history_partial_update**
> AdHocRunHistory ops_v1_history_partial_update(id, data)





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
api_instance = swagger_client.OpsHistoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ad hoc run history.
data = swagger_client.AdHocRunHistory() # AdHocRunHistory | 

try:
    api_response = api_instance.ops_v1_history_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsHistoryApi->ops_v1_history_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ad hoc run history. | 
 **data** | [**AdHocRunHistory**](AdHocRunHistory.md)|  | 

### Return type

[**AdHocRunHistory**](AdHocRunHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_history_read**
> AdHocRunHistory ops_v1_history_read(id)





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
api_instance = swagger_client.OpsHistoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ad hoc run history.

try:
    api_response = api_instance.ops_v1_history_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsHistoryApi->ops_v1_history_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ad hoc run history. | 

### Return type

[**AdHocRunHistory**](AdHocRunHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_history_update**
> AdHocRunHistory ops_v1_history_update(id, data)





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
api_instance = swagger_client.OpsHistoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ad hoc run history.
data = swagger_client.AdHocRunHistory() # AdHocRunHistory | 

try:
    api_response = api_instance.ops_v1_history_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsHistoryApi->ops_v1_history_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ad hoc run history. | 
 **data** | [**AdHocRunHistory**](AdHocRunHistory.md)|  | 

### Return type

[**AdHocRunHistory**](AdHocRunHistory.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

