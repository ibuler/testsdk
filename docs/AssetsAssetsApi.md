# swagger_client.AssetsAssetsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_v1_assets_alive_read**](AssetsAssetsApi.md#assets_v1_assets_alive_read) | **GET** /assets/v1/assets/{id}/alive/ | 
[**assets_v1_assets_create**](AssetsAssetsApi.md#assets_v1_assets_create) | **POST** /assets/v1/assets/ | 
[**assets_v1_assets_delete**](AssetsAssetsApi.md#assets_v1_assets_delete) | **DELETE** /assets/v1/assets/ | 
[**assets_v1_assets_delete_0**](AssetsAssetsApi.md#assets_v1_assets_delete_0) | **DELETE** /assets/v1/assets/{id}/ | 
[**assets_v1_assets_gateway_read**](AssetsAssetsApi.md#assets_v1_assets_gateway_read) | **GET** /assets/v1/assets/{id}/gateway/ | 
[**assets_v1_assets_list**](AssetsAssetsApi.md#assets_v1_assets_list) | **GET** /assets/v1/assets/ | 
[**assets_v1_assets_partial_update**](AssetsAssetsApi.md#assets_v1_assets_partial_update) | **PATCH** /assets/v1/assets/ | 
[**assets_v1_assets_partial_update_0**](AssetsAssetsApi.md#assets_v1_assets_partial_update_0) | **PATCH** /assets/v1/assets/{id}/ | 
[**assets_v1_assets_read**](AssetsAssetsApi.md#assets_v1_assets_read) | **GET** /assets/v1/assets/{id}/ | 
[**assets_v1_assets_refresh_read**](AssetsAssetsApi.md#assets_v1_assets_refresh_read) | **GET** /assets/v1/assets/{id}/refresh/ | 
[**assets_v1_assets_update**](AssetsAssetsApi.md#assets_v1_assets_update) | **PUT** /assets/v1/assets/ | 
[**assets_v1_assets_update_0**](AssetsAssetsApi.md#assets_v1_assets_update_0) | **PUT** /assets/v1/assets/{id}/ | 


# **assets_v1_assets_alive_read**
> TaskID assets_v1_assets_alive_read(id)



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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产.

try:
    api_response = api_instance.assets_v1_assets_alive_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_alive_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产. | 

### Return type

[**TaskID**](TaskID.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_assets_create**
> Asset assets_v1_assets_create(data)



API endpoint that allows Asset to be viewed or edited.

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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Asset() # Asset | 

try:
    api_response = api_instance.assets_v1_assets_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Asset**](Asset.md)|  | 

### Return type

[**Asset**](Asset.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_assets_delete**
> assets_v1_assets_delete(hostname=hostname, ip=ip, systemuser__id=systemuser__id, admin_user__id=admin_user__id, search=search, order=order)



API endpoint that allows Asset to be viewed or edited.

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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
hostname = 'hostname_example' # str |  (optional)
ip = 'ip_example' # str |  (optional)
systemuser__id = 'systemuser__id_example' # str |  (optional)
admin_user__id = 'admin_user__id_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.assets_v1_assets_delete(hostname=hostname, ip=ip, systemuser__id=systemuser__id, admin_user__id=admin_user__id, search=search, order=order)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | [optional] 
 **ip** | **str**|  | [optional] 
 **systemuser__id** | **str**|  | [optional] 
 **admin_user__id** | **str**|  | [optional] 
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

# **assets_v1_assets_delete_0**
> assets_v1_assets_delete_0(id)



API endpoint that allows Asset to be viewed or edited.

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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产.

try:
    api_instance.assets_v1_assets_delete_0(id)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_assets_gateway_read**
> GatewayWithAuth assets_v1_assets_gateway_read(id)





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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产.

try:
    api_response = api_instance.assets_v1_assets_gateway_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_gateway_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产. | 

### Return type

[**GatewayWithAuth**](GatewayWithAuth.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_assets_list**
> InlineResponse2005 assets_v1_assets_list(hostname=hostname, ip=ip, systemuser__id=systemuser__id, admin_user__id=admin_user__id, search=search, order=order, limit=limit, offset=offset)



API endpoint that allows Asset to be viewed or edited.

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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
hostname = 'hostname_example' # str |  (optional)
ip = 'ip_example' # str |  (optional)
systemuser__id = 'systemuser__id_example' # str |  (optional)
admin_user__id = 'admin_user__id_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_assets_list(hostname=hostname, ip=ip, systemuser__id=systemuser__id, admin_user__id=admin_user__id, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**|  | [optional] 
 **ip** | **str**|  | [optional] 
 **systemuser__id** | **str**|  | [optional] 
 **admin_user__id** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_assets_partial_update**
> Asset assets_v1_assets_partial_update(data)



API endpoint that allows Asset to be viewed or edited.

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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Asset() # Asset | 

try:
    api_response = api_instance.assets_v1_assets_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Asset**](Asset.md)|  | 

### Return type

[**Asset**](Asset.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_assets_partial_update_0**
> Asset assets_v1_assets_partial_update_0(id, data)



API endpoint that allows Asset to be viewed or edited.

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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产.
data = swagger_client.Asset() # Asset | 

try:
    api_response = api_instance.assets_v1_assets_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产. | 
 **data** | [**Asset**](Asset.md)|  | 

### Return type

[**Asset**](Asset.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_assets_read**
> Asset assets_v1_assets_read(id)



API endpoint that allows Asset to be viewed or edited.

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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产.

try:
    api_response = api_instance.assets_v1_assets_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产. | 

### Return type

[**Asset**](Asset.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_assets_refresh_read**
> Asset assets_v1_assets_refresh_read(id)



Refresh asset hardware info

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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产.

try:
    api_response = api_instance.assets_v1_assets_refresh_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_refresh_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产. | 

### Return type

[**Asset**](Asset.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_assets_update**
> Asset assets_v1_assets_update(data)



API endpoint that allows Asset to be viewed or edited.

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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Asset() # Asset | 

try:
    api_response = api_instance.assets_v1_assets_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Asset**](Asset.md)|  | 

### Return type

[**Asset**](Asset.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_assets_update_0**
> Asset assets_v1_assets_update_0(id, data)



API endpoint that allows Asset to be viewed or edited.

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
api_instance = swagger_client.AssetsAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 资产.
data = swagger_client.Asset() # Asset | 

try:
    api_response = api_instance.assets_v1_assets_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsAssetsApi->assets_v1_assets_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 资产. | 
 **data** | [**Asset**](Asset.md)|  | 

### Return type

[**Asset**](Asset.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

