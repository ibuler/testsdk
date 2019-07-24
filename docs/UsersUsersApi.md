# swagger_client.UsersUsersApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_v1_users_create**](UsersUsersApi.md#users_v1_users_create) | **POST** /users/v1/users/ | 
[**users_v1_users_delete**](UsersUsersApi.md#users_v1_users_delete) | **DELETE** /users/v1/users/ | 
[**users_v1_users_delete_0**](UsersUsersApi.md#users_v1_users_delete_0) | **DELETE** /users/v1/users/{id}/ | 
[**users_v1_users_groups_partial_update**](UsersUsersApi.md#users_v1_users_groups_partial_update) | **PATCH** /users/v1/users/{id}/groups/ | 
[**users_v1_users_groups_read**](UsersUsersApi.md#users_v1_users_groups_read) | **GET** /users/v1/users/{id}/groups/ | 
[**users_v1_users_groups_update**](UsersUsersApi.md#users_v1_users_groups_update) | **PUT** /users/v1/users/{id}/groups/ | 
[**users_v1_users_list**](UsersUsersApi.md#users_v1_users_list) | **GET** /users/v1/users/ | 
[**users_v1_users_otp_reset_read**](UsersUsersApi.md#users_v1_users_otp_reset_read) | **GET** /users/v1/users/{id}/otp/reset/ | 
[**users_v1_users_partial_update**](UsersUsersApi.md#users_v1_users_partial_update) | **PATCH** /users/v1/users/ | 
[**users_v1_users_partial_update_0**](UsersUsersApi.md#users_v1_users_partial_update_0) | **PATCH** /users/v1/users/{id}/ | 
[**users_v1_users_password_partial_update**](UsersUsersApi.md#users_v1_users_password_partial_update) | **PATCH** /users/v1/users/{id}/password/ | 
[**users_v1_users_password_read**](UsersUsersApi.md#users_v1_users_password_read) | **GET** /users/v1/users/{id}/password/ | 
[**users_v1_users_password_reset_partial_update**](UsersUsersApi.md#users_v1_users_password_reset_partial_update) | **PATCH** /users/v1/users/{id}/password/reset/ | 
[**users_v1_users_password_reset_update**](UsersUsersApi.md#users_v1_users_password_reset_update) | **PUT** /users/v1/users/{id}/password/reset/ | 
[**users_v1_users_password_update**](UsersUsersApi.md#users_v1_users_password_update) | **PUT** /users/v1/users/{id}/password/ | 
[**users_v1_users_pubkey_reset_partial_update**](UsersUsersApi.md#users_v1_users_pubkey_reset_partial_update) | **PATCH** /users/v1/users/{id}/pubkey/reset/ | 
[**users_v1_users_pubkey_reset_update**](UsersUsersApi.md#users_v1_users_pubkey_reset_update) | **PUT** /users/v1/users/{id}/pubkey/reset/ | 
[**users_v1_users_pubkey_update_partial_update**](UsersUsersApi.md#users_v1_users_pubkey_update_partial_update) | **PATCH** /users/v1/users/{id}/pubkey/update/ | 
[**users_v1_users_pubkey_update_update**](UsersUsersApi.md#users_v1_users_pubkey_update_update) | **PUT** /users/v1/users/{id}/pubkey/update/ | 
[**users_v1_users_read**](UsersUsersApi.md#users_v1_users_read) | **GET** /users/v1/users/{id}/ | 
[**users_v1_users_unblock_partial_update**](UsersUsersApi.md#users_v1_users_unblock_partial_update) | **PATCH** /users/v1/users/{id}/unblock/ | 
[**users_v1_users_unblock_update**](UsersUsersApi.md#users_v1_users_unblock_update) | **PUT** /users/v1/users/{id}/unblock/ | 
[**users_v1_users_update**](UsersUsersApi.md#users_v1_users_update) | **PUT** /users/v1/users/ | 
[**users_v1_users_update_0**](UsersUsersApi.md#users_v1_users_update_0) | **PUT** /users/v1/users/{id}/ | 


# **users_v1_users_create**
> User users_v1_users_create(data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_delete**
> users_v1_users_delete(username=username, email=email, name=name, id=id, search=search, order=order)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str |  (optional)
email = 'email_example' # str |  (optional)
name = 'name_example' # str |  (optional)
id = 'id_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.users_v1_users_delete(username=username, email=email, name=name, id=id, search=search, order=order)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
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

# **users_v1_users_delete_0**
> users_v1_users_delete_0(id)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.

try:
    api_instance.users_v1_users_delete_0(id)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_groups_partial_update**
> UserUpdateGroup users_v1_users_groups_partial_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.UserUpdateGroup() # UserUpdateGroup | 

try:
    api_response = api_instance.users_v1_users_groups_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**UserUpdateGroup**](UserUpdateGroup.md)|  | 

### Return type

[**UserUpdateGroup**](UserUpdateGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_groups_read**
> UserUpdateGroup users_v1_users_groups_read(id)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.

try:
    api_response = api_instance.users_v1_users_groups_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 

### Return type

[**UserUpdateGroup**](UserUpdateGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_groups_update**
> UserUpdateGroup users_v1_users_groups_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.UserUpdateGroup() # UserUpdateGroup | 

try:
    api_response = api_instance.users_v1_users_groups_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**UserUpdateGroup**](UserUpdateGroup.md)|  | 

### Return type

[**UserUpdateGroup**](UserUpdateGroup.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_list**
> InlineResponse20022 users_v1_users_list(username=username, email=email, name=name, id=id, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str |  (optional)
email = 'email_example' # str |  (optional)
name = 'name_example' # str |  (optional)
id = 'id_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.users_v1_users_list(username=username, email=email, name=name, id=id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_otp_reset_read**
> users_v1_users_otp_reset_read(id)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.

try:
    api_instance.users_v1_users_otp_reset_read(id)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_otp_reset_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_partial_update**
> User users_v1_users_partial_update(data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_partial_update_0**
> User users_v1_users_partial_update_0(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_password_partial_update**
> ChangeUserPassword users_v1_users_password_partial_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.ChangeUserPassword() # ChangeUserPassword | 

try:
    api_response = api_instance.users_v1_users_password_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_password_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**ChangeUserPassword**](ChangeUserPassword.md)|  | 

### Return type

[**ChangeUserPassword**](ChangeUserPassword.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_password_read**
> ChangeUserPassword users_v1_users_password_read(id)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.

try:
    api_response = api_instance.users_v1_users_password_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_password_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 

### Return type

[**ChangeUserPassword**](ChangeUserPassword.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_password_reset_partial_update**
> User users_v1_users_password_reset_partial_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_password_reset_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_password_reset_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_password_reset_update**
> User users_v1_users_password_reset_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_password_reset_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_password_reset_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_password_update**
> ChangeUserPassword users_v1_users_password_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.ChangeUserPassword() # ChangeUserPassword | 

try:
    api_response = api_instance.users_v1_users_password_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_password_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**ChangeUserPassword**](ChangeUserPassword.md)|  | 

### Return type

[**ChangeUserPassword**](ChangeUserPassword.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_pubkey_reset_partial_update**
> User users_v1_users_pubkey_reset_partial_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_pubkey_reset_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_pubkey_reset_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_pubkey_reset_update**
> User users_v1_users_pubkey_reset_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_pubkey_reset_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_pubkey_reset_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_pubkey_update_partial_update**
> UserPKUpdate users_v1_users_pubkey_update_partial_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.UserPKUpdate() # UserPKUpdate | 

try:
    api_response = api_instance.users_v1_users_pubkey_update_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_pubkey_update_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**UserPKUpdate**](UserPKUpdate.md)|  | 

### Return type

[**UserPKUpdate**](UserPKUpdate.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_pubkey_update_update**
> UserPKUpdate users_v1_users_pubkey_update_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.UserPKUpdate() # UserPKUpdate | 

try:
    api_response = api_instance.users_v1_users_pubkey_update_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_pubkey_update_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**UserPKUpdate**](UserPKUpdate.md)|  | 

### Return type

[**UserPKUpdate**](UserPKUpdate.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_read**
> User users_v1_users_read(id)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.

try:
    api_response = api_instance.users_v1_users_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_unblock_partial_update**
> User users_v1_users_unblock_partial_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_unblock_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_unblock_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_unblock_update**
> User users_v1_users_unblock_update(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_unblock_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_unblock_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_update**
> User users_v1_users_update(data)



rewrite because limit org_admin update superuser

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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_v1_users_update_0**
> User users_v1_users_update_0(id, data)





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
api_instance = swagger_client.UsersUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 用户.
data = swagger_client.User() # User | 

try:
    api_response = api_instance.users_v1_users_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersUsersApi->users_v1_users_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 用户. | 
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

