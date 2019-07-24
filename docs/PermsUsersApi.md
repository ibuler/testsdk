# swagger_client.PermsUsersApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perms_v1_users_assets_list**](PermsUsersApi.md#perms_v1_users_assets_list) | **GET** /perms/v1/users/assets/ | 
[**perms_v1_users_assets_list_0**](PermsUsersApi.md#perms_v1_users_assets_list_0) | **GET** /perms/v1/users/{id}/assets/ | 
[**perms_v1_users_nodes_assets_list**](PermsUsersApi.md#perms_v1_users_nodes_assets_list) | **GET** /perms/v1/users/nodes-assets/ | 
[**perms_v1_users_nodes_assets_list_0**](PermsUsersApi.md#perms_v1_users_nodes_assets_list_0) | **GET** /perms/v1/users/nodes/{node_id}/assets/ | 
[**perms_v1_users_nodes_assets_list_1**](PermsUsersApi.md#perms_v1_users_nodes_assets_list_1) | **GET** /perms/v1/users/{id}/nodes-assets/ | 
[**perms_v1_users_nodes_assets_list_2**](PermsUsersApi.md#perms_v1_users_nodes_assets_list_2) | **GET** /perms/v1/users/{id}/nodes/{node_id}/assets/ | 
[**perms_v1_users_nodes_assets_tree_list**](PermsUsersApi.md#perms_v1_users_nodes_assets_tree_list) | **GET** /perms/v1/users/nodes-assets/tree/ | 
[**perms_v1_users_nodes_assets_tree_list_0**](PermsUsersApi.md#perms_v1_users_nodes_assets_tree_list_0) | **GET** /perms/v1/users/{id}/nodes-assets/tree/ | 
[**perms_v1_users_nodes_list**](PermsUsersApi.md#perms_v1_users_nodes_list) | **GET** /perms/v1/users/nodes/ | 
[**perms_v1_users_nodes_list_0**](PermsUsersApi.md#perms_v1_users_nodes_list_0) | **GET** /perms/v1/users/{id}/nodes/ | 
[**perms_v1_users_nodes_tree_list**](PermsUsersApi.md#perms_v1_users_nodes_tree_list) | **GET** /perms/v1/users/nodes/tree/ | 
[**perms_v1_users_nodes_tree_list_0**](PermsUsersApi.md#perms_v1_users_nodes_tree_list_0) | **GET** /perms/v1/users/{id}/nodes/tree/ | 
[**perms_v1_users_remote_apps_list**](PermsUsersApi.md#perms_v1_users_remote_apps_list) | **GET** /perms/v1/users/remote-apps/ | 
[**perms_v1_users_remote_apps_list_0**](PermsUsersApi.md#perms_v1_users_remote_apps_list_0) | **GET** /perms/v1/users/{id}/remote-apps/ | 
[**perms_v1_users_remote_apps_tree_list**](PermsUsersApi.md#perms_v1_users_remote_apps_tree_list) | **GET** /perms/v1/users/remote-apps/tree/ | 
[**perms_v1_users_remote_apps_tree_list_0**](PermsUsersApi.md#perms_v1_users_remote_apps_tree_list_0) | **GET** /perms/v1/users/{id}/remote-apps/tree/ | 


# **perms_v1_users_assets_list**
> InlineResponse20015 perms_v1_users_assets_list(search=search, order=order, limit=limit, offset=offset)



用户授权的所有资产

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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_assets_list(search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_assets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_assets_list_0**
> InlineResponse20015 perms_v1_users_assets_list_0(id, search=search, order=order, limit=limit, offset=offset)



用户授权的所有资产

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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_assets_list_0(id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_assets_list_0: %s\n" % e)
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

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_nodes_assets_list**
> InlineResponse20016 perms_v1_users_nodes_assets_list(search=search, order=order, limit=limit, offset=offset)



用户授权的节点并带着节点下资产的api

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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_nodes_assets_list(search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_nodes_assets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_nodes_assets_list_0**
> InlineResponse20015 perms_v1_users_nodes_assets_list_0(node_id, search=search, order=order, limit=limit, offset=offset)



查询用户授权的节点下的资产的api, 与上面api不同的是，只返回某个节点下的资产

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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_nodes_assets_list_0(node_id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_nodes_assets_list_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_nodes_assets_list_1**
> InlineResponse20016 perms_v1_users_nodes_assets_list_1(id, search=search, order=order, limit=limit, offset=offset)



用户授权的节点并带着节点下资产的api

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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_nodes_assets_list_1(id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_nodes_assets_list_1: %s\n" % e)
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

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_nodes_assets_list_2**
> InlineResponse20015 perms_v1_users_nodes_assets_list_2(id, node_id, search=search, order=order, limit=limit, offset=offset)



查询用户授权的节点下的资产的api, 与上面api不同的是，只返回某个节点下的资产

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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
node_id = 'node_id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_nodes_assets_list_2(id, node_id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_nodes_assets_list_2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **node_id** | **str**|  | 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_nodes_assets_tree_list**
> InlineResponse20017 perms_v1_users_nodes_assets_tree_list(search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_nodes_assets_tree_list(search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_nodes_assets_tree_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_nodes_assets_tree_list_0**
> InlineResponse20017 perms_v1_users_nodes_assets_tree_list_0(id, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_nodes_assets_tree_list_0(id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_nodes_assets_tree_list_0: %s\n" % e)
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

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_nodes_list**
> InlineResponse20018 perms_v1_users_nodes_list(search=search, order=order, limit=limit, offset=offset)



查询用户授权的所有节点的API

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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_nodes_list(search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_nodes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_nodes_list_0**
> InlineResponse20018 perms_v1_users_nodes_list_0(id, search=search, order=order, limit=limit, offset=offset)



查询用户授权的所有节点的API

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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_nodes_list_0(id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_nodes_list_0: %s\n" % e)
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

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_nodes_tree_list**
> InlineResponse20017 perms_v1_users_nodes_tree_list(search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_nodes_tree_list(search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_nodes_tree_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_nodes_tree_list_0**
> InlineResponse20017 perms_v1_users_nodes_tree_list_0(id, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_nodes_tree_list_0(id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_nodes_tree_list_0: %s\n" % e)
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

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_remote_apps_list**
> InlineResponse200 perms_v1_users_remote_apps_list(search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_remote_apps_list(search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_remote_apps_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_remote_apps_list_0**
> InlineResponse200 perms_v1_users_remote_apps_list_0(id, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_users_remote_apps_list_0(id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_remote_apps_list_0: %s\n" % e)
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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_remote_apps_tree_list**
> list[TreeNode] perms_v1_users_remote_apps_tree_list(search=search, order=order)





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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.perms_v1_users_remote_apps_tree_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_remote_apps_tree_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[TreeNode]**](TreeNode.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_users_remote_apps_tree_list_0**
> list[TreeNode] perms_v1_users_remote_apps_tree_list_0(id, search=search, order=order)





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
api_instance = swagger_client.PermsUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.perms_v1_users_remote_apps_tree_list_0(id, search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsUsersApi->perms_v1_users_remote_apps_tree_list_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[TreeNode]**](TreeNode.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

