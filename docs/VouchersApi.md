# swagger_client.VouchersApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_vouchers**](VouchersApi.md#buy_vouchers) | **POST** /{user}/vouchers/buy | Buys one or more vouchers for the given user
[**buy_vouchers_with_status**](VouchersApi.md#buy_vouchers_with_status) | **POST** /{user}/vouchers/buy-with-status | Buys one or more vouchers for the given user returning the status.
[**get_user_vouchers_data_for_search**](VouchersApi.md#get_user_vouchers_data_for_search) | **GET** /{user}/vouchers/data-for-search | Returns data for searching vouchers a user has bought or redeemed
[**get_voucher_data_for_buy**](VouchersApi.md#get_voucher_data_for_buy) | **GET** /{user}/vouchers/data-for-buy | Returns data for buying a voucher of a specified type
[**get_voucher_data_for_redeem**](VouchersApi.md#get_voucher_data_for_redeem) | **GET** /{user}/vouchers/{token}/data-for-redeem | Returns data for redeeming a voucher by token
[**get_voucher_initial_data_for_redeem**](VouchersApi.md#get_voucher_initial_data_for_redeem) | **GET** /{user}/vouchers/data-for-redeem | Returns initial data for redeeming vouchers
[**get_voucher_qr_code**](VouchersApi.md#get_voucher_qr_code) | **GET** /vouchers/{key}/qr-code | Returns the QR-code image for the given voucher
[**list_voucher_types_for_buy**](VouchersApi.md#list_voucher_types_for_buy) | **GET** /{user}/vouchers/types-for-buy | Returns the voucher types the authenticated user can buy vouchers to the given user
[**redeem_voucher**](VouchersApi.md#redeem_voucher) | **POST** /{user}/vouchers/{token}/redeem | Redeems a voucher for the given user
[**search_user_vouchers**](VouchersApi.md#search_user_vouchers) | **GET** /{user}/vouchers | Searches for vouchers a user has bought or redeemed
[**view_voucher**](VouchersApi.md#view_voucher) | **GET** /vouchers/{key} | Returns data for a particular voucher


# **buy_vouchers**
> list[str] buy_vouchers(user, params, confirmation_password=confirmation_password)

Buys one or more vouchers for the given user

Buys vouchers. If the payment type has custom fields, the values should be passed as well. This service only returns the vouchers list, if  you need information about the voucher status please use  /{user}/vouchers/buy-with-status.  

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
params = swagger_client.BuyVoucher() # BuyVoucher | The buy voucher parameters
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Buys one or more vouchers for the given user
    api_response = api_instance.buy_vouchers(user, params, confirmation_password=confirmation_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->buy_vouchers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **params** | [**BuyVoucher**](BuyVoucher.md)| The buy voucher parameters | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

**list[str]**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buy_vouchers_with_status**
> VoucherBoughtResult buy_vouchers_with_status(user, params, confirmation_password=confirmation_password)

Buys one or more vouchers for the given user returning the status.

Buys vouchers. If the payment type has custom fields, the values should  be passed as well. The status returned in the result is shared by all vouchers. 

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
params = swagger_client.BuyVoucher() # BuyVoucher | The buy voucher parameters
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Buys one or more vouchers for the given user returning the status.
    api_response = api_instance.buy_vouchers_with_status(user, params, confirmation_password=confirmation_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->buy_vouchers_with_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **params** | [**BuyVoucher**](BuyVoucher.md)| The buy voucher parameters | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

[**VoucherBoughtResult**](VoucherBoughtResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_vouchers_data_for_search**
> UserVouchersDataForSearch get_user_vouchers_data_for_search(user, fields=fields, relation=relation)

Returns data for searching vouchers a user has bought or redeemed

Returns configuration data used to search vouchers the user has either bought (default) or redeemed (if `relation` is `redeemed`) 

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
relation = 'relation_example' # str | Indicates the relation used to filter the vouchers. Possible values are: * bought: A voucher the user has bought * redeemed: A voucher the user has redeemed  (optional)

try:
    # Returns data for searching vouchers a user has bought or redeemed
    api_response = api_instance.get_user_vouchers_data_for_search(user, fields=fields, relation=relation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->get_user_vouchers_data_for_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **relation** | **str**| Indicates the relation used to filter the vouchers. Possible values are: * bought: A voucher the user has bought * redeemed: A voucher the user has redeemed  | [optional] 

### Return type

[**UserVouchersDataForSearch**](UserVouchersDataForSearch.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voucher_data_for_buy**
> VoucherDataForBuy get_voucher_data_for_buy(user, type, fields=fields)

Returns data for buying a voucher of a specified type

Data for buying a voucher

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
type = 'type_example' # str | Either the `id` or `internalName` of the voucher type 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data for buying a voucher of a specified type
    api_response = api_instance.get_voucher_data_for_buy(user, type, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->get_voucher_data_for_buy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **type** | **str**| Either the &#x60;id&#x60; or &#x60;internalName&#x60; of the voucher type  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**VoucherDataForBuy**](VoucherDataForBuy.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voucher_data_for_redeem**
> VoucherDataForRedeem get_voucher_data_for_redeem(user, token, fields=fields)

Returns data for redeeming a voucher by token

Data for redeeming a specific voucher

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
token = 'token_example' # str | The voucher token to be redeemed
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data for redeeming a voucher by token
    api_response = api_instance.get_voucher_data_for_redeem(user, token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->get_voucher_data_for_redeem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **token** | **str**| The voucher token to be redeemed | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**VoucherDataForRedeem**](VoucherDataForRedeem.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voucher_initial_data_for_redeem**
> VoucherInitialDataForRedeem get_voucher_initial_data_for_redeem(user, fields=fields)

Returns initial data for redeeming vouchers

Returns initial data for redeeming vouchers

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns initial data for redeeming vouchers
    api_response = api_instance.get_voucher_initial_data_for_redeem(user, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->get_voucher_initial_data_for_redeem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**VoucherInitialDataForRedeem**](VoucherInitialDataForRedeem.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voucher_qr_code**
> get_voucher_qr_code(key, size=size)

Returns the QR-code image for the given voucher

The api documentation page, using swagger-ui (or any direct usage of an image tag), generates a second  request to show the image contents on the preview. This is a new GET request, without passing-in the authentication parameters. As this path requires authentication, the image is shown broken, but the first request works as expected, returning the image content. Optionally, to solve the problem described above and allow to authenticate the user when using sessions, a `sessionToken` or `accessClientToken` plus a `channel` query parameters could be specified. 

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | The voucher `id` or `token`. When the token is fully numeric, it must be preceded by a single quote (`'`). 
size = 'size_example' # str | The possible sizes of images. The actual pixel size depends on the configuration in Cyclos Possible values are: * large: Full image size * medium: Medium thumbnail * small: Small thumbnail  (optional)

try:
    # Returns the QR-code image for the given voucher
    api_instance.get_voucher_qr_code(key, size=size)
except ApiException as e:
    print("Exception when calling VouchersApi->get_voucher_qr_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The voucher &#x60;id&#x60; or &#x60;token&#x60;. When the token is fully numeric, it must be preceded by a single quote (&#x60;&#39;&#x60;).  | 
 **size** | **str**| The possible sizes of images. The actual pixel size depends on the configuration in Cyclos Possible values are: * large: Full image size * medium: Medium thumbnail * small: Small thumbnail  | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/jpeg, image/gif, image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_voucher_types_for_buy**
> list[VoucherTypeDetailed] list_voucher_types_for_buy(user, fields=fields)

Returns the voucher types the authenticated user can buy vouchers to the given user

List the voucher types the user can buy to another user (or himself) 

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns the voucher types the authenticated user can buy vouchers to the given user
    api_response = api_instance.list_voucher_types_for_buy(user, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->list_voucher_types_for_buy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**list[VoucherTypeDetailed]**](VoucherTypeDetailed.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_voucher**
> VoucherRedeemResult redeem_voucher(user, token, redeem=redeem)

Redeems a voucher for the given user

Redeems a voucher  

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
token = 'token_example' # str | The voucher token to be redeemed
redeem = swagger_client.RedeemVoucher() # RedeemVoucher | Additional redeem data (optional)

try:
    # Redeems a voucher for the given user
    api_response = api_instance.redeem_voucher(user, token, redeem=redeem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->redeem_voucher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **token** | **str**| The voucher token to be redeemed | 
 **redeem** | [**RedeemVoucher**](RedeemVoucher.md)| Additional redeem data | [optional] 

### Return type

[**VoucherRedeemResult**](VoucherRedeemResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_vouchers**
> list[VoucherResult] search_user_vouchers(user, fields=fields, amount_range=amount_range, creation_period=creation_period, expiration_period=expiration_period, page=page, page_size=page_size, redeem_period=redeem_period, relation=relation, statuses=statuses, token=token, types=types)

Searches for vouchers a user has bought or redeemed

Returns the list of matching vouchers the given user has either bought (default) or redeemed (if `type` is `redeemed`) 

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
amount_range = [swagger_client.BigDecimal()] # list[BigDecimal] | The minimum / maximum voucher amount  (optional)
creation_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum voucher creation date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
expiration_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum voucher expiration date Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
redeem_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum voucher redeem date Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
relation = 'relation_example' # str | The ways a voucher is related to an user Possible values are: * bought: A voucher the user has bought * redeemed: A voucher the user has redeemed  (optional)
statuses = ['statuses_example'] # list[str] | The voucher statuses Possible values for each array element are: * canceled: The voucher was canceled, and cannot be further used * expired: The voucher has expired without being redeemed * open: The voucher has been generated / bought, and is open * pending: The voucher has been bought, and the corresponding payment is pending for authorization * redeemed: The voucher has been redeemed, and the corresponding payment was done  (optional)
token = 'token_example' # str | The voucher token (with or without mask)  (optional)
types = ['types_example'] # list[str] | The ids or internal names of voucher types  (optional)

try:
    # Searches for vouchers a user has bought or redeemed
    api_response = api_instance.search_user_vouchers(user, fields=fields, amount_range=amount_range, creation_period=creation_period, expiration_period=expiration_period, page=page, page_size=page_size, redeem_period=redeem_period, relation=relation, statuses=statuses, token=token, types=types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->search_user_vouchers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **amount_range** | [**list[BigDecimal]**](BigDecimal.md)| The minimum / maximum voucher amount  | [optional] 
 **creation_period** | [**list[datetime]**](datetime.md)| The minimum / maximum voucher creation date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **expiration_period** | [**list[datetime]**](datetime.md)| The minimum / maximum voucher expiration date Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **redeem_period** | [**list[datetime]**](datetime.md)| The minimum / maximum voucher redeem date Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **relation** | **str**| The ways a voucher is related to an user Possible values are: * bought: A voucher the user has bought * redeemed: A voucher the user has redeemed  | [optional] 
 **statuses** | [**list[str]**](str.md)| The voucher statuses Possible values for each array element are: * canceled: The voucher was canceled, and cannot be further used * expired: The voucher has expired without being redeemed * open: The voucher has been generated / bought, and is open * pending: The voucher has been bought, and the corresponding payment is pending for authorization * redeemed: The voucher has been redeemed, and the corresponding payment was done  | [optional] 
 **token** | **str**| The voucher token (with or without mask)  | [optional] 
 **types** | [**list[str]**](str.md)| The ids or internal names of voucher types  | [optional] 

### Return type

[**list[VoucherResult]**](VoucherResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_voucher**
> VoucherView view_voucher(key, fields=fields)

Returns data for a particular voucher

Returns details about a particular voucher, as well as the transactions used to buy and redeem, and the permissions for authenticated over it. 

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
api_instance = swagger_client.VouchersApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | The voucher `id` or `token`. When the token is fully numeric, it must be preceded by a single quote (`'`). 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data for a particular voucher
    api_response = api_instance.view_voucher(key, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VouchersApi->view_voucher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The voucher &#x60;id&#x60; or &#x60;token&#x60;. When the token is fully numeric, it must be preceded by a single quote (&#x60;&#39;&#x60;).  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**VoucherView**](VoucherView.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

