# swagger_client.XpackCloudApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**xpack_v1_cloud_account_create**](XpackCloudApi.md#xpack_v1_cloud_account_create) | **POST** /xpack/v1/cloud/account/ | 
[**xpack_v1_cloud_account_delete**](XpackCloudApi.md#xpack_v1_cloud_account_delete) | **DELETE** /xpack/v1/cloud/account/ | 
[**xpack_v1_cloud_account_delete_0**](XpackCloudApi.md#xpack_v1_cloud_account_delete_0) | **DELETE** /xpack/v1/cloud/account/{id}/ | 
[**xpack_v1_cloud_account_list**](XpackCloudApi.md#xpack_v1_cloud_account_list) | **GET** /xpack/v1/cloud/account/ | 
[**xpack_v1_cloud_account_partial_update**](XpackCloudApi.md#xpack_v1_cloud_account_partial_update) | **PATCH** /xpack/v1/cloud/account/ | 
[**xpack_v1_cloud_account_partial_update_0**](XpackCloudApi.md#xpack_v1_cloud_account_partial_update_0) | **PATCH** /xpack/v1/cloud/account/{id}/ | 
[**xpack_v1_cloud_account_read**](XpackCloudApi.md#xpack_v1_cloud_account_read) | **GET** /xpack/v1/cloud/account/{id}/ | 
[**xpack_v1_cloud_account_update**](XpackCloudApi.md#xpack_v1_cloud_account_update) | **PUT** /xpack/v1/cloud/account/ | 
[**xpack_v1_cloud_account_update_0**](XpackCloudApi.md#xpack_v1_cloud_account_update_0) | **PUT** /xpack/v1/cloud/account/{id}/ | 
[**xpack_v1_cloud_get_instances_list**](XpackCloudApi.md#xpack_v1_cloud_get_instances_list) | **GET** /xpack/v1/cloud/get-instances/ | 
[**xpack_v1_cloud_get_regions_list**](XpackCloudApi.md#xpack_v1_cloud_get_regions_list) | **GET** /xpack/v1/cloud/get-regions/ | 
[**xpack_v1_cloud_sync_instance_task_create**](XpackCloudApi.md#xpack_v1_cloud_sync_instance_task_create) | **POST** /xpack/v1/cloud/sync-instance-task/ | 
[**xpack_v1_cloud_sync_instance_task_delete**](XpackCloudApi.md#xpack_v1_cloud_sync_instance_task_delete) | **DELETE** /xpack/v1/cloud/sync-instance-task/ | 
[**xpack_v1_cloud_sync_instance_task_delete_0**](XpackCloudApi.md#xpack_v1_cloud_sync_instance_task_delete_0) | **DELETE** /xpack/v1/cloud/sync-instance-task/{id}/ | 
[**xpack_v1_cloud_sync_instance_task_list**](XpackCloudApi.md#xpack_v1_cloud_sync_instance_task_list) | **GET** /xpack/v1/cloud/sync-instance-task/ | 
[**xpack_v1_cloud_sync_instance_task_partial_update**](XpackCloudApi.md#xpack_v1_cloud_sync_instance_task_partial_update) | **PATCH** /xpack/v1/cloud/sync-instance-task/ | 
[**xpack_v1_cloud_sync_instance_task_partial_update_0**](XpackCloudApi.md#xpack_v1_cloud_sync_instance_task_partial_update_0) | **PATCH** /xpack/v1/cloud/sync-instance-task/{id}/ | 
[**xpack_v1_cloud_sync_instance_task_read**](XpackCloudApi.md#xpack_v1_cloud_sync_instance_task_read) | **GET** /xpack/v1/cloud/sync-instance-task/{id}/ | 
[**xpack_v1_cloud_sync_instance_task_run_list**](XpackCloudApi.md#xpack_v1_cloud_sync_instance_task_run_list) | **GET** /xpack/v1/cloud/sync-instance-task/{id}/run/ | 
[**xpack_v1_cloud_sync_instance_task_update**](XpackCloudApi.md#xpack_v1_cloud_sync_instance_task_update) | **PUT** /xpack/v1/cloud/sync-instance-task/ | 
[**xpack_v1_cloud_sync_instance_task_update_0**](XpackCloudApi.md#xpack_v1_cloud_sync_instance_task_update_0) | **PUT** /xpack/v1/cloud/sync-instance-task/{id}/ | 


# **xpack_v1_cloud_account_create**
> Account xpack_v1_cloud_account_create(data)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
data = swagger_client.Account() # Account | 

try:
    api_response = api_instance.xpack_v1_cloud_account_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_account_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Account**](Account.md)|  | 

### Return type

[**Account**](Account.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_account_delete**
> xpack_v1_cloud_account_delete(search=search, order=order)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.xpack_v1_cloud_account_delete(search=search, order=order)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_account_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_account_delete_0**
> xpack_v1_cloud_account_delete_0(id)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 云账号.

try:
    api_instance.xpack_v1_cloud_account_delete_0(id)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_account_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 云账号. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_account_list**
> list[Account] xpack_v1_cloud_account_list(search=search, order=order)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.xpack_v1_cloud_account_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_account_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Account]**](Account.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_account_partial_update**
> Account xpack_v1_cloud_account_partial_update(data)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
data = swagger_client.Account() # Account | 

try:
    api_response = api_instance.xpack_v1_cloud_account_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_account_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Account**](Account.md)|  | 

### Return type

[**Account**](Account.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_account_partial_update_0**
> Account xpack_v1_cloud_account_partial_update_0(id, data)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 云账号.
data = swagger_client.Account() # Account | 

try:
    api_response = api_instance.xpack_v1_cloud_account_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_account_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 云账号. | 
 **data** | [**Account**](Account.md)|  | 

### Return type

[**Account**](Account.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_account_read**
> Account xpack_v1_cloud_account_read(id)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 云账号.

try:
    api_response = api_instance.xpack_v1_cloud_account_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_account_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 云账号. | 

### Return type

[**Account**](Account.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_account_update**
> Account xpack_v1_cloud_account_update(data)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
data = swagger_client.Account() # Account | 

try:
    api_response = api_instance.xpack_v1_cloud_account_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_account_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Account**](Account.md)|  | 

### Return type

[**Account**](Account.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_account_update_0**
> Account xpack_v1_cloud_account_update_0(id, data)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 云账号.
data = swagger_client.Account() # Account | 

try:
    api_response = api_instance.xpack_v1_cloud_account_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_account_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 云账号. | 
 **data** | [**Account**](Account.md)|  | 

### Return type

[**Account**](Account.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_get_instances_list**
> xpack_v1_cloud_get_instances_list()





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))

try:
    api_instance.xpack_v1_cloud_get_instances_list()
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_get_instances_list: %s\n" % e)
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

# **xpack_v1_cloud_get_regions_list**
> xpack_v1_cloud_get_regions_list()





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))

try:
    api_instance.xpack_v1_cloud_get_regions_list()
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_get_regions_list: %s\n" % e)
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

# **xpack_v1_cloud_sync_instance_task_create**
> SyncInstanceTask xpack_v1_cloud_sync_instance_task_create(data)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
data = swagger_client.SyncInstanceTask() # SyncInstanceTask | 

try:
    api_response = api_instance.xpack_v1_cloud_sync_instance_task_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_sync_instance_task_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SyncInstanceTask**](SyncInstanceTask.md)|  | 

### Return type

[**SyncInstanceTask**](SyncInstanceTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_sync_instance_task_delete**
> xpack_v1_cloud_sync_instance_task_delete(search=search, order=order)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.xpack_v1_cloud_sync_instance_task_delete(search=search, order=order)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_sync_instance_task_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_sync_instance_task_delete_0**
> xpack_v1_cloud_sync_instance_task_delete_0(id)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 同步实例任务.

try:
    api_instance.xpack_v1_cloud_sync_instance_task_delete_0(id)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_sync_instance_task_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 同步实例任务. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_sync_instance_task_list**
> list[SyncInstanceTask] xpack_v1_cloud_sync_instance_task_list(search=search, order=order)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.xpack_v1_cloud_sync_instance_task_list(search=search, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_sync_instance_task_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[SyncInstanceTask]**](SyncInstanceTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_sync_instance_task_partial_update**
> SyncInstanceTask xpack_v1_cloud_sync_instance_task_partial_update(data)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
data = swagger_client.SyncInstanceTask() # SyncInstanceTask | 

try:
    api_response = api_instance.xpack_v1_cloud_sync_instance_task_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_sync_instance_task_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SyncInstanceTask**](SyncInstanceTask.md)|  | 

### Return type

[**SyncInstanceTask**](SyncInstanceTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_sync_instance_task_partial_update_0**
> SyncInstanceTask xpack_v1_cloud_sync_instance_task_partial_update_0(id, data)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 同步实例任务.
data = swagger_client.SyncInstanceTask() # SyncInstanceTask | 

try:
    api_response = api_instance.xpack_v1_cloud_sync_instance_task_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_sync_instance_task_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 同步实例任务. | 
 **data** | [**SyncInstanceTask**](SyncInstanceTask.md)|  | 

### Return type

[**SyncInstanceTask**](SyncInstanceTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_sync_instance_task_read**
> SyncInstanceTask xpack_v1_cloud_sync_instance_task_read(id)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 同步实例任务.

try:
    api_response = api_instance.xpack_v1_cloud_sync_instance_task_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_sync_instance_task_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 同步实例任务. | 

### Return type

[**SyncInstanceTask**](SyncInstanceTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_sync_instance_task_run_list**
> xpack_v1_cloud_sync_instance_task_run_list(id)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.xpack_v1_cloud_sync_instance_task_run_list(id)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_sync_instance_task_run_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_sync_instance_task_update**
> SyncInstanceTask xpack_v1_cloud_sync_instance_task_update(data)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
data = swagger_client.SyncInstanceTask() # SyncInstanceTask | 

try:
    api_response = api_instance.xpack_v1_cloud_sync_instance_task_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_sync_instance_task_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SyncInstanceTask**](SyncInstanceTask.md)|  | 

### Return type

[**SyncInstanceTask**](SyncInstanceTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xpack_v1_cloud_sync_instance_task_update_0**
> SyncInstanceTask xpack_v1_cloud_sync_instance_task_update_0(id, data)





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
api_instance = swagger_client.XpackCloudApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 同步实例任务.
data = swagger_client.SyncInstanceTask() # SyncInstanceTask | 

try:
    api_response = api_instance.xpack_v1_cloud_sync_instance_task_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XpackCloudApi->xpack_v1_cloud_sync_instance_task_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 同步实例任务. | 
 **data** | [**SyncInstanceTask**](SyncInstanceTask.md)|  | 

### Return type

[**SyncInstanceTask**](SyncInstanceTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

