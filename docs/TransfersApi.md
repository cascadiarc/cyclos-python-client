# swagger_client.TransfersApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chargeback_transfer**](TransfersApi.md#chargeback_transfer) | **POST** /transfers/{key}/chargeback | Perform the chargeback of a transfer
[**get_transfer_data_for_search**](TransfersApi.md#get_transfer_data_for_search) | **GET** /transfers/data-for-search | Returns data for searching transfers over multiple accounts
[**search_transfers**](TransfersApi.md#search_transfers) | **GET** /transfers | Searches for transfers over multiple accounts
[**view_transfer**](TransfersApi.md#view_transfer) | **GET** /transfers/{key} | Returns details about a transfer


# **chargeback_transfer**
> str chargeback_transfer(key, confirmation_password=confirmation_password)

Perform the chargeback of a transfer

The chargeback generates a new transaction with `kind` = `chargeback`. A new transfer is generated with the same from / to, and negative amount. This will effectively return the amount to the original account. Only top-level transfers can be charged back. For example, a transfer used to charge a fee cannot be charged back. Also, the hability to chargeback a transfer depends on permissions and configuration like the maximum allowed time for the chargeback.  

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Perform the chargeback of a transfer
    api_response = api_instance.chargeback_transfer(key, confirmation_password=confirmation_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->chargeback_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

**str**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer_data_for_search**
> TransferDataForSearch get_transfer_data_for_search(fields=fields)

Returns data for searching transfers over multiple accounts

Returns configuration data for searching transfers over multiple accounts. This operation can only be performed by administrators or brokers over managed users. 

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data for searching transfers over multiple accounts
    api_response = api_instance.get_transfer_data_for_search(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->get_transfer_data_for_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**TransferDataForSearch**](TransferDataForSearch.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_transfers**
> list[TransferResult] search_transfers(fields=fields, access_clients=access_clients, amount_range=amount_range, broker=broker, by=by, channels=channels, charged_back=charged_back, currency=currency, date_period=date_period, excluded_ids=excluded_ids, from_account_type=from_account_type, from_current_access_client=from_current_access_client, groups=groups, include_generated_by_access_client=include_generated_by_access_client, order_by=order_by, page=page, page_size=page_size, statuses=statuses, to_account_type=to_account_type, transaction_number=transaction_number, transfer_filters=transfer_filters, transfer_kinds=transfer_kinds, transfer_types=transfer_types, user=user)

Searches for transfers over multiple accounts

Searches for transfers over multiple accounts. This operation can only be performed by administrators or brokers over managed users. 

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
access_clients = ['access_clients_example'] # list[str] | References to access clients (id or token) used to perform / receive the  transfer.  (optional)
amount_range = [swagger_client.BigDecimal()] # list[BigDecimal] | The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
broker = 'broker_example' # str | Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.  (optional)
by = 'by_example' # str | Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.  (optional)
channels = ['channels_example'] # list[str] | Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.  (optional)
charged_back = true # bool | When set to either `true` will only return transfers that were charged-back. When set to `false`, will only return transfers that were not charged-back. When left blank will not filter by this creterion.  (optional)
currency = 'currency_example' # str | Either id or internal name of the currency  (optional)
date_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of transfers ids to be excluded from the result.  (optional)
from_account_type = 'from_account_type_example' # str | Either id or internal name of the origin account type  (optional)
from_current_access_client = true # bool | Flag indicating whether to include only transfers by the current access client.  (optional)
groups = ['groups_example'] # list[str] | Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.  (optional)
include_generated_by_access_client = true # bool | Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a `ticket` or `paymentRequest` was processed then a new transfer will be generated.  (optional)
order_by = 'order_by_example' # str | Contains the possible 'order by' values when searching for transfers  Possible values are: * amountAsc: The result is ordered by amount descendant * amountDesc: The result is ordered by amount descendant * dateAsc: The result is ordered by date ascendant * dateDesc: The result is ordered by date descendant  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
statuses = ['statuses_example'] # list[str] | Transfer statuses used as search criteria. Each array element should be either the identifier or the status qualified internal name, composed by flow internal name, a dot, and the status internal name. For example, `loan.open` would be a valid internal name.  (optional)
to_account_type = 'to_account_type_example' # str | Either id or internal name of the destination account type  (optional)
transaction_number = 'transaction_number_example' # str | The transaction number of the matching transfer  (optional)
transfer_filters = ['transfer_filters_example'] # list[str] | Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format `accountType.transferFilter`.  (optional)
transfer_kinds = ['transfer_kinds_example'] # list[str] | Indicates the reason the transfer was created Possible values for each array element are: * accountFee: A transfer generated by an account fee charge * chargeback: A transfer which is a chargeback of another transfer * import: An imported transfer * initialCredit: A transfer which is the initial credit for a newly created account * payment: A transfer generated by a direct payment or accepting a webshop order * recurringPayment: A transfer generated when processing a recurring payment * scheduledPaymentInstallment: A transfer generated when processing a scheduled payment installment * transferFee: A transfer generated by a transfer fee charge  (optional)
transfer_types = ['transfer_types_example'] # list[str] | Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format `accountType.transferType`.  (optional)
user = 'user_example' # str | Reference a user that should have either received / performed the transfer.  (optional)

try:
    # Searches for transfers over multiple accounts
    api_response = api_instance.search_transfers(fields=fields, access_clients=access_clients, amount_range=amount_range, broker=broker, by=by, channels=channels, charged_back=charged_back, currency=currency, date_period=date_period, excluded_ids=excluded_ids, from_account_type=from_account_type, from_current_access_client=from_current_access_client, groups=groups, include_generated_by_access_client=include_generated_by_access_client, order_by=order_by, page=page, page_size=page_size, statuses=statuses, to_account_type=to_account_type, transaction_number=transaction_number, transfer_filters=transfer_filters, transfer_kinds=transfer_kinds, transfer_types=transfer_types, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->search_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **access_clients** | [**list[str]**](str.md)| References to access clients (id or token) used to perform / receive the  transfer.  | [optional] 
 **amount_range** | [**list[BigDecimal]**](BigDecimal.md)| The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **broker** | **str**| Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.  | [optional] 
 **by** | **str**| Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.  | [optional] 
 **channels** | [**list[str]**](str.md)| Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.  | [optional] 
 **charged_back** | **bool**| When set to either &#x60;true&#x60; will only return transfers that were charged-back. When set to &#x60;false&#x60;, will only return transfers that were not charged-back. When left blank will not filter by this creterion.  | [optional] 
 **currency** | **str**| Either id or internal name of the currency  | [optional] 
 **date_period** | [**list[datetime]**](datetime.md)| The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| List of transfers ids to be excluded from the result.  | [optional] 
 **from_account_type** | **str**| Either id or internal name of the origin account type  | [optional] 
 **from_current_access_client** | **bool**| Flag indicating whether to include only transfers by the current access client.  | [optional] 
 **groups** | [**list[str]**](str.md)| Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.  | [optional] 
 **include_generated_by_access_client** | **bool**| Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a &#x60;ticket&#x60; or &#x60;paymentRequest&#x60; was processed then a new transfer will be generated.  | [optional] 
 **order_by** | **str**| Contains the possible &#39;order by&#39; values when searching for transfers  Possible values are: * amountAsc: The result is ordered by amount descendant * amountDesc: The result is ordered by amount descendant * dateAsc: The result is ordered by date ascendant * dateDesc: The result is ordered by date descendant  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **statuses** | [**list[str]**](str.md)| Transfer statuses used as search criteria. Each array element should be either the identifier or the status qualified internal name, composed by flow internal name, a dot, and the status internal name. For example, &#x60;loan.open&#x60; would be a valid internal name.  | [optional] 
 **to_account_type** | **str**| Either id or internal name of the destination account type  | [optional] 
 **transaction_number** | **str**| The transaction number of the matching transfer  | [optional] 
 **transfer_filters** | [**list[str]**](str.md)| Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format &#x60;accountType.transferFilter&#x60;.  | [optional] 
 **transfer_kinds** | [**list[str]**](str.md)| Indicates the reason the transfer was created Possible values for each array element are: * accountFee: A transfer generated by an account fee charge * chargeback: A transfer which is a chargeback of another transfer * import: An imported transfer * initialCredit: A transfer which is the initial credit for a newly created account * payment: A transfer generated by a direct payment or accepting a webshop order * recurringPayment: A transfer generated when processing a recurring payment * scheduledPaymentInstallment: A transfer generated when processing a scheduled payment installment * transferFee: A transfer generated by a transfer fee charge  | [optional] 
 **transfer_types** | [**list[str]**](str.md)| Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format &#x60;accountType.transferType&#x60;.  | [optional] 
 **user** | **str**| Reference a user that should have either received / performed the transfer.  | [optional] 

### Return type

[**list[TransferResult]**](TransferResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_transfer**
> TransferView view_transfer(key, fields=fields)

Returns details about a transfer

Returns details about a transfer.

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Either the id or transaction number
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns details about a transfer
    api_response = api_instance.view_transfer(key, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->view_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Either the id or transaction number | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**TransferView**](TransferView.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

