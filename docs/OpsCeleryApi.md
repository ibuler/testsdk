# swagger_client.OpsCeleryApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ops_v1_celery_task_log_read**](OpsCeleryApi.md#ops_v1_celery_task_log_read) | **GET** /ops/v1/celery/task/{id}/log/ | 
[**ops_v1_celery_task_result_read**](OpsCeleryApi.md#ops_v1_celery_task_result_read) | **GET** /ops/v1/celery/task/{id}/result/ | 


# **ops_v1_celery_task_log_read**
> Output ops_v1_celery_task_log_read(id)





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
api_instance = swagger_client.OpsCeleryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.ops_v1_celery_task_log_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsCeleryApi->ops_v1_celery_task_log_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Output**](Output.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ops_v1_celery_task_result_read**
> CeleryResult ops_v1_celery_task_result_read(id)





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
api_instance = swagger_client.OpsCeleryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.ops_v1_celery_task_result_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpsCeleryApi->ops_v1_celery_task_result_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CeleryResult**](CeleryResult.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

