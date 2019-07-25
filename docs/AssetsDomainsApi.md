# swagger_client.AssetsDomainsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_v1_domains_create**](AssetsDomainsApi.md#assets_v1_domains_create) | **POST** /assets/v1/domains/ | 
[**assets_v1_domains_delete**](AssetsDomainsApi.md#assets_v1_domains_delete) | **DELETE** /assets/v1/domains/ | 
[**assets_v1_domains_delete_0**](AssetsDomainsApi.md#assets_v1_domains_delete_0) | **DELETE** /assets/v1/domains/{id}/ | 
[**assets_v1_domains_list**](AssetsDomainsApi.md#assets_v1_domains_list) | **GET** /assets/v1/domains/ | 
[**assets_v1_domains_partial_update**](AssetsDomainsApi.md#assets_v1_domains_partial_update) | **PATCH** /assets/v1/domains/ | 
[**assets_v1_domains_partial_update_0**](AssetsDomainsApi.md#assets_v1_domains_partial_update_0) | **PATCH** /assets/v1/domains/{id}/ | 
[**assets_v1_domains_read**](AssetsDomainsApi.md#assets_v1_domains_read) | **GET** /assets/v1/domains/{id}/ | 
[**assets_v1_domains_update**](AssetsDomainsApi.md#assets_v1_domains_update) | **PUT** /assets/v1/domains/ | 
[**assets_v1_domains_update_0**](AssetsDomainsApi.md#assets_v1_domains_update_0) | **PUT** /assets/v1/domains/{id}/ | 


# **assets_v1_domains_create**
> Domain assets_v1_domains_create(data)





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
api_instance = swagger_client.AssetsDomainsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Domain() # Domain | 

try:
    api_response = api_instance.assets_v1_domains_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsDomainsApi->assets_v1_domains_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Domain**](Domain.md)|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_domains_delete**
> assets_v1_domains_delete(search=search, order=order)





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
api_instance = swagger_client.AssetsDomainsApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.assets_v1_domains_delete(search=search, order=order)
except ApiException as e:
    print("Exception when calling AssetsDomainsApi->assets_v1_domains_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **assets_v1_domains_delete_0**
> assets_v1_domains_delete_0(id)





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
api_instance = swagger_client.AssetsDomainsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 网域.

try:
    api_instance.assets_v1_domains_delete_0(id)
except ApiException as e:
    print("Exception when calling AssetsDomainsApi->assets_v1_domains_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 网域. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_domains_list**
> InlineResponse2008 assets_v1_domains_list(search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.AssetsDomainsApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_domains_list(search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsDomainsApi->assets_v1_domains_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_domains_partial_update**
> Domain assets_v1_domains_partial_update(data)





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
api_instance = swagger_client.AssetsDomainsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Domain() # Domain | 

try:
    api_response = api_instance.assets_v1_domains_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsDomainsApi->assets_v1_domains_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Domain**](Domain.md)|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_domains_partial_update_0**
> Domain assets_v1_domains_partial_update_0(id, data)





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
api_instance = swagger_client.AssetsDomainsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 网域.
data = swagger_client.Domain() # Domain | 

try:
    api_response = api_instance.assets_v1_domains_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsDomainsApi->assets_v1_domains_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 网域. | 
 **data** | [**Domain**](Domain.md)|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_domains_read**
> Domain assets_v1_domains_read(id)





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
api_instance = swagger_client.AssetsDomainsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 网域.

try:
    api_response = api_instance.assets_v1_domains_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsDomainsApi->assets_v1_domains_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 网域. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_domains_update**
> Domain assets_v1_domains_update(data)





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
api_instance = swagger_client.AssetsDomainsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Domain() # Domain | 

try:
    api_response = api_instance.assets_v1_domains_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsDomainsApi->assets_v1_domains_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Domain**](Domain.md)|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_domains_update_0**
> Domain assets_v1_domains_update_0(id, data)





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
api_instance = swagger_client.AssetsDomainsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 网域.
data = swagger_client.Domain() # Domain | 

try:
    api_response = api_instance.assets_v1_domains_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsDomainsApi->assets_v1_domains_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 网域. | 
 **data** | [**Domain**](Domain.md)|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

