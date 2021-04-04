# swagger_client.POSApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_receive_payment_installments**](POSApi.md#calculate_receive_payment_installments) | **GET** /pos/installments | Calculates the default installments for a scheduled payment
[**data_for_receive_payment**](POSApi.md#data_for_receive_payment) | **GET** /pos/data-for-pos | Returns configuration data for receiving a payment (POS)
[**preview_receive_payment**](POSApi.md#preview_receive_payment) | **POST** /pos/preview | Previews a POS payment before receiving it
[**receive_payment**](POSApi.md#receive_payment) | **POST** /pos | Receives a payment (POS)
[**receive_payment_otp**](POSApi.md#receive_payment_otp) | **POST** /pos/otp | Generates a new One-Time-Password (OTP) for a pos payment


# **calculate_receive_payment_installments**
> list[PerformScheduledPaymentInstallment] calculate_receive_payment_installments(_from, count, amount, fields=fields, currency=currency, type=type, first_date=first_date)

Calculates the default installments for a scheduled payment

Used to calculate installments for a scheduled payment. Will return an installment every month. When later receiving the payment, these can be (optionally) customized (such as changing some due dates or amounts) and used on the payment installments.    

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
api_instance = swagger_client.POSApi(swagger_client.ApiClient(configuration))
_from = '_from_example' # str | The payment origin
count = 56 # int | The number of installments
amount = swagger_client.BigDecimal() # BigDecimal | The total scheduled payment amount
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
currency = 'currency_example' # str | The payment currency. Used when no `type` is not provided, to narrow the possible payment types by currency.  (optional)
type = 'type_example' # str | The payment type id or qualified internal name (in the form  `fromAccountType.paymentType`). If not provided, will use the first possible type (possibly narrowed by the `currency` parameter). However, if more than one type is available, a validation error will be raised.  (optional)
first_date = '2013-10-20T19:20:30+01:00' # datetime | The due date of the first installment. If none is provided, it is assumed that the first installment is paid immediately, and others will be with regular 1 month interval  (optional)

try:
    # Calculates the default installments for a scheduled payment
    api_response = api_instance.calculate_receive_payment_installments(_from, count, amount, fields=fields, currency=currency, type=type, first_date=first_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling POSApi->calculate_receive_payment_installments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The payment origin | 
 **count** | **int**| The number of installments | 
 **amount** | **BigDecimal**| The total scheduled payment amount | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **currency** | **str**| The payment currency. Used when no &#x60;type&#x60; is not provided, to narrow the possible payment types by currency.  | [optional] 
 **type** | **str**| The payment type id or qualified internal name (in the form  &#x60;fromAccountType.paymentType&#x60;). If not provided, will use the first possible type (possibly narrowed by the &#x60;currency&#x60; parameter). However, if more than one type is available, a validation error will be raised.  | [optional] 
 **first_date** | **datetime**| The due date of the first installment. If none is provided, it is assumed that the first installment is paid immediately, and others will be with regular 1 month interval  | [optional] 

### Return type

[**list[PerformScheduledPaymentInstallment]**](PerformScheduledPaymentInstallment.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_for_receive_payment**
> DataForTransaction data_for_receive_payment(fields=fields, _from=_from, type=type)

Returns configuration data for receiving a payment (POS)

Returns configuration data for receiving a payment in POS operation  

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
api_instance = swagger_client.POSApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
_from = '_from_example' # str | Identification of the payer user (optional)
type = 'type_example' # str | The payment type id or qualified internal name (in the form `fromAccountType.paymentType`). If no payment type is provided, the possible types will be returned, so the payer can choose.  (optional)

try:
    # Returns configuration data for receiving a payment (POS)
    api_response = api_instance.data_for_receive_payment(fields=fields, _from=_from, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling POSApi->data_for_receive_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **_from** | **str**| Identification of the payer user | [optional] 
 **type** | **str**| The payment type id or qualified internal name (in the form &#x60;fromAccountType.paymentType&#x60;). If no payment type is provided, the possible types will be returned, so the payer can choose.  | [optional] 

### Return type

[**DataForTransaction**](DataForTransaction.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_receive_payment**
> PaymentPreview preview_receive_payment(payment, fields=fields)

Previews a POS payment before receiving it

Previews a payment or scheduled payment. The actual balance checking is not performed in the preview.  

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
api_instance = swagger_client.POSApi(swagger_client.ApiClient(configuration))
payment = swagger_client.PerformPayment() # PerformPayment | The receive payment parameters
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Previews a POS payment before receiving it
    api_response = api_instance.preview_receive_payment(payment, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling POSApi->preview_receive_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment** | [**PerformPayment**](PerformPayment.md)| The receive payment parameters | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**PaymentPreview**](PaymentPreview.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_payment**
> Transaction receive_payment(payment, fields=fields, confirmation_password=confirmation_password)

Receives a payment (POS)

Receives either a direct or scheduled payment in a POS operation for the authenticated user. The payer user should be informed in the `subject` parameter. The payment id is returned on the response, and a link to the transaction details is returned on the `Location` header. 

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
api_instance = swagger_client.POSApi(swagger_client.ApiClient(configuration))
payment = swagger_client.PerformPayment() # PerformPayment | The receive payment parameters
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Receives a payment (POS)
    api_response = api_instance.receive_payment(payment, fields=fields, confirmation_password=confirmation_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling POSApi->receive_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment** | [**PerformPayment**](PerformPayment.md)| The receive payment parameters | 
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

# **receive_payment_otp**
> receive_payment_otp(medium, payment)

Generates a new One-Time-Password (OTP) for a pos payment

Sends a new OTP for the customer of the POS for a payment. The OTP belongs to the payer, not the authenticated user. The entire payment object must be sent on the request body. This is the same object which is sent both either preview or actually receive the payment.  

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
api_instance = swagger_client.POSApi(swagger_client.ApiClient(configuration))
medium = 'medium_example' # str | The medium the user wants to receive the otp Possible values are: * email: The user will receive an email with the information * sms: The user will receive a sms with the information (only if there is at least one phone enabled for sms) 
payment = swagger_client.PerformPayment() # PerformPayment | The receive payment parameters

try:
    # Generates a new One-Time-Password (OTP) for a pos payment
    api_instance.receive_payment_otp(medium, payment)
except ApiException as e:
    print("Exception when calling POSApi->receive_payment_otp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium** | **str**| The medium the user wants to receive the otp Possible values are: * email: The user will receive an email with the information * sms: The user will receive a sms with the information (only if there is at least one phone enabled for sms)  | 
 **payment** | [**PerformPayment**](PerformPayment.md)| The receive payment parameters | 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

