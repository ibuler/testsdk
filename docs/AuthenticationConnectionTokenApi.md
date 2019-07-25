# swagger_client.AuthenticationConnectionTokenApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_v1_connection_token_create**](AuthenticationConnectionTokenApi.md#authentication_v1_connection_token_create) | **POST** /authentication/v1/connection-token/ | 
[**authentication_v1_connection_token_list**](AuthenticationConnectionTokenApi.md#authentication_v1_connection_token_list) | **GET** /authentication/v1/connection-token/ | 


# **authentication_v1_connection_token_create**
> authentication_v1_connection_token_create()





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
api_instance = swagger_client.AuthenticationConnectionTokenApi(swagger_client.ApiClient(configuration))

try:
    api_instance.authentication_v1_connection_token_create()
except ApiException as e:
    print("Exception when calling AuthenticationConnectionTokenApi->authentication_v1_connection_token_create: %s\n" % e)
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

# **authentication_v1_connection_token_list**
> authentication_v1_connection_token_list()





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
api_instance = swagger_client.AuthenticationConnectionTokenApi(swagger_client.ApiClient(configuration))

try:
    api_instance.authentication_v1_connection_token_list()
except ApiException as e:
    print("Exception when calling AuthenticationConnectionTokenApi->authentication_v1_connection_token_list: %s\n" % e)
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

