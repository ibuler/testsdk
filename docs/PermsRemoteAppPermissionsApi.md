# swagger_client.PermsRemoteAppPermissionsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perms_v1_remote_app_permissions_create**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_create) | **POST** /perms/v1/remote-app-permissions/ | 
[**perms_v1_remote_app_permissions_delete**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_delete) | **DELETE** /perms/v1/remote-app-permissions/{id}/ | 
[**perms_v1_remote_app_permissions_list**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_list) | **GET** /perms/v1/remote-app-permissions/ | 
[**perms_v1_remote_app_permissions_partial_update**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_partial_update) | **PATCH** /perms/v1/remote-app-permissions/{id}/ | 
[**perms_v1_remote_app_permissions_read**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_read) | **GET** /perms/v1/remote-app-permissions/{id}/ | 
[**perms_v1_remote_app_permissions_remote_app_add_partial_update**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_remote_app_add_partial_update) | **PATCH** /perms/v1/remote-app-permissions/{id}/remote-app/add/ | 
[**perms_v1_remote_app_permissions_remote_app_add_read**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_remote_app_add_read) | **GET** /perms/v1/remote-app-permissions/{id}/remote-app/add/ | 
[**perms_v1_remote_app_permissions_remote_app_add_update**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_remote_app_add_update) | **PUT** /perms/v1/remote-app-permissions/{id}/remote-app/add/ | 
[**perms_v1_remote_app_permissions_remote_app_remove_partial_update**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_remote_app_remove_partial_update) | **PATCH** /perms/v1/remote-app-permissions/{id}/remote-app/remove/ | 
[**perms_v1_remote_app_permissions_remote_app_remove_read**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_remote_app_remove_read) | **GET** /perms/v1/remote-app-permissions/{id}/remote-app/remove/ | 
[**perms_v1_remote_app_permissions_remote_app_remove_update**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_remote_app_remove_update) | **PUT** /perms/v1/remote-app-permissions/{id}/remote-app/remove/ | 
[**perms_v1_remote_app_permissions_update**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_update) | **PUT** /perms/v1/remote-app-permissions/{id}/ | 
[**perms_v1_remote_app_permissions_user_add_partial_update**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_user_add_partial_update) | **PATCH** /perms/v1/remote-app-permissions/{id}/user/add/ | 
[**perms_v1_remote_app_permissions_user_add_read**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_user_add_read) | **GET** /perms/v1/remote-app-permissions/{id}/user/add/ | 
[**perms_v1_remote_app_permissions_user_add_update**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_user_add_update) | **PUT** /perms/v1/remote-app-permissions/{id}/user/add/ | 
[**perms_v1_remote_app_permissions_user_remove_partial_update**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_user_remove_partial_update) | **PATCH** /perms/v1/remote-app-permissions/{id}/user/remove/ | 
[**perms_v1_remote_app_permissions_user_remove_read**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_user_remove_read) | **GET** /perms/v1/remote-app-permissions/{id}/user/remove/ | 
[**perms_v1_remote_app_permissions_user_remove_update**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_user_remove_update) | **PUT** /perms/v1/remote-app-permissions/{id}/user/remove/ | 
[**perms_v1_remote_app_permissions_user_validate_list**](PermsRemoteAppPermissionsApi.md#perms_v1_remote_app_permissions_user_validate_list) | **GET** /perms/v1/remote-app-permissions/user/validate/ | 


# **perms_v1_remote_app_permissions_create**
> RemoteAppPermission perms_v1_remote_app_permissions_create(data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
data = swagger_client.RemoteAppPermission() # RemoteAppPermission | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RemoteAppPermission**](RemoteAppPermission.md)|  | 

### Return type

[**RemoteAppPermission**](RemoteAppPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_delete**
> perms_v1_remote_app_permissions_delete(id)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.

try:
    api_instance.perms_v1_remote_app_permissions_delete(id)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_list**
> InlineResponse20014 perms_v1_remote_app_permissions_list(name=name, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_remote_app_permissions_list(name=name, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_list: %s\n" % e)
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

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_partial_update**
> RemoteAppPermission perms_v1_remote_app_permissions_partial_update(id, data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.
data = swagger_client.RemoteAppPermission() # RemoteAppPermission | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 
 **data** | [**RemoteAppPermission**](RemoteAppPermission.md)|  | 

### Return type

[**RemoteAppPermission**](RemoteAppPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_read**
> RemoteAppPermission perms_v1_remote_app_permissions_read(id)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.

try:
    api_response = api_instance.perms_v1_remote_app_permissions_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 

### Return type

[**RemoteAppPermission**](RemoteAppPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_remote_app_add_partial_update**
> RemoteAppPermissionUpdateRemoteApp perms_v1_remote_app_permissions_remote_app_add_partial_update(id, data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.
data = swagger_client.RemoteAppPermissionUpdateRemoteApp() # RemoteAppPermissionUpdateRemoteApp | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_remote_app_add_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_remote_app_add_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 
 **data** | [**RemoteAppPermissionUpdateRemoteApp**](RemoteAppPermissionUpdateRemoteApp.md)|  | 

### Return type

[**RemoteAppPermissionUpdateRemoteApp**](RemoteAppPermissionUpdateRemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_remote_app_add_read**
> RemoteAppPermissionUpdateRemoteApp perms_v1_remote_app_permissions_remote_app_add_read(id)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.

try:
    api_response = api_instance.perms_v1_remote_app_permissions_remote_app_add_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_remote_app_add_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 

### Return type

[**RemoteAppPermissionUpdateRemoteApp**](RemoteAppPermissionUpdateRemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_remote_app_add_update**
> RemoteAppPermissionUpdateRemoteApp perms_v1_remote_app_permissions_remote_app_add_update(id, data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.
data = swagger_client.RemoteAppPermissionUpdateRemoteApp() # RemoteAppPermissionUpdateRemoteApp | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_remote_app_add_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_remote_app_add_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 
 **data** | [**RemoteAppPermissionUpdateRemoteApp**](RemoteAppPermissionUpdateRemoteApp.md)|  | 

### Return type

[**RemoteAppPermissionUpdateRemoteApp**](RemoteAppPermissionUpdateRemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_remote_app_remove_partial_update**
> RemoteAppPermissionUpdateRemoteApp perms_v1_remote_app_permissions_remote_app_remove_partial_update(id, data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.
data = swagger_client.RemoteAppPermissionUpdateRemoteApp() # RemoteAppPermissionUpdateRemoteApp | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_remote_app_remove_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_remote_app_remove_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 
 **data** | [**RemoteAppPermissionUpdateRemoteApp**](RemoteAppPermissionUpdateRemoteApp.md)|  | 

### Return type

[**RemoteAppPermissionUpdateRemoteApp**](RemoteAppPermissionUpdateRemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_remote_app_remove_read**
> RemoteAppPermissionUpdateRemoteApp perms_v1_remote_app_permissions_remote_app_remove_read(id)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.

try:
    api_response = api_instance.perms_v1_remote_app_permissions_remote_app_remove_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_remote_app_remove_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 

### Return type

[**RemoteAppPermissionUpdateRemoteApp**](RemoteAppPermissionUpdateRemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_remote_app_remove_update**
> RemoteAppPermissionUpdateRemoteApp perms_v1_remote_app_permissions_remote_app_remove_update(id, data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.
data = swagger_client.RemoteAppPermissionUpdateRemoteApp() # RemoteAppPermissionUpdateRemoteApp | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_remote_app_remove_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_remote_app_remove_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 
 **data** | [**RemoteAppPermissionUpdateRemoteApp**](RemoteAppPermissionUpdateRemoteApp.md)|  | 

### Return type

[**RemoteAppPermissionUpdateRemoteApp**](RemoteAppPermissionUpdateRemoteApp.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_update**
> RemoteAppPermission perms_v1_remote_app_permissions_update(id, data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.
data = swagger_client.RemoteAppPermission() # RemoteAppPermission | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 
 **data** | [**RemoteAppPermission**](RemoteAppPermission.md)|  | 

### Return type

[**RemoteAppPermission**](RemoteAppPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_user_add_partial_update**
> RemoteAppPermissionUpdateUser perms_v1_remote_app_permissions_user_add_partial_update(id, data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.
data = swagger_client.RemoteAppPermissionUpdateUser() # RemoteAppPermissionUpdateUser | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_user_add_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_user_add_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 
 **data** | [**RemoteAppPermissionUpdateUser**](RemoteAppPermissionUpdateUser.md)|  | 

### Return type

[**RemoteAppPermissionUpdateUser**](RemoteAppPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_user_add_read**
> RemoteAppPermissionUpdateUser perms_v1_remote_app_permissions_user_add_read(id)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.

try:
    api_response = api_instance.perms_v1_remote_app_permissions_user_add_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_user_add_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 

### Return type

[**RemoteAppPermissionUpdateUser**](RemoteAppPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_user_add_update**
> RemoteAppPermissionUpdateUser perms_v1_remote_app_permissions_user_add_update(id, data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.
data = swagger_client.RemoteAppPermissionUpdateUser() # RemoteAppPermissionUpdateUser | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_user_add_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_user_add_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 
 **data** | [**RemoteAppPermissionUpdateUser**](RemoteAppPermissionUpdateUser.md)|  | 

### Return type

[**RemoteAppPermissionUpdateUser**](RemoteAppPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_user_remove_partial_update**
> RemoteAppPermissionUpdateUser perms_v1_remote_app_permissions_user_remove_partial_update(id, data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.
data = swagger_client.RemoteAppPermissionUpdateUser() # RemoteAppPermissionUpdateUser | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_user_remove_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_user_remove_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 
 **data** | [**RemoteAppPermissionUpdateUser**](RemoteAppPermissionUpdateUser.md)|  | 

### Return type

[**RemoteAppPermissionUpdateUser**](RemoteAppPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_user_remove_read**
> RemoteAppPermissionUpdateUser perms_v1_remote_app_permissions_user_remove_read(id)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.

try:
    api_response = api_instance.perms_v1_remote_app_permissions_user_remove_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_user_remove_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 

### Return type

[**RemoteAppPermissionUpdateUser**](RemoteAppPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_user_remove_update**
> RemoteAppPermissionUpdateUser perms_v1_remote_app_permissions_user_remove_update(id, data)





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 远程应用授权.
data = swagger_client.RemoteAppPermissionUpdateUser() # RemoteAppPermissionUpdateUser | 

try:
    api_response = api_instance.perms_v1_remote_app_permissions_user_remove_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_user_remove_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 远程应用授权. | 
 **data** | [**RemoteAppPermissionUpdateUser**](RemoteAppPermissionUpdateUser.md)|  | 

### Return type

[**RemoteAppPermissionUpdateUser**](RemoteAppPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_remote_app_permissions_user_validate_list**
> perms_v1_remote_app_permissions_user_validate_list()





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
api_instance = swagger_client.PermsRemoteAppPermissionsApi(swagger_client.ApiClient(configuration))

try:
    api_instance.perms_v1_remote_app_permissions_user_validate_list()
except ApiException as e:
    print("Exception when calling PermsRemoteAppPermissionsApi->perms_v1_remote_app_permissions_user_validate_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

