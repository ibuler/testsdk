# swagger_client.TerminalCommandApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terminal_v1_command_create**](TerminalCommandApi.md#terminal_v1_command_create) | **POST** /terminal/v1/command/ | 
[**terminal_v1_command_delete**](TerminalCommandApi.md#terminal_v1_command_delete) | **DELETE** /terminal/v1/command/{id}/ | 
[**terminal_v1_command_list**](TerminalCommandApi.md#terminal_v1_command_list) | **GET** /terminal/v1/command/ | 
[**terminal_v1_command_partial_update**](TerminalCommandApi.md#terminal_v1_command_partial_update) | **PATCH** /terminal/v1/command/{id}/ | 
[**terminal_v1_command_read**](TerminalCommandApi.md#terminal_v1_command_read) | **GET** /terminal/v1/command/{id}/ | 
[**terminal_v1_command_update**](TerminalCommandApi.md#terminal_v1_command_update) | **PUT** /terminal/v1/command/{id}/ | 


# **terminal_v1_command_create**
> SessionCommand terminal_v1_command_create(data)



接受app发送来的command log, 格式如下 {     \"user\": \"admin\",     \"asset\": \"localhost\",     \"system_user\": \"web\",     \"session\": \"xxxxxx\",     \"input\": \"whoami\",     \"output\": \"d2hvbWFp\",  # base64.b64encode(s)     \"timestamp\": 1485238673.0 }

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
api_instance = swagger_client.TerminalCommandApi(swagger_client.ApiClient(configuration))
data = swagger_client.SessionCommand() # SessionCommand | 

try:
    api_response = api_instance.terminal_v1_command_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalCommandApi->terminal_v1_command_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SessionCommand**](SessionCommand.md)|  | 

### Return type

[**SessionCommand**](SessionCommand.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_command_delete**
> terminal_v1_command_delete(id)



接受app发送来的command log, 格式如下 {     \"user\": \"admin\",     \"asset\": \"localhost\",     \"system_user\": \"web\",     \"session\": \"xxxxxx\",     \"input\": \"whoami\",     \"output\": \"d2hvbWFp\",  # base64.b64encode(s)     \"timestamp\": 1485238673.0 }

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
api_instance = swagger_client.TerminalCommandApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.terminal_v1_command_delete(id)
except ApiException as e:
    print("Exception when calling TerminalCommandApi->terminal_v1_command_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_command_list**
> InlineResponse20019 terminal_v1_command_list(asset=asset, system_user=system_user, user=user, session=session, search=search, order=order, limit=limit, offset=offset)



接受app发送来的command log, 格式如下 {     \"user\": \"admin\",     \"asset\": \"localhost\",     \"system_user\": \"web\",     \"session\": \"xxxxxx\",     \"input\": \"whoami\",     \"output\": \"d2hvbWFp\",  # base64.b64encode(s)     \"timestamp\": 1485238673.0 }

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
api_instance = swagger_client.TerminalCommandApi(swagger_client.ApiClient(configuration))
asset = 'asset_example' # str |  (optional)
system_user = 'system_user_example' # str |  (optional)
user = 'user_example' # str |  (optional)
session = 'session_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.terminal_v1_command_list(asset=asset, system_user=system_user, user=user, session=session, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalCommandApi->terminal_v1_command_list: %s\n" % e)
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

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_command_partial_update**
> SessionCommand terminal_v1_command_partial_update(id, data)



接受app发送来的command log, 格式如下 {     \"user\": \"admin\",     \"asset\": \"localhost\",     \"system_user\": \"web\",     \"session\": \"xxxxxx\",     \"input\": \"whoami\",     \"output\": \"d2hvbWFp\",  # base64.b64encode(s)     \"timestamp\": 1485238673.0 }

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
api_instance = swagger_client.TerminalCommandApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
data = swagger_client.SessionCommand() # SessionCommand | 

try:
    api_response = api_instance.terminal_v1_command_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalCommandApi->terminal_v1_command_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**SessionCommand**](SessionCommand.md)|  | 

### Return type

[**SessionCommand**](SessionCommand.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_command_read**
> SessionCommand terminal_v1_command_read(id)



接受app发送来的command log, 格式如下 {     \"user\": \"admin\",     \"asset\": \"localhost\",     \"system_user\": \"web\",     \"session\": \"xxxxxx\",     \"input\": \"whoami\",     \"output\": \"d2hvbWFp\",  # base64.b64encode(s)     \"timestamp\": 1485238673.0 }

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
api_instance = swagger_client.TerminalCommandApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.terminal_v1_command_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalCommandApi->terminal_v1_command_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SessionCommand**](SessionCommand.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_command_update**
> SessionCommand terminal_v1_command_update(id, data)



接受app发送来的command log, 格式如下 {     \"user\": \"admin\",     \"asset\": \"localhost\",     \"system_user\": \"web\",     \"session\": \"xxxxxx\",     \"input\": \"whoami\",     \"output\": \"d2hvbWFp\",  # base64.b64encode(s)     \"timestamp\": 1485238673.0 }

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
api_instance = swagger_client.TerminalCommandApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
data = swagger_client.SessionCommand() # SessionCommand | 

try:
    api_response = api_instance.terminal_v1_command_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalCommandApi->terminal_v1_command_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**SessionCommand**](SessionCommand.md)|  | 

### Return type

[**SessionCommand**](SessionCommand.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

