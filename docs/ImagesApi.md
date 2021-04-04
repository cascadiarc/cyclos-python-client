# swagger_client.ImagesApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_image**](ImagesApi.md#delete_image) | **DELETE** /images/{idOrKey} | Removes an image by id or key
[**get_ad_images_list_data**](ImagesApi.md#get_ad_images_list_data) | **GET** /marketplace/{ad}/images/list-data | Returns the images of an advertisement, plus additional permissions and data  
[**get_image_content**](ImagesApi.md#get_image_content) | **GET** /images/content/{idOrKey} | Returns an image content by id or key
[**get_image_content_by_id**](ImagesApi.md#get_image_content_by_id) | **GET** /images/{id}/content | (deprecated) Returns an image content by id
[**get_image_content_deprecated**](ImagesApi.md#get_image_content_deprecated) | **GET** /images/{kind}/{file} | Returns an image content
[**get_user_images_list_data**](ImagesApi.md#get_user_images_list_data) | **GET** /{user}/images/list-data | Returns either &#x60;profile&#x60; or &#x60;custom&#x60; images for a given user, plus additional permissions and data  
[**list_ad_images**](ImagesApi.md#list_ad_images) | **GET** /marketplace/{ad}/images | Lists the images of an advertisement 
[**list_temp_images**](ImagesApi.md#list_temp_images) | **GET** /images/temp | Lists temporary images related to the currently authenticated user or guest 
[**list_user_images**](ImagesApi.md#list_user_images) | **GET** /{user}/images | Lists either &#x60;profile&#x60; or &#x60;custom&#x60; images for a given user  
[**reorder_ad_images**](ImagesApi.md#reorder_ad_images) | **PUT** /marketplace/{ad}/images/order | Changes the order of the images of an advertisement  
[**reorder_profile_images**](ImagesApi.md#reorder_profile_images) | **PUT** /{user}/images/order | Changes the order of a user&#39;s profile images  
[**upload_ad_image**](ImagesApi.md#upload_ad_image) | **POST** /marketplace/{ad}/images | Adds a new image for the given advertisement. 
[**upload_contact_info_image**](ImagesApi.md#upload_contact_info_image) | **POST** /contact-infos/{id}/image | Uploads a new image for the given additional contact information. 
[**upload_contact_info_image_deprecated**](ImagesApi.md#upload_contact_info_image_deprecated) | **POST** /contactInfos/{id}/image | This operation is deprecated, use &#x60;POST /contact-infos/{id}/image&#x60; instead.
[**upload_temp_image**](ImagesApi.md#upload_temp_image) | **POST** /images/temp | Adds a new temporary image for the currently authenticated user or guest. 
[**upload_user_image**](ImagesApi.md#upload_user_image) | **POST** /{user}/images | Adds a new image for the given user. The image kind is either  &#x60;profile&#x60; or &#x60;custom&#x60;. 
[**view_image**](ImagesApi.md#view_image) | **GET** /images/{idOrKey} | Returns an image details by id or key


# **delete_image**
> delete_image(id_or_key)

Removes an image by id or key

Removes the image with the given internal id or key. Any image kind can be removed using this operation, but the authenticated user needs the appropriate permission to do so.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id_or_key = 'id_or_key_example' # str | The image id or file name

try:
    # Removes an image by id or key
    api_instance.delete_image(id_or_key)
except ApiException as e:
    print("Exception when calling ImagesApi->delete_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_key** | **str**| The image id or file name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_images_list_data**
> ImagesListData get_ad_images_list_data(ad, fields=fields)

Returns the images of an advertisement, plus additional permissions and data  

Returns the images of an advertisement. Additional data, such as the maximum images and whether the images can be managed by the authenticated user are also returned. 

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
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns the images of an advertisement, plus additional permissions and data  
    api_response = api_instance.get_ad_images_list_data(ad, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_ad_images_list_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**ImagesListData**](ImagesListData.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_content**
> file get_image_content(id_or_key, width=width, height=height)

Returns an image content by id or key

Returns the content of an image, given the image identifier or key. When neither `width` nor `height` are specified, returns the original content. The original ratio is always maintained. When only of one of  the dimensions is specified, it is used as maximum, and the other is calculated. When both are informed, the maximum size with the original ratio that fits both dimensions is used.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id_or_key = 'id_or_key_example' # str | The image id or file name
width = 56 # int | The requested image width (optional)
height = 56 # int | The requested file height (optional)

try:
    # Returns an image content by id or key
    api_response = api_instance.get_image_content(id_or_key, width=width, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_key** | **str**| The image id or file name | 
 **width** | **int**| The requested image width | [optional] 
 **height** | **int**| The requested file height | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/jpeg, image/gif, image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_content_by_id**
> file get_image_content_by_id(id, width=width, height=height)

(deprecated) Returns an image content by id

Returns the content of an image, given the image id. When neither `width` nor `height` are specified, returns the original content. The original ratio is always maintained. When only of one of  the dimensions is specified, it is used as maximum, and the other is calculated. When both are informed, the maximum size with the original ratio that fits both dimensions is used.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id = 'id_example' # str | The object identification
width = 56 # int | The requested image width (optional)
height = 56 # int | The requested file height (optional)

try:
    # (deprecated) Returns an image content by id
    api_response = api_instance.get_image_content_by_id(id, width=width, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_content_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **width** | **int**| The requested image width | [optional] 
 **height** | **int**| The requested file height | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/jpeg, image/gif, image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_content_deprecated**
> file get_image_content_deprecated(kind, file, width=width, height=height)

Returns an image content

(deprecated) Returns the content of an image, given the image kind and key. When neither `width` nor `height` are specified, returns the original content. The original ratio is always maintained. When only of one of  the dimensions is specified, it is used as maximum, and the other is calculated. When both are informed, the maximum size with the original ratio that fits both dimensions is used.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
kind = 'kind_example' # str | Determines the kind of an image Possible values are: * contactInfo: An image of an additional contact information * customFieldValue: An image used as custom field value * marketplace: Advertisement images are associated with an advertisement, be it simple or for web shop. * marketplaceCategory: An image of an advertisement (simple or webshop) * profile: User profile images are those associated with the user profile. The first profile image is used to depict the user on search results. * systemCustom: System custom images are additional images an administrator that can be used on rich text contents. * temp: A temporary image which can upload for later associating with an entity being registered (for example, user or advertisement). * userCustom: User custom images are additional images that can be used on rich text contents. * voucherType: An image of a voucher type 
file = 'file_example' # str | The file name. This is not the original uploaded file name, but a generated one. 
width = 56 # int | The requested image width (optional)
height = 56 # int | The requested file height (optional)

try:
    # Returns an image content
    api_response = api_instance.get_image_content_deprecated(kind, file, width=width, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_content_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**| Determines the kind of an image Possible values are: * contactInfo: An image of an additional contact information * customFieldValue: An image used as custom field value * marketplace: Advertisement images are associated with an advertisement, be it simple or for web shop. * marketplaceCategory: An image of an advertisement (simple or webshop) * profile: User profile images are those associated with the user profile. The first profile image is used to depict the user on search results. * systemCustom: System custom images are additional images an administrator that can be used on rich text contents. * temp: A temporary image which can upload for later associating with an entity being registered (for example, user or advertisement). * userCustom: User custom images are additional images that can be used on rich text contents. * voucherType: An image of a voucher type  | 
 **file** | **str**| The file name. This is not the original uploaded file name, but a generated one.  | 
 **width** | **int**| The requested image width | [optional] 
 **height** | **int**| The requested file height | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/jpeg, image/gif, image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_images_list_data**
> ImagesListData get_user_images_list_data(user, fields=fields, kind=kind)

Returns either `profile` or `custom` images for a given user, plus additional permissions and data  

Returns either `profile` or `custom` images for the given user. For `profile`, the user must be visible by the authenticated user. For `custom`, the authenticated user must either be the owner or a manager (administrator or broker). Custom images are used in rich text content, not images for custom fields. Additional data, such as the maximum images and whether the images can be managed by the authenticated user are also returned. 

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
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
kind = 'kind_example' # str | The kind of images to be returned.   The default value is `profile` Possible values are: * custom: User custom images are additional images that can be used on rich text contents. * profile: User profile images are those associated with the user profile. The first profile image is used to depict the user on search results.  (optional)

try:
    # Returns either `profile` or `custom` images for a given user, plus additional permissions and data  
    api_response = api_instance.get_user_images_list_data(user, fields=fields, kind=kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_user_images_list_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **kind** | **str**| The kind of images to be returned.   The default value is &#x60;profile&#x60; Possible values are: * custom: User custom images are additional images that can be used on rich text contents. * profile: User profile images are those associated with the user profile. The first profile image is used to depict the user on search results.  | [optional] 

### Return type

[**ImagesListData**](ImagesListData.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ad_images**
> list[Image] list_ad_images(ad, fields=fields)

Lists the images of an advertisement 

Returns the images of an advertisement. 

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
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Lists the images of an advertisement 
    api_response = api_instance.list_ad_images(ad, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->list_ad_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**list[Image]**](Image.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_temp_images**
> list[Image] list_temp_images(fields=fields, target=target, guest_key=guest_key, user=user, custom_field=custom_field, custom_field_kind=custom_field_kind)

Lists temporary images related to the currently authenticated user or guest 

Returns all uploaded temporary images by the current user, or guest key. If the current request is as guest and no guest key is given, the IP address is used to match images. Using a key is recommended, because clients that move between WiFi and mobile connection or if the client is in a network with multiple outbound IP addresses, images won't be correctly matched without a key.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
target = 'target_example' # str | The possible targets for a temporary image Possible values are: * advertisement: The image will be used for an advertisement of a specific user * contactInfo: The image will be used for an additional contact information of a specific user * customValue: The image will be used for a value of a specific custom field * userProfile: The image will be used as a profile image for an existing user * userRegistration: The image will be used as a profile image for a newly registered user  (optional)
guest_key = 'guest_key_example' # str | This parameter is only taken into account if the current request is running as guest. It is the key passed by the client when uploading images. If no key is given, images are matched by remote address.  (optional)
user = 'user_example' # str | If the target is `userProfile` or `advertisement`, must be either the id or an identification method of the target user (or advertisement owner).  (optional)
custom_field = 'custom_field_example' # str | If the temp image will be used as the value of a custom field of type image then the corresponding custom field must be given (id or internal name). Otherwise this paremeter will be ignored.   (optional)
custom_field_kind = 'custom_field_kind_example' # str | If a custom field is given then its kind must be given too to allow find it.  Possible values are: * contact: Contact fields. * contactInfo: Additional contact information fields. * custom_operation: Custom operation fields. * document: Document fields. * marketplace: Advertisements field. * record: Record fields. * transaction: Transaction fields. * user: User profile fields.  (optional)

try:
    # Lists temporary images related to the currently authenticated user or guest 
    api_response = api_instance.list_temp_images(fields=fields, target=target, guest_key=guest_key, user=user, custom_field=custom_field, custom_field_kind=custom_field_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->list_temp_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **target** | **str**| The possible targets for a temporary image Possible values are: * advertisement: The image will be used for an advertisement of a specific user * contactInfo: The image will be used for an additional contact information of a specific user * customValue: The image will be used for a value of a specific custom field * userProfile: The image will be used as a profile image for an existing user * userRegistration: The image will be used as a profile image for a newly registered user  | [optional] 
 **guest_key** | **str**| This parameter is only taken into account if the current request is running as guest. It is the key passed by the client when uploading images. If no key is given, images are matched by remote address.  | [optional] 
 **user** | **str**| If the target is &#x60;userProfile&#x60; or &#x60;advertisement&#x60;, must be either the id or an identification method of the target user (or advertisement owner).  | [optional] 
 **custom_field** | **str**| If the temp image will be used as the value of a custom field of type image then the corresponding custom field must be given (id or internal name). Otherwise this paremeter will be ignored.   | [optional] 
 **custom_field_kind** | **str**| If a custom field is given then its kind must be given too to allow find it.  Possible values are: * contact: Contact fields. * contactInfo: Additional contact information fields. * custom_operation: Custom operation fields. * document: Document fields. * marketplace: Advertisements field. * record: Record fields. * transaction: Transaction fields. * user: User profile fields.  | [optional] 

### Return type

[**list[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_images**
> list[Image] list_user_images(user, fields=fields, kind=kind)

Lists either `profile` or `custom` images for a given user  

Returns either `profile` or `custom` images for the given user. For `profile`, the user  must be visible by the authenticated user. Custom images are used in rich text content, not images for custom fields. For `custom`, the authenticated user must either be the owner or a manager (administrator or broker). 

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
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
kind = 'kind_example' # str | The kind of images to be returned.   The default value is `profile` Possible values are: * custom: User custom images are additional images that can be used on rich text contents. * profile: User profile images are those associated with the user profile. The first profile image is used to depict the user on search results.  (optional)

try:
    # Lists either `profile` or `custom` images for a given user  
    api_response = api_instance.list_user_images(user, fields=fields, kind=kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->list_user_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **kind** | **str**| The kind of images to be returned.   The default value is &#x60;profile&#x60; Possible values are: * custom: User custom images are additional images that can be used on rich text contents. * profile: User profile images are those associated with the user profile. The first profile image is used to depict the user on search results.  | [optional] 

### Return type

[**list[Image]**](Image.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_ad_images**
> reorder_ad_images(ad, ids)

Changes the order of the images of an advertisement  

The new order is defined by the list of ids, so that images appear in the same order as the ids. 

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
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
ids = ['ids_example'] # list[str] | The array of ids (comma-separated) reflecting the desired order

try:
    # Changes the order of the images of an advertisement  
    api_instance.reorder_ad_images(ad, ids)
except ApiException as e:
    print("Exception when calling ImagesApi->reorder_ad_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **ids** | [**list[str]**](str.md)| The array of ids (comma-separated) reflecting the desired order | 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_profile_images**
> reorder_profile_images(user, ids)

Changes the order of a user's profile images  

The new order is defined by the list of ids, so that images appear in the same order as the ids. 

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
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
ids = ['ids_example'] # list[str] | The array of ids (comma-separated) reflecting the desired order

try:
    # Changes the order of a user's profile images  
    api_instance.reorder_profile_images(user, ids)
except ApiException as e:
    print("Exception when calling ImagesApi->reorder_profile_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **ids** | [**list[str]**](str.md)| The array of ids (comma-separated) reflecting the desired order | 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_ad_image**
> str upload_ad_image(ad, image, name=name)

Adds a new image for the given advertisement. 

Uploads a new image for the given advertisement. 

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
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))
ad = 'ad_example' # str | Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form `productNumber@user`, with the user identifier as well.      
image = '/path/to/file.txt' # file | The image being uploaded
name = 'name_example' # str | The name for the new image. If not informed will fall back to the original file name in the form data  (optional)

try:
    # Adds a new image for the given advertisement. 
    api_response = api_instance.upload_ad_image(ad, image, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_ad_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad** | **str**| Can be either the advertisement internal identifier or, in case of webshop advertisements, can be the product number (if the owner is the logged user) or a string in the form &#x60;productNumber@user&#x60;, with the user identifier as well.       | 
 **image** | **file**| The image being uploaded | 
 **name** | **str**| The name for the new image. If not informed will fall back to the original file name in the form data  | [optional] 

### Return type

**str**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_contact_info_image**
> str upload_contact_info_image(id, image, name=name)

Uploads a new image for the given additional contact information. 

Saves the given image for the additional contact information. If the given additional contact information already has an image, the old one is removed, and the current image is saved in its place. 

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
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
image = '/path/to/file.txt' # file | The image being uploaded
name = 'name_example' # str | The name for the new image. If not informed will fall back to the original file name in the form data  (optional)

try:
    # Uploads a new image for the given additional contact information. 
    api_response = api_instance.upload_contact_info_image(id, image, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_contact_info_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **image** | **file**| The image being uploaded | 
 **name** | **str**| The name for the new image. If not informed will fall back to the original file name in the form data  | [optional] 

### Return type

**str**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_contact_info_image_deprecated**
> str upload_contact_info_image_deprecated(id, image, name=name)

This operation is deprecated, use `POST /contact-infos/{id}/image` instead.

Saves the given image for the additional contact information. If the given additional contact information already has an image, the old one is removed, and the current image is saved in its place. 

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
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification
image = '/path/to/file.txt' # file | The image being uploaded
name = 'name_example' # str | The name for the new image. If not informed will fall back to the original file name in the form data  (optional)

try:
    # This operation is deprecated, use `POST /contact-infos/{id}/image` instead.
    api_response = api_instance.upload_contact_info_image_deprecated(id, image, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_contact_info_image_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **image** | **file**| The image being uploaded | 
 **name** | **str**| The name for the new image. If not informed will fall back to the original file name in the form data  | [optional] 

### Return type

**str**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_temp_image**
> str upload_temp_image(image, name=name, target=target, guest_key=guest_key, user=user, custom_field=custom_field, custom_field_kind=custom_field_kind)

Adds a new temporary image for the currently authenticated user or guest. 

Uploads a new temporary image. A temporary image should be given a target, which can be: - `userRegistration`: The image will be used as a profile image for a newly registered user; - `userProfile`: The image will be used as a profile image for an existing user; - `advertisement`: The image will be used for an advertisement of a specific user; - `customValue`: The image will be used for a value of a specific custom field. Temporary images won't be immediately associated to the next registered model, but its `id`, which is returned by this operation, must be explicitly passed in, either as the `images` field (for profile or advertisement images) or in the `customValues` field of the model that has custom values (multiple ids can be passed-in as pipe-separated). Images as guest can only be uploaded if on the destination group products the image profile field is allowed at registrations. Users may upload images if they can register new users or create advertisements. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
image = '/path/to/file.txt' # file | The image being uploaded
name = 'name_example' # str | The name for the new image. If not informed will fall back to the original file name in the form data  (optional)
target = 'target_example' # str | The possible targets for a temporary image Possible values are: * advertisement: The image will be used for an advertisement of a specific user * contactInfo: The image will be used for an additional contact information of a specific user * customValue: The image will be used for a value of a specific custom field * userProfile: The image will be used as a profile image for an existing user * userRegistration: The image will be used as a profile image for a newly registered user  (optional)
guest_key = 'guest_key_example' # str | This parameter is only taken into account if the current request is running as guest. It should be a reasonably unique key (for example, an UUID, device identifier or a reasonably large random string) which uniquely identifies the uploaded image as belonging to this \"session\". If no key is given, images uploaded as guest are matched by IP address. Using a key is recommended, because clients that move between WiFi and mobile connection or if the client is in a network with multiple outbound IP addresses, images won't be correctly matched without a key.  (optional)
user = 'user_example' # str | If the target is `userProfile` or `advertisement`, must be either the id or an identification method of the target user (or advertisement owner).  (optional)
custom_field = 'custom_field_example' # str | If the temp image will be used as the value of a custom field of type image then the corresponding custom field must be given (id or internal name). Otherwise this paremeter will be ignored.   (optional)
custom_field_kind = 'custom_field_kind_example' # str | If a custom field is given then its kind must be given too to allow find it. Possible values are: * contact: Contact fields. * contactInfo: Additional contact information fields. * custom_operation: Custom operation fields. * document: Document fields. * marketplace: Advertisements field. * record: Record fields. * transaction: Transaction fields. * user: User profile fields.  (optional)

try:
    # Adds a new temporary image for the currently authenticated user or guest. 
    api_response = api_instance.upload_temp_image(image, name=name, target=target, guest_key=guest_key, user=user, custom_field=custom_field, custom_field_kind=custom_field_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_temp_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| The image being uploaded | 
 **name** | **str**| The name for the new image. If not informed will fall back to the original file name in the form data  | [optional] 
 **target** | **str**| The possible targets for a temporary image Possible values are: * advertisement: The image will be used for an advertisement of a specific user * contactInfo: The image will be used for an additional contact information of a specific user * customValue: The image will be used for a value of a specific custom field * userProfile: The image will be used as a profile image for an existing user * userRegistration: The image will be used as a profile image for a newly registered user  | [optional] 
 **guest_key** | **str**| This parameter is only taken into account if the current request is running as guest. It should be a reasonably unique key (for example, an UUID, device identifier or a reasonably large random string) which uniquely identifies the uploaded image as belonging to this \&quot;session\&quot;. If no key is given, images uploaded as guest are matched by IP address. Using a key is recommended, because clients that move between WiFi and mobile connection or if the client is in a network with multiple outbound IP addresses, images won&#39;t be correctly matched without a key.  | [optional] 
 **user** | **str**| If the target is &#x60;userProfile&#x60; or &#x60;advertisement&#x60;, must be either the id or an identification method of the target user (or advertisement owner).  | [optional] 
 **custom_field** | **str**| If the temp image will be used as the value of a custom field of type image then the corresponding custom field must be given (id or internal name). Otherwise this paremeter will be ignored.   | [optional] 
 **custom_field_kind** | **str**| If a custom field is given then its kind must be given too to allow find it. Possible values are: * contact: Contact fields. * contactInfo: Additional contact information fields. * custom_operation: Custom operation fields. * document: Document fields. * marketplace: Advertisements field. * record: Record fields. * transaction: Transaction fields. * user: User profile fields.  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_user_image**
> str upload_user_image(user, image, kind=kind, name=name)

Adds a new image for the given user. The image kind is either  `profile` or `custom`. 

Uploads a new image, either `profile` (by default) or `custom`, for the given user. Custom images are used in rich text content, not images for custom fields. For uploading images for custom field values, see the documentation for the operation at `POST /images/temp`. 

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
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
image = '/path/to/file.txt' # file | The image being uploaded
kind = 'kind_example' # str | The kind of images to be returned.   The default value is `profile` Possible values are: * custom: User custom images are additional images that can be used on rich text contents. * profile: User profile images are those associated with the user profile. The first profile image is used to depict the user on search results.  (optional)
name = 'name_example' # str | The name for the new image. If not informed will fall back to the original file name in the form data  (optional)

try:
    # Adds a new image for the given user. The image kind is either  `profile` or `custom`. 
    api_response = api_instance.upload_user_image(user, image, kind=kind, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->upload_user_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **image** | **file**| The image being uploaded | 
 **kind** | **str**| The kind of images to be returned.   The default value is &#x60;profile&#x60; Possible values are: * custom: User custom images are additional images that can be used on rich text contents. * profile: User profile images are those associated with the user profile. The first profile image is used to depict the user on search results.  | [optional] 
 **name** | **str**| The name for the new image. If not informed will fall back to the original file name in the form data  | [optional] 

### Return type

**str**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_image**
> ImageView view_image(id_or_key, fields=fields)

Returns an image details by id or key

Returns metadata about an image given its identifier or key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()
id_or_key = 'id_or_key_example' # str | The image id or file name
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns an image details by id or key
    api_response = api_instance.view_image(id_or_key, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->view_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_key** | **str**| The image id or file name | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**ImageView**](ImageView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

