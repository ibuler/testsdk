# swagger_client.AssetsCmdFiltersApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_v1_cmd_filters_create**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_create) | **POST** /assets/v1/cmd-filters/ | 
[**assets_v1_cmd_filters_delete**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_delete) | **DELETE** /assets/v1/cmd-filters/ | 
[**assets_v1_cmd_filters_delete_0**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_delete_0) | **DELETE** /assets/v1/cmd-filters/{id}/ | 
[**assets_v1_cmd_filters_list**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_list) | **GET** /assets/v1/cmd-filters/ | 
[**assets_v1_cmd_filters_partial_update**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_partial_update) | **PATCH** /assets/v1/cmd-filters/ | 
[**assets_v1_cmd_filters_partial_update_0**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_partial_update_0) | **PATCH** /assets/v1/cmd-filters/{id}/ | 
[**assets_v1_cmd_filters_read**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_read) | **GET** /assets/v1/cmd-filters/{id}/ | 
[**assets_v1_cmd_filters_rules_create**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_rules_create) | **POST** /assets/v1/cmd-filters/{filter_pk}/rules/ | 
[**assets_v1_cmd_filters_rules_delete**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_rules_delete) | **DELETE** /assets/v1/cmd-filters/{filter_pk}/rules/{id}/ | 
[**assets_v1_cmd_filters_rules_list**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_rules_list) | **GET** /assets/v1/cmd-filters/{filter_pk}/rules/ | 
[**assets_v1_cmd_filters_rules_partial_update**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_rules_partial_update) | **PATCH** /assets/v1/cmd-filters/{filter_pk}/rules/{id}/ | 
[**assets_v1_cmd_filters_rules_read**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_rules_read) | **GET** /assets/v1/cmd-filters/{filter_pk}/rules/{id}/ | 
[**assets_v1_cmd_filters_rules_update**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_rules_update) | **PUT** /assets/v1/cmd-filters/{filter_pk}/rules/{id}/ | 
[**assets_v1_cmd_filters_update**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_update) | **PUT** /assets/v1/cmd-filters/ | 
[**assets_v1_cmd_filters_update_0**](AssetsCmdFiltersApi.md#assets_v1_cmd_filters_update_0) | **PUT** /assets/v1/cmd-filters/{id}/ | 


# **assets_v1_cmd_filters_create**
> CommandFilter assets_v1_cmd_filters_create(data)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
data = swagger_client.CommandFilter() # CommandFilter | 

try:
    api_response = api_instance.assets_v1_cmd_filters_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CommandFilter**](CommandFilter.md)|  | 

### Return type

[**CommandFilter**](CommandFilter.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_delete**
> assets_v1_cmd_filters_delete(name=name, search=search, order=order)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)

try:
    api_instance.assets_v1_cmd_filters_delete(name=name, search=search, order=order)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
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

# **assets_v1_cmd_filters_delete_0**
> assets_v1_cmd_filters_delete_0(id)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 命令过滤器.

try:
    api_instance.assets_v1_cmd_filters_delete_0(id)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 命令过滤器. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_list**
> InlineResponse2006 assets_v1_cmd_filters_list(name=name, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_cmd_filters_list(name=name, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_partial_update**
> CommandFilter assets_v1_cmd_filters_partial_update(data)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
data = swagger_client.CommandFilter() # CommandFilter | 

try:
    api_response = api_instance.assets_v1_cmd_filters_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CommandFilter**](CommandFilter.md)|  | 

### Return type

[**CommandFilter**](CommandFilter.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_partial_update_0**
> CommandFilter assets_v1_cmd_filters_partial_update_0(id, data)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 命令过滤器.
data = swagger_client.CommandFilter() # CommandFilter | 

try:
    api_response = api_instance.assets_v1_cmd_filters_partial_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 命令过滤器. | 
 **data** | [**CommandFilter**](CommandFilter.md)|  | 

### Return type

[**CommandFilter**](CommandFilter.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_read**
> CommandFilter assets_v1_cmd_filters_read(id)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 命令过滤器.

try:
    api_response = api_instance.assets_v1_cmd_filters_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 命令过滤器. | 

### Return type

[**CommandFilter**](CommandFilter.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_rules_create**
> CommandFilterRule assets_v1_cmd_filters_rules_create(filter_pk, data)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
filter_pk = 'filter_pk_example' # str | 
data = swagger_client.CommandFilterRule() # CommandFilterRule | 

try:
    api_response = api_instance.assets_v1_cmd_filters_rules_create(filter_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_rules_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_pk** | **str**|  | 
 **data** | [**CommandFilterRule**](CommandFilterRule.md)|  | 

### Return type

[**CommandFilterRule**](CommandFilterRule.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_rules_delete**
> assets_v1_cmd_filters_rules_delete(filter_pk, id)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
filter_pk = 'filter_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.assets_v1_cmd_filters_rules_delete(filter_pk, id)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_rules_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_rules_list**
> InlineResponse2007 assets_v1_cmd_filters_rules_list(filter_pk, content=content, search=search, order=order, limit=limit, offset=offset)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
filter_pk = 'filter_pk_example' # str | 
content = 'content_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
order = 'order_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.assets_v1_cmd_filters_rules_list(filter_pk, content=content, search=search, order=order, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_rules_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_pk** | **str**|  | 
 **content** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **order** | **str**| Which field to use when ordering the results. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_rules_partial_update**
> CommandFilterRule assets_v1_cmd_filters_rules_partial_update(filter_pk, id, data)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
filter_pk = 'filter_pk_example' # str | 
id = 'id_example' # str | 
data = swagger_client.CommandFilterRule() # CommandFilterRule | 

try:
    api_response = api_instance.assets_v1_cmd_filters_rules_partial_update(filter_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_rules_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**CommandFilterRule**](CommandFilterRule.md)|  | 

### Return type

[**CommandFilterRule**](CommandFilterRule.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_rules_read**
> CommandFilterRule assets_v1_cmd_filters_rules_read(filter_pk, id)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
filter_pk = 'filter_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.assets_v1_cmd_filters_rules_read(filter_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_rules_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**CommandFilterRule**](CommandFilterRule.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_rules_update**
> CommandFilterRule assets_v1_cmd_filters_rules_update(filter_pk, id, data)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
filter_pk = 'filter_pk_example' # str | 
id = 'id_example' # str | 
data = swagger_client.CommandFilterRule() # CommandFilterRule | 

try:
    api_response = api_instance.assets_v1_cmd_filters_rules_update(filter_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_rules_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**CommandFilterRule**](CommandFilterRule.md)|  | 

### Return type

[**CommandFilterRule**](CommandFilterRule.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_update**
> CommandFilter assets_v1_cmd_filters_update(data)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
data = swagger_client.CommandFilter() # CommandFilter | 

try:
    api_response = api_instance.assets_v1_cmd_filters_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CommandFilter**](CommandFilter.md)|  | 

### Return type

[**CommandFilter**](CommandFilter.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_v1_cmd_filters_update_0**
> CommandFilter assets_v1_cmd_filters_update_0(id, data)





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
api_instance = swagger_client.AssetsCmdFiltersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this 命令过滤器.
data = swagger_client.CommandFilter() # CommandFilter | 

try:
    api_response = api_instance.assets_v1_cmd_filters_update_0(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsCmdFiltersApi->assets_v1_cmd_filters_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this 命令过滤器. | 
 **data** | [**CommandFilter**](CommandFilter.md)|  | 

### Return type

[**CommandFilter**](CommandFilter.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json, text/csv, */*
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

