# swagger_client.UsersProfileApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_v1_profile_read**](UsersProfileApi.md#users_v1_profile_read) | **GET** /users/v1/profile/ | 


# **users_v1_profile_read**
> User users_v1_profile_read()





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
api_instance = swagger_client.UsersProfileApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.users_v1_profile_read()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersProfileApi->users_v1_profile_read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

