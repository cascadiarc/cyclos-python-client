# swagger_client.TransactionsApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transactions_data_for_search**](TransactionsApi.md#get_transactions_data_for_search) | **GET** /{owner}/transactions/data-for-search | Returns data for searching transactions of an account owner
[**search_transactions**](TransactionsApi.md#search_transactions) | **GET** /{owner}/transactions | Searches transactions of an account owner
[**view_transaction**](TransactionsApi.md#view_transaction) | **GET** /transactions/{key} | Returns details about a transaction


# **get_transactions_data_for_search**
> TransactionDataForSearch get_transactions_data_for_search(owner, fields=fields)

Returns data for searching transactions of an account owner

Returns data which can be used to filter a transaction search

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data for searching transactions of an account owner
    api_response = api_instance.get_transactions_data_for_search(owner, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_data_for_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**TransactionDataForSearch**](TransactionDataForSearch.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_transactions**
> list[TransactionResult] search_transactions(owner, fields=fields, access_clients=access_clients, account_types=account_types, amount_range=amount_range, authorization_statuses=authorization_statuses, broker=broker, by=by, channels=channels, date_period=date_period, direction=direction, excluded_ids=excluded_ids, external_payment_statuses=external_payment_statuses, from_current_access_client=from_current_access_client, groups=groups, include_generated_by_access_client=include_generated_by_access_client, kinds=kinds, page=page, page_size=page_size, payment_request_statuses=payment_request_statuses, recurring_payment_statuses=recurring_payment_statuses, scheduled_payment_statuses=scheduled_payment_statuses, ticket_statuses=ticket_statuses, transaction_number=transaction_number, transfer_filters=transfer_filters, transfer_types=transfer_types, user=user)

Searches transactions of an account owner

Returns the transactions of a given account owner that match the specified criteria. Each result will will be relative to this owner. The amount may be positive or negative, depending on whether this owner has performed or received the transaction. 

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
access_clients = ['access_clients_example'] # list[str] | References to access clients (id or token) used to perform / receive the  transfer.  (optional)
account_types = ['account_types_example'] # list[str] | The account types  (optional)
amount_range = [swagger_client.BigDecimal()] # list[BigDecimal] | The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
authorization_statuses = ['authorization_statuses_example'] # list[str] | The status regarding authorization a transaction is in. If configured, transactions can require one or more levels of authorization in order to be processed. If a transaction has the this status null, it means it never went through the authorization process.  Possible values for each array element are: * authorized: The transaction was fully authorized and is processed * canceled: The authorization submission was canceled by the submitter * denied: The authorization was denied * pending: The transaction is pending authorization  (optional)
broker = 'broker_example' # str | Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.  (optional)
by = 'by_example' # str | Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.  (optional)
channels = ['channels_example'] # list[str] | Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.  (optional)
date_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
direction = 'direction_example' # str | Indicates whether from an account POV a transfer is a credit or debit Possible values are: * credit: The transfer impacts the balance positively * debit: The transfer impacts the balance negatively  (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of transfers ids to be excluded from the result.  (optional)
external_payment_statuses = ['external_payment_statuses_example'] # list[str] | The status of an external payment Possible values for each array element are: * canceled: The external payment was canceled * expired: The external payment has expired without the destination user activation * failed: The external payment has failed processing * pending: The external payment is pending, awaiting the destination user to be activated in Cyclos * processed: The external payment was processed, and the destination payment was created  (optional)
from_current_access_client = true # bool | Flag indicating whether to include only transfers by the current access client.  (optional)
groups = ['groups_example'] # list[str] | Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.  (optional)
include_generated_by_access_client = true # bool | Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a `ticket` or `paymentRequest` was processed then a new transfer will be generated.  (optional)
kinds = ['kinds_example'] # list[str] | The kind of a transaction  Possible values for each array element are: * chargeback: Chargeback of a given transfer * externalPayment: A payment to an external user * import: An imported transaction * order: Transaction generated by confirming an order * payment: A direct payment * paymentRequest: A request for another user to accept a payment  * recurringPayment: A payment which is processed again periodically * scheduledPayment: A scheduled payment which is either a payment scheduled for a future date or has multiple installments * ticket: A payment whose the payer is unknown  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
payment_request_statuses = ['payment_request_statuses_example'] # list[str] | The status of a payment request Possible values for each array element are: * canceled: The payment request was canceled * denied: The payment request was denied by the receiver * expired: The payment request has expired - the received did not respond until the expiration date * open: The payment request is open and can be accepted * processed: The payment request was processed, and either a direct or scheduled payment was created from it * scheduled: The payment request has been accepted, and scheduled for processing on a future date  (optional)
recurring_payment_statuses = ['recurring_payment_statuses_example'] # list[str] | The status of a recurring payment Possible values for each array element are: * canceled: The recurring payment was manually canceled * closed: The recurring payment is closed, as the last scheduled occurrence was processed * open: The recurring payment is open, as there are more future occurrences  (optional)
scheduled_payment_statuses = ['scheduled_payment_statuses_example'] # list[str] | The status of a scheduled payment Possible values for each array element are: * blocked: The scheduled payment is blocked - won't have any installment processed until being unblocked again * canceled: The scheduled payment, as well as all open installments were canceled * closed: The scheduled payment is closed * open: The scheduled payment has open installments  (optional)
ticket_statuses = ['ticket_statuses_example'] # list[str] | The status of a ticket Possible values for each array element are: * approved: The ticket was approved by the payer and is waiting to be processed by the receiver to generate the payment * canceled: The ticket was canceled by the receiver before being approved * expired: The ticket has expired without being approved by a payer or canceled by the receiver until the expiration date * open: The ticket was created, but not approved yet * processed: The ticket was approved and processed and the payment was generated  (optional)
transaction_number = 'transaction_number_example' # str | The transaction number of the matching transfer  (optional)
transfer_filters = ['transfer_filters_example'] # list[str] | Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format `accountType.transferFilter`.  (optional)
transfer_types = ['transfer_types_example'] # list[str] | Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format `accountType.transferType`.  (optional)
user = 'user_example' # str | Reference a user that should have either received / performed the transfer.  (optional)

try:
    # Searches transactions of an account owner
    api_response = api_instance.search_transactions(owner, fields=fields, access_clients=access_clients, account_types=account_types, amount_range=amount_range, authorization_statuses=authorization_statuses, broker=broker, by=by, channels=channels, date_period=date_period, direction=direction, excluded_ids=excluded_ids, external_payment_statuses=external_payment_statuses, from_current_access_client=from_current_access_client, groups=groups, include_generated_by_access_client=include_generated_by_access_client, kinds=kinds, page=page, page_size=page_size, payment_request_statuses=payment_request_statuses, recurring_payment_statuses=recurring_payment_statuses, scheduled_payment_statuses=scheduled_payment_statuses, ticket_statuses=ticket_statuses, transaction_number=transaction_number, transfer_filters=transfer_filters, transfer_types=transfer_types, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->search_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **access_clients** | [**list[str]**](str.md)| References to access clients (id or token) used to perform / receive the  transfer.  | [optional] 
 **account_types** | [**list[str]**](str.md)| The account types  | [optional] 
 **amount_range** | [**list[BigDecimal]**](BigDecimal.md)| The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **authorization_statuses** | [**list[str]**](str.md)| The status regarding authorization a transaction is in. If configured, transactions can require one or more levels of authorization in order to be processed. If a transaction has the this status null, it means it never went through the authorization process.  Possible values for each array element are: * authorized: The transaction was fully authorized and is processed * canceled: The authorization submission was canceled by the submitter * denied: The authorization was denied * pending: The transaction is pending authorization  | [optional] 
 **broker** | **str**| Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.  | [optional] 
 **by** | **str**| Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.  | [optional] 
 **channels** | [**list[str]**](str.md)| Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.  | [optional] 
 **date_period** | [**list[datetime]**](datetime.md)| The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **direction** | **str**| Indicates whether from an account POV a transfer is a credit or debit Possible values are: * credit: The transfer impacts the balance positively * debit: The transfer impacts the balance negatively  | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| List of transfers ids to be excluded from the result.  | [optional] 
 **external_payment_statuses** | [**list[str]**](str.md)| The status of an external payment Possible values for each array element are: * canceled: The external payment was canceled * expired: The external payment has expired without the destination user activation * failed: The external payment has failed processing * pending: The external payment is pending, awaiting the destination user to be activated in Cyclos * processed: The external payment was processed, and the destination payment was created  | [optional] 
 **from_current_access_client** | **bool**| Flag indicating whether to include only transfers by the current access client.  | [optional] 
 **groups** | [**list[str]**](str.md)| Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.  | [optional] 
 **include_generated_by_access_client** | **bool**| Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a &#x60;ticket&#x60; or &#x60;paymentRequest&#x60; was processed then a new transfer will be generated.  | [optional] 
 **kinds** | [**list[str]**](str.md)| The kind of a transaction  Possible values for each array element are: * chargeback: Chargeback of a given transfer * externalPayment: A payment to an external user * import: An imported transaction * order: Transaction generated by confirming an order * payment: A direct payment * paymentRequest: A request for another user to accept a payment  * recurringPayment: A payment which is processed again periodically * scheduledPayment: A scheduled payment which is either a payment scheduled for a future date or has multiple installments * ticket: A payment whose the payer is unknown  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **payment_request_statuses** | [**list[str]**](str.md)| The status of a payment request Possible values for each array element are: * canceled: The payment request was canceled * denied: The payment request was denied by the receiver * expired: The payment request has expired - the received did not respond until the expiration date * open: The payment request is open and can be accepted * processed: The payment request was processed, and either a direct or scheduled payment was created from it * scheduled: The payment request has been accepted, and scheduled for processing on a future date  | [optional] 
 **recurring_payment_statuses** | [**list[str]**](str.md)| The status of a recurring payment Possible values for each array element are: * canceled: The recurring payment was manually canceled * closed: The recurring payment is closed, as the last scheduled occurrence was processed * open: The recurring payment is open, as there are more future occurrences  | [optional] 
 **scheduled_payment_statuses** | [**list[str]**](str.md)| The status of a scheduled payment Possible values for each array element are: * blocked: The scheduled payment is blocked - won&#39;t have any installment processed until being unblocked again * canceled: The scheduled payment, as well as all open installments were canceled * closed: The scheduled payment is closed * open: The scheduled payment has open installments  | [optional] 
 **ticket_statuses** | [**list[str]**](str.md)| The status of a ticket Possible values for each array element are: * approved: The ticket was approved by the payer and is waiting to be processed by the receiver to generate the payment * canceled: The ticket was canceled by the receiver before being approved * expired: The ticket has expired without being approved by a payer or canceled by the receiver until the expiration date * open: The ticket was created, but not approved yet * processed: The ticket was approved and processed and the payment was generated  | [optional] 
 **transaction_number** | **str**| The transaction number of the matching transfer  | [optional] 
 **transfer_filters** | [**list[str]**](str.md)| Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format &#x60;accountType.transferFilter&#x60;.  | [optional] 
 **transfer_types** | [**list[str]**](str.md)| Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format &#x60;accountType.transferType&#x60;.  | [optional] 
 **user** | **str**| Reference a user that should have either received / performed the transfer.  | [optional] 

### Return type

[**list[TransactionResult]**](TransactionResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_transaction**
> TransactionView view_transaction(key, fields=fields)

Returns details about a transaction

Returns details about a transaction.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns details about a transaction
    api_response = api_instance.view_transaction(key, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->view_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**TransactionView**](TransactionView.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

