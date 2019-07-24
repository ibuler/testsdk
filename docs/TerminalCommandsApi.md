# swagger_client.TerminalCommandsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terminal_v1_commands_export_list**](TerminalCommandsApi.md#terminal_v1_commands_export_list) | **GET** /terminal/v1/commands/export/ | 


# **terminal_v1_commands_export_list**
> terminal_v1_commands_export_list(asset=asset, system_user=system_user, user=user, session=session, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.TerminalCommandsApi(swagger_client.ApiClient(configuration))
asset = 'asset_example' # str |  (optional)
system_user = 'system_user_example' # str |  (optional)
user = 'user_example' # str |  (optional)
session = 'session_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_instance.terminal_v1_commands_export_list(asset=asset, system_user=system_user, user=user, session=session, search=search, order=order, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling TerminalCommandsApi->terminal_v1_commands_export_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [optional] 
 **system_user** | **str**|  | [optional] 
 **user** | **str**|  | [optional] 
 **session** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

