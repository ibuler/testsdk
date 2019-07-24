# swagger_client.AssetsAdminUsersApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_v1_admin_users_assets_list**](AssetsAdminUsersApi.md#assets_v1_admin_users_assets_list) | **GET** /assets/v1/admin-users/{id}/assets/ | 
[**assets_v1_admin_users_auth_partial_update**](AssetsAdminUsersApi.md#assets_v1_admin_users_auth_partial_update) | **PATCH** /assets/v1/admin-users/{id}/auth/ | 
[**assets_v1_admin_users_auth_update**](AssetsAdminUsersApi.md#assets_v1_admin_users_auth_update) | **PUT** /assets/v1/admin-users/{id}/auth/ | 
[**assets_v1_admin_users_connective_read**](AssetsAdminUsersApi.md#assets_v1_admin_users_connective_read) | **GET** /assets/v1/admin-users/{id}/connective/ | 
[**assets_v1_admin_users_create**](AssetsAdminUsersApi.md#assets_v1_admin_users_create) | **POST** /assets/v1/admin-users/ | 
[**assets_v1_admin_users_delete**](AssetsAdminUsersApi.md#assets_v1_admin_users_delete) | **DELETE** /assets/v1/admin-users/ | 
[**assets_v1_admin_users_delete_0**](AssetsAdminUsersApi.md#assets_v1_admin_users_delete_0) | **DELETE** /assets/v1/admin-users/{id}/ | 
[**assets_v1_admin_users_list**](AssetsAdminUsersApi.md#assets_v1_admin_users_list) | **GET** /assets/v1/admin-users/ | 
[**assets_v1_admin_users_nodes_partial_update**](AssetsAdminUsersApi.md#assets_v1_admin_users_nodes_partial_update) | **PATCH** /assets/v1/admin-users/{id}/nodes/ | 
[**assets_v1_admin_users_nodes_update**](AssetsAdminUsersApi.md#assets_v1_admin_users_nodes_update) | **PUT** /assets/v1/admin-users/{id}/nodes/ | 
[**assets_v1_admin_users_partial_update**](AssetsAdminUsersApi.md#assets_v1_admin_users_partial_update) | **PATCH** /assets/v1/admin-users/ | 
[**assets_v1_admin_users_partial_update_0**](AssetsAdminUsersApi.md#assets_v1_admin_users_partial_update_0) | **PATCH** /assets/v1/admin-users/{id}/ | 
[**assets_v1_admin_users_read**](AssetsAdminUsersApi.md#assets_v1_admin_users_read) | **GET** /assets/v1/admin-users/{id}/ | 
[**assets_v1_admin_users_update**](AssetsAdminUsersApi.md#assets_v1_admin_users_update) | **PUT** /assets/v1/admin-users/ | 
[**assets_v1_admin_users_update_0**](AssetsAdminUsersApi.md#assets_v1_admin_users_update_0) | **PUT** /assets/v1/admin-users/{id}/ | 


# **assets_v1_admin_users_assets_list**
> InlineResponse2002 assets_v1_admin_users_assets_list(id, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_admin_users_assets_list(id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_assets_list: %s\n" % e)
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

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_auth_partial_update**
> AdminUserAuth assets_v1_admin_users_auth_partial_update(id, data)





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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 管理用户.
data = swagger_client.AdminUserAuth() # AdminUserAuth | 

try:
    api_response = api_instance.assets_v1_admin_users_auth_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_auth_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 管理用户. | 
 **data** | [**AdminUserAuth**](AdminUserAuth.md)|  | 

### Return type

[**AdminUserAuth**](AdminUserAuth.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_auth_update**
> AdminUserAuth assets_v1_admin_users_auth_update(id, data)





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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 管理用户.
data = swagger_client.AdminUserAuth() # AdminUserAuth | 

try:
    api_response = api_instance.assets_v1_admin_users_auth_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_auth_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 管理用户. | 
 **data** | [**AdminUserAuth**](AdminUserAuth.md)|  | 

### Return type

[**AdminUserAuth**](AdminUserAuth.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_connective_read**
> TaskID assets_v1_admin_users_connective_read(id)



Test asset admin user assets_connectivity

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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 管理用户.

try:
    api_response = api_instance.assets_v1_admin_users_connective_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_connective_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 管理用户. | 

### Return type

[**TaskID**](TaskID.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_create**
> AdminUser assets_v1_admin_users_create(data)



Admin user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
data = swagger_client.AdminUser() # AdminUser | 

try:
    api_response = api_instance.assets_v1_admin_users_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AdminUser**](AdminUser.md)|  | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_delete**
> assets_v1_admin_users_delete(name=name, username=username, search=search, order=order)



Admin user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
username = 'username_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.assets_v1_admin_users_delete(name=name, username=username, search=search, order=order)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_delete: %s\n" % e)
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

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_delete_0**
> assets_v1_admin_users_delete_0(id)



Admin user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 管理用户.

try:
    api_instance.assets_v1_admin_users_delete_0(id)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 管理用户. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_list**
> InlineResponse2001 assets_v1_admin_users_list(name=name, username=username, search=search, order=order, limit=limit, offset=offset)



Admin user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
username = 'username_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_admin_users_list(name=name, username=username, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_list: %s\n" % e)
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

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_nodes_partial_update**
> ReplaceNodeAdminUser assets_v1_admin_users_nodes_partial_update(id, data)





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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 管理用户.
data = swagger_client.ReplaceNodeAdminUser() # ReplaceNodeAdminUser | 

try:
    api_response = api_instance.assets_v1_admin_users_nodes_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_nodes_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 管理用户. | 
 **data** | [**ReplaceNodeAdminUser**](ReplaceNodeAdminUser.md)|  | 

### Return type

[**ReplaceNodeAdminUser**](ReplaceNodeAdminUser.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_nodes_update**
> ReplaceNodeAdminUser assets_v1_admin_users_nodes_update(id, data)





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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 管理用户.
data = swagger_client.ReplaceNodeAdminUser() # ReplaceNodeAdminUser | 

try:
    api_response = api_instance.assets_v1_admin_users_nodes_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_nodes_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 管理用户. | 
 **data** | [**ReplaceNodeAdminUser**](ReplaceNodeAdminUser.md)|  | 

### Return type

[**ReplaceNodeAdminUser**](ReplaceNodeAdminUser.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_partial_update**
> AdminUser assets_v1_admin_users_partial_update(data)



Admin user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
data = swagger_client.AdminUser() # AdminUser | 

try:
    api_response = api_instance.assets_v1_admin_users_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AdminUser**](AdminUser.md)|  | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_partial_update_0**
> AdminUser assets_v1_admin_users_partial_update_0(id, data)



Admin user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 管理用户.
data = swagger_client.AdminUser() # AdminUser | 

try:
    api_response = api_instance.assets_v1_admin_users_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 管理用户. | 
 **data** | [**AdminUser**](AdminUser.md)|  | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_read**
> AdminUser assets_v1_admin_users_read(id)



Admin user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 管理用户.

try:
    api_response = api_instance.assets_v1_admin_users_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 管理用户. | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_update**
> AdminUser assets_v1_admin_users_update(data)



Admin user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
data = swagger_client.AdminUser() # AdminUser | 

try:
    api_response = api_instance.assets_v1_admin_users_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AdminUser**](AdminUser.md)|  | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_admin_users_update_0**
> AdminUser assets_v1_admin_users_update_0(id, data)



Admin user api set, for add,delete,update,list,retrieve resource

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
api_instance = swagger_client.AssetsAdminUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 管理用户.
data = swagger_client.AdminUser() # AdminUser | 

try:
    api_response = api_instance.assets_v1_admin_users_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAdminUsersApi->assets_v1_admin_users_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 管理用户. | 
 **data** | [**AdminUser**](AdminUser.md)|  | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

