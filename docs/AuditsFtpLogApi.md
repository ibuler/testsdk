# swagger_client.AuditsFtpLogApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audits_v1_ftp_log_create**](AuditsFtpLogApi.md#audits_v1_ftp_log_create) | **POST** /audits/v1/ftp-log/ | 
[**audits_v1_ftp_log_delete**](AuditsFtpLogApi.md#audits_v1_ftp_log_delete) | **DELETE** /audits/v1/ftp-log/{id}/ | 
[**audits_v1_ftp_log_list**](AuditsFtpLogApi.md#audits_v1_ftp_log_list) | **GET** /audits/v1/ftp-log/ | 
[**audits_v1_ftp_log_partial_update**](AuditsFtpLogApi.md#audits_v1_ftp_log_partial_update) | **PATCH** /audits/v1/ftp-log/{id}/ | 
[**audits_v1_ftp_log_read**](AuditsFtpLogApi.md#audits_v1_ftp_log_read) | **GET** /audits/v1/ftp-log/{id}/ | 
[**audits_v1_ftp_log_update**](AuditsFtpLogApi.md#audits_v1_ftp_log_update) | **PUT** /audits/v1/ftp-log/{id}/ | 


# **audits_v1_ftp_log_create**
> FTPLog audits_v1_ftp_log_create(data)





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
api_instance = swagger_client.AuditsFtpLogApi(swagger_client.ApiClient(configuration))
data = swagger_client.FTPLog() # FTPLog | 

try:
    api_response = api_instance.audits_v1_ftp_log_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditsFtpLogApi->audits_v1_ftp_log_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FTPLog**](FTPLog.md)|  | 

### Return type

[**FTPLog**](FTPLog.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audits_v1_ftp_log_delete**
> audits_v1_ftp_log_delete(id)





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
api_instance = swagger_client.AuditsFtpLogApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ftp log.

try:
    api_instance.audits_v1_ftp_log_delete(id)
except ApiException as e:
    print("Exception when calling AuditsFtpLogApi->audits_v1_ftp_log_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ftp log. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audits_v1_ftp_log_list**
> list[FTPLog] audits_v1_ftp_log_list(search=search, order=order)





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
api_instance = swagger_client.AuditsFtpLogApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.audits_v1_ftp_log_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditsFtpLogApi->audits_v1_ftp_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[FTPLog]**](FTPLog.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audits_v1_ftp_log_partial_update**
> FTPLog audits_v1_ftp_log_partial_update(id, data)





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
api_instance = swagger_client.AuditsFtpLogApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ftp log.
data = swagger_client.FTPLog() # FTPLog | 

try:
    api_response = api_instance.audits_v1_ftp_log_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditsFtpLogApi->audits_v1_ftp_log_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ftp log. | 
 **data** | [**FTPLog**](FTPLog.md)|  | 

### Return type

[**FTPLog**](FTPLog.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audits_v1_ftp_log_read**
> FTPLog audits_v1_ftp_log_read(id)





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
api_instance = swagger_client.AuditsFtpLogApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ftp log.

try:
    api_response = api_instance.audits_v1_ftp_log_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditsFtpLogApi->audits_v1_ftp_log_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ftp log. | 

### Return type

[**FTPLog**](FTPLog.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audits_v1_ftp_log_update**
> FTPLog audits_v1_ftp_log_update(id, data)





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
api_instance = swagger_client.AuditsFtpLogApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this ftp log.
data = swagger_client.FTPLog() # FTPLog | 

try:
    api_response = api_instance.audits_v1_ftp_log_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditsFtpLogApi->audits_v1_ftp_log_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ftp log. | 
 **data** | [**FTPLog**](FTPLog.md)|  | 

### Return type

[**FTPLog**](FTPLog.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

