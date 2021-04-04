# swagger_client.SessionsApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_user**](SessionsApi.md#login_user) | **POST** /sessions | Logins a user, returning data from the new session


# **login_user**
> UserAuth login_user(fields=fields, login=login)

Logins a user, returning data from the new session

Created a session for a given user. Must be executed as administrator with permissions. A channel can be specified (defaults to `main`) so the user can be logged in by some external actor (like an website) and then redirected to `<cyclos-root>?sessionToken=<session-token>`. It is also recommended to set in Cyclos the login and logout URLs in the configuration, so, when the user logs out, he will be redirected back to the previous website. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionsApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
login = swagger_client.LoginUser() # LoginUser | Information about the user being logged in (optional)

try:
    # Logins a user, returning data from the new session
    api_response = api_instance.login_user(fields=fields, login=login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->login_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **login** | [**LoginUser**](LoginUser.md)| Information about the user being logged in | [optional] 

### Return type

[**UserAuth**](UserAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

