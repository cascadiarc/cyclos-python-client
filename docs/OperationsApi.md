# swagger_client.OperationsApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ad_operation_data_for_run**](OperationsApi.md#get_ad_operation_data_for_run) | **GET** /marketplace/{ad}/operations/{operation}/data-for-run | Returns configuration data for running a custom operation over an advertisement 
[**get_contact_info_operation_data_for_run**](OperationsApi.md#get_contact_info_operation_data_for_run) | **GET** /contact-infos/{id}/operations/{operation}/data-for-run | Returns configuration data for running a custom operation over an additional contact information 
[**get_contact_operation_data_for_run**](OperationsApi.md#get_contact_operation_data_for_run) | **GET** /contact-list/{id}/operations/{operation}/data-for-run | Returns configuration data for running a custom operation over a contact 
[**get_operation_data_for_run**](OperationsApi.md#get_operation_data_for_run) | **GET** /operations/{operation}/data-for-run | Returns configuration data for running a custom operation without additional scope 
[**get_owner_operation_data_for_run**](OperationsApi.md#get_owner_operation_data_for_run) | **GET** /{owner}/operations/{operation}/data-for-run | Returns configuration data for running a custom operation over an owner 
[**get_record_operation_data_for_run**](OperationsApi.md#get_record_operation_data_for_run) | **GET** /records/{id}/operations/{operation}/data-for-run | Returns configuration data for running a custom operation over a record 
[**get_transfer_operation_data_for_run**](OperationsApi.md#get_transfer_operation_data_for_run) | **GET** /transfer/{key}/operations/{operation}/data-for-run | Returns configuration data for running a custom operation over a transfer 
[**list_operations_by_ad**](OperationsApi.md#list_operations_by_ad) | **GET** /marketplace/{ad}/operations | Lists the custom operations over the given advertisement
[**list_operations_by_contact**](OperationsApi.md#list_operations_by_contact) | **GET** /contact-list/{id}/operations | Lists the custom operations over the given contact
[**list_operations_by_contact_info**](OperationsApi.md#list_operations_by_contact_info) | **GET** /contact-infos/{id}/operations | Lists the custom operations over the given additional contact information 
[**list_operations_by_owner**](OperationsApi.md#list_operations_by_owner) | **GET** /{owner}/operations | Lists the custom operations over the system or user
[**list_operations_by_record**](OperationsApi.md#list_operations_by_record) | **GET** /records/{id}/operations | Lists the custom operations over the given record
[**list_operations_by_transfer**](OperationsApi.md#list_operations_by_transfer) | **GET** /transfers/{key}/operations | Lists the custom operations over the given transfer
[**run_ad_operation**](OperationsApi.md#run_ad_operation) | **POST** /marketplace/{ad}/operations/{operation}/run | Runs a custom operation over an advertisement
[**run_ad_operation_with_upload**](OperationsApi.md#run_ad_operation_with_upload) | **POST** /marketplace/{ad}/operations/{operation}/run-upload | Runs a custom operation over an advertisement while uploading a file 
[**run_contact_info_operation**](OperationsApi.md#run_contact_info_operation) | **POST** /contact-infos/{id}/operations/{operation}/run | Runs a custom operation over an additional contact information 
[**run_contact_info_operation_with_upload**](OperationsApi.md#run_contact_info_operation_with_upload) | **POST** /contact-infos/{id}/operations/{operation}/run-upload | Runs a custom operation over an additional contact information while uploading a file 
[**run_contact_operation**](OperationsApi.md#run_contact_operation) | **POST** /contact-list/{id}/operations/{operation}/run | Runs a custom operation over a contact
[**run_contact_operation_with_upload**](OperationsApi.md#run_contact_operation_with_upload) | **POST** /contact-list/{id}/operations/{operation}/run-upload | Runs a custom operation over an contact while uploading a file 
[**run_custom_operation_callback**](OperationsApi.md#run_custom_operation_callback) | **POST** /operations/callback/{id} | Runs the callback of an external redirect custom operation 
[**run_operation**](OperationsApi.md#run_operation) | **POST** /operations/{operation}/run | Runs a custom operation without additional scope
[**run_operation_with_upload**](OperationsApi.md#run_operation_with_upload) | **POST** /operations/{operation}/run-upload | Runs a custom operation without additional scope while uploading a file 
[**run_owner_operation**](OperationsApi.md#run_owner_operation) | **POST** /{owner}/operations/{operation}/run | Runs a custom operation either for system or user
[**run_owner_operation_with_upload**](OperationsApi.md#run_owner_operation_with_upload) | **POST** /{owner}/operations/{operation}/run-upload | Runs a custom operation either for system or user while uploading a file 
[**run_record_operation**](OperationsApi.md#run_record_operation) | **POST** /records/{id}/operations/{operation}/run | Runs a custom operation over a record
[**run_record_operation_with_upload**](OperationsApi.md#run_record_operation_with_upload) | **POST** /records/{id}/operations/{operation}/run-upload | Runs a custom operation over a record while uploading a file 
[**run_transfer_operation**](OperationsApi.md#run_transfer_operation) | **POST** /transfers/{key}/operations/{operation}/run | Runs a custom operation over a transfer
[**run_transfer_operation_with_upload**](OperationsApi.md#run_transfer_operation_with_upload) | **POST** /transfers/{key}/operations/{operation}/run-upload | Runs a custom operation over a transfer while uploading a file 


# **get_ad_operation_data_for_run**
> OperationDataForRun get_ad_operation_data_for_run(ad, operation, fields=fields)

Returns configuration data for running a custom operation over an advertisement 

Returns data to run a specific custom operation over an advertisement. The operation scope must be `advertisement`.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data for running a custom operation over an advertisement 
    api_response = api_instance.get_ad_operation_data_for_run(ad, operation, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_ad_operation_data_for_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**OperationDataForRun**](OperationDataForRun.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_info_operation_data_for_run**
> OperationDataForRun get_contact_info_operation_data_for_run(id, operation, fields=fields)

Returns configuration data for running a custom operation over an additional contact information 

Returns data to run a specific custom operation over an additional contact information. The operation scope must be `contactInfo`.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data for running a custom operation over an additional contact information 
    api_response = api_instance.get_contact_info_operation_data_for_run(id, operation, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_contact_info_operation_data_for_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**OperationDataForRun**](OperationDataForRun.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_operation_data_for_run**
> OperationDataForRun get_contact_operation_data_for_run(id, operation, fields=fields)

Returns configuration data for running a custom operation over a contact 

Returns data to run a specific custom operation over a contact. The operation scope must be `contact`.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data for running a custom operation over a contact 
    api_response = api_instance.get_contact_operation_data_for_run(id, operation, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_contact_operation_data_for_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**OperationDataForRun**](OperationDataForRun.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_data_for_run**
> OperationDataForRun get_operation_data_for_run(operation, fields=fields)

Returns configuration data for running a custom operation without additional scope 

Returns data to run a specific custom operation, which must not have any additional scope to run, such as user, contact, record or advertisement. Hence, this path is suitable for custom operations with scope `system` or `internal`.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data for running a custom operation without additional scope 
    api_response = api_instance.get_operation_data_for_run(operation, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_operation_data_for_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**OperationDataForRun**](OperationDataForRun.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_owner_operation_data_for_run**
> OperationDataForRun get_owner_operation_data_for_run(owner, operation, fields=fields)

Returns configuration data for running a custom operation over an owner 

Returns data to run a specific custom operation over a given user or system if the `system` owner is used. The operation scope must match, being either `system` or `user`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data for running a custom operation over an owner 
    api_response = api_instance.get_owner_operation_data_for_run(owner, operation, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_owner_operation_data_for_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**OperationDataForRun**](OperationDataForRun.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_record_operation_data_for_run**
> OperationDataForRun get_record_operation_data_for_run(id, operation, fields=fields)

Returns configuration data for running a custom operation over a record 

Returns data to run a specific custom operation over a record. The operation scope must be `record`.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data for running a custom operation over a record 
    api_response = api_instance.get_record_operation_data_for_run(id, operation, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_record_operation_data_for_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**OperationDataForRun**](OperationDataForRun.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer_operation_data_for_run**
> OperationDataForRun get_transfer_operation_data_for_run(key, operation, fields=fields)

Returns configuration data for running a custom operation over a transfer 

Returns data to run a specific custom operation over a transfer. The operation scope must be `transfer`.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data for running a custom operation over a transfer 
    api_response = api_instance.get_transfer_operation_data_for_run(key, operation, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_transfer_operation_data_for_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**OperationDataForRun**](OperationDataForRun.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operations_by_ad**
> list[Operation] list_operations_by_ad(ad, fields=fields)

Lists the custom operations over the given advertisement

Returns the custom operations the authenticated user can run over the given advertisement. All returned operations have the scope `advertisement`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Lists the custom operations over the given advertisement
    api_response = api_instance.list_operations_by_ad(ad, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->list_operations_by_ad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**list[Operation]**](Operation.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operations_by_contact**
> list[Operation] list_operations_by_contact(id, fields=fields)

Lists the custom operations over the given contact

Returns the custom operations the authenticated user can run over the given contact. All returned operations have the scope `contact`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Lists the custom operations over the given contact
    api_response = api_instance.list_operations_by_contact(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->list_operations_by_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**list[Operation]**](Operation.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operations_by_contact_info**
> list[Operation] list_operations_by_contact_info(id, fields=fields)

Lists the custom operations over the given additional contact information 

Returns the custom operations the authenticated user can run over the given additional contact iformation. All returned operations have the scope `contactInfo`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Lists the custom operations over the given additional contact information 
    api_response = api_instance.list_operations_by_contact_info(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->list_operations_by_contact_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**list[Operation]**](Operation.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operations_by_owner**
> list[Operation] list_operations_by_owner(owner, fields=fields)

Lists the custom operations over the system or user

Returns the custom operations the authenticated user can run over the given user or system if the `system` owner is used.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Lists the custom operations over the system or user
    api_response = api_instance.list_operations_by_owner(owner, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->list_operations_by_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**list[Operation]**](Operation.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operations_by_record**
> list[Operation] list_operations_by_record(id, fields=fields)

Lists the custom operations over the given record

Returns the custom operations the authenticated user can run over the given record. All returned operations have the scope `record`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Lists the custom operations over the given record
    api_response = api_instance.list_operations_by_record(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->list_operations_by_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**list[Operation]**](Operation.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operations_by_transfer**
> list[Operation] list_operations_by_transfer(key, fields=fields)

Lists the custom operations over the given transfer

Returns the custom operations the authenticated user can run over the given transfer. All returned operations have the scope `transfer`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Lists the custom operations over the given transfer
    api_response = api_instance.list_operations_by_transfer(key, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->list_operations_by_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**list[Operation]**](Operation.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_ad_operation**
> RunOperationResult run_ad_operation(ad, operation, fields=fields, params=params)

Runs a custom operation over an advertisement

Runs a specific custom operation over a given advertisement. The operation scope must be `advertisement`. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = swagger_client.RunOperation() # RunOperation | The custom operation parameters (optional)

try:
    # Runs a custom operation over an advertisement
    api_response = api_instance.run_ad_operation(ad, operation, fields=fields, params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_ad_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | [**RunOperation**](RunOperation.md)| The custom operation parameters | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_ad_operation_with_upload**
> RunOperationResult run_ad_operation_with_upload(ad, operation, fields=fields, params=params, file=file)

Runs a custom operation over an advertisement while uploading a file 

Runs a specific custom operation over a given advertisement. The operation scope must be `advertisement`. This path allows uploading a file, by using a `multipart-form-data` post. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = 'params_example' # str | The custom operation parameters, encoded as `RunOperation`.   (optional)
file = '/path/to/file.txt' # file | The file being uploaded (optional)

try:
    # Runs a custom operation over an advertisement while uploading a file 
    api_response = api_instance.run_ad_operation_with_upload(ad, operation, fields=fields, params=params, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_ad_operation_with_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | **str**| The custom operation parameters, encoded as &#x60;RunOperation&#x60;.   | [optional] 
 **file** | **file**| The file being uploaded | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_contact_info_operation**
> RunOperationResult run_contact_info_operation(id, operation, fields=fields, params=params)

Runs a custom operation over an additional contact information 

Runs a specific custom operation over a given additional contact information. The operation scope must be `contactInfo`. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = swagger_client.RunOperation() # RunOperation | The custom operation parameters (optional)

try:
    # Runs a custom operation over an additional contact information 
    api_response = api_instance.run_contact_info_operation(id, operation, fields=fields, params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_contact_info_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | [**RunOperation**](RunOperation.md)| The custom operation parameters | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_contact_info_operation_with_upload**
> RunOperationResult run_contact_info_operation_with_upload(id, operation, fields=fields, params=params, file=file)

Runs a custom operation over an additional contact information while uploading a file 

Runs a specific custom operation over a given additional contact information. The operation scope must be `contactInfo`. This path allows uploading a file, by using a `multipart-form-data` post. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = 'params_example' # str | The custom operation parameters, encoded as `RunOperation`.   (optional)
file = '/path/to/file.txt' # file | The file being uploaded (optional)

try:
    # Runs a custom operation over an additional contact information while uploading a file 
    api_response = api_instance.run_contact_info_operation_with_upload(id, operation, fields=fields, params=params, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_contact_info_operation_with_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | **str**| The custom operation parameters, encoded as &#x60;RunOperation&#x60;.   | [optional] 
 **file** | **file**| The file being uploaded | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_contact_operation**
> RunOperationResult run_contact_operation(id, operation, fields=fields, params=params)

Runs a custom operation over a contact

Runs a specific custom operation over a given contact. The operation scope must be `contact`. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = swagger_client.RunOperation() # RunOperation | The custom operation parameters (optional)

try:
    # Runs a custom operation over a contact
    api_response = api_instance.run_contact_operation(id, operation, fields=fields, params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_contact_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | [**RunOperation**](RunOperation.md)| The custom operation parameters | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_contact_operation_with_upload**
> RunOperationResult run_contact_operation_with_upload(id, operation, fields=fields, params=params, file=file)

Runs a custom operation over an contact while uploading a file 

Runs a specific custom operation over a given contact. The operation scope must be `contact`. This path allows uploading a file, by using a `multipart-form-data` post. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = 'params_example' # str | The custom operation parameters, encoded as `RunOperation`.   (optional)
file = '/path/to/file.txt' # file | The file being uploaded (optional)

try:
    # Runs a custom operation over an contact while uploading a file 
    api_response = api_instance.run_contact_operation_with_upload(id, operation, fields=fields, params=params, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_contact_operation_with_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | **str**| The custom operation parameters, encoded as &#x60;RunOperation&#x60;.   | [optional] 
 **file** | **file**| The file being uploaded | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_custom_operation_callback**
> RunOperationResult run_custom_operation_callback(id, token=token, callback_request=callback_request)

Runs the callback of an external redirect custom operation 

Custom operations may be configured in Cyclos to be of result type `externalRedirect`. In such case, the regular execution returns an URL to which redirect clients. Once the external page processing is complete, the user is redirected back, so the operation can be completed. This operation should be executed to complete the payment. In order for the external service receive the correct URL, Cyclos need to have a link generation script that handles the link type `EXTERNAL_REDIRECT`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
id = 'id_example' # str | The external redirect identifier. Received as part of the URL which is generated by Cyclos to the external service to use as callback. 
token = 'token_example' # str | The security token which is received as part of the URL which is generated by Cyclos to the external service to use as callback.  (optional)
callback_request = swagger_client.HttpRequestData() # HttpRequestData | Data of the original callback request sent by the external service  (optional)

try:
    # Runs the callback of an external redirect custom operation 
    api_response = api_instance.run_custom_operation_callback(id, token=token, callback_request=callback_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_custom_operation_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The external redirect identifier. Received as part of the URL which is generated by Cyclos to the external service to use as callback.  | 
 **token** | **str**| The security token which is received as part of the URL which is generated by Cyclos to the external service to use as callback.  | [optional] 
 **callback_request** | [**HttpRequestData**](HttpRequestData.md)| Data of the original callback request sent by the external service  | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_operation**
> RunOperationResult run_operation(operation, fields=fields, params=params)

Runs a custom operation without additional scope

Runs a specific custom operation without additional scope. Is suitable for operations with scope `system` or `internal`. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = swagger_client.RunOperation() # RunOperation | The custom operation parameters (optional)

try:
    # Runs a custom operation without additional scope
    api_response = api_instance.run_operation(operation, fields=fields, params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | [**RunOperation**](RunOperation.md)| The custom operation parameters | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_operation_with_upload**
> RunOperationResult run_operation_with_upload(operation, fields=fields, params=params, file=file)

Runs a custom operation without additional scope while uploading a file 

Runs a specific custom operation without additional scope. Is suitable for operations with scope `system` or `internal`.  This path allows uploading a file, by using a `multipart-form-data` post. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = 'params_example' # str | The custom operation parameters, encoded as `RunOperation`.   (optional)
file = '/path/to/file.txt' # file | The file being uploaded (optional)

try:
    # Runs a custom operation without additional scope while uploading a file 
    api_response = api_instance.run_operation_with_upload(operation, fields=fields, params=params, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_operation_with_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | **str**| The custom operation parameters, encoded as &#x60;RunOperation&#x60;.   | [optional] 
 **file** | **file**| The file being uploaded | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_owner_operation**
> RunOperationResult run_owner_operation(owner, operation, fields=fields, params=params)

Runs a custom operation either for system or user

Runs a specific custom operation over a given user or system if the `system` owner is used. The operation scope must match, being either `system` or `user`.  If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = swagger_client.RunOperation() # RunOperation | The custom operation parameters (optional)

try:
    # Runs a custom operation either for system or user
    api_response = api_instance.run_owner_operation(owner, operation, fields=fields, params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_owner_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | [**RunOperation**](RunOperation.md)| The custom operation parameters | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_owner_operation_with_upload**
> RunOperationResult run_owner_operation_with_upload(owner, operation, fields=fields, params=params, file=file)

Runs a custom operation either for system or user while uploading a file 

Runs a specific custom operation over a given user or system if the `system` owner is used. The operation scope must match, being either `system` or `user`.  This path allows uploading a file, by using a `multipart-form-data` post. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = 'params_example' # str | The custom operation parameters, encoded as `RunOperation`.   (optional)
file = '/path/to/file.txt' # file | The file being uploaded (optional)

try:
    # Runs a custom operation either for system or user while uploading a file 
    api_response = api_instance.run_owner_operation_with_upload(owner, operation, fields=fields, params=params, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_owner_operation_with_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | **str**| The custom operation parameters, encoded as &#x60;RunOperation&#x60;.   | [optional] 
 **file** | **file**| The file being uploaded | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_record_operation**
> RunOperationResult run_record_operation(id, operation, fields=fields, params=params)

Runs a custom operation over a record

Runs a specific custom operation over a given record. The operation scope must be `record`. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = swagger_client.RunOperation() # RunOperation | The custom operation parameters (optional)

try:
    # Runs a custom operation over a record
    api_response = api_instance.run_record_operation(id, operation, fields=fields, params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_record_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | [**RunOperation**](RunOperation.md)| The custom operation parameters | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_record_operation_with_upload**
> RunOperationResult run_record_operation_with_upload(id, operation, fields=fields, params=params, file=file)

Runs a custom operation over a record while uploading a file 

Runs a specific custom operation over a given record. The operation scope must be `record`. This path allows uploading a file, by using a `multipart-form-data` post. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = 'params_example' # str | The custom operation parameters, encoded as `RunOperation`.   (optional)
file = '/path/to/file.txt' # file | The file being uploaded (optional)

try:
    # Runs a custom operation over a record while uploading a file 
    api_response = api_instance.run_record_operation_with_upload(id, operation, fields=fields, params=params, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_record_operation_with_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | **str**| The custom operation parameters, encoded as &#x60;RunOperation&#x60;.   | [optional] 
 **file** | **file**| The file being uploaded | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_transfer_operation**
> RunOperationResult run_transfer_operation(key, operation, fields=fields, params=params)

Runs a custom operation over a transfer

Runs a specific custom operation over a given transfer. The operation scope must be `transfer`. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = swagger_client.RunOperation() # RunOperation | The custom operation parameters (optional)

try:
    # Runs a custom operation over a transfer
    api_response = api_instance.run_transfer_operation(key, operation, fields=fields, params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_transfer_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | [**RunOperation**](RunOperation.md)| The custom operation parameters | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_transfer_operation_with_upload**
> RunOperationResult run_transfer_operation_with_upload(key, operation, fields=fields, params=params, file=file)

Runs a custom operation over a transfer while uploading a file 

Runs a specific custom operation over a given transfer. The operation scope must be `transfer`. This path allows uploading a file, by using a `multipart-form-data` post. If the operation resulted in a file download (either because the `resultType` is `fileDownload` or is a `resultPage` running for either PDF or CSV) the resulting contente type will be of the file itself. Otherwise will result in an `application/json` with the result object.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: accessClient
configuration = swagger_client.Configuration()
configuration.api_key['Access-Client-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Access-Client-Token'] = 'Bearer'
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number
operation = 'operation_example' # str | Either the id or internal name of the custom operation
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
params = 'params_example' # str | The custom operation parameters, encoded as `RunOperation`.   (optional)
file = '/path/to/file.txt' # file | The file being uploaded (optional)

try:
    # Runs a custom operation over a transfer while uploading a file 
    api_response = api_instance.run_transfer_operation_with_upload(key, operation, fields=fields, params=params, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->run_transfer_operation_with_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number | 
 **operation** | **str**| Either the id or internal name of the custom operation | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **params** | **str**| The custom operation parameters, encoded as &#x60;RunOperation&#x60;.   | [optional] 
 **file** | **file**| The file being uploaded | [optional] 

### Return type

[**RunOperationResult**](RunOperationResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

