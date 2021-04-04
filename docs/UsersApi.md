# swagger_client.UsersApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Registers a new user
[**get_data_for_edit_full_profile**](UsersApi.md#get_data_for_edit_full_profile) | **GET** /users/{user}/data-for-edit-profile | Returns data for editing the full profile at once
[**get_data_for_map_directory**](UsersApi.md#get_data_for_map_directory) | **GET** /users/map/data-for-search | Get configuration data for searching the user directory (map)
[**get_groups_for_user_registration**](UsersApi.md#get_groups_for_user_registration) | **GET** /users/groups-for-registration | Returns the groups the authenticated user or guest can register on
[**get_user_data_for_edit**](UsersApi.md#get_user_data_for_edit) | **GET** /users/{user}/data-for-edit | Get configuration data to edit a user profile
[**get_user_data_for_new**](UsersApi.md#get_user_data_for_new) | **GET** /users/data-for-new | Get configuration data for registering new users
[**get_user_data_for_search**](UsersApi.md#get_user_data_for_search) | **GET** /users/data-for-search | Get configuration data for searching users
[**save_user_full_profile**](UsersApi.md#save_user_full_profile) | **POST** /users/{user}/profile | Edits the full profile at once
[**search_map_directory**](UsersApi.md#search_map_directory) | **GET** /users/map | Search the user directory (map)
[**search_users**](UsersApi.md#search_users) | **GET** /users | Search for users
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{user} | Save a user details
[**validate_email_change**](UsersApi.md#validate_email_change) | **POST** /users/validate/email-change/{key} | Validates an e-mail via a validation key
[**validate_user_registration**](UsersApi.md#validate_user_registration) | **POST** /users/validate/registration/{key} | Validates an user registration via a key sent by e-mail
[**validate_user_registration_field**](UsersApi.md#validate_user_registration_field) | **GET** /users/validate/{group}/{field} | Validates the value of a single field for user registration
[**view_user**](UsersApi.md#view_user) | **GET** /users/{user} | View a user details


# **create_user**
> UserRegistrationResult create_user(body)

Registers a new user

Can either be a public registration, requiring no authorization, or a user registration by an administrator or broker. The public registration normally requires a CAPTCHA challenge to prevent bots. On user registration the following data is also created:  * Address;  * Mobile phone;  * Landline phone;  * Images.   After the registration those data are managed separately than the user profile data.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.UserNew() # UserNew | The user to be registered

try:
    # Registers a new user
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserNew**](UserNew.md)| The user to be registered | 

### Return type

[**UserRegistrationResult**](UserRegistrationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_for_edit_full_profile**
> DataForEditFullProfile get_data_for_edit_full_profile(user, fields=fields)

Returns data for editing the full profile at once

The returned data contains all profile-related entities: such as profile fields, phones, addresses, images and additional contact information 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data for editing the full profile at once
    api_response = api_instance.get_data_for_edit_full_profile(user, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_data_for_edit_full_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**DataForEditFullProfile**](DataForEditFullProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_for_map_directory**
> UserDataForMap get_data_for_map_directory(fields=fields)

Get configuration data for searching the user directory (map)

Returns data with the current configuration regarding the user  directory (map) 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Get configuration data for searching the user directory (map)
    api_response = api_instance.get_data_for_map_directory(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_data_for_map_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**UserDataForMap**](UserDataForMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_for_user_registration**
> list[GroupForRegistration] get_groups_for_user_registration(fields=fields, as_member=as_member)

Returns the groups the authenticated user or guest can register on

Returns the list of groups the authenticated user can use to perform a new user registration. If authenticated as guest, will return the groups currently set for public registration. When there is an authenticated administrator, broker or member, will be the configured groups for new users. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
as_member = true # bool | Flag required only when the authenticated user is a member and a broker, in that case we need to distingish between both. If true then the groups returned will be those allowed as member, otherwise will return the goups allowed as broker.    (optional)

try:
    # Returns the groups the authenticated user or guest can register on
    api_response = api_instance.get_groups_for_user_registration(fields=fields, as_member=as_member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_groups_for_user_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **as_member** | **bool**| Flag required only when the authenticated user is a member and a broker, in that case we need to distingish between both. If true then the groups returned will be those allowed as member, otherwise will return the goups allowed as broker.    | [optional] 

### Return type

[**list[GroupForRegistration]**](GroupForRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_data_for_edit**
> UserDataForEdit get_user_data_for_edit(user, fields=fields)

Get configuration data to edit a user profile

Returns data to edit a user profile. 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Get configuration data to edit a user profile
    api_response = api_instance.get_user_data_for_edit(user, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_data_for_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**UserDataForEdit**](UserDataForEdit.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_data_for_new**
> UserDataForNew get_user_data_for_new(group, fields=fields, as_member=as_member)

Get configuration data for registering new users

Almost every aspect of a user profile is configurable in Cyclos, such as enabled basic profile fields, custom profile fields, address fields, phone configuration and so on. As such, if a front-end needs to be robust to such a dynamic nature, it should get this information in order to create a correct registration form.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
group = 'group_example' # str | The intial group for the new user
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
as_member = true # bool | Flag required only when the authenticated user is a member and a broker, in that case we need to distingish between both. If true then the configuration data for registering new users as member will be returned, otherwise will return the configuration data for registering as broker.            (optional)

try:
    # Get configuration data for registering new users
    api_response = api_instance.get_user_data_for_new(group, fields=fields, as_member=as_member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_data_for_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The intial group for the new user | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **as_member** | **bool**| Flag required only when the authenticated user is a member and a broker, in that case we need to distingish between both. If true then the configuration data for registering new users as member will be returned, otherwise will return the configuration data for registering as broker.            | [optional] 

### Return type

[**UserDataForNew**](UserDataForNew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_data_for_search**
> UserDataForSearch get_user_data_for_search(fields=fields)

Get configuration data for searching users

Returns data with the current configuration regarding the user search 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Get configuration data for searching users
    api_response = api_instance.get_user_data_for_search(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_data_for_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**UserDataForSearch**](UserDataForSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_user_full_profile**
> FullProfileEditResult save_user_full_profile(user, body, fields=fields, confirmation_password=confirmation_password)

Edits the full profile at once

Saves in a single, transactional operation, the full user profile, that is: allows saving the basic fields and creating / modifying / removing phones, addresses, additional contacts and images at once. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
body = swagger_client.FullProfileEdit() # FullProfileEdit | The full profile data
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Edits the full profile at once
    api_response = api_instance.save_user_full_profile(user, body, fields=fields, confirmation_password=confirmation_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->save_user_full_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **body** | [**FullProfileEdit**](FullProfileEdit.md)| The full profile data | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

[**FullProfileEditResult**](FullProfileEditResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_map_directory**
> list[UserResult] search_map_directory(fields=fields, activation_period=activation_period, address_result=address_result, brokers=brokers, creation_period=creation_period, exclude_contacts=exclude_contacts, groups=groups, ignore_profile_fields_in_list=ignore_profile_fields_in_list, include_group=include_group, include_group_set=include_group_set, keywords=keywords, last_login_period=last_login_period, latitude=latitude, longitude=longitude, main_broker_only=main_broker_only, max_distance=max_distance, order_by=order_by, page=page, page_size=page_size, profile_fields=profile_fields, roles=roles, statuses=statuses, users_to_exclude=users_to_exclude, users_to_include=users_to_include)

Search the user directory (map)

Returns a page of users in the map directory that match a given criteria 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
activation_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user activation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
address_result = 'address_result_example' # str | Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (`latitude` and `longitude`) * none: Addresses are not returned. * primary: The primary (default) user address is returned  (optional)
brokers = ['brokers_example'] # list[str] | Either id or a principal (login name, e-mail, etc) for brokers  (optional)
creation_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user creation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
exclude_contacts = true # bool | When set to `true` will not return any user that is already a contact of the currently authenticated user.  (optional)
groups = ['groups_example'] # list[str] | Either id or internal names of groups / group sets  (optional)
ignore_profile_fields_in_list = true # bool | When set to `true`, instead of returning users with corresponding profile fields set on list, will return them with `display` and `shortDisplay`.   (optional)
include_group = true # bool | When set to `true` and the logged user has permission to view user groups, will return the `group` property on users.   (optional)
include_group_set = true # bool | When set to `true` and the logged user has permission to view user group sets, will return the `groupSet` property on users.   (optional)
keywords = 'keywords_example' # str | Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  (optional)
last_login_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user last login date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
latitude = 1.2 # float | The reference latitude for distance searches  (optional)
longitude = 1.2 # float | The reference longitude for distance searches  (optional)
main_broker_only = true # bool | When set to `true`, will match only users that have the brokers as set in the `brokers` parameter as main broker.   (optional)
max_distance = 1.2 # float | Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both `longitude` and `latitude` parameters are passed with the actual reference position.  (optional)
order_by = 'order_by_example' # str | Possible options for ordering the results of an user search. Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * creationDate: Newly registered users are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * random: Users will be randomly returned * relevance: This is the default if keywords are used. Best matching users come first.  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
profile_fields = ['profile_fields_example'] # list[str] | User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, `profileFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, `profileFields=field1:valueA|valueB`. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `profileFields=rank:bronze|silver,birthDate:2000-01-01|2001-12-31` would match results whose custom field with internal name 'rank' is either bronze or silver, and whose 'birthDate' is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `profileFields=birthDate:|2001-12-31`. The basic profile fields have one of the following identifiers: * `name` or `fullName`: Full name; * `username`, `loginName` or `login`: Login name; * `email`: E-mail; * `phone`: Phone; * `accountNumber`, `account`: Account number; * `image`: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the `addressFieldsInSearch` field in the corresponding result from a data-for-search request.  The specific address fields are: * `address`: Searches on any address field (not a specific field); * `address.address`: Searches on the fields that represent the   street address, which are `addressLine1`,    `addressLine2`,   `street`,   `buildingNumber` and   `complement`. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * `address.zip`: Searches for matching zip (postal) code; * `address.poBox`: Searches for matching postal box; * `address.neighborhood`: Searches by neighborhood; * `address.city`: Searches by city; * `address.region`: Searches by region (or state); * `address.country`: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `profileFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `profileFields=dynamic:'business`.  (optional)
roles = ['roles_example'] # list[str] | The main role the user has. Possible values for each array element are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \"sub-user\" created by a member to manage his data.  (optional)
statuses = ['statuses_example'] # list[str] | The possible statuses for an user Possible values for each array element are: * active: The user is active and can use the system normally. * blocked: The user has been blocked from accessing the system. Other users still see him/her. * disabled: The user has been disabled - he/she cannot access the system and is invisible by other users. * pending: The user registration is pending a confirmation. Probably the user has received an e-mail with a link that must be followed to complete the activation. The user is invisible by other users. * purged: The user was permanently removed and had all his private data removed. Only transactions are kept for historical reasons. * removed: The user was permanently removed. It's profile is kept for historical purposes.  (optional)
users_to_exclude = ['users_to_exclude_example'] # list[str] | Indicated the users to be excluded from the result  (optional)
users_to_include = ['users_to_include_example'] # list[str] | Indicated the users to be included in the result.  Any other user not present in this list will be excluded from the result.  (optional)

try:
    # Search the user directory (map)
    api_response = api_instance.search_map_directory(fields=fields, activation_period=activation_period, address_result=address_result, brokers=brokers, creation_period=creation_period, exclude_contacts=exclude_contacts, groups=groups, ignore_profile_fields_in_list=ignore_profile_fields_in_list, include_group=include_group, include_group_set=include_group_set, keywords=keywords, last_login_period=last_login_period, latitude=latitude, longitude=longitude, main_broker_only=main_broker_only, max_distance=max_distance, order_by=order_by, page=page, page_size=page_size, profile_fields=profile_fields, roles=roles, statuses=statuses, users_to_exclude=users_to_exclude, users_to_include=users_to_include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->search_map_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **activation_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user activation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **address_result** | **str**| Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (&#x60;latitude&#x60; and &#x60;longitude&#x60;) * none: Addresses are not returned. * primary: The primary (default) user address is returned  | [optional] 
 **brokers** | [**list[str]**](str.md)| Either id or a principal (login name, e-mail, etc) for brokers  | [optional] 
 **creation_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user creation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **exclude_contacts** | **bool**| When set to &#x60;true&#x60; will not return any user that is already a contact of the currently authenticated user.  | [optional] 
 **groups** | [**list[str]**](str.md)| Either id or internal names of groups / group sets  | [optional] 
 **ignore_profile_fields_in_list** | **bool**| When set to &#x60;true&#x60;, instead of returning users with corresponding profile fields set on list, will return them with &#x60;display&#x60; and &#x60;shortDisplay&#x60;.   | [optional] 
 **include_group** | **bool**| When set to &#x60;true&#x60; and the logged user has permission to view user groups, will return the &#x60;group&#x60; property on users.   | [optional] 
 **include_group_set** | **bool**| When set to &#x60;true&#x60; and the logged user has permission to view user group sets, will return the &#x60;groupSet&#x60; property on users.   | [optional] 
 **keywords** | **str**| Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  | [optional] 
 **last_login_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user last login date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **latitude** | **float**| The reference latitude for distance searches  | [optional] 
 **longitude** | **float**| The reference longitude for distance searches  | [optional] 
 **main_broker_only** | **bool**| When set to &#x60;true&#x60;, will match only users that have the brokers as set in the &#x60;brokers&#x60; parameter as main broker.   | [optional] 
 **max_distance** | **float**| Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both &#x60;longitude&#x60; and &#x60;latitude&#x60; parameters are passed with the actual reference position.  | [optional] 
 **order_by** | **str**| Possible options for ordering the results of an user search. Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * creationDate: Newly registered users are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * random: Users will be randomly returned * relevance: This is the default if keywords are used. Best matching users come first.  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **profile_fields** | [**list[str]**](str.md)| User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, &#x60;profileFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, &#x60;profileFields&#x3D;field1:valueA|valueB&#x60;. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;profileFields&#x3D;rank:bronze|silver,birthDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#39;rank&#39; is either bronze or silver, and whose &#39;birthDate&#39; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;profileFields&#x3D;birthDate:|2001-12-31&#x60;. The basic profile fields have one of the following identifiers: * &#x60;name&#x60; or &#x60;fullName&#x60;: Full name; * &#x60;username&#x60;, &#x60;loginName&#x60; or &#x60;login&#x60;: Login name; * &#x60;email&#x60;: E-mail; * &#x60;phone&#x60;: Phone; * &#x60;accountNumber&#x60;, &#x60;account&#x60;: Account number; * &#x60;image&#x60;: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the &#x60;addressFieldsInSearch&#x60; field in the corresponding result from a data-for-search request.  The specific address fields are: * &#x60;address&#x60;: Searches on any address field (not a specific field); * &#x60;address.address&#x60;: Searches on the fields that represent the   street address, which are &#x60;addressLine1&#x60;,    &#x60;addressLine2&#x60;,   &#x60;street&#x60;,   &#x60;buildingNumber&#x60; and   &#x60;complement&#x60;. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * &#x60;address.zip&#x60;: Searches for matching zip (postal) code; * &#x60;address.poBox&#x60;: Searches for matching postal box; * &#x60;address.neighborhood&#x60;: Searches by neighborhood; * &#x60;address.city&#x60;: Searches by city; * &#x60;address.region&#x60;: Searches by region (or state); * &#x60;address.country&#x60;: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: &#x60;profileFields&#x3D;dynamic:a|b|c&#x60;. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: &#x60;profileFields&#x3D;dynamic:&#39;business&#x60;.  | [optional] 
 **roles** | [**list[str]**](str.md)| The main role the user has. Possible values for each array element are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \&quot;sub-user\&quot; created by a member to manage his data.  | [optional] 
 **statuses** | [**list[str]**](str.md)| The possible statuses for an user Possible values for each array element are: * active: The user is active and can use the system normally. * blocked: The user has been blocked from accessing the system. Other users still see him/her. * disabled: The user has been disabled - he/she cannot access the system and is invisible by other users. * pending: The user registration is pending a confirmation. Probably the user has received an e-mail with a link that must be followed to complete the activation. The user is invisible by other users. * purged: The user was permanently removed and had all his private data removed. Only transactions are kept for historical reasons. * removed: The user was permanently removed. It&#39;s profile is kept for historical purposes.  | [optional] 
 **users_to_exclude** | [**list[str]**](str.md)| Indicated the users to be excluded from the result  | [optional] 
 **users_to_include** | [**list[str]**](str.md)| Indicated the users to be included in the result.  Any other user not present in this list will be excluded from the result.  | [optional] 

### Return type

[**list[UserResult]**](UserResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> list[UserResult] search_users(fields=fields, activation_period=activation_period, address_result=address_result, brokers=brokers, creation_period=creation_period, exclude_contacts=exclude_contacts, groups=groups, ignore_profile_fields_in_list=ignore_profile_fields_in_list, include_group=include_group, include_group_set=include_group_set, keywords=keywords, last_login_period=last_login_period, latitude=latitude, longitude=longitude, main_broker_only=main_broker_only, max_distance=max_distance, order_by=order_by, page=page, page_size=page_size, profile_fields=profile_fields, roles=roles, statuses=statuses, users_to_exclude=users_to_exclude, users_to_include=users_to_include)

Search for users

Returns a page of users that match a given criteria. The fields returned depend on the products, in the profile fields of other users setting. Only fields (both basic or custom) marked to be returned on user list are returned. If no fields are set to be returned, or if the `ignoreProfileFieldsInList` flag is true in the given query then the resulting objects will have the `display` and `shortDisplay` filled in.  However, those fields are not returned when another profile field is returned, preventing duplicated data to be returned.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
activation_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user activation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
address_result = 'address_result_example' # str | Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (`latitude` and `longitude`) * none: Addresses are not returned. * primary: The primary (default) user address is returned  (optional)
brokers = ['brokers_example'] # list[str] | Either id or a principal (login name, e-mail, etc) for brokers  (optional)
creation_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user creation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
exclude_contacts = true # bool | When set to `true` will not return any user that is already a contact of the currently authenticated user.  (optional)
groups = ['groups_example'] # list[str] | Either id or internal names of groups / group sets  (optional)
ignore_profile_fields_in_list = true # bool | When set to `true`, instead of returning users with corresponding profile fields set on list, will return them with `display` and `shortDisplay`.   (optional)
include_group = true # bool | When set to `true` and the logged user has permission to view user groups, will return the `group` property on users.   (optional)
include_group_set = true # bool | When set to `true` and the logged user has permission to view user group sets, will return the `groupSet` property on users.   (optional)
keywords = 'keywords_example' # str | Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  (optional)
last_login_period = ['2013-10-20T19:20:30+01:00'] # list[datetime] | The minimum / maximum user last login date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  (optional)
latitude = 1.2 # float | The reference latitude for distance searches  (optional)
longitude = 1.2 # float | The reference longitude for distance searches  (optional)
main_broker_only = true # bool | When set to `true`, will match only users that have the brokers as set in the `brokers` parameter as main broker.   (optional)
max_distance = 1.2 # float | Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both `longitude` and `latitude` parameters are passed with the actual reference position.  (optional)
order_by = 'order_by_example' # str | Possible options for ordering the results of an user search. Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * creationDate: Newly registered users are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * random: Users will be randomly returned * relevance: This is the default if keywords are used. Best matching users come first.  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)
profile_fields = ['profile_fields_example'] # list[str] | User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, `profileFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, `profileFields=field1:valueA|valueB`. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `profileFields=rank:bronze|silver,birthDate:2000-01-01|2001-12-31` would match results whose custom field with internal name 'rank' is either bronze or silver, and whose 'birthDate' is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `profileFields=birthDate:|2001-12-31`. The basic profile fields have one of the following identifiers: * `name` or `fullName`: Full name; * `username`, `loginName` or `login`: Login name; * `email`: E-mail; * `phone`: Phone; * `accountNumber`, `account`: Account number; * `image`: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the `addressFieldsInSearch` field in the corresponding result from a data-for-search request.  The specific address fields are: * `address`: Searches on any address field (not a specific field); * `address.address`: Searches on the fields that represent the   street address, which are `addressLine1`,    `addressLine2`,   `street`,   `buildingNumber` and   `complement`. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * `address.zip`: Searches for matching zip (postal) code; * `address.poBox`: Searches for matching postal box; * `address.neighborhood`: Searches by neighborhood; * `address.city`: Searches by city; * `address.region`: Searches by region (or state); * `address.country`: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `profileFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `profileFields=dynamic:'business`.  (optional)
roles = ['roles_example'] # list[str] | The main role the user has. Possible values for each array element are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \"sub-user\" created by a member to manage his data.  (optional)
statuses = ['statuses_example'] # list[str] | The possible statuses for an user Possible values for each array element are: * active: The user is active and can use the system normally. * blocked: The user has been blocked from accessing the system. Other users still see him/her. * disabled: The user has been disabled - he/she cannot access the system and is invisible by other users. * pending: The user registration is pending a confirmation. Probably the user has received an e-mail with a link that must be followed to complete the activation. The user is invisible by other users. * purged: The user was permanently removed and had all his private data removed. Only transactions are kept for historical reasons. * removed: The user was permanently removed. It's profile is kept for historical purposes.  (optional)
users_to_exclude = ['users_to_exclude_example'] # list[str] | Indicated the users to be excluded from the result  (optional)
users_to_include = ['users_to_include_example'] # list[str] | Indicated the users to be included in the result.  Any other user not present in this list will be excluded from the result.  (optional)

try:
    # Search for users
    api_response = api_instance.search_users(fields=fields, activation_period=activation_period, address_result=address_result, brokers=brokers, creation_period=creation_period, exclude_contacts=exclude_contacts, groups=groups, ignore_profile_fields_in_list=ignore_profile_fields_in_list, include_group=include_group, include_group_set=include_group_set, keywords=keywords, last_login_period=last_login_period, latitude=latitude, longitude=longitude, main_broker_only=main_broker_only, max_distance=max_distance, order_by=order_by, page=page, page_size=page_size, profile_fields=profile_fields, roles=roles, statuses=statuses, users_to_exclude=users_to_exclude, users_to_include=users_to_include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **activation_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user activation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **address_result** | **str**| Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (&#x60;latitude&#x60; and &#x60;longitude&#x60;) * none: Addresses are not returned. * primary: The primary (default) user address is returned  | [optional] 
 **brokers** | [**list[str]**](str.md)| Either id or a principal (login name, e-mail, etc) for brokers  | [optional] 
 **creation_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user creation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **exclude_contacts** | **bool**| When set to &#x60;true&#x60; will not return any user that is already a contact of the currently authenticated user.  | [optional] 
 **groups** | [**list[str]**](str.md)| Either id or internal names of groups / group sets  | [optional] 
 **ignore_profile_fields_in_list** | **bool**| When set to &#x60;true&#x60;, instead of returning users with corresponding profile fields set on list, will return them with &#x60;display&#x60; and &#x60;shortDisplay&#x60;.   | [optional] 
 **include_group** | **bool**| When set to &#x60;true&#x60; and the logged user has permission to view user groups, will return the &#x60;group&#x60; property on users.   | [optional] 
 **include_group_set** | **bool**| When set to &#x60;true&#x60; and the logged user has permission to view user group sets, will return the &#x60;groupSet&#x60; property on users.   | [optional] 
 **keywords** | **str**| Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.  | [optional] 
 **last_login_period** | [**list[datetime]**](datetime.md)| The minimum / maximum user last login date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
 **latitude** | **float**| The reference latitude for distance searches  | [optional] 
 **longitude** | **float**| The reference longitude for distance searches  | [optional] 
 **main_broker_only** | **bool**| When set to &#x60;true&#x60;, will match only users that have the brokers as set in the &#x60;brokers&#x60; parameter as main broker.   | [optional] 
 **max_distance** | **float**| Maximum straight-line distance between the informed location and the resulting address. Is measured either in kilometers or miles, depending on the configuration. Only accepted if both &#x60;longitude&#x60; and &#x60;latitude&#x60; parameters are passed with the actual reference position.  | [optional] 
 **order_by** | **str**| Possible options for ordering the results of an user search. Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * creationDate: Newly registered users are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * random: Users will be randomly returned * relevance: This is the default if keywords are used. Best matching users come first.  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 
 **profile_fields** | [**list[str]**](str.md)| User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, &#x60;profileFields&#x3D;field1:value1,field2:value2&#x60;. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, &#x60;profileFields&#x3D;field1:valueA|valueB&#x60;. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, &#x60;profileFields&#x3D;rank:bronze|silver,birthDate:2000-01-01|2001-12-31&#x60; would match results whose custom field with internal name &#39;rank&#39; is either bronze or silver, and whose &#39;birthDate&#39; is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like &#x60;profileFields&#x3D;birthDate:|2001-12-31&#x60;. The basic profile fields have one of the following identifiers: * &#x60;name&#x60; or &#x60;fullName&#x60;: Full name; * &#x60;username&#x60;, &#x60;loginName&#x60; or &#x60;login&#x60;: Login name; * &#x60;email&#x60;: E-mail; * &#x60;phone&#x60;: Phone; * &#x60;accountNumber&#x60;, &#x60;account&#x60;: Account number; * &#x60;image&#x60;: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the &#x60;addressFieldsInSearch&#x60; field in the corresponding result from a data-for-search request.  The specific address fields are: * &#x60;address&#x60;: Searches on any address field (not a specific field); * &#x60;address.address&#x60;: Searches on the fields that represent the   street address, which are &#x60;addressLine1&#x60;,    &#x60;addressLine2&#x60;,   &#x60;street&#x60;,   &#x60;buildingNumber&#x60; and   &#x60;complement&#x60;. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * &#x60;address.zip&#x60;: Searches for matching zip (postal) code; * &#x60;address.poBox&#x60;: Searches for matching postal box; * &#x60;address.neighborhood&#x60;: Searches by neighborhood; * &#x60;address.city&#x60;: Searches by city; * &#x60;address.region&#x60;: Searches by region (or state); * &#x60;address.country&#x60;: Searches by ISO 3166-1 alpha-2 country code.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: &#x60;profileFields&#x3D;dynamic:a|b|c&#x60;. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: &#x60;profileFields&#x3D;dynamic:&#39;business&#x60;.  | [optional] 
 **roles** | [**list[str]**](str.md)| The main role the user has. Possible values for each array element are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \&quot;sub-user\&quot; created by a member to manage his data.  | [optional] 
 **statuses** | [**list[str]**](str.md)| The possible statuses for an user Possible values for each array element are: * active: The user is active and can use the system normally. * blocked: The user has been blocked from accessing the system. Other users still see him/her. * disabled: The user has been disabled - he/she cannot access the system and is invisible by other users. * pending: The user registration is pending a confirmation. Probably the user has received an e-mail with a link that must be followed to complete the activation. The user is invisible by other users. * purged: The user was permanently removed and had all his private data removed. Only transactions are kept for historical reasons. * removed: The user was permanently removed. It&#39;s profile is kept for historical purposes.  | [optional] 
 **users_to_exclude** | [**list[str]**](str.md)| Indicated the users to be excluded from the result  | [optional] 
 **users_to_include** | [**list[str]**](str.md)| Indicated the users to be included in the result.  Any other user not present in this list will be excluded from the result.  | [optional] 

### Return type

[**list[UserResult]**](UserResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(user, body, confirmation_password=confirmation_password)

Save a user details

Saves the user profile. Only the basic fields (full name, login name, e-mail) and custom fields can be saved with this operation. Addresses, phones and images must be managed through their own paths. 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
body = swagger_client.UserEdit() # UserEdit | The user to be saved
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Save a user details
    api_instance.update_user(user, body, confirmation_password=confirmation_password)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **body** | [**UserEdit**](UserEdit.md)| The user to be saved | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_email_change**
> str validate_email_change(key)

Validates an e-mail via a validation key

When the user e-mail is changed, and the configuration enables the validation, an e-mail is sent to the new user e-mail, with a link to verify it. In this case, only after verifying the new e-mail it is effectively set as the new e-mail. This operation effectively verifies the new e-mail. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
key = 'key_example' # str | The validation key sent via e-mail

try:
    # Validates an e-mail via a validation key
    api_response = api_instance.validate_email_change(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->validate_email_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The validation key sent via e-mail | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_user_registration**
> UserRegistrationResult validate_user_registration(key, fields=fields)

Validates an user registration via a key sent by e-mail

When a user is registered, and the configuration enables the validation, an e-mail is sent to user e-mail, with a link to verify it. In this case, only after verifying the e-mail the user is activated. This operation effectively verifies the e-mail and performs the user activation. However, depending on the settings, the initial user status might be blocked or inactive.   

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
key = 'key_example' # str | The validation key sent via e-mail
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Validates an user registration via a key sent by e-mail
    api_response = api_instance.validate_user_registration(key, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->validate_user_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The validation key sent via e-mail | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**UserRegistrationResult**](UserRegistrationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_user_registration_field**
> str validate_user_registration_field(group, field, value, as_member=as_member)

Validates the value of a single field for user registration

Validates the value of a field which will be used for registering a user, returning either `204 No Content` if the field is valid or `200` with the error description if the field is invalid. Notice that the result is the validation error. If a `422` status code is returned it means that either the given `field` is invalid or the given `value` is empty. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
group = 'group_example' # str | The internal name or id of the group in which the user is being registered  
field = 'field_example' # str | One of: `name` (full name), `username` (login name), `email`, `mobilePhone`, `landLinePhone` or the internal name of a custom field.  
value = 'value_example' # str | The value to be validated
as_member = true # bool | Flag required only when the authenticated user is a member and a broker, in that case we need to distingish between both. If true then the groups returned will be those allowed as member, otherwise will return the goups allowed as broker.    (optional)

try:
    # Validates the value of a single field for user registration
    api_response = api_instance.validate_user_registration_field(group, field, value, as_member=as_member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->validate_user_registration_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The internal name or id of the group in which the user is being registered   | 
 **field** | **str**| One of: &#x60;name&#x60; (full name), &#x60;username&#x60; (login name), &#x60;email&#x60;, &#x60;mobilePhone&#x60;, &#x60;landLinePhone&#x60; or the internal name of a custom field.   | 
 **value** | **str**| The value to be validated | 
 **as_member** | **bool**| Flag required only when the authenticated user is a member and a broker, in that case we need to distingish between both. If true then the groups returned will be those allowed as member, otherwise will return the goups allowed as broker.    | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_user**
> UserView view_user(user, fields=fields)

View a user details

Returns the profile information of a user / operator. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user = 'user_example' # str | Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, `'1234567890`;     * `self` for the currently authenticated user. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # View a user details
    api_response = api_instance.view_user(user, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->view_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Can be one of: * a user identification value, such as id, username, e-mail, phone, etc.   Id is always allowed, others depend on Cyclos configuration. Note that   a valid numeric value is always considered as id. For example, when   using another identification method that can be numeric only, prefix   the value with a single quote (like in Excel spreadsheets), for   example, &#x60;&#39;1234567890&#x60;;     * &#x60;self&#x60; for the currently authenticated user.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**UserView**](UserView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

