# swagger_client.NFCApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_nfc**](NFCApi.md#cancel_nfc) | **POST** /nfc/cancel | Cancels a NFC tag
[**get_nfc_data_for_initialize**](NFCApi.md#get_nfc_data_for_initialize) | **GET** /nfc/data-for-initialize | Returns data for NFC tag initialization. Optionally the user can personalize the tag too.
[**get_nfc_data_for_personalize**](NFCApi.md#get_nfc_data_for_personalize) | **GET** /nfc/data-for-personalize | Returns data for perfornalizing an initialized NFC tag for a user
[**get_nfc_token**](NFCApi.md#get_nfc_token) | **GET** /nfc/{tokenType}/{value} | Retrieve the NFC token detailed data
[**get_otp_for_personalize_nfc**](NFCApi.md#get_otp_for_personalize_nfc) | **POST** /nfc/personalize/otp | Generates a new One-Time-Password (OTP) for a personalizing a NFC tag 
[**initialize_nfc**](NFCApi.md#initialize_nfc) | **POST** /nfc/initialize | Initializes a NFC tag
[**nfc_external_auth**](NFCApi.md#nfc_external_auth) | **POST** /nfc/external-auth | NFC external authentication
[**personalize_nfc**](NFCApi.md#personalize_nfc) | **POST** /nfc/personalize | Personalizes a NFC tag


# **cancel_nfc**
> cancel_nfc(params)

Cancels a NFC tag

Cancels a NFC token. Must be authenticated as a manager (administrator / broker) of the token owner, and have the correct permission.  

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
api_instance = swagger_client.NFCApi(swagger_client.ApiClient(configuration))
params = swagger_client.NfcTokenParameter() # NfcTokenParameter | The parameters for canceling. 

try:
    # Cancels a NFC tag
    api_instance.cancel_nfc(params)
except ApiException as e:
    print("Exception when calling NFCApi->cancel_nfc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**NfcTokenParameter**](NfcTokenParameter.md)| The parameters for canceling.  | 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfc_data_for_initialize**
> NfcDataForInitialize get_nfc_data_for_initialize(fields=fields)

Returns data for NFC tag initialization. Optionally the user can personalize the tag too.

Returns data with the NFC token types the authenticated user can use to initialize NFC tags. 

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
api_instance = swagger_client.NFCApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data for NFC tag initialization. Optionally the user can personalize the tag too.
    api_response = api_instance.get_nfc_data_for_initialize(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFCApi->get_nfc_data_for_initialize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**NfcDataForInitialize**](NfcDataForInitialize.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfc_data_for_personalize**
> NfcDataForPersonalize get_nfc_data_for_personalize(token_type, user, fields=fields)

Returns data for perfornalizing an initialized NFC tag for a user

Returns data for personalizing a NFC tag for a given user. 

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
api_instance = swagger_client.NFCApi(swagger_client.ApiClient(configuration))
token_type = 'token_type_example' # str | The token type reference (id or internal name) of the token principal type, which is stored on the NFC card being personalized.  
user = 'user_example' # str | The user reference (id or an identification method) of the user to whom the NFC tag will be personalized. When authenticated as a manager of that user (administrator or broker) no confirmation password will be required for the personalization. However, if the authenticated user is not a manager, the user will be required a confirmation password. 
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data for perfornalizing an initialized NFC tag for a user
    api_response = api_instance.get_nfc_data_for_personalize(token_type, user, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFCApi->get_nfc_data_for_personalize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type** | **str**| The token type reference (id or internal name) of the token principal type, which is stored on the NFC card being personalized.   | 
 **user** | **str**| The user reference (id or an identification method) of the user to whom the NFC tag will be personalized. When authenticated as a manager of that user (administrator or broker) no confirmation password will be required for the personalization. However, if the authenticated user is not a manager, the user will be required a confirmation password.  | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**NfcDataForPersonalize**](NfcDataForPersonalize.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfc_token**
> TokenDetailed get_nfc_token(token_type, value)

Retrieve the NFC token detailed data

Returns the token's data and the user owner of the token (i.e the assigned user, if any)

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
api_instance = swagger_client.NFCApi(swagger_client.ApiClient(configuration))
token_type = 'token_type_example' # str | The internal name or id of the token type
value = 'value_example' # str | The token value

try:
    # Retrieve the NFC token detailed data
    api_response = api_instance.get_nfc_token(token_type, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFCApi->get_nfc_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_type** | **str**| The internal name or id of the token type | 
 **value** | **str**| The token value | 

### Return type

[**TokenDetailed**](TokenDetailed.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_otp_for_personalize_nfc**
> get_otp_for_personalize_nfc(medium, params)

Generates a new One-Time-Password (OTP) for a personalizing a NFC tag 

Sends a new OTP for the customer which will own the NFC tag. The OTP belongs to the NFC tag owner, not the authenticated user. 

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
api_instance = swagger_client.NFCApi(swagger_client.ApiClient(configuration))
medium = 'medium_example' # str | The medium the user wants to receive the otp Possible values are: * email: The user will receive an email with the information * sms: The user will receive a sms with the information (only if there is at least one phone enabled for sms) 
params = swagger_client.NfcPersonalizeOtpParameter() # NfcPersonalizeOtpParameter | The parameters identifying the token and the user

try:
    # Generates a new One-Time-Password (OTP) for a personalizing a NFC tag 
    api_instance.get_otp_for_personalize_nfc(medium, params)
except ApiException as e:
    print("Exception when calling NFCApi->get_otp_for_personalize_nfc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium** | **str**| The medium the user wants to receive the otp Possible values are: * email: The user will receive an email with the information * sms: The user will receive a sms with the information (only if there is at least one phone enabled for sms)  | 
 **params** | [**NfcPersonalizeOtpParameter**](NfcPersonalizeOtpParameter.md)| The parameters identifying the token and the user | 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_nfc**
> NfcInitializeResult initialize_nfc(params)

Initializes a NFC tag

Initializes a NFC tag, creating a new `token` in Cyclos. Returns the keys (PICC Master Key, Application Master Key and the Operational Key) to be stored on the NFC tag. 

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
api_instance = swagger_client.NFCApi(swagger_client.ApiClient(configuration))
params = swagger_client.NfcInitializeParameter() # NfcInitializeParameter | The parameters for initializing the NFC tag. If the `user` value is left blank, the NFC tag will be only initialized, but not personalized (assigned to any user). If a user is given, the permission to personalize is required (besides the permission to initialize), and is a shortcut to initializing and later personalizing the tag. The initialization is a sensitive operation, as the result contains the plain keys that should be stored on the NFC tag. Hence, can only be performed by managers (with granted permission). Later on, other users (for example, businesses) will be able to personalize the NFC tag for customers.  

try:
    # Initializes a NFC tag
    api_response = api_instance.initialize_nfc(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFCApi->initialize_nfc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**NfcInitializeParameter**](NfcInitializeParameter.md)| The parameters for initializing the NFC tag. If the &#x60;user&#x60; value is left blank, the NFC tag will be only initialized, but not personalized (assigned to any user). If a user is given, the permission to personalize is required (besides the permission to initialize), and is a shortcut to initializing and later personalizing the tag. The initialization is a sensitive operation, as the result contains the plain keys that should be stored on the NFC tag. Hence, can only be performed by managers (with granted permission). Later on, other users (for example, businesses) will be able to personalize the NFC tag for customers.   | 

### Return type

[**NfcInitializeResult**](NfcInitializeResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfc_external_auth**
> NfcExternalAuthenticateResult nfc_external_auth(params)

NFC external authentication

The NFC tag will normally perform a mutual authentication, by first generating a challenge that must be encrypted by the external system with the device key. With this the external system is authenticated. Cyclos also returns a challenge that should be encrypted by the NFC tag. This challenge can later be passed in specific operations (for example, when performing a payment) for Cyclos to make sure the NFC tag is present on the operation. 

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
api_instance = swagger_client.NFCApi(swagger_client.ApiClient(configuration))
params = swagger_client.NfcExternalAuthenticateParameter() # NfcExternalAuthenticateParameter | The parameters for the external authentication. If the `token` value is informed, it will be performed an external authentication with the token itself, using the Application Master Key (AMK). If the `token` is not informed, the authentication will be done using the PICC Master Key (PMK), which is useful, for example, when initializing the NFC tag.  

try:
    # NFC external authentication
    api_response = api_instance.nfc_external_auth(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFCApi->nfc_external_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**NfcExternalAuthenticateParameter**](NfcExternalAuthenticateParameter.md)| The parameters for the external authentication. If the &#x60;token&#x60; value is informed, it will be performed an external authentication with the token itself, using the Application Master Key (AMK). If the &#x60;token&#x60; is not informed, the authentication will be done using the PICC Master Key (PMK), which is useful, for example, when initializing the NFC tag.   | 

### Return type

[**NfcExternalAuthenticateResult**](NfcExternalAuthenticateResult.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **personalize_nfc**
> personalize_nfc(params, confirmation_password=confirmation_password)

Personalizes a NFC tag

Personalization requires a NFC tag that was previously initialized, but is still unassigned. This operation doesn't store any key in the NFC tag itself, hence the plain keys are not returned. What is needed is an external authentication with the NFC tag, in order to ensure the card is physically present. The flow for personalizing a tag is: - `GET /nfc/data-for-personalize?user={user}`: Obtain the data for   personalizing NFC tags for this user. The most important information   is which the confirmation password will be required, if any; - `POST /nfc/external-auth`: With a challenge previously encrypted by the   NFC tag, invoke this operation. If the challenge matches the NFC token   in Cyclos, it will be encrypted and returned. Also a new challenge will   be returned, which should be then encrypted by the NFC tag for later   being sent back; - `POST /nfc/personalize`: With the encrypted challenge and the   confirmation password (if any), this operation will update the NFC   token in Cyclos, so it is now assigned to the specified user. From   this point on, the NFC tag is operational. 

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
api_instance = swagger_client.NFCApi(swagger_client.ApiClient(configuration))
params = swagger_client.NfcPersonalizeParameter() # NfcPersonalizeParameter | The parameters for the initialization. 
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Personalizes a NFC tag
    api_instance.personalize_nfc(params, confirmation_password=confirmation_password)
except ApiException as e:
    print("Exception when calling NFCApi->personalize_nfc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**NfcPersonalizeParameter**](NfcPersonalizeParameter.md)| The parameters for the initialization.  | 
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

