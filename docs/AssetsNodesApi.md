# swagger_client.AssetsNodesApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_v1_nodes_assets_add_partial_update**](AssetsNodesApi.md#assets_v1_nodes_assets_add_partial_update) | **PATCH** /assets/v1/nodes/{id}/assets/add/ | 
[**assets_v1_nodes_assets_add_update**](AssetsNodesApi.md#assets_v1_nodes_assets_add_update) | **PUT** /assets/v1/nodes/{id}/assets/add/ | 
[**assets_v1_nodes_assets_list**](AssetsNodesApi.md#assets_v1_nodes_assets_list) | **GET** /assets/v1/nodes/{id}/assets/ | 
[**assets_v1_nodes_assets_remove_partial_update**](AssetsNodesApi.md#assets_v1_nodes_assets_remove_partial_update) | **PATCH** /assets/v1/nodes/{id}/assets/remove/ | 
[**assets_v1_nodes_assets_remove_update**](AssetsNodesApi.md#assets_v1_nodes_assets_remove_update) | **PUT** /assets/v1/nodes/{id}/assets/remove/ | 
[**assets_v1_nodes_assets_replace_partial_update**](AssetsNodesApi.md#assets_v1_nodes_assets_replace_partial_update) | **PATCH** /assets/v1/nodes/{id}/assets/replace/ | 
[**assets_v1_nodes_assets_replace_update**](AssetsNodesApi.md#assets_v1_nodes_assets_replace_update) | **PUT** /assets/v1/nodes/{id}/assets/replace/ | 
[**assets_v1_nodes_children_add_partial_update**](AssetsNodesApi.md#assets_v1_nodes_children_add_partial_update) | **PATCH** /assets/v1/nodes/{id}/children/add/ | 
[**assets_v1_nodes_children_add_update**](AssetsNodesApi.md#assets_v1_nodes_children_add_update) | **PUT** /assets/v1/nodes/{id}/children/add/ | 
[**assets_v1_nodes_children_create**](AssetsNodesApi.md#assets_v1_nodes_children_create) | **POST** /assets/v1/nodes/children/ | 
[**assets_v1_nodes_children_create_0**](AssetsNodesApi.md#assets_v1_nodes_children_create_0) | **POST** /assets/v1/nodes/{id}/children/ | 
[**assets_v1_nodes_children_list**](AssetsNodesApi.md#assets_v1_nodes_children_list) | **GET** /assets/v1/nodes/children/ | 
[**assets_v1_nodes_children_list_0**](AssetsNodesApi.md#assets_v1_nodes_children_list_0) | **GET** /assets/v1/nodes/{id}/children/ | 
[**assets_v1_nodes_children_tree_list**](AssetsNodesApi.md#assets_v1_nodes_children_tree_list) | **GET** /assets/v1/nodes/children/tree/ | 
[**assets_v1_nodes_create**](AssetsNodesApi.md#assets_v1_nodes_create) | **POST** /assets/v1/nodes/ | 
[**assets_v1_nodes_delete**](AssetsNodesApi.md#assets_v1_nodes_delete) | **DELETE** /assets/v1/nodes/{id}/ | 
[**assets_v1_nodes_list**](AssetsNodesApi.md#assets_v1_nodes_list) | **GET** /assets/v1/nodes/ | 
[**assets_v1_nodes_partial_update**](AssetsNodesApi.md#assets_v1_nodes_partial_update) | **PATCH** /assets/v1/nodes/{id}/ | 
[**assets_v1_nodes_read**](AssetsNodesApi.md#assets_v1_nodes_read) | **GET** /assets/v1/nodes/{id}/ | 
[**assets_v1_nodes_refresh_assets_amount_list**](AssetsNodesApi.md#assets_v1_nodes_refresh_assets_amount_list) | **GET** /assets/v1/nodes/refresh-assets-amount/ | 
[**assets_v1_nodes_refresh_hardware_info_list**](AssetsNodesApi.md#assets_v1_nodes_refresh_hardware_info_list) | **GET** /assets/v1/nodes/{id}/refresh-hardware-info/ | 
[**assets_v1_nodes_test_connective_list**](AssetsNodesApi.md#assets_v1_nodes_test_connective_list) | **GET** /assets/v1/nodes/{id}/test-connective/ | 
[**assets_v1_nodes_tree_list**](AssetsNodesApi.md#assets_v1_nodes_tree_list) | **GET** /assets/v1/nodes/tree/ | 
[**assets_v1_nodes_update**](AssetsNodesApi.md#assets_v1_nodes_update) | **PUT** /assets/v1/nodes/{id}/ | 


# **assets_v1_nodes_assets_add_partial_update**
> NodeAssets assets_v1_nodes_assets_add_partial_update(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.NodeAssets() # NodeAssets | 

try:
    api_response = api_instance.assets_v1_nodes_assets_add_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_assets_add_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**NodeAssets**](NodeAssets.md)|  | 

### Return type

[**NodeAssets**](NodeAssets.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_assets_add_update**
> NodeAssets assets_v1_nodes_assets_add_update(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.NodeAssets() # NodeAssets | 

try:
    api_response = api_instance.assets_v1_nodes_assets_add_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_assets_add_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**NodeAssets**](NodeAssets.md)|  | 

### Return type

[**NodeAssets**](NodeAssets.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_assets_list**
> list[Asset] assets_v1_nodes_assets_list(id, search=search, order=order)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.assets_v1_nodes_assets_list(id, search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_assets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Asset]**](Asset.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_assets_remove_partial_update**
> NodeAssets assets_v1_nodes_assets_remove_partial_update(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.NodeAssets() # NodeAssets | 

try:
    api_response = api_instance.assets_v1_nodes_assets_remove_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_assets_remove_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**NodeAssets**](NodeAssets.md)|  | 

### Return type

[**NodeAssets**](NodeAssets.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_assets_remove_update**
> NodeAssets assets_v1_nodes_assets_remove_update(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.NodeAssets() # NodeAssets | 

try:
    api_response = api_instance.assets_v1_nodes_assets_remove_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_assets_remove_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**NodeAssets**](NodeAssets.md)|  | 

### Return type

[**NodeAssets**](NodeAssets.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_assets_replace_partial_update**
> NodeAssets assets_v1_nodes_assets_replace_partial_update(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.NodeAssets() # NodeAssets | 

try:
    api_response = api_instance.assets_v1_nodes_assets_replace_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_assets_replace_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**NodeAssets**](NodeAssets.md)|  | 

### Return type

[**NodeAssets**](NodeAssets.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_assets_replace_update**
> NodeAssets assets_v1_nodes_assets_replace_update(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.NodeAssets() # NodeAssets | 

try:
    api_response = api_instance.assets_v1_nodes_assets_replace_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_assets_replace_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**NodeAssets**](NodeAssets.md)|  | 

### Return type

[**NodeAssets**](NodeAssets.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_children_add_partial_update**
> NodeAddChildren assets_v1_nodes_children_add_partial_update(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.NodeAddChildren() # NodeAddChildren | 

try:
    api_response = api_instance.assets_v1_nodes_children_add_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_children_add_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**NodeAddChildren**](NodeAddChildren.md)|  | 

### Return type

[**NodeAddChildren**](NodeAddChildren.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_children_add_update**
> NodeAddChildren assets_v1_nodes_children_add_update(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.NodeAddChildren() # NodeAddChildren | 

try:
    api_response = api_instance.assets_v1_nodes_children_add_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_children_add_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**NodeAddChildren**](NodeAddChildren.md)|  | 

### Return type

[**NodeAddChildren**](NodeAddChildren.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_children_create**
> Node assets_v1_nodes_children_create(data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
data = swagger_client.Node() # Node | 

try:
    api_response = api_instance.assets_v1_nodes_children_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_children_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Node**](Node.md)|  | 

### Return type

[**Node**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_children_create_0**
> Node assets_v1_nodes_children_create_0(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.Node() # Node | 

try:
    api_response = api_instance.assets_v1_nodes_children_create_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_children_create_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**Node**](Node.md)|  | 

### Return type

[**Node**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_children_list**
> list[Node] assets_v1_nodes_children_list(search=search, order=order)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.assets_v1_nodes_children_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_children_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Node]**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_children_list_0**
> list[Node] assets_v1_nodes_children_list_0(id, search=search, order=order)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.assets_v1_nodes_children_list_0(id, search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_children_list_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Node]**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_children_tree_list**
> list[TreeNode] assets_v1_nodes_children_tree_list(search=search, order=order)



节点子节点作为树返回， [   {     \"id\": \"\",     \"name\": \"\",     \"pId\": \"\",     \"meta\": \"\"   } ]

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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.assets_v1_nodes_children_tree_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_children_tree_list: %s\n" % e)
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

# **assets_v1_nodes_create**
> Node assets_v1_nodes_create(data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
data = swagger_client.Node() # Node | 

try:
    api_response = api_instance.assets_v1_nodes_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Node**](Node.md)|  | 

### Return type

[**Node**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_delete**
> assets_v1_nodes_delete(id)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.

try:
    api_instance.assets_v1_nodes_delete(id)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_list**
> list[Node] assets_v1_nodes_list(value=value, key=key, search=search, order=order)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
value = 'value_example' # str |  (optional)
key = 'key_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.assets_v1_nodes_list(value=value, key=key, search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | [optional] 
 **key** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Node]**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_partial_update**
> Node assets_v1_nodes_partial_update(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.Node() # Node | 

try:
    api_response = api_instance.assets_v1_nodes_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**Node**](Node.md)|  | 

### Return type

[**Node**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_read**
> Node assets_v1_nodes_read(id)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.

try:
    api_response = api_instance.assets_v1_nodes_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 

### Return type

[**Node**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_nodes_refresh_assets_amount_list**
> assets_v1_nodes_refresh_assets_amount_list()





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.assets_v1_nodes_refresh_assets_amount_list()
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_refresh_assets_amount_list: %s\n" % e)
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

# **assets_v1_nodes_refresh_hardware_info_list**
> assets_v1_nodes_refresh_hardware_info_list(id)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.assets_v1_nodes_refresh_hardware_info_list(id)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_refresh_hardware_info_list: %s\n" % e)
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

# **assets_v1_nodes_test_connective_list**
> assets_v1_nodes_test_connective_list(id)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.assets_v1_nodes_test_connective_list(id)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_test_connective_list: %s\n" % e)
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

# **assets_v1_nodes_tree_list**
> list[TreeNode] assets_v1_nodes_tree_list(search=search, order=order)



获取节点列表树 [   {     \"id\": \"\",     \"name\": \"\",     \"pId\": \"\",     \"meta\": \"\"   } ]

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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.assets_v1_nodes_tree_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_tree_list: %s\n" % e)
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

# **assets_v1_nodes_update**
> Node assets_v1_nodes_update(id, data)





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
api_instance = swagger_client.AssetsNodesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 节点.
data = swagger_client.Node() # Node | 

try:
    api_response = api_instance.assets_v1_nodes_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsNodesApi->assets_v1_nodes_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 节点. | 
 **data** | [**Node**](Node.md)|  | 

### Return type

[**Node**](Node.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

