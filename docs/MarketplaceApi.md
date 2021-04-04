# swagger_client.MarketplaceApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_order_by_buyer**](MarketplaceApi.md#accept_order_by_buyer) | **POST** /orders/{order}/buyer/accept | Accepts a pending order by buyer.
[**accept_order_by_seller**](MarketplaceApi.md#accept_order_by_seller) | **POST** /orders/{order}/seller/accept | Accepts a pending order by seller.
[**add_item_to_shopping_cart**](MarketplaceApi.md#add_item_to_shopping_cart) | **POST** /shopping-carts/items/{ad} | Adds the given webshop ad to the corresponding shopping cart.
[**adjust_and_get_shopping_cart_details**](MarketplaceApi.md#adjust_and_get_shopping_cart_details) | **POST** /shopping-carts/{id}/adjust | Adjusts a shopping cart items, returning its details.
[**checkout_shopping_cart**](MarketplaceApi.md#checkout_shopping_cart) | **POST** /shopping-carts/{id}/checkout | Checks out a shopping cart.
[**create_ad**](MarketplaceApi.md#create_ad) | **POST** /{user}/marketplace | Creates a new advertisement for the given user.
[**create_ad_question**](MarketplaceApi.md#create_ad_question) | **POST** /marketplace/{ad}/questions | Creates a new advertisement question.
[**delete_ad**](MarketplaceApi.md#delete_ad) | **DELETE** /marketplace/{ad} | Removes an advertisement.
[**delete_ad_question**](MarketplaceApi.md#delete_ad_question) | **DELETE** /questions/{id} | Removes an advertisement question.
[**get_ad_data_for_edit**](MarketplaceApi.md#get_ad_data_for_edit) | **GET** /marketplace/{ad}/data-for-edit | Returns configuration data for editing an advertisement.
[**get_ad_data_for_new**](MarketplaceApi.md#get_ad_data_for_new) | **GET** /{user}/marketplace/data-for-new | Returns configuration data for creating a new advertisement for a user and kind. 
[**get_ad_data_for_search**](MarketplaceApi.md#get_ad_data_for_search) | **GET** /marketplace/data-for-search | Returns configuration data for searching advertisements.
[**get_ad_question**](MarketplaceApi.md#get_ad_question) | **GET** /questions/{id} | Returns details of an advertisement question.
[**get_data_for_set_delivery_method**](MarketplaceApi.md#get_data_for_set_delivery_method) | **GET** /orders/{order}/seller/data-for-set-delivery | Returns configuration data to set delivery method data by seller.
[**get_order_data_for_accept_by_buyer**](MarketplaceApi.md#get_order_data_for_accept_by_buyer) | **GET** /orders/{order}/buyer/data-for-accept | Returns configuration data for accept an order by buyer.
[**get_shopping_cart_data_for_checkout**](MarketplaceApi.md#get_shopping_cart_data_for_checkout) | **GET** /shopping-carts/{id}/data-for-checkout | Returns configuration data for check-out a shopping cart.
[**get_shopping_cart_details**](MarketplaceApi.md#get_shopping_cart_details) | **GET** /shopping-carts/{id} | Returns details of a shopping cart.
[**get_shopping_carts**](MarketplaceApi.md#get_shopping_carts) | **GET** /shopping-carts | Returns the shopping carts list.
[**get_user_ads_data_for_search**](MarketplaceApi.md#get_user_ads_data_for_search) | **GET** /{user}/marketplace/data-for-search | Returns configuration data for searching advertisements of a user.
[**modify_item_quantity_on_shopping_cart**](MarketplaceApi.md#modify_item_quantity_on_shopping_cart) | **PUT** /shopping-carts/items/{ad} | Modifies the corresponding cart with the new quantity for the given webshop ad. 
[**reject_order**](MarketplaceApi.md#reject_order) | **POST** /orders/{order}/reject | Rejects a pending order.
[**remove_item_from_shopping_cart**](MarketplaceApi.md#remove_item_from_shopping_cart) | **DELETE** /shopping-carts/items/{ad} | Removes the given webshop ad from the corresponding shopping cart.
[**remove_shopping_cart**](MarketplaceApi.md#remove_shopping_cart) | **DELETE** /shopping-carts/{id} | Removes a shopping cart.
[**search_ads**](MarketplaceApi.md#search_ads) | **GET** /marketplace | Searches for advertisements.
[**search_user_ads**](MarketplaceApi.md#search_user_ads) | **GET** /{user}/marketplace | Searches for advertisements of a specific user.
[**search_user_orders**](MarketplaceApi.md#search_user_orders) | **GET** /{user}/orders | Searches for orders of a specific user.
[**set_delivery_method**](MarketplaceApi.md#set_delivery_method) | **POST** /orders/{order}/seller/set-delivery | Sets delivery method data by seller.
[**update_ad**](MarketplaceApi.md#update_ad) | **PUT** /marketplace/{ad} | Updates an existing advertisement.
[**view_ad**](MarketplaceApi.md#view_ad) | **GET** /marketplace/{ad} | Returns details of an advertisement.
[**view_order**](MarketplaceApi.md#view_order) | **GET** /orders/{order} | Returns details of an order.


# **accept_order_by_buyer**
> accept_order_by_buyer(order, confirmation_password=confirmation_password, params=params)

Accepts a pending order by buyer.

Accepts a pending order by buyer generating the corresponding payment. The order status must be `pendingBuyer` to be  accepted by the authenticated user (i.e the buyer).  The `paymentType` and the `confirmationPassword` are required under the  following circumstances:  `paymentType`: Only required if the order was generated as a sale by the  seller and not from the shopping cart check-out (Sales are not supported yet).  `confirmationPassword`: Only required if at check-out a delivery method was  not set or its charge type is `negotiatied`.      The possible statuses after an order acceptance are: * `paymentPending`: if the generated payment is  awaiting for authorization;          * `completed`: if the payment was done.       

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
order = 'order_example' # str | Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote. 
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)
params = swagger_client.AcceptOrderByBuyer() # AcceptOrderByBuyer | The parameters for accepting the order. (optional)

try:
    # Accepts a pending order by buyer.
    api_instance.accept_order_by_buyer(order, confirmation_password=confirmation_password, params=params)
except ApiException as e:
    print("Exception when calling MarketplaceApi->accept_order_by_buyer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote.  | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 
 **params** | [**AcceptOrderByBuyer**](AcceptOrderByBuyer.md)| The parameters for accepting the order. | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accept_order_by_seller**
> accept_order_by_seller(order, params=params)

Accepts a pending order by seller.

Accepts a pending order by seller generating the corresponding payment. The order status must be `pendingSeller` to be  accepted by the authenticated user (i.e seller).  The possible statuses after an order acceptance are: * `paymentPending`: if the generated payment is  awaiting for authorization;         * `completed`: if the payment was done.       

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
order = 'order_example' # str | Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote. 
params = swagger_client.AcceptOrderBySeller() # AcceptOrderBySeller | The parameters for accepting the order. (optional)

try:
    # Accepts a pending order by seller.
    api_instance.accept_order_by_seller(order, params=params)
except ApiException as e:
    print("Exception when calling MarketplaceApi->accept_order_by_seller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote.  | 
 **params** | [**AcceptOrderBySeller**](AcceptOrderBySeller.md)| The parameters for accepting the order. | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_to_shopping_cart**
> int add_item_to_shopping_cart(ad, quantity=quantity)

Adds the given webshop ad to the corresponding shopping cart.

Adds the given webshop ad to the corresponding shopping cart according to the seller and currency and returns the total number of webshop ads in all carts. Optionally a quantity can be specified. The different shopping carts are created dynamically according to the seller and currency.     E.g if the user adds the following webshop ads (i.e items): * 1 from Seller1 in Dolars; * 2 from Seller1 in Euros; * 1 from Seller2 un Dolars.  Then the following three carts will be created for the authenticated user: * 1 cart containing 1 item offered by Seller1 in Dolars; * 1 cart containing 2 item offered by Seller1 in Euros; * 1 cart containing 1 item offered by Seller2 in Dolars.  Finally, the total number of wbshop ads returned will be 4.  For those quantity-limited products the given quantity could have been  adjusted to met the restrictions. You can view the adjustment applied to  each item when retrieving the details of a shopping cart. if you want to  remove the adjustment just send a new request to modify the quantity  (using `PUT /shopping-carts/items/{ad}`) and specify the current quantity  (i.e the already adjusted and returned in the details of the shopping cart) as the parameter. 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
quantity = 1.2 # float | The quantity being added. It could be a decimal number only if the  corresponding webshop ad allows it.  (optional)

try:
    # Adds the given webshop ad to the corresponding shopping cart.
    api_response = api_instance.add_item_to_shopping_cart(ad, quantity=quantity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->add_item_to_shopping_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **quantity** | **float**| The quantity being added. It could be a decimal number only if the  corresponding webshop ad allows it.  | [optional] 

### Return type

**int**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjust_and_get_shopping_cart_details**
> ShoppingCartView adjust_and_get_shopping_cart_details(id, fields=fields)

Adjusts a shopping cart items, returning its details.

Works like `GET /shopping-carts/{id}`, but first adjusts the status of all items. For each item checks both the availability and the quantity, setting to corresponding `availability` or `quantityAdjustment` property if anything was modified. 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Adjusts a shopping cart items, returning its details.
    api_response = api_instance.adjust_and_get_shopping_cart_details(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->adjust_and_get_shopping_cart_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**ShoppingCartView**](ShoppingCartView.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_shopping_cart**
> int checkout_shopping_cart(id, checkout, confirmation_password=confirmation_password)

Checks out a shopping cart.

Checks out the given shopping cart associated to the authenticated user. After the check-out the purchase order will be awaiting for the seller's  acceptance (i. e with status `pendingSeller`). 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
checkout = swagger_client.ShoppingCartCheckout() # ShoppingCartCheckout | The data for check-out.
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Checks out a shopping cart.
    api_response = api_instance.checkout_shopping_cart(id, checkout, confirmation_password=confirmation_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->checkout_shopping_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **checkout** | [**ShoppingCartCheckout**](ShoppingCartCheckout.md)| The data for check-out. | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

**int**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ad**
> str create_ad(user, advertisement)

Creates a new advertisement for the given user.

Creates a new advertisement for the given user. 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
advertisement = swagger_client.AdNew() # AdNew | The advertisement to be created.

try:
    # Creates a new advertisement for the given user.
    api_response = api_instance.create_ad(user, advertisement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->create_ad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **advertisement** | [**AdNew**](AdNew.md)| The advertisement to be created. | 

### Return type

**str**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ad_question**
> str create_ad_question(ad, question)

Creates a new advertisement question.

Creates a new question for an advertisement and associate it to the  authenticated user. 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
question = 'question_example' # str | 

try:
    # Creates a new advertisement question.
    api_response = api_instance.create_ad_question(ad, question)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->create_ad_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **question** | **str**|  | 

### Return type

**str**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: text/plain; charset=utf-8
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ad**
> delete_ad(ad)

Removes an advertisement.

Removes an advertisement by id.

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      

try:
    # Removes an advertisement.
    api_instance.delete_ad(ad)
except ApiException as e:
    print("Exception when calling MarketplaceApi->delete_ad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ad_question**
> delete_ad_question(id)

Removes an advertisement question.

Removes an advertisement question created for the authenticated user. 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification

try:
    # Removes an advertisement question.
    api_instance.delete_ad_question(id)
except ApiException as e:
    print("Exception when calling MarketplaceApi->delete_ad_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_data_for_edit**
> AdDataForEdit get_ad_data_for_edit(ad, fields=fields)

Returns configuration data for editing an advertisement.

Returns configuration data which can be used to edit an advertisement. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceApi()
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data for editing an advertisement.
    api_response = api_instance.get_ad_data_for_edit(ad, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->get_ad_data_for_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**AdDataForEdit**](AdDataForEdit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_data_for_new**
> AdDataForNew get_ad_data_for_new(user, fields=fields, kind=kind)

Returns configuration data for creating a new advertisement for a user and kind. 

Returns data for creating a new advertisement for the given user. The `kind` should be informed. If not set, `simple` is assumed. Currently only `simple` advertisements can be created through this API.       

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceApi()
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
kind = 'kind_example' # str | The possible kinds of an advertisement Possible values are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  (optional)

try:
    # Returns configuration data for creating a new advertisement for a user and kind. 
    api_response = api_instance.get_ad_data_for_new(user, fields=fields, kind=kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->get_ad_data_for_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **kind** | **str**| The possible kinds of an advertisement Possible values are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  | [optional] 

### Return type

[**AdDataForNew**](AdDataForNew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_data_for_search**
> AdDataForSearch get_ad_data_for_search(fields=fields, kind=kind, brokered=brokered)

Returns configuration data for searching advertisements.

Returns data needed on for a general advertisements search.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
kind = 'kind_example' # str | Indicates the kind of advertisement that should be searched. When nothing is passed (default) all kinds will be searched. Possible values are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  (optional)
brokered = true # bool | If the authenticated is a broker, passing the `true` value will indicate the advertisements to be searched are from managed users of that broker. The default is `false`.  (optional)

try:
    # Returns configuration data for searching advertisements.
    api_response = api_instance.get_ad_data_for_search(fields=fields, kind=kind, brokered=brokered)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->get_ad_data_for_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **kind** | **str**| Indicates the kind of advertisement that should be searched. When nothing is passed (default) all kinds will be searched. Possible values are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  | [optional] 
 **brokered** | **bool**| If the authenticated is a broker, passing the &#x60;true&#x60; value will indicate the advertisements to be searched are from managed users of that broker. The default is &#x60;false&#x60;.  | [optional] 

### Return type

[**AdDataForSearch**](AdDataForSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_question**
> AdQuestionView get_ad_question(id, fields=fields)

Returns details of an advertisement question.

Return detailed information of an advertisement question.

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns details of an advertisement question.
    api_response = api_instance.get_ad_question(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->get_ad_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**AdQuestionView**](AdQuestionView.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_for_set_delivery_method**
> OrderDataForSetDeliveryMethod get_data_for_set_delivery_method(order, fields=fields)

Returns configuration data to set delivery method data by seller.

Returns configuration data to set delivery method data by seller of an  order given by id.  

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
order = 'order_example' # str | Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data to set delivery method data by seller.
    api_response = api_instance.get_data_for_set_delivery_method(order, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->get_data_for_set_delivery_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**OrderDataForSetDeliveryMethod**](OrderDataForSetDeliveryMethod.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_data_for_accept_by_buyer**
> OrderDataForAcceptByBuyer get_order_data_for_accept_by_buyer(order, fields=fields)

Returns configuration data for accept an order by buyer.

Returns configuration data for accept an order given by id as the buyer. 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
order = 'order_example' # str | Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data for accept an order by buyer.
    api_response = api_instance.get_order_data_for_accept_by_buyer(order, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->get_order_data_for_accept_by_buyer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**OrderDataForAcceptByBuyer**](OrderDataForAcceptByBuyer.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shopping_cart_data_for_checkout**
> ShoppingCartDataForCheckout get_shopping_cart_data_for_checkout(id, fields=fields)

Returns configuration data for check-out a shopping cart.

Returns configuration data for check-out the given shopping cart by id. 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data for check-out a shopping cart.
    api_response = api_instance.get_shopping_cart_data_for_checkout(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->get_shopping_cart_data_for_checkout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**ShoppingCartDataForCheckout**](ShoppingCartDataForCheckout.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shopping_cart_details**
> ShoppingCartView get_shopping_cart_details(id, fields=fields)

Returns details of a shopping cart.

Returns the details of a shopping cart by id with all webshop ads offered by the same seller and in the same currency. 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns details of a shopping cart.
    api_response = api_instance.get_shopping_cart_details(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->get_shopping_cart_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**ShoppingCartView**](ShoppingCartView.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shopping_carts**
> list[ShoppingCartResult] get_shopping_carts(fields=fields)

Returns the shopping carts list.

Returns the shopping carts for the authenticated user. Each cart contains  all webshop ads offered by the same seller and in the same currency. 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns the shopping carts list.
    api_response = api_instance.get_shopping_carts(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->get_shopping_carts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**list[ShoppingCartResult]**](ShoppingCartResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ads_data_for_search**
> UserAdsDataForSearch get_user_ads_data_for_search(user, fields=fields, kind=kind)

Returns configuration data for searching advertisements of a user.

Returns data needed on for a user's advertisements search.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceApi()
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
kind = 'kind_example' # str | Indicates the kind of advertisement that should be searched. When nothing is passed (default) all kinds will be searched. Possible values are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  (optional)

try:
    # Returns configuration data for searching advertisements of a user.
    api_response = api_instance.get_user_ads_data_for_search(user, fields=fields, kind=kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->get_user_ads_data_for_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **kind** | **str**| Indicates the kind of advertisement that should be searched. When nothing is passed (default) all kinds will be searched. Possible values are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  | [optional] 

### Return type

[**UserAdsDataForSearch**](UserAdsDataForSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_item_quantity_on_shopping_cart**
> int modify_item_quantity_on_shopping_cart(ad, quantity)

Modifies the corresponding cart with the new quantity for the given webshop ad. 

Modifies the corresponding shopping cart with the new quantity for the  given webshop ad only if it was already added to the cart of the authenticted user and returns the total number of webshop ads in all carts.  For those quantity-limited products the given quantity could have been  adjusted to met the restrictions. You can view the adjustment applied to  each item when retrieving the details of a shopping cart. if you want to  remove the adjustment just send a new request to modify the quantity  and specify the current quantity (i.e the already adjusted and returned  in the details of the shopping cart) as the parameter. 

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
quantity = 1.2 # float | The new quantity for the given webshop ad. It could be a decimal  number only if the corresponding webshop ad allows it. If zero then the webshop ad is removed from the cart. 

try:
    # Modifies the corresponding cart with the new quantity for the given webshop ad. 
    api_response = api_instance.modify_item_quantity_on_shopping_cart(ad, quantity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->modify_item_quantity_on_shopping_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **quantity** | **float**| The new quantity for the given webshop ad. It could be a decimal  number only if the corresponding webshop ad allows it. If zero then the webshop ad is removed from the cart.  | 

### Return type

**int**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_order**
> reject_order(order, params=params)

Rejects a pending order.

Rejects a pending order by buyer or seller. The order status must be `pendingBuyer` or  `pendingSeller` to be rejected by the authenticated.  user (buyer/seller).  The possible statuses after an order rejection are: * `rejectedBySeller`: if the authenticated user is  the seller; * `rejectedByBuyer`: if the authenticated user is  the buyer.     

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
order = 'order_example' # str | Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote. 
params = swagger_client.RejectOrder() # RejectOrder | The parameters for rejecting the order. (optional)

try:
    # Rejects a pending order.
    api_instance.reject_order(order, params=params)
except ApiException as e:
    print("Exception when calling MarketplaceApi->reject_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote.  | 
 **params** | [**RejectOrder**](RejectOrder.md)| The parameters for rejecting the order. | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_item_from_shopping_cart**
> int remove_item_from_shopping_cart(ad)

Removes the given webshop ad from the corresponding shopping cart.

Removes the given webshop ad from the corresponding shopping cart  according to the seller and currency and returns the total number of  the remaining webshop ads in all carts.  

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      

try:
    # Removes the given webshop ad from the corresponding shopping cart.
    api_response = api_instance.remove_item_from_shopping_cart(ad)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->remove_item_from_shopping_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 

### Return type

**int**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shopping_cart**
> int remove_shopping_cart(id)

Removes a shopping cart.

Removes the given shopping cart by id and returns the total number of  the webshop ads in the remaining all carts.  

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification

try:
    # Removes a shopping cart.
    api_response = api_instance.remove_shopping_cart(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->remove_shopping_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 

### Return type

**int**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ads**
> list[AdResult] search_ads(fields=fields, address_result=address_result, broker=broker, category=category, currency=currency, custom_fields=custom_fields, expiration_period=expiration_period, groups=groups, has_images=has_images, keywords=keywords, kind=kind, latitude=latitude, longitude=longitude, max_distance=max_distance, order_by=order_by, owner=owner, page=page, page_size=page_size, price_range=price_range, profile_fields=profile_fields, publication_period=publication_period, return_editable=return_editable, statuses=statuses)

Searches for advertisements.

Returns a page of advertisements that match a given criteria. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
address_result = 'address_result_example' # str | Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (`latitude` and `longitude`) * none: Addresses are not returned.  (optional)
broker = 'broker_example' # str | Either id or an identification, such as login name, e-mail, etc, for the broker of the advertisement owner. The allowed identification methods are those the authenticated user can use on keywords search.  (optional)
category = 'category_example' # str | Either id or internal name of a category  (optional)
currency = 'currency_example' # str | Either id or internal name of a currency for the price  (optional)
custom_fields = ['custom_fields_example'] # list[str] | Advertisement custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, `customFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields=field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `customFields=tradeType:offer|search,extraDate:2000-01-01|2001-12-31` would match results whose custom field with internal name `tradeType` is either `offer` or `search`, and whose `extraDate` is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `customFields=extraDate:|2001-12-31`. A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `customFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `customFields=dynamic:'business`.  (optional)
expiration_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum expiration date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
groups = ['groups_example'] # list[str] | Array of either id or internal names of user groups the advertisement owner must belong to  (optional)
has_images = true # bool | When set to `true` only advertisements with images are returned  (optional)
keywords = 'keywords_example' # str | Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  (optional)
kind = 'kind_example' # str | The possible kinds of an advertisement Possible values are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  (optional)
latitude = 1.2 # float | The reference latitude for distance searches  (optional)
longitude = 1.2 # float | The reference longitude for distance searches  (optional)
max_distance = 1.2 # float | Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both `longitude` and `latitude` parameters are passed with the actual reference position.  (optional)
order_by = 'order_by_example' # str | Indicates how advertisements results are ordered. Possible values are: * date: Newest advertisements are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * priceAsc: Smaller prices are returned first. Advertisements without price are returned last. * priceDesc: Higher prices are returned first. Advertisements without price are returned last. * random: Without definite order * relevance: This is the default if keywords are used. Best matching advertisements come first.  (optional)
owner = 'owner_example' # str | Either id or an identification, such as login name, e-mail, etc, for the advertisement owner. The allowed identification methods are those the authenticated user can use on keywords search.  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
price_range = [swagger_client.BigDecimal()] # list[BigDecimal] | The minumum / maximum price. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
profile_fields = ['profile_fields_example'] # list[str] | User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, `profileFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, `profileFields=field1:valueA|valueB`. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `profileFields=rank:bronze|silver,birthDate:2000-01-01|2001-12-31` would match results whose custom field with internal name 'rank' is either bronze or silver, and whose 'birthDate' is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `profileFields=birthDate:|2001-12-31`. The basic profile fields have one of the following identifiers: * `name` or `fullName`: Full name; * `username`, `loginName` or `login`: Login name; * `email`: E-mail; * `phone`: Phone; * `accountNumber`, `account`: Account number; * `image`: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the `addressFieldsInSearch` field in the corresponding result from a data-for-search request.  The specific address fields are: * `address`: Searches on any address field (not a specific field); * `address.address`: Searches on the fields that represent the   street address, which are `addressLine1`,    `addressLine2`,   `street`,   `buildingNumber` and   `complement`. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * `address.zip`: Searches for matching zip (postal) code; * `address.poBox`: Searches for matching postal box; * `address.neighborhood`: Searches by neighborhood; * `address.city`: Searches by city; * `address.region`: Searches by region (or state); * `address.country`: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `profileFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `profileFields=dynamic:'business`.  (optional)
publication_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum publication date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
return_editable = true # bool | Whether to return the editable property. Passing `true` will impact the performance a bit, as for each returned advertisement some statuses and permissions need to be checked.  (optional)
statuses = ['statuses_example'] # list[str] | The possible status for an advertisement Possible values for each array element are: * active: The advertisement is published and can be seen by other users. * disabled: The advertisement is disabled because the owner no longer has access to the currency of the advertisement. It cannot be seen by other users. * draft: In draft status, only the owner can see and edit the advertisement. This status is only possible if the system is configured to require authorizations. * expired: The advertisement publication period has already expired, and cannot be seen by other users. * hidden: The advertisement is manually hidden from other users * pending: The advertisement is pending for an authorization and cannot be seen by other users. This status is only possible if the system is configured to require authorizations. * scheduled: The advertisement has a future publication period, and cannot be seen by other users.   (optional)

try:
    # Searches for advertisements.
    api_response = api_instance.search_ads(fields=fields, address_result=address_result, broker=broker, category=category, currency=currency, custom_fields=custom_fields, expiration_period=expiration_period, groups=groups, has_images=has_images, keywords=keywords, kind=kind, latitude=latitude, longitude=longitude, max_distance=max_distance, order_by=order_by, owner=owner, page=page, page_size=page_size, price_range=price_range, profile_fields=profile_fields, publication_period=publication_period, return_editable=return_editable, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->search_ads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **address_result** | **str**| Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (&#x60;latitude&#x60; and &#x60;longitude&#x60;) * none: Addresses are not returned.  | [optional] 
 **broker** | **str**| Either id or an identification, such as login name, e-mail, etc, for the broker of the advertisement owner. The allowed identification methods are those the authenticated user can use on keywords search.  | [optional] 
 **category** | **str**| Either id or internal name of a category  | [optional] 
 **currency** | **str**| Either id or internal name of a currency for the price  | [optional] 
 **custom_fields** | [**list[str]**](str.md)| Advertisement custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, &#x60;customFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields&#x3D;field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;customFields&#x3D;tradeType:offer|search,extraDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#x60;tradeType&#x60; is either &#x60;offer&#x60; or &#x60;search&#x60;, and whose &#x60;extraDate&#x60; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;customFields&#x3D;extraDate:|2001-12-31&#x60;. A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: &#x60;customFields&#x3D;dynamic:a|b|c&#x60;. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: &#x60;customFields&#x3D;dynamic:&#39;business&#x60;.  | [optional] 
 **expiration_period** | [**list[datetime]**](datetime.md)| The minimum / maximum expiration date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **groups** | [**list[str]**](str.md)| Array of either id or internal names of user groups the advertisement owner must belong to  | [optional] 
 **has_images** | **bool**| When set to &#x60;true&#x60; only advertisements with images are returned  | [optional] 
 **keywords** | **str**| Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  | [optional] 
 **kind** | **str**| The possible kinds of an advertisement Possible values are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  | [optional] 
 **latitude** | **float**| The reference latitude for distance searches  | [optional] 
 **longitude** | **float**| The reference longitude for distance searches  | [optional] 
 **max_distance** | **float**| Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both &#x60;longitude&#x60; and &#x60;latitude&#x60; parameters are passed with the actual reference position.  | [optional] 
 **order_by** | **str**| Indicates how advertisements results are ordered. Possible values are: * date: Newest advertisements are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * priceAsc: Smaller prices are returned first. Advertisements without price are returned last. * priceDesc: Higher prices are returned first. Advertisements without price are returned last. * random: Without definite order * relevance: This is the default if keywords are used. Best matching advertisements come first.  | [optional] 
 **owner** | **str**| Either id or an identification, such as login name, e-mail, etc, for the advertisement owner. The allowed identification methods are those the authenticated user can use on keywords search.  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **price_range** | [**list[BigDecimal]**](BigDecimal.md)| The minumum / maximum price. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **profile_fields** | [**list[str]**](str.md)| User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, &#x60;profileFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, &#x60;profileFields&#x3D;field1:valueA|valueB&#x60;. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;profileFields&#x3D;rank:bronze|silver,birthDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#39;rank&#39; is either bronze or silver, and whose &#39;birthDate&#39; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;profileFields&#x3D;birthDate:|2001-12-31&#x60;. The basic profile fields have one of the following identifiers: * &#x60;name&#x60; or &#x60;fullName&#x60;: Full name; * &#x60;username&#x60;, &#x60;loginName&#x60; or &#x60;login&#x60;: Login name; * &#x60;email&#x60;: E-mail; * &#x60;phone&#x60;: Phone; * &#x60;accountNumber&#x60;, &#x60;account&#x60;: Account number; * &#x60;image&#x60;: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the &#x60;addressFieldsInSearch&#x60; field in the corresponding result from a data-for-search request.  The specific address fields are: * &#x60;address&#x60;: Searches on any address field (not a specific field); * &#x60;address.address&#x60;: Searches on the fields that represent the   street address, which are &#x60;addressLine1&#x60;,    &#x60;addressLine2&#x60;,   &#x60;street&#x60;,   &#x60;buildingNumber&#x60; and   &#x60;complement&#x60;. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * &#x60;address.zip&#x60;: Searches for matching zip (postal) code; * &#x60;address.poBox&#x60;: Searches for matching postal box; * &#x60;address.neighborhood&#x60;: Searches by neighborhood; * &#x60;address.city&#x60;: Searches by city; * &#x60;address.region&#x60;: Searches by region (or state); * &#x60;address.country&#x60;: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: &#x60;profileFields&#x3D;dynamic:a|b|c&#x60;. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: &#x60;profileFields&#x3D;dynamic:&#39;business&#x60;.  | [optional] 
 **publication_period** | [**list[datetime]**](datetime.md)| The minimum / maximum publication date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **return_editable** | **bool**| Whether to return the editable property. Passing &#x60;true&#x60; will impact the performance a bit, as for each returned advertisement some statuses and permissions need to be checked.  | [optional] 
 **statuses** | [**list[str]**](str.md)| The possible status for an advertisement Possible values for each array element are: * active: The advertisement is published and can be seen by other users. * disabled: The advertisement is disabled because the owner no longer has access to the currency of the advertisement. It cannot be seen by other users. * draft: In draft status, only the owner can see and edit the advertisement. This status is only possible if the system is configured to require authorizations. * expired: The advertisement publication period has already expired, and cannot be seen by other users. * hidden: The advertisement is manually hidden from other users * pending: The advertisement is pending for an authorization and cannot be seen by other users. This status is only possible if the system is configured to require authorizations. * scheduled: The advertisement has a future publication period, and cannot be seen by other users.   | [optional] 

### Return type

[**list[AdResult]**](AdResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_ads**
> list[AdResult] search_user_ads(user, address_result=address_result, category=category, currency=currency, custom_fields=custom_fields, expiration_period=expiration_period, has_images=has_images, keywords=keywords, kind=kind, latitude=latitude, longitude=longitude, max_distance=max_distance, order_by=order_by, page=page, page_size=page_size, price_range=price_range, profile_fields=profile_fields, publication_period=publication_period, statuses=statuses)

Searches for advertisements of a specific user.

Returns a page of advertisements that match a given criteria for a given  user. Equivallent to calling `GET /marketplace?owner={user}`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceApi()
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
address_result = 'address_result_example' # str | Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (`latitude` and `longitude`) * none: Addresses are not returned.  (optional)
category = 'category_example' # str | Either id or internal name of a category  (optional)
currency = 'currency_example' # str | Either id or internal name of a currency for the price  (optional)
custom_fields = ['custom_fields_example'] # list[str] | Advertisement custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, `customFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields=field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `customFields=tradeType:offer|search,extraDate:2000-01-01|2001-12-31` would match results whose custom field with internal name `tradeType` is either `offer` or `search`, and whose `extraDate` is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `customFields=extraDate:|2001-12-31`. A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `customFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `customFields=dynamic:'business`.  (optional)
expiration_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum expiration date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
has_images = true # bool | When set to `true` only advertisements with images are returned  (optional)
keywords = 'keywords_example' # str | Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  (optional)
kind = 'kind_example' # str | The possible kinds of an advertisement Possible values are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  (optional)
latitude = 1.2 # float | The reference latitude for distance searches  (optional)
longitude = 1.2 # float | The reference longitude for distance searches  (optional)
max_distance = 1.2 # float | Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both `longitude` and `latitude` parameters are passed with the actual reference position.  (optional)
order_by = 'order_by_example' # str | Indicates how advertisements results are ordered. Possible values are: * date: Newest advertisements are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * priceAsc: Smaller prices are returned first. Advertisements without price are returned last. * priceDesc: Higher prices are returned first. Advertisements without price are returned last. * random: Without definite order * relevance: This is the default if keywords are used. Best matching advertisements come first.  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
price_range = [swagger_client.BigDecimal()] # list[BigDecimal] | The minumum / maximum price. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
profile_fields = ['profile_fields_example'] # list[str] | User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, `profileFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, `profileFields=field1:valueA|valueB`. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `profileFields=rank:bronze|silver,birthDate:2000-01-01|2001-12-31` would match results whose custom field with internal name 'rank' is either bronze or silver, and whose 'birthDate' is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `profileFields=birthDate:|2001-12-31`. The basic profile fields have one of the following identifiers: * `name` or `fullName`: Full name; * `username`, `loginName` or `login`: Login name; * `email`: E-mail; * `phone`: Phone; * `accountNumber`, `account`: Account number; * `image`: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the `addressFieldsInSearch` field in the corresponding result from a data-for-search request.  The specific address fields are: * `address`: Searches on any address field (not a specific field); * `address.address`: Searches on the fields that represent the   street address, which are `addressLine1`,    `addressLine2`,   `street`,   `buildingNumber` and   `complement`. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * `address.zip`: Searches for matching zip (postal) code; * `address.poBox`: Searches for matching postal box; * `address.neighborhood`: Searches by neighborhood; * `address.city`: Searches by city; * `address.region`: Searches by region (or state); * `address.country`: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `profileFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `profileFields=dynamic:'business`.  (optional)
publication_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum publication date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
statuses = ['statuses_example'] # list[str] | The possible status for an advertisement Possible values for each array element are: * active: The advertisement is published and can be seen by other users. * disabled: The advertisement is disabled because the owner no longer has access to the currency of the advertisement. It cannot be seen by other users. * draft: In draft status, only the owner can see and edit the advertisement. This status is only possible if the system is configured to require authorizations. * expired: The advertisement publication period has already expired, and cannot be seen by other users. * hidden: The advertisement is manually hidden from other users * pending: The advertisement is pending for an authorization and cannot be seen by other users. This status is only possible if the system is configured to require authorizations. * scheduled: The advertisement has a future publication period, and cannot be seen by other users.   (optional)

try:
    # Searches for advertisements of a specific user.
    api_response = api_instance.search_user_ads(user, address_result=address_result, category=category, currency=currency, custom_fields=custom_fields, expiration_period=expiration_period, has_images=has_images, keywords=keywords, kind=kind, latitude=latitude, longitude=longitude, max_distance=max_distance, order_by=order_by, page=page, page_size=page_size, price_range=price_range, profile_fields=profile_fields, publication_period=publication_period, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->search_user_ads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **address_result** | **str**| Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (&#x60;latitude&#x60; and &#x60;longitude&#x60;) * none: Addresses are not returned.  | [optional] 
 **category** | **str**| Either id or internal name of a category  | [optional] 
 **currency** | **str**| Either id or internal name of a currency for the price  | [optional] 
 **custom_fields** | [**list[str]**](str.md)| Advertisement custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, &#x60;customFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields&#x3D;field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;customFields&#x3D;tradeType:offer|search,extraDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#x60;tradeType&#x60; is either &#x60;offer&#x60; or &#x60;search&#x60;, and whose &#x60;extraDate&#x60; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;customFields&#x3D;extraDate:|2001-12-31&#x60;. A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: &#x60;customFields&#x3D;dynamic:a|b|c&#x60;. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: &#x60;customFields&#x3D;dynamic:&#39;business&#x60;.  | [optional] 
 **expiration_period** | [**list[datetime]**](datetime.md)| The minimum / maximum expiration date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **has_images** | **bool**| When set to &#x60;true&#x60; only advertisements with images are returned  | [optional] 
 **keywords** | **str**| Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  | [optional] 
 **kind** | **str**| The possible kinds of an advertisement Possible values are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  | [optional] 
 **latitude** | **float**| The reference latitude for distance searches  | [optional] 
 **longitude** | **float**| The reference longitude for distance searches  | [optional] 
 **max_distance** | **float**| Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both &#x60;longitude&#x60; and &#x60;latitude&#x60; parameters are passed with the actual reference position.  | [optional] 
 **order_by** | **str**| Indicates how advertisements results are ordered. Possible values are: * date: Newest advertisements are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * priceAsc: Smaller prices are returned first. Advertisements without price are returned last. * priceDesc: Higher prices are returned first. Advertisements without price are returned last. * random: Without definite order * relevance: This is the default if keywords are used. Best matching advertisements come first.  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **price_range** | [**list[BigDecimal]**](BigDecimal.md)| The minumum / maximum price. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **profile_fields** | [**list[str]**](str.md)| User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, &#x60;profileFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, &#x60;profileFields&#x3D;field1:valueA|valueB&#x60;. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;profileFields&#x3D;rank:bronze|silver,birthDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#39;rank&#39; is either bronze or silver, and whose &#39;birthDate&#39; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;profileFields&#x3D;birthDate:|2001-12-31&#x60;. The basic profile fields have one of the following identifiers: * &#x60;name&#x60; or &#x60;fullName&#x60;: Full name; * &#x60;username&#x60;, &#x60;loginName&#x60; or &#x60;login&#x60;: Login name; * &#x60;email&#x60;: E-mail; * &#x60;phone&#x60;: Phone; * &#x60;accountNumber&#x60;, &#x60;account&#x60;: Account number; * &#x60;image&#x60;: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the &#x60;addressFieldsInSearch&#x60; field in the corresponding result from a data-for-search request.  The specific address fields are: * &#x60;address&#x60;: Searches on any address field (not a specific field); * &#x60;address.address&#x60;: Searches on the fields that represent the   street address, which are &#x60;addressLine1&#x60;,    &#x60;addressLine2&#x60;,   &#x60;street&#x60;,   &#x60;buildingNumber&#x60; and   &#x60;complement&#x60;. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * &#x60;address.zip&#x60;: Searches for matching zip (postal) code; * &#x60;address.poBox&#x60;: Searches for matching postal box; * &#x60;address.neighborhood&#x60;: Searches by neighborhood; * &#x60;address.city&#x60;: Searches by city; * &#x60;address.region&#x60;: Searches by region (or state); * &#x60;address.country&#x60;: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: &#x60;profileFields&#x3D;dynamic:a|b|c&#x60;. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: &#x60;profileFields&#x3D;dynamic:&#39;business&#x60;.  | [optional] 
 **publication_period** | [**list[datetime]**](datetime.md)| The minimum / maximum publication date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **statuses** | [**list[str]**](str.md)| The possible status for an advertisement Possible values for each array element are: * active: The advertisement is published and can be seen by other users. * disabled: The advertisement is disabled because the owner no longer has access to the currency of the advertisement. It cannot be seen by other users. * draft: In draft status, only the owner can see and edit the advertisement. This status is only possible if the system is configured to require authorizations. * expired: The advertisement publication period has already expired, and cannot be seen by other users. * hidden: The advertisement is manually hidden from other users * pending: The advertisement is pending for an authorization and cannot be seen by other users. This status is only possible if the system is configured to require authorizations. * scheduled: The advertisement has a future publication period, and cannot be seen by other users.   | [optional] 

### Return type

[**list[AdResult]**](AdResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_orders**
> list[UserOrderResult] search_user_orders(user, fields=fields, creation_period=creation_period, number=number, page=page, page_size=page_size, related_user=related_user, sales=sales, statuses=statuses)

Searches for orders of a specific user.

Returns a page of orders that match a given criteria for a given user.  The authenticated user must be the seller, buyer or a manager user with  permission to view purchases or sales. Note: A list of statuses is accepted but at this moment only one status  can be specified.  

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
creation_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum order creation date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
number = 'number_example' # str | The generated order number according to the webshop settings.  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
related_user = 'related_user_example' # str | Either id or an identification, such as login name, e-mail, etc, for the seller or buyer according whether we are searching for purchases  or sales. The allowed identification methods are those the authenticated user can use on keywords search.      (optional)
sales = true # bool | Are we searching for sales or purchases? If not specified it's assumed purchases (i.e `false`)  (optional)
statuses = ['statuses_example'] # list[str] | The possible statuses for an order Possible values for each array element are: * completed: The order was accepted by the seller and/or buyer and the related payment was done. * disposed: The order was marked as disposed because the seller and/or buyer were removed or they do not have any account in the order's currency. * draft: The order has been created by the seller, but has not yet been sent to the buyer for approval * paymentCanceled: The related payment was not done because was canceled after finish the authorization process. * paymentDenied: The related payment was not done because was denied. * paymentPending: The order was accepted by the seller and/or buyer and the related payment is waiting for authorization. * pendingBuyer: The order is pending by the buyer's action. * pendingSeller: The order is pending by the seller's action. * rejectedByBuyer: The order was rejected by the buyer. * rejectedBySeller: The order was rejected by the seller.  (optional)

try:
    # Searches for orders of a specific user.
    api_response = api_instance.search_user_orders(user, fields=fields, creation_period=creation_period, number=number, page=page, page_size=page_size, related_user=related_user, sales=sales, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->search_user_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **creation_period** | [**list[datetime]**](datetime.md)| The minimum / maximum order creation date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **number** | **str**| The generated order number according to the webshop settings.  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **related_user** | **str**| Either id or an identification, such as login name, e-mail, etc, for the seller or buyer according whether we are searching for purchases  or sales. The allowed identification methods are those the authenticated user can use on keywords search.      | [optional] 
 **sales** | **bool**| Are we searching for sales or purchases? If not specified it&#39;s assumed purchases (i.e &#x60;false&#x60;)  | [optional] 
 **statuses** | [**list[str]**](str.md)| The possible statuses for an order Possible values for each array element are: * completed: The order was accepted by the seller and/or buyer and the related payment was done. * disposed: The order was marked as disposed because the seller and/or buyer were removed or they do not have any account in the order&#39;s currency. * draft: The order has been created by the seller, but has not yet been sent to the buyer for approval * paymentCanceled: The related payment was not done because was canceled after finish the authorization process. * paymentDenied: The related payment was not done because was denied. * paymentPending: The order was accepted by the seller and/or buyer and the related payment is waiting for authorization. * pendingBuyer: The order is pending by the buyer&#39;s action. * pendingSeller: The order is pending by the seller&#39;s action. * rejectedByBuyer: The order was rejected by the buyer. * rejectedBySeller: The order was rejected by the seller.  | [optional] 

### Return type

[**list[UserOrderResult]**](UserOrderResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_delivery_method**
> set_delivery_method(order, params=params)

Sets delivery method data by seller.

Sets the delivery method data by seller for the order given by id. This operation can be used only if the order is in status  `pendingSeller` and has not already set delivery  method data. After the delivery method has been set the order will be enter in status  `pendingBuyer` to be accepted by buyer.       

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
order = 'order_example' # str | Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote. 
params = swagger_client.SetDeliveryMethod() # SetDeliveryMethod | The parameters for setting the delivery method. (optional)

try:
    # Sets delivery method data by seller.
    api_instance.set_delivery_method(order, params=params)
except ApiException as e:
    print("Exception when calling MarketplaceApi->set_delivery_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote.  | 
 **params** | [**SetDeliveryMethod**](SetDeliveryMethod.md)| The parameters for setting the delivery method. | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ad**
> update_ad(ad, advertisement)

Updates an existing advertisement.

Updates an existing advertisement.

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
advertisement = swagger_client.AdEdit() # AdEdit | The advertisement to be edited.

try:
    # Updates an existing advertisement.
    api_instance.update_ad(ad, advertisement)
except ApiException as e:
    print("Exception when calling MarketplaceApi->update_ad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **advertisement** | [**AdEdit**](AdEdit.md)| The advertisement to be edited. | 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_ad**
> AdView view_ad(ad, fields=fields)

Returns details of an advertisement.

Returns detailed information of an advertisement. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketplaceApi()
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns details of an advertisement.
    api_response = api_instance.view_ad(ad, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->view_ad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**AdView**](AdView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_order**
> OrderView view_order(order, fields=fields)

Returns details of an order.

Returns detailed information of an order given by id.

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
api_instance = swagger_client.MarketplaceApi(swagger_client.ApiClient(configuration))
order = 'order_example' # str | Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns details of an order.
    api_response = api_instance.view_order(order, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->view_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Either the order id or number. If the number is solely comprised of numbers, it must be prefixed by a single quote.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**OrderView**](OrderView.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

