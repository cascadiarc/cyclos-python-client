# swagger_client.CaptchaApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_captcha_content**](CaptchaApi.md#get_captcha_content) | **GET** /captcha/{id} | Returns a captcha image content
[**new_captcha**](CaptchaApi.md#new_captcha) | **POST** /captcha | Returns a new captcha challenge


# **get_captcha_content**
> file get_captcha_content(id, group=group, width=width, height=height)

Returns a captcha image content

Returns the image content of a captcha text. When neither `width` nor `height` are specified, returns the original size. The original ratio is always maintained. When only of one of  the dimensions is specified, it is used as maximum, and the other is calculated. When both are informed, the maximum size with the original ratio that fits both dimensions is used.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaApi()
id = 'id_example' # str | The object identification
group = 'group_example' # str | On public / user registration, it is possible to specify a destination group, so the captcha background image will be taken from this new group's configured theme.  (optional)
width = 56 # int | The requested image width (optional)
height = 56 # int | The requested file height (optional)

try:
    # Returns a captcha image content
    api_response = api_instance.get_captcha_content(id, group=group, width=width, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptchaApi->get_captcha_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **group** | **str**| On public / user registration, it is possible to specify a destination group, so the captcha background image will be taken from this new group&#39;s configured theme.  | [optional] 
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

# **new_captcha**
> str new_captcha(group=group)

Returns a new captcha challenge

Only allowed when internal captchas are in use.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaApi()
group = 'group_example' # str | On public / user registration, it is possible to specify a destination group, so the captcha background image will be taken from this new group's configured theme.  (optional)

try:
    # Returns a new captcha challenge
    api_response = api_instance.new_captcha(group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptchaApi->new_captcha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| On public / user registration, it is possible to specify a destination group, so the captcha background image will be taken from this new group&#39;s configured theme.  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

