# swagger_client.UsersOtpApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_v1_otp_auth_create**](UsersOtpApi.md#users_v1_otp_auth_create) | **POST** /users/v1/otp/auth/ | 
[**users_v1_otp_reset_read**](UsersOtpApi.md#users_v1_otp_reset_read) | **GET** /users/v1/otp/reset/ | 


# **users_v1_otp_auth_create**
> users_v1_otp_auth_create()





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
api_instance = swagger_client.UsersOtpApi(swagger_client.ApiClient(configuration))

try:
    api_instance.users_v1_otp_auth_create()
except ApiException as e:
    print("Exception when calling UsersOtpApi->users_v1_otp_auth_create: %s\n" % e)
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

# **users_v1_otp_reset_read**
> users_v1_otp_reset_read()





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
api_instance = swagger_client.UsersOtpApi(swagger_client.ApiClient(configuration))

try:
    api_instance.users_v1_otp_reset_read()
except ApiException as e:
    print("Exception when calling UsersOtpApi->users_v1_otp_reset_read: %s\n" % e)
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

