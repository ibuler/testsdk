# swagger_client.AssetsGatewaysApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_v1_gateways_create**](AssetsGatewaysApi.md#assets_v1_gateways_create) | **POST** /assets/v1/gateways/ | 
[**assets_v1_gateways_delete**](AssetsGatewaysApi.md#assets_v1_gateways_delete) | **DELETE** /assets/v1/gateways/ | 
[**assets_v1_gateways_delete_0**](AssetsGatewaysApi.md#assets_v1_gateways_delete_0) | **DELETE** /assets/v1/gateways/{id}/ | 
[**assets_v1_gateways_list**](AssetsGatewaysApi.md#assets_v1_gateways_list) | **GET** /assets/v1/gateways/ | 
[**assets_v1_gateways_partial_update**](AssetsGatewaysApi.md#assets_v1_gateways_partial_update) | **PATCH** /assets/v1/gateways/ | 
[**assets_v1_gateways_partial_update_0**](AssetsGatewaysApi.md#assets_v1_gateways_partial_update_0) | **PATCH** /assets/v1/gateways/{id}/ | 
[**assets_v1_gateways_read**](AssetsGatewaysApi.md#assets_v1_gateways_read) | **GET** /assets/v1/gateways/{id}/ | 
[**assets_v1_gateways_test_connective_create**](AssetsGatewaysApi.md#assets_v1_gateways_test_connective_create) | **POST** /assets/v1/gateways/{id}/test-connective/ | 
[**assets_v1_gateways_update**](AssetsGatewaysApi.md#assets_v1_gateways_update) | **PUT** /assets/v1/gateways/ | 
[**assets_v1_gateways_update_0**](AssetsGatewaysApi.md#assets_v1_gateways_update_0) | **PUT** /assets/v1/gateways/{id}/ | 


# **assets_v1_gateways_create**
> Gateway assets_v1_gateways_create(data)





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
api_instance = swagger_client.AssetsGatewaysApi(swagger_client.ApiClient(configuration))
data = swagger_client.Gateway() # Gateway | 

try:
    api_response = api_instance.assets_v1_gateways_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsGatewaysApi->assets_v1_gateways_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Gateway**](Gateway.md)|  | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_gateways_delete**
> assets_v1_gateways_delete(domain__name=domain__name, name=name, username=username, ip=ip, domain=domain, search=search, order=order)





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
api_instance = swagger_client.AssetsGatewaysApi(swagger_client.ApiClient(configuration))
domain__name = 'domain__name_example' # str |  (optional)
name = 'name_example' # str |  (optional)
username = 'username_example' # str |  (optional)
ip = 'ip_example' # str |  (optional)
domain = 'domain_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.assets_v1_gateways_delete(domain__name=domain__name, name=name, username=username, ip=ip, domain=domain, search=search, order=order)
except ApiException as e:
    print("Exception when calling AssetsGatewaysApi->assets_v1_gateways_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain__name** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **ip** | **str**|  | [optional] 
 **domain** | **str**|  | [optional] 
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

# **assets_v1_gateways_delete_0**
> assets_v1_gateways_delete_0(id)





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
api_instance = swagger_client.AssetsGatewaysApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 网关.

try:
    api_instance.assets_v1_gateways_delete_0(id)
except ApiException as e:
    print("Exception when calling AssetsGatewaysApi->assets_v1_gateways_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 网关. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_gateways_list**
> InlineResponse2009 assets_v1_gateways_list(domain__name=domain__name, name=name, username=username, ip=ip, domain=domain, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.AssetsGatewaysApi(swagger_client.ApiClient(configuration))
domain__name = 'domain__name_example' # str |  (optional)
name = 'name_example' # str |  (optional)
username = 'username_example' # str |  (optional)
ip = 'ip_example' # str |  (optional)
domain = 'domain_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_gateways_list(domain__name=domain__name, name=name, username=username, ip=ip, domain=domain, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsGatewaysApi->assets_v1_gateways_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain__name** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **ip** | **str**|  | [optional] 
 **domain** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_gateways_partial_update**
> Gateway assets_v1_gateways_partial_update(data)





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
api_instance = swagger_client.AssetsGatewaysApi(swagger_client.ApiClient(configuration))
data = swagger_client.Gateway() # Gateway | 

try:
    api_response = api_instance.assets_v1_gateways_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsGatewaysApi->assets_v1_gateways_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Gateway**](Gateway.md)|  | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_gateways_partial_update_0**
> Gateway assets_v1_gateways_partial_update_0(id, data)





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
api_instance = swagger_client.AssetsGatewaysApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 网关.
data = swagger_client.Gateway() # Gateway | 

try:
    api_response = api_instance.assets_v1_gateways_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsGatewaysApi->assets_v1_gateways_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 网关. | 
 **data** | [**Gateway**](Gateway.md)|  | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_gateways_read**
> Gateway assets_v1_gateways_read(id)





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
api_instance = swagger_client.AssetsGatewaysApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 网关.

try:
    api_response = api_instance.assets_v1_gateways_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsGatewaysApi->assets_v1_gateways_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 网关. | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_gateways_test_connective_create**
> assets_v1_gateways_test_connective_create(id)





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
api_instance = swagger_client.AssetsGatewaysApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.assets_v1_gateways_test_connective_create(id)
except ApiException as e:
    print("Exception when calling AssetsGatewaysApi->assets_v1_gateways_test_connective_create: %s\n" % e)
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

# **assets_v1_gateways_update**
> Gateway assets_v1_gateways_update(data)





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
api_instance = swagger_client.AssetsGatewaysApi(swagger_client.ApiClient(configuration))
data = swagger_client.Gateway() # Gateway | 

try:
    api_response = api_instance.assets_v1_gateways_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsGatewaysApi->assets_v1_gateways_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Gateway**](Gateway.md)|  | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_gateways_update_0**
> Gateway assets_v1_gateways_update_0(id, data)





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
api_instance = swagger_client.AssetsGatewaysApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 网关.
data = swagger_client.Gateway() # Gateway | 

try:
    api_response = api_instance.assets_v1_gateways_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsGatewaysApi->assets_v1_gateways_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 网关. | 
 **data** | [**Gateway**](Gateway.md)|  | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

