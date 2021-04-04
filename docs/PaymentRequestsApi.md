# swagger_client.PaymentRequestsApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_payment_request**](PaymentRequestsApi.md#accept_payment_request) | **POST** /payment-requests/{key}/accept | Accepts a payment request.
[**cancel_payment_request**](PaymentRequestsApi.md#cancel_payment_request) | **POST** /payment-requests/{key}/cancel | Cancels a payment request.
[**change_payment_request_expiration_date**](PaymentRequestsApi.md#change_payment_request_expiration_date) | **POST** /payment-requests/{key}/change-expiration | Changes the payment request expiration.
[**data_for_send_payment_request**](PaymentRequestsApi.md#data_for_send_payment_request) | **GET** /{owner}/payment-requests/data-for-send | Returns configuration data for sending a payment request
[**preview_payment_request**](PaymentRequestsApi.md#preview_payment_request) | **GET** /payment-requests/{key}/preview | Previews the payment performed when accepting the given payment request. 
[**reject_payment_request**](PaymentRequestsApi.md#reject_payment_request) | **POST** /payment-requests/{key}/reject | Rejects a payment request.
[**reschedule_payment_request**](PaymentRequestsApi.md#reschedule_payment_request) | **POST** /payment-requests/{key}/reschedule | Reschedules a payment request.
[**send_payment_request**](PaymentRequestsApi.md#send_payment_request) | **POST** /{owner}/payment-requests | Sends a payment request from the given owner


# **accept_payment_request**
> Transaction accept_payment_request(key, params, fields=fields, confirmation_password=confirmation_password)

Accepts a payment request.

Accepts a payment request in status `open`. After accepting the payment request its resultant status could be  `processed` (and the corresponding  sheduled or direct payment was generated) or  `scheduled`.    This can be done only by managers or the payer (i.e the request's recipient)  with permission to accept. 

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number.
params = swagger_client.AcceptOrReschedulePaymentRequest() # AcceptOrReschedulePaymentRequest | The parameters to accept a payment request
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Accepts a payment request.
    api_response = api_instance.accept_payment_request(key, params, fields=fields, confirmation_password=confirmation_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->accept_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number. | 
 **params** | [**AcceptOrReschedulePaymentRequest**](AcceptOrReschedulePaymentRequest.md)| The parameters to accept a payment request | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_payment_request**
> cancel_payment_request(key, confirmation_password=confirmation_password, comments=comments)

Cancels a payment request.

Cancels a payment request in status `open`. This can be done only by managers or the payee with permission to cancel. 

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)
comments = 'comments_example' # str | A comment for the cancel action the payee/manager can set. (optional)

try:
    # Cancels a payment request.
    api_instance.cancel_payment_request(key, confirmation_password=confirmation_password, comments=comments)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->cancel_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 
 **comments** | **str**| A comment for the cancel action the payee/manager can set. | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_payment_request_expiration_date**
> change_payment_request_expiration_date(key, params, fields=fields, confirmation_password=confirmation_password)

Changes the payment request expiration.

Change the expiration date of a payment request in status  `open` or `expired`. This can be done only by managers or the payee (i.e the request's sender)  with permission to change the expiration. 

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number.
params = swagger_client.ChangePaymentRequestExpirationDate() # ChangePaymentRequestExpirationDate | The parameters to change the payment request's expiration date
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Changes the payment request expiration.
    api_instance.change_payment_request_expiration_date(key, params, fields=fields, confirmation_password=confirmation_password)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->change_payment_request_expiration_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number. | 
 **params** | [**ChangePaymentRequestExpirationDate**](ChangePaymentRequestExpirationDate.md)| The parameters to change the payment request&#39;s expiration date | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_for_send_payment_request**
> DataForTransaction data_for_send_payment_request(owner, fields=fields, to=to, type=type)

Returns configuration data for sending a payment request

Returns configuration data for sending a payment request 

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
to = 'to_example' # str | The payment request destination, which is either string `system` for a payment request to system or a user identification. The payment request destination is the one that performs the payment once it is accepted.  (optional)
type = 'type_example' # str | The payment type id or qualified internal name (in the form `fromAccountType.paymentType`). If no payment type is provided, the possible types will be returned, so the payer can choose.  (optional)

try:
    # Returns configuration data for sending a payment request
    api_response = api_instance.data_for_send_payment_request(owner, fields=fields, to=to, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->data_for_send_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **to** | **str**| The payment request destination, which is either string &#x60;system&#x60; for a payment request to system or a user identification. The payment request destination is the one that performs the payment once it is accepted.  | [optional] 
 **type** | **str**| The payment type id or qualified internal name (in the form &#x60;fromAccountType.paymentType&#x60;). If no payment type is provided, the possible types will be returned, so the payer can choose.  | [optional] 

### Return type

[**DataForTransaction**](DataForTransaction.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_payment_request**
> PaymentPreview preview_payment_request(key, fields=fields)

Previews the payment performed when accepting the given payment request. 

Previews the payment ony if the payment request status is  `open` or  `scheduled`. 

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number.
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Previews the payment performed when accepting the given payment request. 
    api_response = api_instance.preview_payment_request(key, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->preview_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number. | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**PaymentPreview**](PaymentPreview.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_payment_request**
> reject_payment_request(key, confirmation_password=confirmation_password, comments=comments)

Rejects a payment request.

Rejects a payment request in status `open`. This can be done only by managers or the payer (i.e the request's recipient) with permission to accept. 

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)
comments = 'comments_example' # str | A comment for the reject action the payer can set. (optional)

try:
    # Rejects a payment request.
    api_instance.reject_payment_request(key, confirmation_password=confirmation_password, comments=comments)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->reject_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 
 **comments** | **str**| A comment for the reject action the payer can set. | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reschedule_payment_request**
> Transaction reschedule_payment_request(key, params, fields=fields, confirmation_password=confirmation_password)

Reschedules a payment request.

Reschedules an already accepted and scheduled payment request (i.e with  status `scheduled`). If the new processing date is null then the payment request will be  processed immediately generating the corresponding payment. Otherwise it will be scheduled to be processed at the given date.  This can be done only by managers or the payer (i.e the request's recipient)  with permission to accept. 

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number.
params = swagger_client.AcceptOrReschedulePaymentRequest() # AcceptOrReschedulePaymentRequest | The parameters to reschedule a payment request.
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Reschedules a payment request.
    api_response = api_instance.reschedule_payment_request(key, params, fields=fields, confirmation_password=confirmation_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->reschedule_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number. | 
 **params** | [**AcceptOrReschedulePaymentRequest**](AcceptOrReschedulePaymentRequest.md)| The parameters to reschedule a payment request. | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_payment_request**
> Transaction send_payment_request(owner, payment_request, fields=fields)

Sends a payment request from the given owner

Sends a payment request from the owner indicated on the path (which will receive the payment once the request is accepted) to the owner specified on the body (which will perform the payment once the request is accepted). The destination user should be informed in the `subject` parameter. If the `subject` is `system`, the payment request is sent to a system account, and has to be accepted by an administrator. The payment request id is returned on the response, and a link to the transaction details is returned on the `Location` header. 

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
api_instance = swagger_client.PaymentRequestsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
payment_request = swagger_client.SendPaymentRequest() # SendPaymentRequest | The send payment request parameters
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Sends a payment request from the given owner
    api_response = api_instance.send_payment_request(owner, payment_request, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentRequestsApi->send_payment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **payment_request** | [**SendPaymentRequest**](SendPaymentRequest.md)| The send payment request parameters | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

