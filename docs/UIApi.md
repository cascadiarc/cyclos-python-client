# swagger_client.UIApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_for_ui**](UIApi.md#data_for_ui) | **GET** /ui/data-for-ui | Returns useful data required to properly display a user interface


# **data_for_ui**
> DataForUi data_for_ui(fields=fields, kind=kind, cyclos_version=cyclos_version, header_if=header_if, footer_if=footer_if, theme_if=theme_if, theme_by_components=theme_by_components)

Returns useful data required to properly display a user interface

The returned data contains settings and also content like header, footer  and theme. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UIApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
kind = 'kind_example' # str | Specifies the kind of user interface to get data for. If null then no  data related to the UI will be returned. Possible values are: * custom: A custom front-end application. Has no headers, footers or theme * main: The main web user interface * mobile: The mobile application user interface * pay: The Ticket / Easy invoice confirmation application user interface  (optional)
cyclos_version = 'cyclos_version_example' # str | The last known Cyclos version. Sometimes, data to be cached depends on the version of the Cyclos application, and this helps controlling such cases  (optional)
header_if = 'header_if_example' # str | Controls the header cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it.  (optional)
footer_if = 'footer_if_example' # str | Controls the footer cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it.  (optional)
theme_if = 'theme_if_example' # str | Controls the theme cache. If is a boolean value (`true` or `false`) will forcibly return or skip the content. Otherwise, it should be a string in the form `id|version`. In this case, the content will be returned only when changed. When blank will always return it.  (optional)
theme_by_components = true # bool | Flag used to indicate how the theme must be returned (if returned): true means the theme components (base / advanced definitions and custom style) will be filled. Otherwise the final CSS (i. e the theme content). Only valid if the kind of the user interface is NOT `mobile`. For that kind the theme es always returned by its components.  (optional)

try:
    # Returns useful data required to properly display a user interface
    api_response = api_instance.data_for_ui(fields=fields, kind=kind, cyclos_version=cyclos_version, header_if=header_if, footer_if=footer_if, theme_if=theme_if, theme_by_components=theme_by_components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UIApi->data_for_ui: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **kind** | **str**| Specifies the kind of user interface to get data for. If null then no  data related to the UI will be returned. Possible values are: * custom: A custom front-end application. Has no headers, footers or theme * main: The main web user interface * mobile: The mobile application user interface * pay: The Ticket / Easy invoice confirmation application user interface  | [optional] 
 **cyclos_version** | **str**| The last known Cyclos version. Sometimes, data to be cached depends on the version of the Cyclos application, and this helps controlling such cases  | [optional] 
 **header_if** | **str**| Controls the header cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it.  | [optional] 
 **footer_if** | **str**| Controls the footer cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it.  | [optional] 
 **theme_if** | **str**| Controls the theme cache. If is a boolean value (&#x60;true&#x60; or &#x60;false&#x60;) will forcibly return or skip the content. Otherwise, it should be a string in the form &#x60;id|version&#x60;. In this case, the content will be returned only when changed. When blank will always return it.  | [optional] 
 **theme_by_components** | **bool**| Flag used to indicate how the theme must be returned (if returned): true means the theme components (base / advanced definitions and custom style) will be filled. Otherwise the final CSS (i. e the theme content). Only valid if the kind of the user interface is NOT &#x60;mobile&#x60;. For that kind the theme es always returned by its components.  | [optional] 

### Return type

[**DataForUi**](DataForUi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

