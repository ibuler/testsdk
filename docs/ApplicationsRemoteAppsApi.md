# swagger_client.ApplicationsRemoteAppsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_v1_remote_apps_connection_info_read**](ApplicationsRemoteAppsApi.md#applications_v1_remote_apps_connection_info_read) | **GET** /applications/v1/remote-apps/{id}/connection-info/ | 
[**applications_v1_remote_apps_create**](ApplicationsRemoteAppsApi.md#applications_v1_remote_apps_create) | **POST** /applications/v1/remote-apps/ | 
[**applications_v1_remote_apps_delete**](ApplicationsRemoteAppsApi.md#applications_v1_remote_apps_delete) | **DELETE** /applications/v1/remote-apps/ | 
[**applications_v1_remote_apps_delete_0**](ApplicationsRemoteAppsApi.md#applications_v1_remote_apps_delete_0) | **DELETE** /applications/v1/remote-apps/{id}/ | 
[**applications_v1_remote_apps_list**](ApplicationsRemoteAppsApi.md#applications_v1_remote_apps_list) | **GET** /applications/v1/remote-apps/ | 
[**applications_v1_remote_apps_partial_update**](ApplicationsRemoteAppsApi.md#applications_v1_remote_apps_partial_update) | **PATCH** /applications/v1/remote-apps/ | 
[**applications_v1_remote_apps_partial_update_0**](ApplicationsRemoteAppsApi.md#applications_v1_remote_apps_partial_update_0) | **PATCH** /applications/v1/remote-apps/{id}/ | 
[**applications_v1_remote_apps_read**](ApplicationsRemoteAppsApi.md#applications_v1_remote_apps_read) | **GET** /applications/v1/remote-apps/{id}/ | 
[**applications_v1_remote_apps_update**](ApplicationsRemoteAppsApi.md#applications_v1_remote_apps_update) | **PUT** /applications/v1/remote-apps/ | 
[**applications_v1_remote_apps_update_0**](ApplicationsRemoteAppsApi.md#applications_v1_remote_apps_update_0) | **PUT** /applications/v1/remote-apps/{id}/ | 


# **applications_v1_remote_apps_connection_info_read**
> RemoteAppConnectionInfo applications_v1_remote_apps_connection_info_read(id)





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
api_instance = swagger_client.ApplicationsRemoteAppsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用.

try:
    api_response = api_instance.applications_v1_remote_apps_connection_info_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsRemoteAppsApi->applications_v1_remote_apps_connection_info_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用. | 

### Return type

[**RemoteAppConnectionInfo**](RemoteAppConnectionInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_v1_remote_apps_create**
> RemoteApp applications_v1_remote_apps_create(data)





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
api_instance = swagger_client.ApplicationsRemoteAppsApi(swagger_client.ApiClient(configuration))
data = swagger_client.RemoteApp() # RemoteApp | 

try:
    api_response = api_instance.applications_v1_remote_apps_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsRemoteAppsApi->applications_v1_remote_apps_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RemoteApp**](RemoteApp.md)|  | 

### Return type

[**RemoteApp**](RemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_v1_remote_apps_delete**
> applications_v1_remote_apps_delete(name=name, search=search, order=order)





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
api_instance = swagger_client.ApplicationsRemoteAppsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.applications_v1_remote_apps_delete(name=name, search=search, order=order)
except ApiException as e:
    print("Exception when calling ApplicationsRemoteAppsApi->applications_v1_remote_apps_delete: %s\n" % e)
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

# **applications_v1_remote_apps_delete_0**
> applications_v1_remote_apps_delete_0(id)





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
api_instance = swagger_client.ApplicationsRemoteAppsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用.

try:
    api_instance.applications_v1_remote_apps_delete_0(id)
except ApiException as e:
    print("Exception when calling ApplicationsRemoteAppsApi->applications_v1_remote_apps_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_v1_remote_apps_list**
> InlineResponse200 applications_v1_remote_apps_list(name=name, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.ApplicationsRemoteAppsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.applications_v1_remote_apps_list(name=name, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsRemoteAppsApi->applications_v1_remote_apps_list: %s\n" % e)
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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_v1_remote_apps_partial_update**
> RemoteApp applications_v1_remote_apps_partial_update(data)





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
api_instance = swagger_client.ApplicationsRemoteAppsApi(swagger_client.ApiClient(configuration))
data = swagger_client.RemoteApp() # RemoteApp | 

try:
    api_response = api_instance.applications_v1_remote_apps_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsRemoteAppsApi->applications_v1_remote_apps_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RemoteApp**](RemoteApp.md)|  | 

### Return type

[**RemoteApp**](RemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_v1_remote_apps_partial_update_0**
> RemoteApp applications_v1_remote_apps_partial_update_0(id, data)





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
api_instance = swagger_client.ApplicationsRemoteAppsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用.
data = swagger_client.RemoteApp() # RemoteApp | 

try:
    api_response = api_instance.applications_v1_remote_apps_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsRemoteAppsApi->applications_v1_remote_apps_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用. | 
 **data** | [**RemoteApp**](RemoteApp.md)|  | 

### Return type

[**RemoteApp**](RemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_v1_remote_apps_read**
> RemoteApp applications_v1_remote_apps_read(id)





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
api_instance = swagger_client.ApplicationsRemoteAppsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用.

try:
    api_response = api_instance.applications_v1_remote_apps_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsRemoteAppsApi->applications_v1_remote_apps_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用. | 

### Return type

[**RemoteApp**](RemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_v1_remote_apps_update**
> RemoteApp applications_v1_remote_apps_update(data)





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
api_instance = swagger_client.ApplicationsRemoteAppsApi(swagger_client.ApiClient(configuration))
data = swagger_client.RemoteApp() # RemoteApp | 

try:
    api_response = api_instance.applications_v1_remote_apps_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsRemoteAppsApi->applications_v1_remote_apps_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RemoteApp**](RemoteApp.md)|  | 

### Return type

[**RemoteApp**](RemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_v1_remote_apps_update_0**
> RemoteApp applications_v1_remote_apps_update_0(id, data)





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
api_instance = swagger_client.ApplicationsRemoteAppsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用.
data = swagger_client.RemoteApp() # RemoteApp | 

try:
    api_response = api_instance.applications_v1_remote_apps_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsRemoteAppsApi->applications_v1_remote_apps_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用. | 
 **data** | [**RemoteApp**](RemoteApp.md)|  | 

### Return type

[**RemoteApp**](RemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

