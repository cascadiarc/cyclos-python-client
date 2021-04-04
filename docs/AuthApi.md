# swagger_client.AuthApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_forgotten_password**](AuthApi.md#change_forgotten_password) | **POST** /auth/forgotten-password | Changes the a forgotten password after have completed the request 
[**disconnect_current_client**](AuthApi.md#disconnect_current_client) | **DELETE** /auth/access-client | Disconnect the current access client
[**forgotten_password_request**](AuthApi.md#forgotten_password_request) | **POST** /auth/forgotten-password/request | Requests a forgotten password, notifying the user with instructions to reset it 
[**get_current_auth**](AuthApi.md#get_current_auth) | **GET** /auth | Returns data about the currently authenticated user
[**get_data_for_change_forgotten_password**](AuthApi.md#get_data_for_change_forgotten_password) | **GET** /auth/forgotten-password/data-for-change | Returns configuration data used to change a forgotten password after the initial request 
[**get_data_for_login**](AuthApi.md#get_data_for_login) | **GET** /auth/data-for-login | Returns data containing the configuration for logging-in
[**get_secondary_password_input**](AuthApi.md#get_secondary_password_input) | **GET** /auth/session/secondary-password | Returns the data for a secondary access password input
[**login**](AuthApi.md#login) | **POST** /auth/session | Logs-in the currently authenticated user
[**logout**](AuthApi.md#logout) | **DELETE** /auth/session | Log-out the current session
[**new_otp**](AuthApi.md#new_otp) | **POST** /auth/otp | Generates a new One-Time-Password (OTP) for the authenticated user
[**validate_secondary_password**](AuthApi.md#validate_secondary_password) | **POST** /auth/session/secondary-password | Validates the current pending session


# **change_forgotten_password**
> change_forgotten_password(params)

Changes the a forgotten password after have completed the request 

Changes the password (if manual), or sends a new one by e-mail (if generated) after the forgotten password reset process is completed.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
params = swagger_client.ChangeForgottenPassword() # ChangeForgottenPassword | The parameters for changing the password

try:
    # Changes the a forgotten password after have completed the request 
    api_instance.change_forgotten_password(params)
except ApiException as e:
    print("Exception when calling AuthApi->change_forgotten_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**ChangeForgottenPassword**](ChangeForgottenPassword.md)| The parameters for changing the password | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_current_client**
> disconnect_current_client(confirmation_password=confirmation_password)

Disconnect the current access client

Changes the status of the access client used for authentication, disconnecting it. To be reused, it has to be activated again. 

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

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
confirmation_password = 'confirmation_password_example' # str | The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  (optional)

try:
    # Disconnect the current access client
    api_instance.disconnect_current_client(confirmation_password=confirmation_password)
except ApiException as e:
    print("Exception when calling AuthApi->disconnect_current_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirmation_password** | **str**| The password used to confirm this action, if needed. The actual password type, if any, depends on the Cyclos configuration for the current channel.  | [optional] 

### Return type

void (empty response body)

### Authorization

[accessClient](../README.md#accessClient)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgotten_password_request**
> forgotten_password_request(params)

Requests a forgotten password, notifying the user with instructions to reset it 

Sends an e-mail (in the future SMS will be supported) with instructions on how to reset the password, in case it was forgotten. In order to work, the Cyclos configuration options, both to show the forgotten password link and to enable for users need to be set. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
params = swagger_client.ForgottenPasswordRequest() # ForgottenPasswordRequest | The parameters for requesting a forgotten password reset

try:
    # Requests a forgotten password, notifying the user with instructions to reset it 
    api_instance.forgotten_password_request(params)
except ApiException as e:
    print("Exception when calling AuthApi->forgotten_password_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**ForgottenPasswordRequest**](ForgottenPasswordRequest.md)| The parameters for requesting a forgotten password reset | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_auth**
> Auth get_current_auth(fields=fields)

Returns data about the currently authenticated user

Returns the logged user information. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data about the currently authenticated user
    api_response = api_instance.get_current_auth(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_current_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**Auth**](Auth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_for_change_forgotten_password**
> DataForChangeForgottenPassword get_data_for_change_forgotten_password(key, fields=fields)

Returns configuration data used to change a forgotten password after the initial request 

After the user has requested a forgotten password reset, using the `POST /auth/forgotten-password/request` path, the link on the received e-mail will contain a key which can be used to actually change the password. This key must be passed to this operation in order to request input on the new password, and maybe confirm the security question, depending on the Cyclos configuration.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
key = 'key_example' # str | The validation key which was sent by e-mail to the user
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns configuration data used to change a forgotten password after the initial request 
    api_response = api_instance.get_data_for_change_forgotten_password(key, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_data_for_change_forgotten_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The validation key which was sent by e-mail to the user | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**DataForChangeForgottenPassword**](DataForChangeForgottenPassword.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_for_login**
> DataForLogin get_data_for_login(fields=fields)

Returns data containing the configuration for logging-in

Contains data useful for login, such as the allowed user identification methods, the password type and data for the forgot password request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns data containing the configuration for logging-in
    api_response = api_instance.get_data_for_login(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_data_for_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**DataForLogin**](DataForLogin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secondary_password_input**
> PasswordInput get_secondary_password_input()

Returns the data for a secondary access password input

Returns the data for a secondary access password input. Only if there is secondary access password configured for the channel. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # Returns the data for a secondary access password input
    api_response = api_instance.get_secondary_password_input()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_secondary_password_input: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PasswordInput**](PasswordInput.md)

### Authorization

[session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> Auth login(fields=fields, cookie=cookie, timeout_in_seconds=timeout_in_seconds)

Logs-in the currently authenticated user

Logs-in the currently authenticated user, returning the session token. This token can then be used on subsequent requests. After finishing the session, the user can then logout by sending an HTTP DELETE to /auth. 

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

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
cookie = true # bool | If true then the server add the `Session-Token` cookie to the response  containing only the second half of the session token.  (optional)
timeout_in_seconds = 56 # int | The timeout in seconds for the created session. If this value is not given or it is greater than that for the channel then the timeout  for the channel will be used.  (optional)

try:
    # Logs-in the currently authenticated user
    api_response = api_instance.login(fields=fields, cookie=cookie, timeout_in_seconds=timeout_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **cookie** | **bool**| If true then the server add the &#x60;Session-Token&#x60; cookie to the response  containing only the second half of the session token.  | [optional] 
 **timeout_in_seconds** | **int**| The timeout in seconds for the created session. If this value is not given or it is greater than that for the channel then the timeout  for the channel will be used.  | [optional] 

### Return type

[**Auth**](Auth.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout(cookie=cookie)

Log-out the current session

Invalidates the session used for authentication

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
cookie = true # bool | If true then the server add the `Session-Token` cookie with a null value to erase it.   (optional)

try:
    # Log-out the current session
    api_instance.logout(cookie=cookie)
except ApiException as e:
    print("Exception when calling AuthApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cookie** | **bool**| If true then the server add the &#x60;Session-Token&#x60; cookie with a null value to erase it.   | [optional] 

### Return type

void (empty response body)

### Authorization

[session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_otp**
> list[str] new_otp(medium)

Generates a new One-Time-Password (OTP) for the authenticated user

Sends a new OTP for the authenticated user. Used when the confirmation password of a specific action. Used when `PasswordInput.mode` is `otp`.  

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
medium = 'medium_example' # str | The medium the user wants to receive the OTP Possible values are: * email: The user will receive an email with the information * sms: The user will receive a sms with the information (only if there is at least one phone enabled for sms) 

try:
    # Generates a new One-Time-Password (OTP) for the authenticated user
    api_response = api_instance.new_otp(medium)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->new_otp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium** | **str**| The medium the user wants to receive the OTP Possible values are: * email: The user will receive an email with the information * sms: The user will receive a sms with the information (only if there is at least one phone enabled for sms)  | 

### Return type

**list[str]**

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_secondary_password**
> validate_secondary_password(password)

Validates the current pending session

Validates a pending session using the secondary access password (if any) configured for the current channel. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: session
configuration = swagger_client.Configuration()
configuration.api_key['Session-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
password = 'password_example' # str | The secondary access password 

try:
    # Validates the current pending session
    api_instance.validate_secondary_password(password)
except ApiException as e:
    print("Exception when calling AuthApi->validate_secondary_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The secondary access password  | 

### Return type

void (empty response body)

### Authorization

[session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

