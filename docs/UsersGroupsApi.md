# swagger_client.UsersGroupsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_v1_groups_create**](UsersGroupsApi.md#users_v1_groups_create) | **POST** /users/v1/groups/ | 
[**users_v1_groups_delete**](UsersGroupsApi.md#users_v1_groups_delete) | **DELETE** /users/v1/groups/ | 
[**users_v1_groups_delete_0**](UsersGroupsApi.md#users_v1_groups_delete_0) | **DELETE** /users/v1/groups/{id}/ | 
[**users_v1_groups_list**](UsersGroupsApi.md#users_v1_groups_list) | **GET** /users/v1/groups/ | 
[**users_v1_groups_partial_update**](UsersGroupsApi.md#users_v1_groups_partial_update) | **PATCH** /users/v1/groups/ | 
[**users_v1_groups_partial_update_0**](UsersGroupsApi.md#users_v1_groups_partial_update_0) | **PATCH** /users/v1/groups/{id}/ | 
[**users_v1_groups_read**](UsersGroupsApi.md#users_v1_groups_read) | **GET** /users/v1/groups/{id}/ | 
[**users_v1_groups_update**](UsersGroupsApi.md#users_v1_groups_update) | **PUT** /users/v1/groups/ | 
[**users_v1_groups_update_0**](UsersGroupsApi.md#users_v1_groups_update_0) | **PUT** /users/v1/groups/{id}/ | 
[**users_v1_groups_users_partial_update**](UsersGroupsApi.md#users_v1_groups_users_partial_update) | **PATCH** /users/v1/groups/{id}/users/ | 
[**users_v1_groups_users_read**](UsersGroupsApi.md#users_v1_groups_users_read) | **GET** /users/v1/groups/{id}/users/ | 
[**users_v1_groups_users_update**](UsersGroupsApi.md#users_v1_groups_users_update) | **PUT** /users/v1/groups/{id}/users/ | 


# **users_v1_groups_create**
> UserGroup users_v1_groups_create(data)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
data = swagger_client.UserGroup() # UserGroup | 

try:
    api_response = api_instance.users_v1_groups_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_groups_delete**
> users_v1_groups_delete(name=name, search=search, order=order)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.users_v1_groups_delete(name=name, search=search, order=order)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_delete: %s\n" % e)
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

# **users_v1_groups_delete_0**
> users_v1_groups_delete_0(id)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户组.

try:
    api_instance.users_v1_groups_delete_0(id)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户组. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_groups_list**
> InlineResponse20021 users_v1_groups_list(name=name, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.users_v1_groups_list(name=name, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_list: %s\n" % e)
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

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_groups_partial_update**
> UserGroup users_v1_groups_partial_update(data)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
data = swagger_client.UserGroup() # UserGroup | 

try:
    api_response = api_instance.users_v1_groups_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_groups_partial_update_0**
> UserGroup users_v1_groups_partial_update_0(id, data)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户组.
data = swagger_client.UserGroup() # UserGroup | 

try:
    api_response = api_instance.users_v1_groups_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户组. | 
 **data** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_groups_read**
> UserGroup users_v1_groups_read(id)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户组.

try:
    api_response = api_instance.users_v1_groups_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户组. | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_groups_update**
> UserGroup users_v1_groups_update(data)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
data = swagger_client.UserGroup() # UserGroup | 

try:
    api_response = api_instance.users_v1_groups_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_groups_update_0**
> UserGroup users_v1_groups_update_0(id, data)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户组.
data = swagger_client.UserGroup() # UserGroup | 

try:
    api_response = api_instance.users_v1_groups_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户组. | 
 **data** | [**UserGroup**](UserGroup.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_groups_users_partial_update**
> UserGroupUpdateMember users_v1_groups_users_partial_update(id, data)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户组.
data = swagger_client.UserGroupUpdateMember() # UserGroupUpdateMember | 

try:
    api_response = api_instance.users_v1_groups_users_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_users_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户组. | 
 **data** | [**UserGroupUpdateMember**](UserGroupUpdateMember.md)|  | 

### Return type

[**UserGroupUpdateMember**](UserGroupUpdateMember.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_groups_users_read**
> UserGroupUpdateMember users_v1_groups_users_read(id)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户组.

try:
    api_response = api_instance.users_v1_groups_users_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_users_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户组. | 

### Return type

[**UserGroupUpdateMember**](UserGroupUpdateMember.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_groups_users_update**
> UserGroupUpdateMember users_v1_groups_users_update(id, data)





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
api_instance = swagger_client.UsersGroupsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户组.
data = swagger_client.UserGroupUpdateMember() # UserGroupUpdateMember | 

try:
    api_response = api_instance.users_v1_groups_users_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->users_v1_groups_users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户组. | 
 **data** | [**UserGroupUpdateMember**](UserGroupUpdateMember.md)|  | 

### Return type

[**UserGroupUpdateMember**](UserGroupUpdateMember.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

