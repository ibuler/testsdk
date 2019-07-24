# swagger_client.AuthenticationAuthApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_v1_auth_create**](AuthenticationAuthApi.md#authentication_v1_auth_create) | **POST** /authentication/v1/auth/ | 


# **authentication_v1_auth_create**
> authentication_v1_auth_create()





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
api_instance = swagger_client.AuthenticationAuthApi(swagger_client.ApiClient(configuration))

try:
    api_instance.authentication_v1_auth_create()
except ApiException as e:
    print("Exception when calling AuthenticationAuthApi->authentication_v1_auth_create: %s\n" % e)
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

