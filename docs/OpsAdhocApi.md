# swagger_client.OpsAdhocApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ops_v1_adhoc_create**](OpsAdhocApi.md#ops_v1_adhoc_create) | **POST** /ops/v1/adhoc/ | 
[**ops_v1_adhoc_delete**](OpsAdhocApi.md#ops_v1_adhoc_delete) | **DELETE** /ops/v1/adhoc/{id}/ | 
[**ops_v1_adhoc_list**](OpsAdhocApi.md#ops_v1_adhoc_list) | **GET** /ops/v1/adhoc/ | 
[**ops_v1_adhoc_partial_update**](OpsAdhocApi.md#ops_v1_adhoc_partial_update) | **PATCH** /ops/v1/adhoc/{id}/ | 
[**ops_v1_adhoc_read**](OpsAdhocApi.md#ops_v1_adhoc_read) | **GET** /ops/v1/adhoc/{id}/ | 
[**ops_v1_adhoc_update**](OpsAdhocApi.md#ops_v1_adhoc_update) | **PUT** /ops/v1/adhoc/{id}/ | 


# **ops_v1_adhoc_create**
> AdHoc ops_v1_adhoc_create(data)





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
api_instance = swagger_client.OpsAdhocApi(swagger_client.ApiClient(configuration))
data = swagger_client.AdHoc() # AdHoc | 

try:
    api_response = api_instance.ops_v1_adhoc_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsAdhocApi->ops_v1_adhoc_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AdHoc**](AdHoc.md)|  | 

### Return type

[**AdHoc**](AdHoc.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_adhoc_delete**
> ops_v1_adhoc_delete(id)





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
api_instance = swagger_client.OpsAdhocApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ad hoc.

try:
    api_instance.ops_v1_adhoc_delete(id)
except ApiException as e:
    print("Exception when calling OpsAdhocApi->ops_v1_adhoc_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ad hoc. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_adhoc_list**
> list[AdHoc] ops_v1_adhoc_list(search=search, order=order)





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
api_instance = swagger_client.OpsAdhocApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.ops_v1_adhoc_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsAdhocApi->ops_v1_adhoc_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[AdHoc]**](AdHoc.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_adhoc_partial_update**
> AdHoc ops_v1_adhoc_partial_update(id, data)





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
api_instance = swagger_client.OpsAdhocApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ad hoc.
data = swagger_client.AdHoc() # AdHoc | 

try:
    api_response = api_instance.ops_v1_adhoc_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsAdhocApi->ops_v1_adhoc_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ad hoc. | 
 **data** | [**AdHoc**](AdHoc.md)|  | 

### Return type

[**AdHoc**](AdHoc.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_adhoc_read**
> AdHoc ops_v1_adhoc_read(id)





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
api_instance = swagger_client.OpsAdhocApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ad hoc.

try:
    api_response = api_instance.ops_v1_adhoc_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsAdhocApi->ops_v1_adhoc_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ad hoc. | 

### Return type

[**AdHoc**](AdHoc.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_adhoc_update**
> AdHoc ops_v1_adhoc_update(id, data)





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
api_instance = swagger_client.OpsAdhocApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ad hoc.
data = swagger_client.AdHoc() # AdHoc | 

try:
    api_response = api_instance.ops_v1_adhoc_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsAdhocApi->ops_v1_adhoc_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ad hoc. | 
 **data** | [**AdHoc**](AdHoc.md)|  | 

### Return type

[**AdHoc**](AdHoc.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

