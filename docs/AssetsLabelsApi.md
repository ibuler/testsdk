# swagger_client.AssetsLabelsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_v1_labels_create**](AssetsLabelsApi.md#assets_v1_labels_create) | **POST** /assets/v1/labels/ | 
[**assets_v1_labels_delete**](AssetsLabelsApi.md#assets_v1_labels_delete) | **DELETE** /assets/v1/labels/ | 
[**assets_v1_labels_delete_0**](AssetsLabelsApi.md#assets_v1_labels_delete_0) | **DELETE** /assets/v1/labels/{id}/ | 
[**assets_v1_labels_list**](AssetsLabelsApi.md#assets_v1_labels_list) | **GET** /assets/v1/labels/ | 
[**assets_v1_labels_partial_update**](AssetsLabelsApi.md#assets_v1_labels_partial_update) | **PATCH** /assets/v1/labels/ | 
[**assets_v1_labels_partial_update_0**](AssetsLabelsApi.md#assets_v1_labels_partial_update_0) | **PATCH** /assets/v1/labels/{id}/ | 
[**assets_v1_labels_read**](AssetsLabelsApi.md#assets_v1_labels_read) | **GET** /assets/v1/labels/{id}/ | 
[**assets_v1_labels_update**](AssetsLabelsApi.md#assets_v1_labels_update) | **PUT** /assets/v1/labels/ | 
[**assets_v1_labels_update_0**](AssetsLabelsApi.md#assets_v1_labels_update_0) | **PUT** /assets/v1/labels/{id}/ | 


# **assets_v1_labels_create**
> Label assets_v1_labels_create(data)





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
api_instance = swagger_client.AssetsLabelsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Label() # Label | 

try:
    api_response = api_instance.assets_v1_labels_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsLabelsApi->assets_v1_labels_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Label**](Label.md)|  | 

### Return type

[**Label**](Label.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_labels_delete**
> assets_v1_labels_delete(name=name, value=value, search=search, order=order)





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
api_instance = swagger_client.AssetsLabelsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
value = 'value_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.assets_v1_labels_delete(name=name, value=value, search=search, order=order)
except ApiException as e:
    print("Exception when calling AssetsLabelsApi->assets_v1_labels_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **value** | **str**|  | [optional] 
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

# **assets_v1_labels_delete_0**
> assets_v1_labels_delete_0(id)





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
api_instance = swagger_client.AssetsLabelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.assets_v1_labels_delete_0(id)
except ApiException as e:
    print("Exception when calling AssetsLabelsApi->assets_v1_labels_delete_0: %s\n" % e)
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

# **assets_v1_labels_list**
> InlineResponse20010 assets_v1_labels_list(name=name, value=value, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.AssetsLabelsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
value = 'value_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_labels_list(name=name, value=value, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsLabelsApi->assets_v1_labels_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **value** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_labels_partial_update**
> Label assets_v1_labels_partial_update(data)





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
api_instance = swagger_client.AssetsLabelsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Label() # Label | 

try:
    api_response = api_instance.assets_v1_labels_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsLabelsApi->assets_v1_labels_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Label**](Label.md)|  | 

### Return type

[**Label**](Label.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_labels_partial_update_0**
> Label assets_v1_labels_partial_update_0(id, data)





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
api_instance = swagger_client.AssetsLabelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
data = swagger_client.Label() # Label | 

try:
    api_response = api_instance.assets_v1_labels_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsLabelsApi->assets_v1_labels_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Label**](Label.md)|  | 

### Return type

[**Label**](Label.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_labels_read**
> Label assets_v1_labels_read(id)





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
api_instance = swagger_client.AssetsLabelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.assets_v1_labels_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsLabelsApi->assets_v1_labels_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Label**](Label.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_labels_update**
> Label assets_v1_labels_update(data)





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
api_instance = swagger_client.AssetsLabelsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Label() # Label | 

try:
    api_response = api_instance.assets_v1_labels_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsLabelsApi->assets_v1_labels_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Label**](Label.md)|  | 

### Return type

[**Label**](Label.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_labels_update_0**
> Label assets_v1_labels_update_0(id, data)





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
api_instance = swagger_client.AssetsLabelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
data = swagger_client.Label() # Label | 

try:
    api_response = api_instance.assets_v1_labels_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsLabelsApi->assets_v1_labels_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Label**](Label.md)|  | 

### Return type

[**Label**](Label.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

