# swagger_client.SettingsTerminalApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_v1_terminal_command_storage_create_create**](SettingsTerminalApi.md#settings_v1_terminal_command_storage_create_create) | **POST** /settings/v1/terminal/command-storage/create/ | 
[**settings_v1_terminal_command_storage_delete_create**](SettingsTerminalApi.md#settings_v1_terminal_command_storage_delete_create) | **POST** /settings/v1/terminal/command-storage/delete/ | 
[**settings_v1_terminal_replay_storage_create_create**](SettingsTerminalApi.md#settings_v1_terminal_replay_storage_create_create) | **POST** /settings/v1/terminal/replay-storage/create/ | 
[**settings_v1_terminal_replay_storage_delete_create**](SettingsTerminalApi.md#settings_v1_terminal_replay_storage_delete_create) | **POST** /settings/v1/terminal/replay-storage/delete/ | 


# **settings_v1_terminal_command_storage_create_create**
> settings_v1_terminal_command_storage_create_create()





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
api_instance = swagger_client.SettingsTerminalApi(swagger_client.ApiClient(configuration))

try:
    api_instance.settings_v1_terminal_command_storage_create_create()
except ApiException as e:
    print("Exception when calling SettingsTerminalApi->settings_v1_terminal_command_storage_create_create: %s\n" % e)
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

# **settings_v1_terminal_command_storage_delete_create**
> settings_v1_terminal_command_storage_delete_create()





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
api_instance = swagger_client.SettingsTerminalApi(swagger_client.ApiClient(configuration))

try:
    api_instance.settings_v1_terminal_command_storage_delete_create()
except ApiException as e:
    print("Exception when calling SettingsTerminalApi->settings_v1_terminal_command_storage_delete_create: %s\n" % e)
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

# **settings_v1_terminal_replay_storage_create_create**
> settings_v1_terminal_replay_storage_create_create()





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
api_instance = swagger_client.SettingsTerminalApi(swagger_client.ApiClient(configuration))

try:
    api_instance.settings_v1_terminal_replay_storage_create_create()
except ApiException as e:
    print("Exception when calling SettingsTerminalApi->settings_v1_terminal_replay_storage_create_create: %s\n" % e)
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

# **settings_v1_terminal_replay_storage_delete_create**
> settings_v1_terminal_replay_storage_delete_create()





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
api_instance = swagger_client.SettingsTerminalApi(swagger_client.ApiClient(configuration))

try:
    api_instance.settings_v1_terminal_replay_storage_delete_create()
except ApiException as e:
    print("Exception when calling SettingsTerminalApi->settings_v1_terminal_replay_storage_delete_create: %s\n" % e)
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

