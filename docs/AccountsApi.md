# swagger_client.AccountsApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_balance_history**](AccountsApi.md#get_account_balance_history) | **GET** /{owner}/accounts/{accountType}/balances-history | Returns the account balances over time
[**get_account_history_data_by_owner_and_type**](AccountsApi.md#get_account_history_data_by_owner_and_type) | **GET** /{owner}/accounts/{accountType}/data-for-history | Returns data for searching an account history by owner and type
[**get_account_status_by_owner_and_type**](AccountsApi.md#get_account_status_by_owner_and_type) | **GET** /{owner}/accounts/{accountType} | Returns the status of an account by owner and type
[**get_user_balances_data**](AccountsApi.md#get_user_balances_data) | **GET** /accounts/data-for-user-balances | Returns data for searching users together with their balances
[**get_user_balances_summary**](AccountsApi.md#get_user_balances_summary) | **GET** /accounts/{accountType}/user-balances/summary | Returns summarized information for the user balances search
[**list_accounts_by_owner**](AccountsApi.md#list_accounts_by_owner) | **GET** /{owner}/accounts | Lists accounts of the given owner with their statuses
[**search_account_history**](AccountsApi.md#search_account_history) | **GET** /{owner}/accounts/{accountType}/history | Search an account history
[**search_users_with_balances**](AccountsApi.md#search_users_with_balances) | **GET** /accounts/{accountType}/user-balances | Searches for users together with balance information


# **get_account_balance_history**
> AccountBalanceHistoryResult get_account_balance_history(owner, account_type, fields=fields, date_period=date_period, interval_unit=interval_unit, interval_count=interval_count)

Returns the account balances over time

Receives a period and an interval, returning the balance over each corresponding date. The maximum number of data points is 60, so it is possible to get the balances per day over 2 months. For larger periods, use weeks or months. When no period is given, assumes the beginning of current year or the account creation date, whichever is newer. When no interval is given, one is assumed. Also returns status of the given account 

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
account_type = 'account_type_example' # str | The account type
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
date_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
interval_unit = 'interval_unit_example' # str | The time unit for the data point interval Possible values are: * days: Day(s) * hours: Hour(s) * millis: Millisecond(s) * minutes: Minute(s) * months: Month(s) * seconds: Second(s) * weeks: Week(s) * years: Year(s)  (optional)
interval_count = 56 # int | A data point every X units. For example, it is possible to request the balance every 3 days. Defaults to 1.  (optional)

try:
    # Returns the account balances over time
    api_response = api_instance.get_account_balance_history(owner, account_type, fields=fields, date_period=date_period, interval_unit=interval_unit, interval_count=interval_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_balance_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **account_type** | **str**| The account type | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **date_period** | [**list[datetime]**](datetime.md)| The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **interval_unit** | **str**| The time unit for the data point interval Possible values are: * days: Day(s) * hours: Hour(s) * millis: Millisecond(s) * minutes: Minute(s) * months: Month(s) * seconds: Second(s) * weeks: Week(s) * years: Year(s)  | [optional] 
 **interval_count** | **int**| A data point every X units. For example, it is possible to request the balance every 3 days. Defaults to 1.  | [optional] 

### Return type

[**AccountBalanceHistoryResult**](AccountBalanceHistoryResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_history_data_by_owner_and_type**
> DataForAccountHistory get_account_history_data_by_owner_and_type(owner, account_type, fields=fields)

Returns data for searching an account history by owner and type

Returns configuration data for searching entries in a specific account history, as well as status information for that account information. 

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
account_type = 'account_type_example' # str | The internal name or id of the account type
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data for searching an account history by owner and type
    api_response = api_instance.get_account_history_data_by_owner_and_type(owner, account_type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_history_data_by_owner_and_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **account_type** | **str**| The internal name or id of the account type | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**DataForAccountHistory**](DataForAccountHistory.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_status_by_owner_and_type**
> AccountWithHistoryStatus get_account_status_by_owner_and_type(owner, account_type, fields=fields, access_clients=access_clients, amount_range=amount_range, broker=broker, by=by, channels=channels, charged_back=charged_back, custom_fields=custom_fields, date_period=date_period, direction=direction, excluded_ids=excluded_ids, from_current_access_client=from_current_access_client, groups=groups, include_generated_by_access_client=include_generated_by_access_client, page=page, page_size=page_size, statuses=statuses, transaction_number=transaction_number, transfer_filters=transfer_filters, transfer_kinds=transfer_kinds, transfer_types=transfer_types, user=user)

Returns the status of an account by owner and type

Returns the account status for a specific account. The account type may be either the identifier or internal name. The status will contain both instant status information, that is, the same fields as `AccountStatus`, plus status that depend on the input parameters, such as those defined in `AccountWithHistoryStatus`. The actual data inside the result depend on the configuration, in the `Account status indicators` option, which is used to limit the amount of data returned. 

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
account_type = 'account_type_example' # str | The account type
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
access_clients = ['access_clients_example'] # list[str] | References to access clients (id or token) used to perform / receive the  transfer.  (optional)
amount_range = [swagger_client.BigDecimal()] # list[BigDecimal] | The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
broker = 'broker_example' # str | Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.  (optional)
by = 'by_example' # str | Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.  (optional)
channels = ['channels_example'] # list[str] | Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.  (optional)
charged_back = true # bool | When set to either `true` will only return transfers that were charged-back. When set to `false`, will only return transfers that were not charged-back. When left blank will not filter by this creterion.  (optional)
custom_fields = ['custom_fields_example'] # list[str] | Transaction custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, `customFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields=field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `customFields=rank:bronze|silver,documentDate:2000-01-01|2001-12-31` would match results whose custom field with internal name `rank` is either `bronze` or `silver`, and whose `documentDate` is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `customFields=documentDate:|2001-12-31`. A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `customFields=dynamic:a|b|c`. However, it is also possible to perform a partial-match search using the dynamic value label. In this case a single value, prefixed or enclosed by single quotes should be used. For example: `customFields=dynamic:'business` or `customFields=dynamic:'business'`.         (optional)
date_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
direction = 'direction_example' # str | Indicates whether from an account POV a transfer is a credit or debit Possible values are: * credit: The transfer impacts the balance positively * debit: The transfer impacts the balance negatively  (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of transfers ids to be excluded from the result.  (optional)
from_current_access_client = true # bool | Flag indicating whether to include only transfers by the current access client.  (optional)
groups = ['groups_example'] # list[str] | Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.  (optional)
include_generated_by_access_client = true # bool | Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a `ticket` or `paymentRequest` was processed then a new transfer will be generated.  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
statuses = ['statuses_example'] # list[str] | Transfer statuses used as search criteria. Each array element should be either the identifier or the status qualified internal name, composed by flow internal name, a dot, and the status internal name. For example, `loan.open` would be a valid internal name.  (optional)
transaction_number = 'transaction_number_example' # str | The transaction number of the matching transfer  (optional)
transfer_filters = ['transfer_filters_example'] # list[str] | Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format `accountType.transferFilter`.  (optional)
transfer_kinds = ['transfer_kinds_example'] # list[str] | Indicates the reason the transfer was created Possible values for each array element are: * accountFee: A transfer generated by an account fee charge * chargeback: A transfer which is a chargeback of another transfer * import: An imported transfer * initialCredit: A transfer which is the initial credit for a newly created account * payment: A transfer generated by a direct payment or accepting a webshop order * recurringPayment: A transfer generated when processing a recurring payment * scheduledPaymentInstallment: A transfer generated when processing a scheduled payment installment * transferFee: A transfer generated by a transfer fee charge  (optional)
transfer_types = ['transfer_types_example'] # list[str] | Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format `accountType.transferType`.  (optional)
user = 'user_example' # str | Reference a user that should have either received / performed the transfer.  (optional)

try:
    # Returns the status of an account by owner and type
    api_response = api_instance.get_account_status_by_owner_and_type(owner, account_type, fields=fields, access_clients=access_clients, amount_range=amount_range, broker=broker, by=by, channels=channels, charged_back=charged_back, custom_fields=custom_fields, date_period=date_period, direction=direction, excluded_ids=excluded_ids, from_current_access_client=from_current_access_client, groups=groups, include_generated_by_access_client=include_generated_by_access_client, page=page, page_size=page_size, statuses=statuses, transaction_number=transaction_number, transfer_filters=transfer_filters, transfer_kinds=transfer_kinds, transfer_types=transfer_types, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_status_by_owner_and_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **account_type** | **str**| The account type | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **access_clients** | [**list[str]**](str.md)| References to access clients (id or token) used to perform / receive the  transfer.  | [optional] 
 **amount_range** | [**list[BigDecimal]**](BigDecimal.md)| The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **broker** | **str**| Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.  | [optional] 
 **by** | **str**| Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.  | [optional] 
 **channels** | [**list[str]**](str.md)| Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.  | [optional] 
 **charged_back** | **bool**| When set to either &#x60;true&#x60; will only return transfers that were charged-back. When set to &#x60;false&#x60;, will only return transfers that were not charged-back. When left blank will not filter by this creterion.  | [optional] 
 **custom_fields** | [**list[str]**](str.md)| Transaction custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, &#x60;customFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields&#x3D;field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;customFields&#x3D;rank:bronze|silver,documentDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#x60;rank&#x60; is either &#x60;bronze&#x60; or &#x60;silver&#x60;, and whose &#x60;documentDate&#x60; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;customFields&#x3D;documentDate:|2001-12-31&#x60;. A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: &#x60;customFields&#x3D;dynamic:a|b|c&#x60;. However, it is also possible to perform a partial-match search using the dynamic value label. In this case a single value, prefixed or enclosed by single quotes should be used. For example: &#x60;customFields&#x3D;dynamic:&#39;business&#x60; or &#x60;customFields&#x3D;dynamic:&#39;business&#39;&#x60;.         | [optional] 
 **date_period** | [**list[datetime]**](datetime.md)| The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **direction** | **str**| Indicates whether from an account POV a transfer is a credit or debit Possible values are: * credit: The transfer impacts the balance positively * debit: The transfer impacts the balance negatively  | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| List of transfers ids to be excluded from the result.  | [optional] 
 **from_current_access_client** | **bool**| Flag indicating whether to include only transfers by the current access client.  | [optional] 
 **groups** | [**list[str]**](str.md)| Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.  | [optional] 
 **include_generated_by_access_client** | **bool**| Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a &#x60;ticket&#x60; or &#x60;paymentRequest&#x60; was processed then a new transfer will be generated.  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **statuses** | [**list[str]**](str.md)| Transfer statuses used as search criteria. Each array element should be either the identifier or the status qualified internal name, composed by flow internal name, a dot, and the status internal name. For example, &#x60;loan.open&#x60; would be a valid internal name.  | [optional] 
 **transaction_number** | **str**| The transaction number of the matching transfer  | [optional] 
 **transfer_filters** | [**list[str]**](str.md)| Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format &#x60;accountType.transferFilter&#x60;.  | [optional] 
 **transfer_kinds** | [**list[str]**](str.md)| Indicates the reason the transfer was created Possible values for each array element are: * accountFee: A transfer generated by an account fee charge * chargeback: A transfer which is a chargeback of another transfer * import: An imported transfer * initialCredit: A transfer which is the initial credit for a newly created account * payment: A transfer generated by a direct payment or accepting a webshop order * recurringPayment: A transfer generated when processing a recurring payment * scheduledPaymentInstallment: A transfer generated when processing a scheduled payment installment * transferFee: A transfer generated by a transfer fee charge  | [optional] 
 **transfer_types** | [**list[str]**](str.md)| Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format &#x60;accountType.transferType&#x60;.  | [optional] 
 **user** | **str**| Reference a user that should have either received / performed the transfer.  | [optional] 

### Return type

[**AccountWithHistoryStatus**](AccountWithHistoryStatus.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_balances_data**
> DataForUserBalancesSearch get_user_balances_data(fields=fields)

Returns data for searching users together with their balances

Returns configuration data for searching users together with their balances. The account types are returned, and the account type needs to be passed in the other `user-balances` operations. 

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data for searching users together with their balances
    api_response = api_instance.get_user_balances_data(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_user_balances_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**DataForUserBalancesSearch**](DataForUserBalancesSearch.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_balances_summary**
> UsersWithBalanceSummary get_user_balances_summary(account_type, fields=fields, activation_period=activation_period, address_result=address_result, balance_range=balance_range, brokers=brokers, creation_period=creation_period, groups=groups, include_group=include_group, include_group_set=include_group_set, keywords=keywords, last_incoming_transfer_period=last_incoming_transfer_period, last_login_period=last_login_period, last_outgoing_transfer_period=last_outgoing_transfer_period, latitude=latitude, longitude=longitude, main_broker_only=main_broker_only, max_distance=max_distance, medium_balance_range=medium_balance_range, negative_since_period=negative_since_period, page=page, page_size=page_size, profile_fields=profile_fields, users_to_exclude=users_to_exclude, users_to_include=users_to_include)

Returns summarized information for the user balances search

Returns summaries for each balance level (if ranges are defined in either account type or filter), as well as the total summary. 

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_type = 'account_type_example' # str | The account type 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
activation_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user activation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
address_result = 'address_result_example' # str | Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (`latitude` and `longitude`) * none: Addresses are not returned. * primary: The primary (default) user address is returned  (optional)
balance_range = [56] # list[int] | The minimum and / or maximum balance for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
brokers = ['brokers_example'] # list[str] | Either id or a principal (login name, e-mail, etc) for brokers  (optional)
creation_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user creation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
groups = ['groups_example'] # list[str] | Either id or internal names of groups / group sets  (optional)
include_group = true # bool | When set to `true` and the logged user has permission to view user groups, will return the `group` property on users.   (optional)
include_group_set = true # bool | When set to `true` and the logged user has permission to view user group sets, will return the `groupSet` property on users.   (optional)
keywords = 'keywords_example' # str | Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  (optional)
last_incoming_transfer_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum date of the last incoming transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
last_login_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user last login date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
last_outgoing_transfer_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum date of the last outgoing transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
latitude = 1.2 # float | The reference latitude for distance searches  (optional)
longitude = 1.2 # float | The reference longitude for distance searches  (optional)
main_broker_only = true # bool | When set to `true`, will match only users that have the brokers as set in the `brokers` parameter as main broker.   (optional)
max_distance = 1.2 # float | Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both `longitude` and `latitude` parameters are passed with the actual reference position.  (optional)
medium_balance_range = [56] # list[int] | An array with 2 elements, describing the lower and upper medium balance bounds. If not specified, the range defined in the account type will be used. If that one is also not defined, there will be no definitions for balance levels. Both bounds need to be set as 2 element in the array, or it won't be considered.  (optional)
negative_since_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum negative-since date for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
profile_fields = ['profile_fields_example'] # list[str] | User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, `profileFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, `profileFields=field1:valueA|valueB`. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `profileFields=rank:bronze|silver,birthDate:2000-01-01|2001-12-31` would match results whose custom field with internal name 'rank' is either bronze or silver, and whose 'birthDate' is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `profileFields=birthDate:|2001-12-31`. The basic profile fields have one of the following identifiers: * `name` or `fullName`: Full name; * `username`, `loginName` or `login`: Login name; * `email`: E-mail; * `phone`: Phone; * `accountNumber`, `account`: Account number; * `image`: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the `addressFieldsInSearch` field in the corresponding result from a data-for-search request.  The specific address fields are: * `address`: Searches on any address field (not a specific field); * `address.address`: Searches on the fields that represent the   street address, which are `addressLine1`,    `addressLine2`,   `street`,   `buildingNumber` and   `complement`. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * `address.zip`: Searches for matching zip (postal) code; * `address.poBox`: Searches for matching postal box; * `address.neighborhood`: Searches by neighborhood; * `address.city`: Searches by city; * `address.region`: Searches by region (or state); * `address.country`: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `profileFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `profileFields=dynamic:'business`.  (optional)
users_to_exclude = ['users_to_exclude_example'] # list[str] | Indicated the users to be excluded from the result  (optional)
users_to_include = ['users_to_include_example'] # list[str] | Indicated the users to be included in the result.  Any other user not present in this list will be excluded from the result.  (optional)

try:
    # Returns summarized information for the user balances search
    api_response = api_instance.get_user_balances_summary(account_type, fields=fields, activation_period=activation_period, address_result=address_result, balance_range=balance_range, brokers=brokers, creation_period=creation_period, groups=groups, include_group=include_group, include_group_set=include_group_set, keywords=keywords, last_incoming_transfer_period=last_incoming_transfer_period, last_login_period=last_login_period, last_outgoing_transfer_period=last_outgoing_transfer_period, latitude=latitude, longitude=longitude, main_broker_only=main_broker_only, max_distance=max_distance, medium_balance_range=medium_balance_range, negative_since_period=negative_since_period, page=page, page_size=page_size, profile_fields=profile_fields, users_to_exclude=users_to_exclude, users_to_include=users_to_include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_user_balances_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**| The account type  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **activation_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user activation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **address_result** | **str**| Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (&#x60;latitude&#x60; and &#x60;longitude&#x60;) * none: Addresses are not returned. * primary: The primary (default) user address is returned  | [optional] 
 **balance_range** | [**list[int]**](int.md)| The minimum and / or maximum balance for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **brokers** | [**list[str]**](str.md)| Either id or a principal (login name, e-mail, etc) for brokers  | [optional] 
 **creation_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user creation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **groups** | [**list[str]**](str.md)| Either id or internal names of groups / group sets  | [optional] 
 **include_group** | **bool**| When set to &#x60;true&#x60; and the logged user has permission to view user groups, will return the &#x60;group&#x60; property on users.   | [optional] 
 **include_group_set** | **bool**| When set to &#x60;true&#x60; and the logged user has permission to view user group sets, will return the &#x60;groupSet&#x60; property on users.   | [optional] 
 **keywords** | **str**| Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  | [optional] 
 **last_incoming_transfer_period** | [**list[datetime]**](datetime.md)| The minimum / maximum date of the last incoming transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **last_login_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user last login date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **last_outgoing_transfer_period** | [**list[datetime]**](datetime.md)| The minimum / maximum date of the last outgoing transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **latitude** | **float**| The reference latitude for distance searches  | [optional] 
 **longitude** | **float**| The reference longitude for distance searches  | [optional] 
 **main_broker_only** | **bool**| When set to &#x60;true&#x60;, will match only users that have the brokers as set in the &#x60;brokers&#x60; parameter as main broker.   | [optional] 
 **max_distance** | **float**| Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both &#x60;longitude&#x60; and &#x60;latitude&#x60; parameters are passed with the actual reference position.  | [optional] 
 **medium_balance_range** | [**list[int]**](int.md)| An array with 2 elements, describing the lower and upper medium balance bounds. If not specified, the range defined in the account type will be used. If that one is also not defined, there will be no definitions for balance levels. Both bounds need to be set as 2 element in the array, or it won&#39;t be considered.  | [optional] 
 **negative_since_period** | [**list[datetime]**](datetime.md)| The minimum / maximum negative-since date for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **profile_fields** | [**list[str]**](str.md)| User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, &#x60;profileFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, &#x60;profileFields&#x3D;field1:valueA|valueB&#x60;. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;profileFields&#x3D;rank:bronze|silver,birthDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#39;rank&#39; is either bronze or silver, and whose &#39;birthDate&#39; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;profileFields&#x3D;birthDate:|2001-12-31&#x60;. The basic profile fields have one of the following identifiers: * &#x60;name&#x60; or &#x60;fullName&#x60;: Full name; * &#x60;username&#x60;, &#x60;loginName&#x60; or &#x60;login&#x60;: Login name; * &#x60;email&#x60;: E-mail; * &#x60;phone&#x60;: Phone; * &#x60;accountNumber&#x60;, &#x60;account&#x60;: Account number; * &#x60;image&#x60;: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the &#x60;addressFieldsInSearch&#x60; field in the corresponding result from a data-for-search request.  The specific address fields are: * &#x60;address&#x60;: Searches on any address field (not a specific field); * &#x60;address.address&#x60;: Searches on the fields that represent the   street address, which are &#x60;addressLine1&#x60;,    &#x60;addressLine2&#x60;,   &#x60;street&#x60;,   &#x60;buildingNumber&#x60; and   &#x60;complement&#x60;. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * &#x60;address.zip&#x60;: Searches for matching zip (postal) code; * &#x60;address.poBox&#x60;: Searches for matching postal box; * &#x60;address.neighborhood&#x60;: Searches by neighborhood; * &#x60;address.city&#x60;: Searches by city; * &#x60;address.region&#x60;: Searches by region (or state); * &#x60;address.country&#x60;: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: &#x60;profileFields&#x3D;dynamic:a|b|c&#x60;. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: &#x60;profileFields&#x3D;dynamic:&#39;business&#x60;.  | [optional] 
 **users_to_exclude** | [**list[str]**](str.md)| Indicated the users to be excluded from the result  | [optional] 
 **users_to_include** | [**list[str]**](str.md)| Indicated the users to be included in the result.  Any other user not present in this list will be excluded from the result.  | [optional] 

### Return type

[**UsersWithBalanceSummary**](UsersWithBalanceSummary.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts_by_owner**
> list[AccountWithStatus] list_accounts_by_owner(owner, fields=fields)

Lists accounts of the given owner with their statuses

Lists all visible accounts of the given user, or system accounts if the owner 'system' is used. Each account has status information, like the current balance, avaliable balance and so on. However, the returned data depend on the configuration, in the `Account status indicators` option, which is used to limit the amount of data returned. 

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Lists accounts of the given owner with their statuses
    api_response = api_instance.list_accounts_by_owner(owner, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->list_accounts_by_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**list[AccountWithStatus]**](AccountWithStatus.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_account_history**
> list[AccountHistoryResult] search_account_history(owner, account_type, fields=fields, access_clients=access_clients, amount_range=amount_range, broker=broker, by=by, channels=channels, charged_back=charged_back, custom_fields=custom_fields, date_period=date_period, direction=direction, excluded_ids=excluded_ids, from_current_access_client=from_current_access_client, groups=groups, include_generated_by_access_client=include_generated_by_access_client, order_by=order_by, page=page, page_size=page_size, statuses=statuses, transaction_number=transaction_number, transfer_filters=transfer_filters, transfer_kinds=transfer_kinds, transfer_types=transfer_types, user=user)

Search an account history

Returns a page of account history entries for a specific account, according to the given criteria 

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
owner = 'owner_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user; * `system` for data that belongs to the system. 
account_type = 'account_type_example' # str | The account type
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
access_clients = ['access_clients_example'] # list[str] | References to access clients (id or token) used to perform / receive the  transfer.  (optional)
amount_range = [swagger_client.BigDecimal()] # list[BigDecimal] | The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
broker = 'broker_example' # str | Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.  (optional)
by = 'by_example' # str | Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.  (optional)
channels = ['channels_example'] # list[str] | Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.  (optional)
charged_back = true # bool | When set to either `true` will only return transfers that were charged-back. When set to `false`, will only return transfers that were not charged-back. When left blank will not filter by this creterion.  (optional)
custom_fields = ['custom_fields_example'] # list[str] | Transaction custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, `customFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields=field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `customFields=rank:bronze|silver,documentDate:2000-01-01|2001-12-31` would match results whose custom field with internal name `rank` is either `bronze` or `silver`, and whose `documentDate` is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `customFields=documentDate:|2001-12-31`. A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `customFields=dynamic:a|b|c`. However, it is also possible to perform a partial-match search using the dynamic value label. In this case a single value, prefixed or enclosed by single quotes should be used. For example: `customFields=dynamic:'business` or `customFields=dynamic:'business'`.         (optional)
date_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
direction = 'direction_example' # str | Indicates whether from an account POV a transfer is a credit or debit Possible values are: * credit: The transfer impacts the balance positively * debit: The transfer impacts the balance negatively  (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of transfers ids to be excluded from the result.  (optional)
from_current_access_client = true # bool | Flag indicating whether to include only transfers by the current access client.  (optional)
groups = ['groups_example'] # list[str] | Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.  (optional)
include_generated_by_access_client = true # bool | Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a `ticket` or `paymentRequest` was processed then a new transfer will be generated.  (optional)
order_by = 'order_by_example' # str | Contains the possible 'order by' values when searching for transfers  Possible values are: * amountAsc: The result is ordered by amount descendant * amountDesc: The result is ordered by amount descendant * dateAsc: The result is ordered by date ascendant * dateDesc: The result is ordered by date descendant  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
statuses = ['statuses_example'] # list[str] | Transfer statuses used as search criteria. Each array element should be either the identifier or the status qualified internal name, composed by flow internal name, a dot, and the status internal name. For example, `loan.open` would be a valid internal name.  (optional)
transaction_number = 'transaction_number_example' # str | The transaction number of the matching transfer  (optional)
transfer_filters = ['transfer_filters_example'] # list[str] | Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format `accountType.transferFilter`.  (optional)
transfer_kinds = ['transfer_kinds_example'] # list[str] | Indicates the reason the transfer was created Possible values for each array element are: * accountFee: A transfer generated by an account fee charge * chargeback: A transfer which is a chargeback of another transfer * import: An imported transfer * initialCredit: A transfer which is the initial credit for a newly created account * payment: A transfer generated by a direct payment or accepting a webshop order * recurringPayment: A transfer generated when processing a recurring payment * scheduledPaymentInstallment: A transfer generated when processing a scheduled payment installment * transferFee: A transfer generated by a transfer fee charge  (optional)
transfer_types = ['transfer_types_example'] # list[str] | Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format `accountType.transferType`.  (optional)
user = 'user_example' # str | Reference a user that should have either received / performed the transfer.  (optional)

try:
    # Search an account history
    api_response = api_instance.search_account_history(owner, account_type, fields=fields, access_clients=access_clients, amount_range=amount_range, broker=broker, by=by, channels=channels, charged_back=charged_back, custom_fields=custom_fields, date_period=date_period, direction=direction, excluded_ids=excluded_ids, from_current_access_client=from_current_access_client, groups=groups, include_generated_by_access_client=include_generated_by_access_client, order_by=order_by, page=page, page_size=page_size, statuses=statuses, transaction_number=transaction_number, transfer_filters=transfer_filters, transfer_kinds=transfer_kinds, transfer_types=transfer_types, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->search_account_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user; * &#x60;system&#x60; for data that belongs to the system.  | 
 **account_type** | **str**| The account type | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **access_clients** | [**list[str]**](str.md)| References to access clients (id or token) used to perform / receive the  transfer.  | [optional] 
 **amount_range** | [**list[BigDecimal]**](BigDecimal.md)| The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **broker** | **str**| Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.  | [optional] 
 **by** | **str**| Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.  | [optional] 
 **channels** | [**list[str]**](str.md)| Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.  | [optional] 
 **charged_back** | **bool**| When set to either &#x60;true&#x60; will only return transfers that were charged-back. When set to &#x60;false&#x60;, will only return transfers that were not charged-back. When left blank will not filter by this creterion.  | [optional] 
 **custom_fields** | [**list[str]**](str.md)| Transaction custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, &#x60;customFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields&#x3D;field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;customFields&#x3D;rank:bronze|silver,documentDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#x60;rank&#x60; is either &#x60;bronze&#x60; or &#x60;silver&#x60;, and whose &#x60;documentDate&#x60; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;customFields&#x3D;documentDate:|2001-12-31&#x60;. A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: &#x60;customFields&#x3D;dynamic:a|b|c&#x60;. However, it is also possible to perform a partial-match search using the dynamic value label. In this case a single value, prefixed or enclosed by single quotes should be used. For example: &#x60;customFields&#x3D;dynamic:&#39;business&#x60; or &#x60;customFields&#x3D;dynamic:&#39;business&#39;&#x60;.         | [optional] 
 **date_period** | [**list[datetime]**](datetime.md)| The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **direction** | **str**| Indicates whether from an account POV a transfer is a credit or debit Possible values are: * credit: The transfer impacts the balance positively * debit: The transfer impacts the balance negatively  | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| List of transfers ids to be excluded from the result.  | [optional] 
 **from_current_access_client** | **bool**| Flag indicating whether to include only transfers by the current access client.  | [optional] 
 **groups** | [**list[str]**](str.md)| Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.  | [optional] 
 **include_generated_by_access_client** | **bool**| Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a &#x60;ticket&#x60; or &#x60;paymentRequest&#x60; was processed then a new transfer will be generated.  | [optional] 
 **order_by** | **str**| Contains the possible &#39;order by&#39; values when searching for transfers  Possible values are: * amountAsc: The result is ordered by amount descendant * amountDesc: The result is ordered by amount descendant * dateAsc: The result is ordered by date ascendant * dateDesc: The result is ordered by date descendant  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **statuses** | [**list[str]**](str.md)| Transfer statuses used as search criteria. Each array element should be either the identifier or the status qualified internal name, composed by flow internal name, a dot, and the status internal name. For example, &#x60;loan.open&#x60; would be a valid internal name.  | [optional] 
 **transaction_number** | **str**| The transaction number of the matching transfer  | [optional] 
 **transfer_filters** | [**list[str]**](str.md)| Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format &#x60;accountType.transferFilter&#x60;.  | [optional] 
 **transfer_kinds** | [**list[str]**](str.md)| Indicates the reason the transfer was created Possible values for each array element are: * accountFee: A transfer generated by an account fee charge * chargeback: A transfer which is a chargeback of another transfer * import: An imported transfer * initialCredit: A transfer which is the initial credit for a newly created account * payment: A transfer generated by a direct payment or accepting a webshop order * recurringPayment: A transfer generated when processing a recurring payment * scheduledPaymentInstallment: A transfer generated when processing a scheduled payment installment * transferFee: A transfer generated by a transfer fee charge  | [optional] 
 **transfer_types** | [**list[str]**](str.md)| Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format &#x60;accountType.transferType&#x60;.  | [optional] 
 **user** | **str**| Reference a user that should have either received / performed the transfer.  | [optional] 

### Return type

[**list[AccountHistoryResult]**](AccountHistoryResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_with_balances**
> list[UserWithBalanceResult] search_users_with_balances(account_type, fields=fields, activation_period=activation_period, address_result=address_result, balance_range=balance_range, brokers=brokers, creation_period=creation_period, groups=groups, include_group=include_group, include_group_set=include_group_set, keywords=keywords, last_incoming_transfer_period=last_incoming_transfer_period, last_login_period=last_login_period, last_outgoing_transfer_period=last_outgoing_transfer_period, latitude=latitude, longitude=longitude, main_broker_only=main_broker_only, max_distance=max_distance, medium_balance_range=medium_balance_range, negative_since_period=negative_since_period, order_by=order_by, page=page, page_size=page_size, profile_fields=profile_fields, users_to_exclude=users_to_exclude, users_to_include=users_to_include)

Searches for users together with balance information

Returns the users, together with their balances 

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_type = 'account_type_example' # str | The account type 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
activation_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user activation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
address_result = 'address_result_example' # str | Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (`latitude` and `longitude`) * none: Addresses are not returned. * primary: The primary (default) user address is returned  (optional)
balance_range = [56] # list[int] | The minimum and / or maximum balance for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
brokers = ['brokers_example'] # list[str] | Either id or a principal (login name, e-mail, etc) for brokers  (optional)
creation_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user creation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
groups = ['groups_example'] # list[str] | Either id or internal names of groups / group sets  (optional)
include_group = true # bool | When set to `true` and the logged user has permission to view user groups, will return the `group` property on users.   (optional)
include_group_set = true # bool | When set to `true` and the logged user has permission to view user group sets, will return the `groupSet` property on users.   (optional)
keywords = 'keywords_example' # str | Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  (optional)
last_incoming_transfer_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum date of the last incoming transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
last_login_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user last login date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
last_outgoing_transfer_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum date of the last outgoing transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
latitude = 1.2 # float | The reference latitude for distance searches  (optional)
longitude = 1.2 # float | The reference longitude for distance searches  (optional)
main_broker_only = true # bool | When set to `true`, will match only users that have the brokers as set in the `brokers` parameter as main broker.   (optional)
max_distance = 1.2 # float | Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both `longitude` and `latitude` parameters are passed with the actual reference position.  (optional)
medium_balance_range = [56] # list[int] | An array with 2 elements, describing the lower and upper medium balance bounds. If not specified, the range defined in the account type will be used. If that one is also not defined, there will be no definitions for balance levels. Both bounds need to be set as 2 element in the array, or it won't be considered.  (optional)
negative_since_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum negative-since date for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
order_by = 'order_by_example' # str | Contains the possible 'order by' values when searching for users with balances  Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * balanceAsc: User are ordered by balance, lower balances first. * balanceDesc: User are ordered by balance, higher balances first.  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
profile_fields = ['profile_fields_example'] # list[str] | User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, `profileFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, `profileFields=field1:valueA|valueB`. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `profileFields=rank:bronze|silver,birthDate:2000-01-01|2001-12-31` would match results whose custom field with internal name 'rank' is either bronze or silver, and whose 'birthDate' is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `profileFields=birthDate:|2001-12-31`. The basic profile fields have one of the following identifiers: * `name` or `fullName`: Full name; * `username`, `loginName` or `login`: Login name; * `email`: E-mail; * `phone`: Phone; * `accountNumber`, `account`: Account number; * `image`: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the `addressFieldsInSearch` field in the corresponding result from a data-for-search request.  The specific address fields are: * `address`: Searches on any address field (not a specific field); * `address.address`: Searches on the fields that represent the   street address, which are `addressLine1`,    `addressLine2`,   `street`,   `buildingNumber` and   `complement`. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * `address.zip`: Searches for matching zip (postal) code; * `address.poBox`: Searches for matching postal box; * `address.neighborhood`: Searches by neighborhood; * `address.city`: Searches by city; * `address.region`: Searches by region (or state); * `address.country`: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `profileFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `profileFields=dynamic:'business`.  (optional)
users_to_exclude = ['users_to_exclude_example'] # list[str] | Indicated the users to be excluded from the result  (optional)
users_to_include = ['users_to_include_example'] # list[str] | Indicated the users to be included in the result.  Any other user not present in this list will be excluded from the result.  (optional)

try:
    # Searches for users together with balance information
    api_response = api_instance.search_users_with_balances(account_type, fields=fields, activation_period=activation_period, address_result=address_result, balance_range=balance_range, brokers=brokers, creation_period=creation_period, groups=groups, include_group=include_group, include_group_set=include_group_set, keywords=keywords, last_incoming_transfer_period=last_incoming_transfer_period, last_login_period=last_login_period, last_outgoing_transfer_period=last_outgoing_transfer_period, latitude=latitude, longitude=longitude, main_broker_only=main_broker_only, max_distance=max_distance, medium_balance_range=medium_balance_range, negative_since_period=negative_since_period, order_by=order_by, page=page, page_size=page_size, profile_fields=profile_fields, users_to_exclude=users_to_exclude, users_to_include=users_to_include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->search_users_with_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_type** | **str**| The account type  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **activation_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user activation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **address_result** | **str**| Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (&#x60;latitude&#x60; and &#x60;longitude&#x60;) * none: Addresses are not returned. * primary: The primary (default) user address is returned  | [optional] 
 **balance_range** | [**list[int]**](int.md)| The minimum and / or maximum balance for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **brokers** | [**list[str]**](str.md)| Either id or a principal (login name, e-mail, etc) for brokers  | [optional] 
 **creation_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user creation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **groups** | [**list[str]**](str.md)| Either id or internal names of groups / group sets  | [optional] 
 **include_group** | **bool**| When set to &#x60;true&#x60; and the logged user has permission to view user groups, will return the &#x60;group&#x60; property on users.   | [optional] 
 **include_group_set** | **bool**| When set to &#x60;true&#x60; and the logged user has permission to view user group sets, will return the &#x60;groupSet&#x60; property on users.   | [optional] 
 **keywords** | **str**| Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  | [optional] 
 **last_incoming_transfer_period** | [**list[datetime]**](datetime.md)| The minimum / maximum date of the last incoming transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **last_login_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user last login date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **last_outgoing_transfer_period** | [**list[datetime]**](datetime.md)| The minimum / maximum date of the last outgoing transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **latitude** | **float**| The reference latitude for distance searches  | [optional] 
 **longitude** | **float**| The reference longitude for distance searches  | [optional] 
 **main_broker_only** | **bool**| When set to &#x60;true&#x60;, will match only users that have the brokers as set in the &#x60;brokers&#x60; parameter as main broker.   | [optional] 
 **max_distance** | **float**| Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both &#x60;longitude&#x60; and &#x60;latitude&#x60; parameters are passed with the actual reference position.  | [optional] 
 **medium_balance_range** | [**list[int]**](int.md)| An array with 2 elements, describing the lower and upper medium balance bounds. If not specified, the range defined in the account type will be used. If that one is also not defined, there will be no definitions for balance levels. Both bounds need to be set as 2 element in the array, or it won&#39;t be considered.  | [optional] 
 **negative_since_period** | [**list[datetime]**](datetime.md)| The minimum / maximum negative-since date for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **order_by** | **str**| Contains the possible &#39;order by&#39; values when searching for users with balances  Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * balanceAsc: User are ordered by balance, lower balances first. * balanceDesc: User are ordered by balance, higher balances first.  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **profile_fields** | [**list[str]**](str.md)| User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, &#x60;profileFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, &#x60;profileFields&#x3D;field1:valueA|valueB&#x60;. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;profileFields&#x3D;rank:bronze|silver,birthDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#39;rank&#39; is either bronze or silver, and whose &#39;birthDate&#39; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;profileFields&#x3D;birthDate:|2001-12-31&#x60;. The basic profile fields have one of the following identifiers: * &#x60;name&#x60; or &#x60;fullName&#x60;: Full name; * &#x60;username&#x60;, &#x60;loginName&#x60; or &#x60;login&#x60;: Login name; * &#x60;email&#x60;: E-mail; * &#x60;phone&#x60;: Phone; * &#x60;accountNumber&#x60;, &#x60;account&#x60;: Account number; * &#x60;image&#x60;: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the &#x60;addressFieldsInSearch&#x60; field in the corresponding result from a data-for-search request.  The specific address fields are: * &#x60;address&#x60;: Searches on any address field (not a specific field); * &#x60;address.address&#x60;: Searches on the fields that represent the   street address, which are &#x60;addressLine1&#x60;,    &#x60;addressLine2&#x60;,   &#x60;street&#x60;,   &#x60;buildingNumber&#x60; and   &#x60;complement&#x60;. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * &#x60;address.zip&#x60;: Searches for matching zip (postal) code; * &#x60;address.poBox&#x60;: Searches for matching postal box; * &#x60;address.neighborhood&#x60;: Searches by neighborhood; * &#x60;address.city&#x60;: Searches by city; * &#x60;address.region&#x60;: Searches by region (or state); * &#x60;address.country&#x60;: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: &#x60;profileFields&#x3D;dynamic:a|b|c&#x60;. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: &#x60;profileFields&#x3D;dynamic:&#39;business&#x60;.  | [optional] 
 **users_to_exclude** | [**list[str]**](str.md)| Indicated the users to be excluded from the result  | [optional] 
 **users_to_include** | [**list[str]**](str.md)| Indicated the users to be included in the result.  Any other user not present in this list will be excluded from the result.  | [optional] 

### Return type

[**list[UserWithBalanceResult]**](UserWithBalanceResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

