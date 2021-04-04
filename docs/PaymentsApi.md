# swagger_client.PaymentsApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_perform_payment_installments**](PaymentsApi.md#calculate_perform_payment_installments) | **GET** /{owner}/payments/installments | Calculates the default installments for a scheduled payment
[**data_for_perform_payment**](PaymentsApi.md#data_for_perform_payment) | **GET** /{owner}/payments/data-for-perform | Returns configuration data for performing a payment
[**get_payment_qr_code**](PaymentsApi.md#get_payment_qr_code) | **GET** /payments/qr-code | Returns the QR-code image for the given payment&#39;s parameters
[**perform_payment**](PaymentsApi.md#perform_payment) | **POST** /{owner}/payments | Performs a payment from the given owner
[**preview_payment**](PaymentsApi.md#preview_payment) | **POST** /{owner}/payments/preview | Previews a payment before performing it


# **calculate_perform_payment_installments**
> list[PerformScheduledPaymentInstallment] calculate_perform_payment_installments(owner, to, count, amount, fields=fields, currency=currency, type=type, first_date=first_date)

Calculates the default installments for a scheduled payment

Used to calculate installments for a scheduled payment. Will return an installment every month. When later performing the payment, these can be (optionally) customized (such as changing some due dates or amounts) and used on the payment installments.    

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
to = 'to_example' # str | The payment destination
count = 56 # int | The number of installments
amount = swagger_client.BigDecimal() # BigDecimal | The total scheduled payment amount
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
currency = 'currency_example' # str | The payment currency. Used when no `type` is not provided, to narrow the possible payment types by currency.  (optional)
type = 'type_example' # str | The payment type id or qualified internal name (in the form  `fromAccountType.paymentType`). If not provided, will use the first possible type (possibly narrowed by the `currency` parameter). However, if more than one type is available, a validation error will be raised.  (optional)
first_date = '2013-10-20T19:20:30+01:00' # datetime | The due date of the first installment. If none is provided, it is assumed that the first installment is paid immediately, and others will be with regular 1 month interval  (optional)

try:
    # Calculates the default installments for a scheduled payment
    api_response = api_instance.calculate_perform_payment_installments(owner, to, count, amount, fields=fields, currency=currency, type=type, first_date=first_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->calculate_perform_payment_installments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **to** | **str**| The payment destination | 
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

# **data_for_perform_payment**
> DataForTransaction data_for_perform_payment(owner, fields=fields, to=to, type=type)

Returns configuration data for performing a payment

Returns configuration data for performing a payment  

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
to = 'to_example' # str | The payment destination. Either the string `system` for a payment to system or a user identification.  (optional)
type = 'type_example' # str | The payment type id or qualified internal name (in the form `fromAccountType.paymentType`). If no payment type is provided, the possible types will be returned, so the payer can choose.  (optional)

try:
    # Returns configuration data for performing a payment
    api_response = api_instance.data_for_perform_payment(owner, fields=fields, to=to, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->data_for_perform_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **to** | **str**| The payment destination. Either the string &#x60;system&#x60; for a payment to system or a user identification.  | [optional] 
 **type** | **str**| The payment type id or qualified internal name (in the form &#x60;fromAccountType.paymentType&#x60;). If no payment type is provided, the possible types will be returned, so the payer can choose.  | [optional] 

### Return type

[**DataForTransaction**](DataForTransaction.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_qr_code**
> file get_payment_qr_code(to, amount=amount, description=description, type=type, custom_fields=custom_fields, size=size)

Returns the QR-code image for the given payment's parameters

The generated image could be scanned (e.g by the mobile application) to  create a payment ready to be confirmed.   

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
to = 'to_example' # str | The payment receiver
amount = swagger_client.BigDecimal() # BigDecimal | The payment amount (optional)
description = 'description_example' # str | The payment description (optional)
type = 'type_example' # str | The payment type, either the id or qualified internal name (in the form `fromAccountType.paymentType`).  (optional)
custom_fields = ['custom_fields_example'] # list[str] | Custom field values. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, `customFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, profileFields=field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `customFields=rank:bronze|silver,birthDate:2000-01-01|2001-12-31` would match results whose custom field with internal name `rank` is either bronze or silver, and whose `birthDate` is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `customFields=birthDate:|2001-12-31`.        (optional)
size = 'size_example' # str | The possible sizes of images. The actual pixel size depends on the configuration in Cyclos Possible values are: * large: Full image size * medium: Medium thumbnail * small: Small thumbnail  (optional)

try:
    # Returns the QR-code image for the given payment's parameters
    api_response = api_instance.get_payment_qr_code(to, amount=amount, description=description, type=type, custom_fields=custom_fields, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_qr_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **str**| The payment receiver | 
 **amount** | **BigDecimal**| The payment amount | [optional] 
 **description** | **str**| The payment description | [optional] 
 **type** | **str**| The payment type, either the id or qualified internal name (in the form &#x60;fromAccountType.paymentType&#x60;).  | [optional] 
 **custom_fields** | [**list[str]**](str.md)| Custom field values. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, &#x60;customFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, profileFields&#x3D;field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;customFields&#x3D;rank:bronze|silver,birthDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#x60;rank&#x60; is either bronze or silver, and whose &#x60;birthDate&#x60; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;customFields&#x3D;birthDate:|2001-12-31&#x60;.        | [optional] 
 **size** | **str**| The possible sizes of images. The actual pixel size depends on the configuration in Cyclos Possible values are: * large: Full image size * medium: Medium thumbnail * small: Small thumbnail  | [optional] 

### Return type

[**file**](file.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/jpeg, image/gif, image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_payment**
> Transaction perform_payment(owner, payment, fields=fields, confirmation_password=confirmation_password)

Performs a payment from the given owner

Performs either a direct or scheduled payment from the owner indicated on the path to the owner specified on the body. The destination user should be informed in the `subject` parameter. If the `subject` is `system`, it will be a payment to a system account. The payment id is returned on the response, and a link to the transaction details is returned on the `Location` header. 

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
payment = swagger_client.PerformPayment() # PerformPayment | The perform payment parameters
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Performs a payment from the given owner
    api_response = api_instance.perform_payment(owner, payment, fields=fields, confirmation_password=confirmation_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->perform_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **payment** | [**PerformPayment**](PerformPayment.md)| The perform payment parameters | 
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

# **preview_payment**
> PaymentPreview preview_payment(owner, payment, fields=fields)

Previews a payment before performing it

Previews a payment, scheduled or recurring payment. The actual balance checking is not performed in the preview.  

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
payment = swagger_client.PerformPayment() # PerformPayment | The perform payment parameters
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Previews a payment before performing it
    api_response = api_instance.preview_payment(owner, payment, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->preview_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **payment** | [**PerformPayment**](PerformPayment.md)| The perform payment parameters | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**PaymentPreview**](PaymentPreview.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

