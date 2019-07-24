# swagger_client.TerminalSessionsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terminal_v1_sessions_create**](TerminalSessionsApi.md#terminal_v1_sessions_create) | **POST** /terminal/v1/sessions/ | 
[**terminal_v1_sessions_delete**](TerminalSessionsApi.md#terminal_v1_sessions_delete) | **DELETE** /terminal/v1/sessions/ | 
[**terminal_v1_sessions_delete_0**](TerminalSessionsApi.md#terminal_v1_sessions_delete_0) | **DELETE** /terminal/v1/sessions/{id}/ | 
[**terminal_v1_sessions_list**](TerminalSessionsApi.md#terminal_v1_sessions_list) | **GET** /terminal/v1/sessions/ | 
[**terminal_v1_sessions_partial_update**](TerminalSessionsApi.md#terminal_v1_sessions_partial_update) | **PATCH** /terminal/v1/sessions/ | 
[**terminal_v1_sessions_partial_update_0**](TerminalSessionsApi.md#terminal_v1_sessions_partial_update_0) | **PATCH** /terminal/v1/sessions/{id}/ | 
[**terminal_v1_sessions_read**](TerminalSessionsApi.md#terminal_v1_sessions_read) | **GET** /terminal/v1/sessions/{id}/ | 
[**terminal_v1_sessions_replay_create**](TerminalSessionsApi.md#terminal_v1_sessions_replay_create) | **POST** /terminal/v1/sessions/{id}/replay/ | 
[**terminal_v1_sessions_replay_read**](TerminalSessionsApi.md#terminal_v1_sessions_replay_read) | **GET** /terminal/v1/sessions/{id}/replay/ | 
[**terminal_v1_sessions_update**](TerminalSessionsApi.md#terminal_v1_sessions_update) | **PUT** /terminal/v1/sessions/ | 
[**terminal_v1_sessions_update_0**](TerminalSessionsApi.md#terminal_v1_sessions_update_0) | **PUT** /terminal/v1/sessions/{id}/ | 


# **terminal_v1_sessions_create**
> Session terminal_v1_sessions_create(data)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Session() # Session | 

try:
    api_response = api_instance.terminal_v1_sessions_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_sessions_delete**
> terminal_v1_sessions_delete(user=user, asset=asset, system_user=system_user, remote_addr=remote_addr, protocol=protocol, terminal=terminal, is_finished=is_finished, search=search, order=order)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
system_user = 'system_user_example' # str |  (optional)
remote_addr = 'remote_addr_example' # str |  (optional)
protocol = 'protocol_example' # str |  (optional)
terminal = 'terminal_example' # str |  (optional)
is_finished = 'is_finished_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.terminal_v1_sessions_delete(user=user, asset=asset, system_user=system_user, remote_addr=remote_addr, protocol=protocol, terminal=terminal, is_finished=is_finished, search=search, order=order)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **system_user** | **str**|  | [optional] 
 **remote_addr** | **str**|  | [optional] 
 **protocol** | **str**|  | [optional] 
 **terminal** | **str**|  | [optional] 
 **is_finished** | **str**|  | [optional] 
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

# **terminal_v1_sessions_delete_0**
> terminal_v1_sessions_delete_0(id)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this session.

try:
    api_instance.terminal_v1_sessions_delete_0(id)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this session. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_sessions_list**
> InlineResponse20020 terminal_v1_sessions_list(user=user, asset=asset, system_user=system_user, remote_addr=remote_addr, protocol=protocol, terminal=terminal, is_finished=is_finished, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
system_user = 'system_user_example' # str |  (optional)
remote_addr = 'remote_addr_example' # str |  (optional)
protocol = 'protocol_example' # str |  (optional)
terminal = 'terminal_example' # str |  (optional)
is_finished = 'is_finished_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.terminal_v1_sessions_list(user=user, asset=asset, system_user=system_user, remote_addr=remote_addr, protocol=protocol, terminal=terminal, is_finished=is_finished, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **system_user** | **str**|  | [optional] 
 **remote_addr** | **str**|  | [optional] 
 **protocol** | **str**|  | [optional] 
 **terminal** | **str**|  | [optional] 
 **is_finished** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_sessions_partial_update**
> Session terminal_v1_sessions_partial_update(data)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Session() # Session | 

try:
    api_response = api_instance.terminal_v1_sessions_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_sessions_partial_update_0**
> Session terminal_v1_sessions_partial_update_0(id, data)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this session.
data = swagger_client.Session() # Session | 

try:
    api_response = api_instance.terminal_v1_sessions_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this session. | 
 **data** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_sessions_read**
> Session terminal_v1_sessions_read(id)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this session.

try:
    api_response = api_instance.terminal_v1_sessions_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this session. | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_sessions_replay_create**
> terminal_v1_sessions_replay_create(id)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.terminal_v1_sessions_replay_create(id)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_replay_create: %s\n" % e)
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

# **terminal_v1_sessions_replay_read**
> terminal_v1_sessions_replay_read(id)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.terminal_v1_sessions_replay_read(id)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_replay_read: %s\n" % e)
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

# **terminal_v1_sessions_update**
> Session terminal_v1_sessions_update(data)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Session() # Session | 

try:
    api_response = api_instance.terminal_v1_sessions_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_sessions_update_0**
> Session terminal_v1_sessions_update_0(id, data)





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
api_instance = swagger_client.TerminalSessionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this session.
data = swagger_client.Session() # Session | 

try:
    api_response = api_instance.terminal_v1_sessions_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalSessionsApi->terminal_v1_sessions_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this session. | 
 **data** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

