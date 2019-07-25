# swagger_client.AuthenticationOtpApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_v1_otp_auth_create**](AuthenticationOtpApi.md#authentication_v1_otp_auth_create) | **POST** /authentication/v1/otp/auth/ | 
[**authentication_v1_otp_verify_create**](AuthenticationOtpApi.md#authentication_v1_otp_verify_create) | **POST** /authentication/v1/otp/verify/ | 


# **authentication_v1_otp_auth_create**
> authentication_v1_otp_auth_create()





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
api_instance = swagger_client.AuthenticationOtpApi(swagger_client.ApiClient(configuration))

try:
    api_instance.authentication_v1_otp_auth_create()
except ApiException as e:
    print("Exception when calling AuthenticationOtpApi->authentication_v1_otp_auth_create: %s\n" % e)
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

# **authentication_v1_otp_verify_create**
> OtpVerify authentication_v1_otp_verify_create(data)





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
api_instance = swagger_client.AuthenticationOtpApi(swagger_client.ApiClient(configuration))
data = swagger_client.OtpVerify() # OtpVerify | 

try:
    api_response = api_instance.authentication_v1_otp_verify_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationOtpApi->authentication_v1_otp_verify_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**OtpVerify**](OtpVerify.md)|  | 

### Return type

[**OtpVerify**](OtpVerify.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

