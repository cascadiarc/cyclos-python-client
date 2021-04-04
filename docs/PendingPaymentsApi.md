# swagger_client.PendingPaymentsApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_pending_payment**](PendingPaymentsApi.md#authorize_pending_payment) | **POST** /pending-payments/{key}/authorize | Authorizes a pending payment.
[**cancel_pending_payment**](PendingPaymentsApi.md#cancel_pending_payment) | **POST** /pending-payments/{key}/cancel | Cancels the authorization process of a pending payment.
[**deny_pending_payment**](PendingPaymentsApi.md#deny_pending_payment) | **POST** /pending-payments/{key}/deny | Denies a pending payment.


# **authorize_pending_payment**
> TransactionAuthorizationLevelData authorize_pending_payment(key, params, fields=fields, confirmation_password=confirmation_password)

Authorizes a pending payment.

Authorizes a payment / scheduled payment / recurring payment whose authorization status is `pending`. 

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
api_instance = swagger_client.PendingPaymentsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number.
params = swagger_client.PendingPaymentActionParams() # PendingPaymentActionParams | Contains the action comments
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Authorizes a pending payment.
    api_response = api_instance.authorize_pending_payment(key, params, fields=fields, confirmation_password=confirmation_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PendingPaymentsApi->authorize_pending_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number. | 
 **params** | [**PendingPaymentActionParams**](PendingPaymentActionParams.md)| Contains the action comments | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

[**TransactionAuthorizationLevelData**](TransactionAuthorizationLevelData.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_pending_payment**
> cancel_pending_payment(key, params, confirmation_password=confirmation_password)

Cancels the authorization process of a pending payment.

Cancels a payment / scheduled payment / recurring payment whose authorization status is `pending`. This action is performed by the payer. 

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
api_instance = swagger_client.PendingPaymentsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number.
params = swagger_client.PendingPaymentActionParams() # PendingPaymentActionParams | Contains the action comments
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Cancels the authorization process of a pending payment.
    api_instance.cancel_pending_payment(key, params, confirmation_password=confirmation_password)
except ApiException as e:
    print("Exception when calling PendingPaymentsApi->cancel_pending_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number. | 
 **params** | [**PendingPaymentActionParams**](PendingPaymentActionParams.md)| Contains the action comments | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deny_pending_payment**
> deny_pending_payment(key, params, confirmation_password=confirmation_password)

Denies a pending payment.

Denies a payment / scheduled payment / recurring payment whose authorization status is `pending`. 

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
api_instance = swagger_client.PendingPaymentsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number.
params = swagger_client.PendingPaymentActionParams() # PendingPaymentActionParams | Contains the action comments
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Denies a pending payment.
    api_instance.deny_pending_payment(key, params, confirmation_password=confirmation_password)
except ApiException as e:
    print("Exception when calling PendingPaymentsApi->deny_pending_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number. | 
 **params** | [**PendingPaymentActionParams**](PendingPaymentActionParams.md)| Contains the action comments | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

