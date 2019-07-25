# swagger_client.AssetsAssetUsersApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_v1_asset_users_auth_info_read**](AssetsAssetUsersApi.md#assets_v1_asset_users_auth_info_read) | **GET** /assets/v1/asset-users/auth-info/ | 
[**assets_v1_asset_users_create**](AssetsAssetUsersApi.md#assets_v1_asset_users_create) | **POST** /assets/v1/asset-users/ | 
[**assets_v1_asset_users_list**](AssetsAssetUsersApi.md#assets_v1_asset_users_list) | **GET** /assets/v1/asset-users/ | 
[**assets_v1_asset_users_read**](AssetsAssetUsersApi.md#assets_v1_asset_users_read) | **GET** /assets/v1/asset-users/{id}/ | 
[**assets_v1_asset_users_test_connective_read**](AssetsAssetUsersApi.md#assets_v1_asset_users_test_connective_read) | **GET** /assets/v1/asset-users/test-connective/ | 


# **assets_v1_asset_users_auth_info_read**
> AssetUserAuthInfo assets_v1_asset_users_auth_info_read()





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
api_instance = swagger_client.AssetsAssetUsersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.assets_v1_asset_users_auth_info_read()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetUsersApi->assets_v1_asset_users_auth_info_read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AssetUserAuthInfo**](AssetUserAuthInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_asset_users_create**
> AssetUser assets_v1_asset_users_create(data)





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
api_instance = swagger_client.AssetsAssetUsersApi(swagger_client.ApiClient(configuration))
data = swagger_client.AssetUser() # AssetUser | 

try:
    api_response = api_instance.assets_v1_asset_users_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetUsersApi->assets_v1_asset_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AssetUser**](AssetUser.md)|  | 

### Return type

[**AssetUser**](AssetUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_asset_users_list**
> InlineResponse2004 assets_v1_asset_users_list(order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.AssetsAssetUsersApi(swagger_client.ApiClient(configuration))
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_asset_users_list(order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetUsersApi->assets_v1_asset_users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_asset_users_read**
> AssetUser assets_v1_asset_users_read(id)





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
api_instance = swagger_client.AssetsAssetUsersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.assets_v1_asset_users_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetUsersApi->assets_v1_asset_users_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AssetUser**](AssetUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_asset_users_test_connective_read**
> TaskID assets_v1_asset_users_test_connective_read()



Test asset users connective

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
api_instance = swagger_client.AssetsAssetUsersApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.assets_v1_asset_users_test_connective_read()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetUsersApi->assets_v1_asset_users_test_connective_read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaskID**](TaskID.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

