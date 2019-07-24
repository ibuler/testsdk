# swagger_client.TerminalTerminalApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terminal_v1_terminal_access_key_list**](TerminalTerminalApi.md#terminal_v1_terminal_access_key_list) | **GET** /terminal/v1/terminal/{terminal}/access-key/ | 
[**terminal_v1_terminal_config_list**](TerminalTerminalApi.md#terminal_v1_terminal_config_list) | **GET** /terminal/v1/terminal/config/ | 
[**terminal_v1_terminal_create**](TerminalTerminalApi.md#terminal_v1_terminal_create) | **POST** /terminal/v1/terminal/ | 
[**terminal_v1_terminal_delete**](TerminalTerminalApi.md#terminal_v1_terminal_delete) | **DELETE** /terminal/v1/terminal/{id}/ | 
[**terminal_v1_terminal_list**](TerminalTerminalApi.md#terminal_v1_terminal_list) | **GET** /terminal/v1/terminal/ | 
[**terminal_v1_terminal_partial_update**](TerminalTerminalApi.md#terminal_v1_terminal_partial_update) | **PATCH** /terminal/v1/terminal/{id}/ | 
[**terminal_v1_terminal_read**](TerminalTerminalApi.md#terminal_v1_terminal_read) | **GET** /terminal/v1/terminal/{id}/ | 
[**terminal_v1_terminal_sessions_create**](TerminalTerminalApi.md#terminal_v1_terminal_sessions_create) | **POST** /terminal/v1/terminal/{terminal}/sessions/ | 
[**terminal_v1_terminal_sessions_delete**](TerminalTerminalApi.md#terminal_v1_terminal_sessions_delete) | **DELETE** /terminal/v1/terminal/{terminal}/sessions/ | 
[**terminal_v1_terminal_sessions_delete_0**](TerminalTerminalApi.md#terminal_v1_terminal_sessions_delete_0) | **DELETE** /terminal/v1/terminal/{terminal}/sessions/{id}/ | 
[**terminal_v1_terminal_sessions_list**](TerminalTerminalApi.md#terminal_v1_terminal_sessions_list) | **GET** /terminal/v1/terminal/{terminal}/sessions/ | 
[**terminal_v1_terminal_sessions_partial_update**](TerminalTerminalApi.md#terminal_v1_terminal_sessions_partial_update) | **PATCH** /terminal/v1/terminal/{terminal}/sessions/ | 
[**terminal_v1_terminal_sessions_partial_update_0**](TerminalTerminalApi.md#terminal_v1_terminal_sessions_partial_update_0) | **PATCH** /terminal/v1/terminal/{terminal}/sessions/{id}/ | 
[**terminal_v1_terminal_sessions_read**](TerminalTerminalApi.md#terminal_v1_terminal_sessions_read) | **GET** /terminal/v1/terminal/{terminal}/sessions/{id}/ | 
[**terminal_v1_terminal_sessions_update**](TerminalTerminalApi.md#terminal_v1_terminal_sessions_update) | **PUT** /terminal/v1/terminal/{terminal}/sessions/ | 
[**terminal_v1_terminal_sessions_update_0**](TerminalTerminalApi.md#terminal_v1_terminal_sessions_update_0) | **PUT** /terminal/v1/terminal/{terminal}/sessions/{id}/ | 
[**terminal_v1_terminal_status_create**](TerminalTerminalApi.md#terminal_v1_terminal_status_create) | **POST** /terminal/v1/terminal/{terminal}/status/ | 
[**terminal_v1_terminal_status_delete**](TerminalTerminalApi.md#terminal_v1_terminal_status_delete) | **DELETE** /terminal/v1/terminal/{terminal}/status/{id}/ | 
[**terminal_v1_terminal_status_list**](TerminalTerminalApi.md#terminal_v1_terminal_status_list) | **GET** /terminal/v1/terminal/{terminal}/status/ | 
[**terminal_v1_terminal_status_partial_update**](TerminalTerminalApi.md#terminal_v1_terminal_status_partial_update) | **PATCH** /terminal/v1/terminal/{terminal}/status/{id}/ | 
[**terminal_v1_terminal_status_read**](TerminalTerminalApi.md#terminal_v1_terminal_status_read) | **GET** /terminal/v1/terminal/{terminal}/status/{id}/ | 
[**terminal_v1_terminal_status_update**](TerminalTerminalApi.md#terminal_v1_terminal_status_update) | **PUT** /terminal/v1/terminal/{terminal}/status/{id}/ | 
[**terminal_v1_terminal_update**](TerminalTerminalApi.md#terminal_v1_terminal_update) | **PUT** /terminal/v1/terminal/{id}/ | 


# **terminal_v1_terminal_access_key_list**
> terminal_v1_terminal_access_key_list(terminal)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
terminal = 'terminal_example' # str | 

try:
    api_instance.terminal_v1_terminal_access_key_list(terminal)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_access_key_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_config_list**
> terminal_v1_terminal_config_list()





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))

try:
    api_instance.terminal_v1_terminal_config_list()
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_config_list: %s\n" % e)
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

# **terminal_v1_terminal_create**
> Terminal terminal_v1_terminal_create(data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
data = swagger_client.Terminal() # Terminal | 

try:
    api_response = api_instance.terminal_v1_terminal_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Terminal**](Terminal.md)|  | 

### Return type

[**Terminal**](Terminal.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_delete**
> terminal_v1_terminal_delete(id)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this terminal.

try:
    api_instance.terminal_v1_terminal_delete(id)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this terminal. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_list**
> list[Terminal] terminal_v1_terminal_list(search=search, order=order)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.terminal_v1_terminal_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Terminal]**](Terminal.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_partial_update**
> Terminal terminal_v1_terminal_partial_update(id, data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this terminal.
data = swagger_client.Terminal() # Terminal | 

try:
    api_response = api_instance.terminal_v1_terminal_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this terminal. | 
 **data** | [**Terminal**](Terminal.md)|  | 

### Return type

[**Terminal**](Terminal.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_read**
> Terminal terminal_v1_terminal_read(id)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this terminal.

try:
    api_response = api_instance.terminal_v1_terminal_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this terminal. | 

### Return type

[**Terminal**](Terminal.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_sessions_create**
> Session terminal_v1_terminal_sessions_create(terminal, data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
terminal = 'terminal_example' # str | 
data = swagger_client.Session() # Session | 

try:
    api_response = api_instance.terminal_v1_terminal_sessions_create(terminal, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_sessions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal** | **str**|  | 
 **data** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_sessions_delete**
> terminal_v1_terminal_sessions_delete(terminal, user=user, asset=asset, system_user=system_user, remote_addr=remote_addr, protocol=protocol, terminal2=terminal2, is_finished=is_finished, search=search, order=order)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
terminal = 'terminal_example' # str | 
user = 'user_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
system_user = 'system_user_example' # str |  (optional)
remote_addr = 'remote_addr_example' # str |  (optional)
protocol = 'protocol_example' # str |  (optional)
terminal2 = 'terminal_example' # str |  (optional)
is_finished = 'is_finished_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.terminal_v1_terminal_sessions_delete(terminal, user=user, asset=asset, system_user=system_user, remote_addr=remote_addr, protocol=protocol, terminal2=terminal2, is_finished=is_finished, search=search, order=order)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_sessions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal** | **str**|  | 
 **user** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **system_user** | **str**|  | [optional] 
 **remote_addr** | **str**|  | [optional] 
 **protocol** | **str**|  | [optional] 
 **terminal2** | **str**|  | [optional] 
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

# **terminal_v1_terminal_sessions_delete_0**
> terminal_v1_terminal_sessions_delete_0(id, terminal)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this session.
terminal = 'terminal_example' # str | 

try:
    api_instance.terminal_v1_terminal_sessions_delete_0(id, terminal)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_sessions_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this session. | 
 **terminal** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_sessions_list**
> InlineResponse20020 terminal_v1_terminal_sessions_list(terminal, user=user, asset=asset, system_user=system_user, remote_addr=remote_addr, protocol=protocol, terminal2=terminal2, is_finished=is_finished, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
terminal = 'terminal_example' # str | 
user = 'user_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
system_user = 'system_user_example' # str |  (optional)
remote_addr = 'remote_addr_example' # str |  (optional)
protocol = 'protocol_example' # str |  (optional)
terminal2 = 'terminal_example' # str |  (optional)
is_finished = 'is_finished_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.terminal_v1_terminal_sessions_list(terminal, user=user, asset=asset, system_user=system_user, remote_addr=remote_addr, protocol=protocol, terminal2=terminal2, is_finished=is_finished, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_sessions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal** | **str**|  | 
 **user** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **system_user** | **str**|  | [optional] 
 **remote_addr** | **str**|  | [optional] 
 **protocol** | **str**|  | [optional] 
 **terminal2** | **str**|  | [optional] 
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

# **terminal_v1_terminal_sessions_partial_update**
> Session terminal_v1_terminal_sessions_partial_update(terminal, data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
terminal = 'terminal_example' # str | 
data = swagger_client.Session() # Session | 

try:
    api_response = api_instance.terminal_v1_terminal_sessions_partial_update(terminal, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_sessions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal** | **str**|  | 
 **data** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_sessions_partial_update_0**
> Session terminal_v1_terminal_sessions_partial_update_0(id, terminal, data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this session.
terminal = 'terminal_example' # str | 
data = swagger_client.Session() # Session | 

try:
    api_response = api_instance.terminal_v1_terminal_sessions_partial_update_0(id, terminal, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_sessions_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this session. | 
 **terminal** | **str**|  | 
 **data** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_sessions_read**
> Session terminal_v1_terminal_sessions_read(id, terminal)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this session.
terminal = 'terminal_example' # str | 

try:
    api_response = api_instance.terminal_v1_terminal_sessions_read(id, terminal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_sessions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this session. | 
 **terminal** | **str**|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_sessions_update**
> Session terminal_v1_terminal_sessions_update(terminal, data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
terminal = 'terminal_example' # str | 
data = swagger_client.Session() # Session | 

try:
    api_response = api_instance.terminal_v1_terminal_sessions_update(terminal, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_sessions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal** | **str**|  | 
 **data** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_sessions_update_0**
> Session terminal_v1_terminal_sessions_update_0(id, terminal, data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this session.
terminal = 'terminal_example' # str | 
data = swagger_client.Session() # Session | 

try:
    api_response = api_instance.terminal_v1_terminal_sessions_update_0(id, terminal, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_sessions_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this session. | 
 **terminal** | **str**|  | 
 **data** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_status_create**
> Status terminal_v1_terminal_status_create(terminal, data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
terminal = 'terminal_example' # str | 
data = swagger_client.Status() # Status | 

try:
    api_response = api_instance.terminal_v1_terminal_status_create(terminal, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_status_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal** | **str**|  | 
 **data** | [**Status**](Status.md)|  | 

### Return type

[**Status**](Status.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_status_delete**
> terminal_v1_terminal_status_delete(id, terminal)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this status.
terminal = 'terminal_example' # str | 

try:
    api_instance.terminal_v1_terminal_status_delete(id, terminal)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_status_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this status. | 
 **terminal** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_status_list**
> list[Status] terminal_v1_terminal_status_list(terminal, search=search, order=order)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
terminal = 'terminal_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.terminal_v1_terminal_status_list(terminal, search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_status_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal** | **str**|  | 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Status]**](Status.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_status_partial_update**
> Status terminal_v1_terminal_status_partial_update(id, terminal, data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this status.
terminal = 'terminal_example' # str | 
data = swagger_client.Status() # Status | 

try:
    api_response = api_instance.terminal_v1_terminal_status_partial_update(id, terminal, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_status_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this status. | 
 **terminal** | **str**|  | 
 **data** | [**Status**](Status.md)|  | 

### Return type

[**Status**](Status.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_status_read**
> Status terminal_v1_terminal_status_read(id, terminal)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this status.
terminal = 'terminal_example' # str | 

try:
    api_response = api_instance.terminal_v1_terminal_status_read(id, terminal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_status_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this status. | 
 **terminal** | **str**|  | 

### Return type

[**Status**](Status.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_status_update**
> Status terminal_v1_terminal_status_update(id, terminal, data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this status.
terminal = 'terminal_example' # str | 
data = swagger_client.Status() # Status | 

try:
    api_response = api_instance.terminal_v1_terminal_status_update(id, terminal, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this status. | 
 **terminal** | **str**|  | 
 **data** | [**Status**](Status.md)|  | 

### Return type

[**Status**](Status.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminal_v1_terminal_update**
> Terminal terminal_v1_terminal_update(id, data)





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
api_instance = swagger_client.TerminalTerminalApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this terminal.
data = swagger_client.Terminal() # Terminal | 

try:
    api_response = api_instance.terminal_v1_terminal_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalTerminalApi->terminal_v1_terminal_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this terminal. | 
 **data** | [**Terminal**](Terminal.md)|  | 

### Return type

[**Terminal**](Terminal.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

