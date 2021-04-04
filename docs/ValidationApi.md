# swagger_client.ValidationApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_email_change**](ValidationApi.md#validate_email_change) | **POST** /validate/email-change/{key} | Validate a pending e-mail change.
[**validate_user_registration**](ValidationApi.md#validate_user_registration) | **POST** /validate/registration/{key} | Validate a pending user registration.


# **validate_email_change**
> validate_email_change(key)

Validate a pending e-mail change.

Validate an e-mail change for the given validation key. After validating  the change, the email is effectively changed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidationApi()
key = 'key_example' # str | The e-mail change validation key the user has received.  

try:
    # Validate a pending e-mail change.
    api_instance.validate_email_change(key)
except ApiException as e:
    print("Exception when calling ValidationApi->validate_email_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The e-mail change validation key the user has received.   | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_user_registration**
> UserRegistrationResult validate_user_registration(key)

Validate a pending user registration.

Validate a pending user registration for the given validation key.  After validating the registration is completed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidationApi()
key = 'key_example' # str | The registration validation key the user has received. 

try:
    # Validate a pending user registration.
    api_response = api_instance.validate_user_registration(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidationApi->validate_user_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The registration validation key the user has received.  | 

### Return type

[**UserRegistrationResult**](UserRegistrationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

