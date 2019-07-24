# swagger_client.CommonResourcesApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**common_v1_resources_cache_create**](CommonResourcesApi.md#common_v1_resources_cache_create) | **POST** /common/v1/resources/cache/ | 


# **common_v1_resources_cache_create**
> common_v1_resources_cache_create()





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
api_instance = swagger_client.CommonResourcesApi(swagger_client.ApiClient(configuration))

try:
    api_instance.common_v1_resources_cache_create()
except ApiException as e:
    print("Exception when calling CommonResourcesApi->common_v1_resources_cache_create: %s\n" % e)
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

