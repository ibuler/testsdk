# swagger_client.OrgsOrgsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgs_v1_orgs_create**](OrgsOrgsApi.md#orgs_v1_orgs_create) | **POST** /orgs/v1/orgs/ | 
[**orgs_v1_orgs_delete**](OrgsOrgsApi.md#orgs_v1_orgs_delete) | **DELETE** /orgs/v1/orgs/{id}/ | 
[**orgs_v1_orgs_list**](OrgsOrgsApi.md#orgs_v1_orgs_list) | **GET** /orgs/v1/orgs/ | 
[**orgs_v1_orgs_membership_admins_create**](OrgsOrgsApi.md#orgs_v1_orgs_membership_admins_create) | **POST** /orgs/v1/orgs/{org_id}/membership/admins/ | 
[**orgs_v1_orgs_membership_admins_delete**](OrgsOrgsApi.md#orgs_v1_orgs_membership_admins_delete) | **DELETE** /orgs/v1/orgs/{org_id}/membership/admins/{user_id}/ | 
[**orgs_v1_orgs_membership_admins_list**](OrgsOrgsApi.md#orgs_v1_orgs_membership_admins_list) | **GET** /orgs/v1/orgs/{org_id}/membership/admins/ | 
[**orgs_v1_orgs_membership_admins_read**](OrgsOrgsApi.md#orgs_v1_orgs_membership_admins_read) | **GET** /orgs/v1/orgs/{org_id}/membership/admins/{user_id}/ | 
[**orgs_v1_orgs_membership_users_create**](OrgsOrgsApi.md#orgs_v1_orgs_membership_users_create) | **POST** /orgs/v1/orgs/{org_id}/membership/users/ | 
[**orgs_v1_orgs_membership_users_delete**](OrgsOrgsApi.md#orgs_v1_orgs_membership_users_delete) | **DELETE** /orgs/v1/orgs/{org_id}/membership/users/{user_id}/ | 
[**orgs_v1_orgs_membership_users_list**](OrgsOrgsApi.md#orgs_v1_orgs_membership_users_list) | **GET** /orgs/v1/orgs/{org_id}/membership/users/ | 
[**orgs_v1_orgs_membership_users_read**](OrgsOrgsApi.md#orgs_v1_orgs_membership_users_read) | **GET** /orgs/v1/orgs/{org_id}/membership/users/{user_id}/ | 
[**orgs_v1_orgs_partial_update**](OrgsOrgsApi.md#orgs_v1_orgs_partial_update) | **PATCH** /orgs/v1/orgs/{id}/ | 
[**orgs_v1_orgs_read**](OrgsOrgsApi.md#orgs_v1_orgs_read) | **GET** /orgs/v1/orgs/{id}/ | 
[**orgs_v1_orgs_update**](OrgsOrgsApi.md#orgs_v1_orgs_update) | **PUT** /orgs/v1/orgs/{id}/ | 


# **orgs_v1_orgs_create**
> Org orgs_v1_orgs_create(data)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Org() # Org | 

try:
    api_response = api_instance.orgs_v1_orgs_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Org**](Org.md)|  | 

### Return type

[**Org**](Org.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_delete**
> orgs_v1_orgs_delete(id)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 组织.

try:
    api_instance.orgs_v1_orgs_delete(id)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 组织. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_list**
> list[OrgRead] orgs_v1_orgs_list(search=search, order=order)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.orgs_v1_orgs_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[OrgRead]**](OrgRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_membership_admins_create**
> OrgMembershipAdmin orgs_v1_orgs_membership_admins_create(org_id, data)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
org_id = 'org_id_example' # str | 
data = swagger_client.OrgMembershipAdmin() # OrgMembershipAdmin | 

try:
    api_response = api_instance.orgs_v1_orgs_membership_admins_create(org_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_membership_admins_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **data** | [**OrgMembershipAdmin**](OrgMembershipAdmin.md)|  | 

### Return type

[**OrgMembershipAdmin**](OrgMembershipAdmin.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_membership_admins_delete**
> orgs_v1_orgs_membership_admins_delete(org_id, user_id)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
org_id = 'org_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.orgs_v1_orgs_membership_admins_delete(org_id, user_id)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_membership_admins_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_membership_admins_list**
> list[OrgMembershipAdmin] orgs_v1_orgs_membership_admins_list(org_id, search=search, order=order)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
org_id = 'org_id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.orgs_v1_orgs_membership_admins_list(org_id, search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_membership_admins_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[OrgMembershipAdmin]**](OrgMembershipAdmin.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_membership_admins_read**
> OrgMembershipAdmin orgs_v1_orgs_membership_admins_read(org_id, user_id)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
org_id = 'org_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.orgs_v1_orgs_membership_admins_read(org_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_membership_admins_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**OrgMembershipAdmin**](OrgMembershipAdmin.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_membership_users_create**
> OrgMembershipUser orgs_v1_orgs_membership_users_create(org_id, data)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
org_id = 'org_id_example' # str | 
data = swagger_client.OrgMembershipUser() # OrgMembershipUser | 

try:
    api_response = api_instance.orgs_v1_orgs_membership_users_create(org_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_membership_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **data** | [**OrgMembershipUser**](OrgMembershipUser.md)|  | 

### Return type

[**OrgMembershipUser**](OrgMembershipUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_membership_users_delete**
> orgs_v1_orgs_membership_users_delete(org_id, user_id)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
org_id = 'org_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.orgs_v1_orgs_membership_users_delete(org_id, user_id)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_membership_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_membership_users_list**
> list[OrgMembershipUser] orgs_v1_orgs_membership_users_list(org_id, search=search, order=order)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
org_id = 'org_id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.orgs_v1_orgs_membership_users_list(org_id, search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_membership_users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[OrgMembershipUser]**](OrgMembershipUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_membership_users_read**
> OrgMembershipUser orgs_v1_orgs_membership_users_read(org_id, user_id)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
org_id = 'org_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.orgs_v1_orgs_membership_users_read(org_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_membership_users_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**OrgMembershipUser**](OrgMembershipUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_partial_update**
> Org orgs_v1_orgs_partial_update(id, data)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 组织.
data = swagger_client.Org() # Org | 

try:
    api_response = api_instance.orgs_v1_orgs_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 组织. | 
 **data** | [**Org**](Org.md)|  | 

### Return type

[**Org**](Org.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_read**
> OrgRead orgs_v1_orgs_read(id)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 组织.

try:
    api_response = api_instance.orgs_v1_orgs_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 组织. | 

### Return type

[**OrgRead**](OrgRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_v1_orgs_update**
> Org orgs_v1_orgs_update(id, data)





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
api_instance = swagger_client.OrgsOrgsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 组织.
data = swagger_client.Org() # Org | 

try:
    api_response = api_instance.orgs_v1_orgs_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsOrgsApi->orgs_v1_orgs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 组织. | 
 **data** | [**Org**](Org.md)|  | 

### Return type

[**Org**](Org.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

