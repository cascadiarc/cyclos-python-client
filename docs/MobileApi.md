# swagger_client.MobileApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_for_mobile_guest**](MobileApi.md#data_for_mobile_guest) | **GET** /mobile/data-for-guest | Returns data the mobile application uses while in guest mode
[**data_for_mobile_user**](MobileApi.md#data_for_mobile_user) | **GET** /mobile/data-for-user | Returns data the mobile application uses in either user or POS mode 
[**mobile_page_content**](MobileApi.md#mobile_page_content) | **GET** /mobile/page/{id} | Returns the content of a mobile page 


# **data_for_mobile_guest**
> DataForMobileGuest data_for_mobile_guest(fields=fields, cyclos_version=cyclos_version, header_if=header_if, footer_if=footer_if, theme_if=theme_if, translations_if=translations_if)

Returns data the mobile application uses while in guest mode

The data returned can be controlled with a cache key. Each data type has a parameter, such as `headerIf`, which returns the data only if it has changed since the last request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
cyclos_version = 'cyclos_version_example' # str | The last known Cyclos version. Sometimes, data to be cached depends on the version of the Cyclos application, and this helps controlling such cases  (optional)
header_if = 'header_if_example' # str | Controls the header cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it.  (optional)
footer_if = 'footer_if_example' # str | Controls the footer cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it.  (optional)
theme_if = 'theme_if_example' # str | Controls the theme cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it.  (optional)
translations_if = 'translations_if_example' # str | Controls the translations cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it.  (optional)

try:
    # Returns data the mobile application uses while in guest mode
    api_response = api_instance.data_for_mobile_guest(fields=fields, cyclos_version=cyclos_version, header_if=header_if, footer_if=footer_if, theme_if=theme_if, translations_if=translations_if)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->data_for_mobile_guest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **cyclos_version** | **str**| The last known Cyclos version. Sometimes, data to be cached depends on the version of the Cyclos application, and this helps controlling such cases  | [optional] 
 **header_if** | **str**| Controls the header cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it.  | [optional] 
 **footer_if** | **str**| Controls the footer cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it.  | [optional] 
 **theme_if** | **str**| Controls the theme cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it.  | [optional] 
 **translations_if** | **str**| Controls the translations cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it.  | [optional] 

### Return type

[**DataForMobileGuest**](DataForMobileGuest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_for_mobile_user**
> DataForMobileUser data_for_mobile_user(fields=fields, cyclos_version=cyclos_version, theme_if=theme_if, translations_if=translations_if, mobile_help_if=mobile_help_if, pos_help_if=pos_help_if)

Returns data the mobile application uses in either user or POS mode 

The data returned can be controlled with a cache key. Each data type has a parameter, such as `helpIf`, which returns the data only if it has changed since the last request. 

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
api_instance = swagger_client.MobileApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
cyclos_version = 'cyclos_version_example' # str | The last known Cyclos version. Sometimes, data to be cached depends on the version of the Cyclos application, and this helps controlling such cases  (optional)
theme_if = 'theme_if_example' # str | Controls the theme cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it.  (optional)
translations_if = 'translations_if_example' # str | Controls the translations cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it.  (optional)
mobile_help_if = 'mobile_help_if_example' # str | Controls the mobile help cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it. Only taken into account when not accessing as access client (not in POS mode).  (optional)
pos_help_if = 'pos_help_if_example' # str | Controls the POS help cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it. Only taken into account when accessing as access client (POS mode).  (optional)

try:
    # Returns data the mobile application uses in either user or POS mode 
    api_response = api_instance.data_for_mobile_user(fields=fields, cyclos_version=cyclos_version, theme_if=theme_if, translations_if=translations_if, mobile_help_if=mobile_help_if, pos_help_if=pos_help_if)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->data_for_mobile_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **cyclos_version** | **str**| The last known Cyclos version. Sometimes, data to be cached depends on the version of the Cyclos application, and this helps controlling such cases  | [optional] 
 **theme_if** | **str**| Controls the theme cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it.  | [optional] 
 **translations_if** | **str**| Controls the translations cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it.  | [optional] 
 **mobile_help_if** | **str**| Controls the mobile help cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it. Only taken into account when not accessing as access client (not in POS mode).  | [optional] 
 **pos_help_if** | **str**| Controls the POS help cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it. Only taken into account when accessing as access client (POS mode).  | [optional] 

### Return type

[**DataForMobileUser**](DataForMobileUser.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mobile_page_content**
> str mobile_page_content(id)

Returns the content of a mobile page 

Returns the content of a mobile page, either by id or internal name 

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
api_instance = swagger_client.MobileApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The mobile page id

try:
    # Returns the content of a mobile page 
    api_response = api_instance.mobile_page_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileApi->mobile_page_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The mobile page id | 

### Return type

**str**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

