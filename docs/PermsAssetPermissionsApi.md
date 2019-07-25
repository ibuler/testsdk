# swagger_client.PermsAssetPermissionsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perms_v1_asset_permissions_asset_add_partial_update**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_asset_add_partial_update) | **PATCH** /perms/v1/asset-permissions/{id}/asset/add/ | 
[**perms_v1_asset_permissions_asset_add_read**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_asset_add_read) | **GET** /perms/v1/asset-permissions/{id}/asset/add/ | 
[**perms_v1_asset_permissions_asset_add_update**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_asset_add_update) | **PUT** /perms/v1/asset-permissions/{id}/asset/add/ | 
[**perms_v1_asset_permissions_asset_remove_partial_update**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_asset_remove_partial_update) | **PATCH** /perms/v1/asset-permissions/{id}/asset/remove/ | 
[**perms_v1_asset_permissions_asset_remove_read**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_asset_remove_read) | **GET** /perms/v1/asset-permissions/{id}/asset/remove/ | 
[**perms_v1_asset_permissions_asset_remove_update**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_asset_remove_update) | **PUT** /perms/v1/asset-permissions/{id}/asset/remove/ | 
[**perms_v1_asset_permissions_assets_list**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_assets_list) | **GET** /perms/v1/asset-permissions/{id}/assets/ | 
[**perms_v1_asset_permissions_create**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_create) | **POST** /perms/v1/asset-permissions/ | 
[**perms_v1_asset_permissions_delete**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_delete) | **DELETE** /perms/v1/asset-permissions/{id}/ | 
[**perms_v1_asset_permissions_list**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_list) | **GET** /perms/v1/asset-permissions/ | 
[**perms_v1_asset_permissions_partial_update**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_partial_update) | **PATCH** /perms/v1/asset-permissions/{id}/ | 
[**perms_v1_asset_permissions_read**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_read) | **GET** /perms/v1/asset-permissions/{id}/ | 
[**perms_v1_asset_permissions_update**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_update) | **PUT** /perms/v1/asset-permissions/{id}/ | 
[**perms_v1_asset_permissions_user_actions_read**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_user_actions_read) | **GET** /perms/v1/asset-permissions/user/actions/ | 
[**perms_v1_asset_permissions_user_add_partial_update**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_user_add_partial_update) | **PATCH** /perms/v1/asset-permissions/{id}/user/add/ | 
[**perms_v1_asset_permissions_user_add_read**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_user_add_read) | **GET** /perms/v1/asset-permissions/{id}/user/add/ | 
[**perms_v1_asset_permissions_user_add_update**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_user_add_update) | **PUT** /perms/v1/asset-permissions/{id}/user/add/ | 
[**perms_v1_asset_permissions_user_remove_partial_update**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_user_remove_partial_update) | **PATCH** /perms/v1/asset-permissions/{id}/user/remove/ | 
[**perms_v1_asset_permissions_user_remove_read**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_user_remove_read) | **GET** /perms/v1/asset-permissions/{id}/user/remove/ | 
[**perms_v1_asset_permissions_user_remove_update**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_user_remove_update) | **PUT** /perms/v1/asset-permissions/{id}/user/remove/ | 
[**perms_v1_asset_permissions_user_validate_list**](PermsAssetPermissionsApi.md#perms_v1_asset_permissions_user_validate_list) | **GET** /perms/v1/asset-permissions/user/validate/ | 


# **perms_v1_asset_permissions_asset_add_partial_update**
> AssetPermissionUpdateAsset perms_v1_asset_permissions_asset_add_partial_update(id, data)





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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.
data = swagger_client.AssetPermissionUpdateAsset() # AssetPermissionUpdateAsset | 

try:
    api_response = api_instance.perms_v1_asset_permissions_asset_add_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_asset_add_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 
 **data** | [**AssetPermissionUpdateAsset**](AssetPermissionUpdateAsset.md)|  | 

### Return type

[**AssetPermissionUpdateAsset**](AssetPermissionUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_asset_add_read**
> AssetPermissionUpdateAsset perms_v1_asset_permissions_asset_add_read(id)





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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.

try:
    api_response = api_instance.perms_v1_asset_permissions_asset_add_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_asset_add_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 

### Return type

[**AssetPermissionUpdateAsset**](AssetPermissionUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_asset_add_update**
> AssetPermissionUpdateAsset perms_v1_asset_permissions_asset_add_update(id, data)





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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.
data = swagger_client.AssetPermissionUpdateAsset() # AssetPermissionUpdateAsset | 

try:
    api_response = api_instance.perms_v1_asset_permissions_asset_add_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_asset_add_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 
 **data** | [**AssetPermissionUpdateAsset**](AssetPermissionUpdateAsset.md)|  | 

### Return type

[**AssetPermissionUpdateAsset**](AssetPermissionUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_asset_remove_partial_update**
> AssetPermissionUpdateAsset perms_v1_asset_permissions_asset_remove_partial_update(id, data)



将用户从授权中移除，Detail页面会调用

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.
data = swagger_client.AssetPermissionUpdateAsset() # AssetPermissionUpdateAsset | 

try:
    api_response = api_instance.perms_v1_asset_permissions_asset_remove_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_asset_remove_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 
 **data** | [**AssetPermissionUpdateAsset**](AssetPermissionUpdateAsset.md)|  | 

### Return type

[**AssetPermissionUpdateAsset**](AssetPermissionUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_asset_remove_read**
> AssetPermissionUpdateAsset perms_v1_asset_permissions_asset_remove_read(id)



将用户从授权中移除，Detail页面会调用

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.

try:
    api_response = api_instance.perms_v1_asset_permissions_asset_remove_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_asset_remove_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 

### Return type

[**AssetPermissionUpdateAsset**](AssetPermissionUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_asset_remove_update**
> AssetPermissionUpdateAsset perms_v1_asset_permissions_asset_remove_update(id, data)



将用户从授权中移除，Detail页面会调用

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.
data = swagger_client.AssetPermissionUpdateAsset() # AssetPermissionUpdateAsset | 

try:
    api_response = api_instance.perms_v1_asset_permissions_asset_remove_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_asset_remove_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 
 **data** | [**AssetPermissionUpdateAsset**](AssetPermissionUpdateAsset.md)|  | 

### Return type

[**AssetPermissionUpdateAsset**](AssetPermissionUpdateAsset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_assets_list**
> InlineResponse20013 perms_v1_asset_permissions_assets_list(id, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_asset_permissions_assets_list(id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_assets_list: %s\n" % e)
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

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_create**
> AssetPermissionCreateUpdate perms_v1_asset_permissions_create(data)



资产授权列表的增删改查api

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
data = swagger_client.AssetPermissionCreateUpdate() # AssetPermissionCreateUpdate | 

try:
    api_response = api_instance.perms_v1_asset_permissions_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AssetPermissionCreateUpdate**](AssetPermissionCreateUpdate.md)|  | 

### Return type

[**AssetPermissionCreateUpdate**](AssetPermissionCreateUpdate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_delete**
> perms_v1_asset_permissions_delete(id)



资产授权列表的增删改查api

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.

try:
    api_instance.perms_v1_asset_permissions_delete(id)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_list**
> InlineResponse20012 perms_v1_asset_permissions_list(name=name, search=search, order=order, limit=limit, offset=offset)



资产授权列表的增删改查api

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.perms_v1_asset_permissions_list(name=name, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_list: %s\n" % e)
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

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_partial_update**
> AssetPermissionCreateUpdate perms_v1_asset_permissions_partial_update(id, data)



资产授权列表的增删改查api

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.
data = swagger_client.AssetPermissionCreateUpdate() # AssetPermissionCreateUpdate | 

try:
    api_response = api_instance.perms_v1_asset_permissions_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 
 **data** | [**AssetPermissionCreateUpdate**](AssetPermissionCreateUpdate.md)|  | 

### Return type

[**AssetPermissionCreateUpdate**](AssetPermissionCreateUpdate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_read**
> AssetPermissionCreateUpdate perms_v1_asset_permissions_read(id)



资产授权列表的增删改查api

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.

try:
    api_response = api_instance.perms_v1_asset_permissions_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 

### Return type

[**AssetPermissionCreateUpdate**](AssetPermissionCreateUpdate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_update**
> AssetPermissionCreateUpdate perms_v1_asset_permissions_update(id, data)



资产授权列表的增删改查api

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.
data = swagger_client.AssetPermissionCreateUpdate() # AssetPermissionCreateUpdate | 

try:
    api_response = api_instance.perms_v1_asset_permissions_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 
 **data** | [**AssetPermissionCreateUpdate**](AssetPermissionCreateUpdate.md)|  | 

### Return type

[**AssetPermissionCreateUpdate**](AssetPermissionCreateUpdate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_user_actions_read**
> Actions perms_v1_asset_permissions_user_actions_read()





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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.perms_v1_asset_permissions_user_actions_read()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_user_actions_read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Actions**](Actions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_user_add_partial_update**
> AssetPermissionUpdateUser perms_v1_asset_permissions_user_add_partial_update(id, data)





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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.
data = swagger_client.AssetPermissionUpdateUser() # AssetPermissionUpdateUser | 

try:
    api_response = api_instance.perms_v1_asset_permissions_user_add_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_user_add_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 
 **data** | [**AssetPermissionUpdateUser**](AssetPermissionUpdateUser.md)|  | 

### Return type

[**AssetPermissionUpdateUser**](AssetPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_user_add_read**
> AssetPermissionUpdateUser perms_v1_asset_permissions_user_add_read(id)





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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.

try:
    api_response = api_instance.perms_v1_asset_permissions_user_add_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_user_add_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 

### Return type

[**AssetPermissionUpdateUser**](AssetPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_user_add_update**
> AssetPermissionUpdateUser perms_v1_asset_permissions_user_add_update(id, data)





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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.
data = swagger_client.AssetPermissionUpdateUser() # AssetPermissionUpdateUser | 

try:
    api_response = api_instance.perms_v1_asset_permissions_user_add_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_user_add_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 
 **data** | [**AssetPermissionUpdateUser**](AssetPermissionUpdateUser.md)|  | 

### Return type

[**AssetPermissionUpdateUser**](AssetPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_user_remove_partial_update**
> AssetPermissionUpdateUser perms_v1_asset_permissions_user_remove_partial_update(id, data)



将用户从授权中移除，Detail页面会调用

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.
data = swagger_client.AssetPermissionUpdateUser() # AssetPermissionUpdateUser | 

try:
    api_response = api_instance.perms_v1_asset_permissions_user_remove_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_user_remove_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 
 **data** | [**AssetPermissionUpdateUser**](AssetPermissionUpdateUser.md)|  | 

### Return type

[**AssetPermissionUpdateUser**](AssetPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_user_remove_read**
> AssetPermissionUpdateUser perms_v1_asset_permissions_user_remove_read(id)



将用户从授权中移除，Detail页面会调用

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.

try:
    api_response = api_instance.perms_v1_asset_permissions_user_remove_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_user_remove_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 

### Return type

[**AssetPermissionUpdateUser**](AssetPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_user_remove_update**
> AssetPermissionUpdateUser perms_v1_asset_permissions_user_remove_update(id, data)



将用户从授权中移除，Detail页面会调用

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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产授权.
data = swagger_client.AssetPermissionUpdateUser() # AssetPermissionUpdateUser | 

try:
    api_response = api_instance.perms_v1_asset_permissions_user_remove_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_user_remove_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产授权. | 
 **data** | [**AssetPermissionUpdateUser**](AssetPermissionUpdateUser.md)|  | 

### Return type

[**AssetPermissionUpdateUser**](AssetPermissionUpdateUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perms_v1_asset_permissions_user_validate_list**
> perms_v1_asset_permissions_user_validate_list()





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
api_instance = swagger_client.PermsAssetPermissionsApi(swagger_client.ApiClient(configuration))

try:
    api_instance.perms_v1_asset_permissions_user_validate_list()
except ApiException as e:
    print("Exception when calling PermsAssetPermissionsApi->perms_v1_asset_permissions_user_validate_list: %s\n" % e)
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

