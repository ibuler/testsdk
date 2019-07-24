# swagger_client.SettingsMailApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_v1_mail_testing_create**](SettingsMailApi.md#settings_v1_mail_testing_create) | **POST** /settings/v1/mail/testing/ | 


# **settings_v1_mail_testing_create**
> settings_v1_mail_testing_create()





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
api_instance = swagger_client.SettingsMailApi(swagger_client.ApiClient(configuration))

try:
    api_instance.settings_v1_mail_testing_create()
except ApiException as e:
    print("Exception when calling SettingsMailApi->settings_v1_mail_testing_create: %s\n" % e)
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

