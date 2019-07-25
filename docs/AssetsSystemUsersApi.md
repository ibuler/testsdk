# swagger_client.AssetsSystemUsersApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_v1_system_users_asset_auth_info_read**](AssetsSystemUsersApi.md#assets_v1_system_users_asset_auth_info_read) | **GET** /assets/v1/system-users/{id}/asset/{aid}/auth-info/ | 
[**assets_v1_system_users_asset_push_read**](AssetsSystemUsersApi.md#assets_v1_system_users_asset_push_read) | **GET** /assets/v1/system-users/{id}/asset/{aid}/push/ | 
[**assets_v1_system_users_asset_test_read**](AssetsSystemUsersApi.md#assets_v1_system_users_asset_test_read) | **GET** /assets/v1/system-users/{id}/asset/{aid}/test/ | 
[**assets_v1_system_users_assets_list**](AssetsSystemUsersApi.md#assets_v1_system_users_assets_list) | **GET** /assets/v1/system-users/{id}/assets/ | 
[**assets_v1_system_users_auth_info_delete**](AssetsSystemUsersApi.md#assets_v1_system_users_auth_info_delete) | **DELETE** /assets/v1/system-users/{id}/auth-info/ | 
[**assets_v1_system_users_auth_info_partial_update**](AssetsSystemUsersApi.md#assets_v1_system_users_auth_info_partial_update) | **PATCH** /assets/v1/system-users/{id}/auth-info/ | 
[**assets_v1_system_users_auth_info_read**](AssetsSystemUsersApi.md#assets_v1_system_users_auth_info_read) | **GET** /assets/v1/system-users/{id}/auth-info/ | 
[**assets_v1_system_users_auth_info_update**](AssetsSystemUsersApi.md#assets_v1_system_users_auth_info_update) | **PUT** /assets/v1/system-users/{id}/auth-info/ | 
[**assets_v1_system_users_cmd_filter_rules_list**](AssetsSystemUsersApi.md#assets_v1_system_users_cmd_filter_rules_list) | **GET** /assets/v1/system-users/{id}/cmd-filter-rules/ | 
[**assets_v1_system_users_connective_read**](AssetsSystemUsersApi.md#assets_v1_system_users_connective_read) | **GET** /assets/v1/system-users/{id}/connective/ | 
[**assets_v1_system_users_create**](AssetsSystemUsersApi.md#assets_v1_system_users_create) | **POST** /assets/v1/system-users/ | 
[**assets_v1_system_users_delete**](AssetsSystemUsersApi.md#assets_v1_system_users_delete) | **DELETE** /assets/v1/system-users/ | 
[**assets_v1_system_users_delete_0**](AssetsSystemUsersApi.md#assets_v1_system_users_delete_0) | **DELETE** /assets/v1/system-users/{id}/ | 
[**assets_v1_system_users_list**](AssetsSystemUsersApi.md#assets_v1_system_users_list) | **GET** /assets/v1/system-users/ | 
[**assets_v1_system_users_partial_update**](AssetsSystemUsersApi.md#assets_v1_system_users_partial_update) | **PATCH** /assets/v1/system-users/ | 
[**assets_v1_system_users_partial_update_0**](AssetsSystemUsersApi.md#assets_v1_system_users_partial_update_0) | **PATCH** /assets/v1/system-users/{id}/ | 
[**assets_v1_system_users_push_read**](AssetsSystemUsersApi.md#assets_v1_system_users_push_read) | **GET** /assets/v1/system-users/{id}/push/ | 
[**assets_v1_system_users_read**](AssetsSystemUsersApi.md#assets_v1_system_users_read) | **GET** /assets/v1/system-users/{id}/ | 
[**assets_v1_system_users_update**](AssetsSystemUsersApi.md#assets_v1_system_users_update) | **PUT** /assets/v1/system-users/ | 
[**assets_v1_system_users_update_0**](AssetsSystemUsersApi.md#assets_v1_system_users_update_0) | **PUT** /assets/v1/system-users/{id}/ | 


# **assets_v1_system_users_asset_auth_info_read**
> SystemUserAuth assets_v1_system_users_asset_auth_info_read(aid, id)



Get system user with asset auth info

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
aid = 'aid_example' # str | 
id = 'id_example' # str | A UUID string identifying this 系统用户.

try:
    api_response = api_instance.assets_v1_system_users_asset_auth_info_read(aid, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_asset_auth_info_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**|  | 
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 

### Return type

[**SystemUserAuth**](SystemUserAuth.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_asset_push_read**
> TaskID assets_v1_system_users_asset_push_read(aid, id)





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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
aid = 'aid_example' # str | 
id = 'id_example' # str | A UUID string identifying this 系统用户.

try:
    api_response = api_instance.assets_v1_system_users_asset_push_read(aid, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_asset_push_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**|  | 
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 

### Return type

[**TaskID**](TaskID.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_asset_test_read**
> TaskID assets_v1_system_users_asset_test_read(aid, id)





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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
aid = 'aid_example' # str | 
id = 'id_example' # str | A UUID string identifying this 系统用户.

try:
    api_response = api_instance.assets_v1_system_users_asset_test_read(aid, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_asset_test_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**|  | 
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 

### Return type

[**TaskID**](TaskID.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_assets_list**
> InlineResponse2002 assets_v1_system_users_assets_list(id, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_system_users_assets_list(id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_assets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_auth_info_delete**
> assets_v1_system_users_auth_info_delete(id)



Get system user auth info

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 系统用户.

try:
    api_instance.assets_v1_system_users_auth_info_delete(id)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_auth_info_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_auth_info_partial_update**
> SystemUserAuth assets_v1_system_users_auth_info_partial_update(id, data)



Get system user auth info

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 系统用户.
data = swagger_client.SystemUserAuth() # SystemUserAuth | 

try:
    api_response = api_instance.assets_v1_system_users_auth_info_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_auth_info_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 
 **data** | [**SystemUserAuth**](SystemUserAuth.md)|  | 

### Return type

[**SystemUserAuth**](SystemUserAuth.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_auth_info_read**
> SystemUserAuth assets_v1_system_users_auth_info_read(id)



Get system user auth info

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 系统用户.

try:
    api_response = api_instance.assets_v1_system_users_auth_info_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_auth_info_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 

### Return type

[**SystemUserAuth**](SystemUserAuth.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_auth_info_update**
> SystemUserAuth assets_v1_system_users_auth_info_update(id, data)



Get system user auth info

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 系统用户.
data = swagger_client.SystemUserAuth() # SystemUserAuth | 

try:
    api_response = api_instance.assets_v1_system_users_auth_info_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_auth_info_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 
 **data** | [**SystemUserAuth**](SystemUserAuth.md)|  | 

### Return type

[**SystemUserAuth**](SystemUserAuth.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_cmd_filter_rules_list**
> list[CommandFilterRule] assets_v1_system_users_cmd_filter_rules_list(id, search=search, order=order)





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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.assets_v1_system_users_cmd_filter_rules_list(id, search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_cmd_filter_rules_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[CommandFilterRule]**](CommandFilterRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_connective_read**
> CeleryTask assets_v1_system_users_connective_read(id)



Push system user to cluster assets api

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 系统用户.

try:
    api_response = api_instance.assets_v1_system_users_connective_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_connective_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 

### Return type

[**CeleryTask**](CeleryTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_create**
> SystemUser assets_v1_system_users_create(data)



System user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
data = swagger_client.SystemUser() # SystemUser | 

try:
    api_response = api_instance.assets_v1_system_users_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SystemUser**](SystemUser.md)|  | 

### Return type

[**SystemUser**](SystemUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_delete**
> assets_v1_system_users_delete(name=name, username=username, search=search, order=order)



System user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
username = 'username_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.assets_v1_system_users_delete(name=name, username=username, search=search, order=order)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
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

# **assets_v1_system_users_delete_0**
> assets_v1_system_users_delete_0(id)



System user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 系统用户.

try:
    api_instance.assets_v1_system_users_delete_0(id)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_list**
> InlineResponse20011 assets_v1_system_users_list(name=name, username=username, search=search, order=order, limit=limit, offset=offset)



System user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
username = 'username_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_system_users_list(name=name, username=username, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_partial_update**
> SystemUser assets_v1_system_users_partial_update(data)



System user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
data = swagger_client.SystemUser() # SystemUser | 

try:
    api_response = api_instance.assets_v1_system_users_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SystemUser**](SystemUser.md)|  | 

### Return type

[**SystemUser**](SystemUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_partial_update_0**
> SystemUser assets_v1_system_users_partial_update_0(id, data)



System user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 系统用户.
data = swagger_client.SystemUser() # SystemUser | 

try:
    api_response = api_instance.assets_v1_system_users_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 
 **data** | [**SystemUser**](SystemUser.md)|  | 

### Return type

[**SystemUser**](SystemUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_push_read**
> CeleryTask assets_v1_system_users_push_read(id)



Push system user to cluster assets api

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 系统用户.

try:
    api_response = api_instance.assets_v1_system_users_push_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_push_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 

### Return type

[**CeleryTask**](CeleryTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_read**
> SystemUser assets_v1_system_users_read(id)



System user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 系统用户.

try:
    api_response = api_instance.assets_v1_system_users_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 

### Return type

[**SystemUser**](SystemUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_update**
> SystemUser assets_v1_system_users_update(data)



System user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
data = swagger_client.SystemUser() # SystemUser | 

try:
    api_response = api_instance.assets_v1_system_users_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SystemUser**](SystemUser.md)|  | 

### Return type

[**SystemUser**](SystemUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_system_users_update_0**
> SystemUser assets_v1_system_users_update_0(id, data)



System user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsSystemUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 系统用户.
data = swagger_client.SystemUser() # SystemUser | 

try:
    api_response = api_instance.assets_v1_system_users_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsSystemUsersApi->assets_v1_system_users_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 系统用户. | 
 **data** | [**SystemUser**](SystemUser.md)|  | 

### Return type

[**SystemUser**](SystemUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

