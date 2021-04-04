# swagger_client.NotificationsApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_notification**](NotificationsApi.md#delete_notification) | **DELETE** /notifications/{id} | Removes a notification by id.
[**mark_as_viewed**](NotificationsApi.md#mark_as_viewed) | **POST** /notifications/viewed | Update the last view date for the notifications.
[**mark_notifications_as_read**](NotificationsApi.md#mark_notifications_as_read) | **POST** /notifications/mark-as-read | Marks a list of notifications as read.
[**notifications_status**](NotificationsApi.md#notifications_status) | **GET** /notifications/status | Return information about the received notifications.
[**search_notifications**](NotificationsApi.md#search_notifications) | **GET** /notifications | Searches for the notifications the authenticated user has received.
[**view_notification**](NotificationsApi.md#view_notification) | **GET** /notifications/{id} | Returns the notification details.


# **delete_notification**
> delete_notification(id)

Removes a notification by id.

Removes a notification for the authenticated user by id. 

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
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The object identification

try:
    # Removes a notification by id.
    api_instance.delete_notification(id)
except ApiException as e:
    print("Exception when calling NotificationsApi->delete_notification: %s\n" % e)
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

# **mark_as_viewed**
> mark_as_viewed()

Update the last view date for the notifications.

Update the last view date for the notifications. This will be used to calculate the number of new notifications returned by the  `POST /notifications/status` operation. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()

try:
    # Update the last view date for the notifications.
    api_instance.mark_as_viewed()
except ApiException as e:
    print("Exception when calling NotificationsApi->mark_as_viewed: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_notifications_as_read**
> mark_notifications_as_read(ids)

Marks a list of notifications as read.

Marks a list of notifications, given by id, as read.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
ids = ['ids_example'] # list[str] | The notifications (comma-separated list of identifiers) to mark as read.

try:
    # Marks a list of notifications as read.
    api_instance.mark_notifications_as_read(ids)
except ApiException as e:
    print("Exception when calling NotificationsApi->mark_notifications_as_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| The notifications (comma-separated list of identifiers) to mark as read. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_status**
> NotificationsStatus notifications_status()

Return information about the received notifications.

Return information about the status of the received notifications (unread, new, etc).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()

try:
    # Return information about the received notifications.
    api_response = api_instance.notifications_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->notifications_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationsStatus**](NotificationsStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_notifications**
> list[Notification] search_notifications(fields=fields, only_new=only_new, only_unread=only_unread, page=page, page_size=page_size)

Searches for the notifications the authenticated user has received.

Returns an ordered page of notifications the authenticated user has received (newest first). 

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
api_instance = swagger_client.NotificationsApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
only_new = true # bool | Boolean value indicating wether return only the new notifications received after the last view date tracked using `POST /notifications/viewed`   (optional)
only_unread = true # bool | Boolean value indicating wether return only the unread notifications  (optional)
page = 56 # int | The page number (zero-based) of the search. The default value is zero.  (optional)
page_size = 56 # int | The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  (optional)

try:
    # Searches for the notifications the authenticated user has received.
    api_response = api_instance.search_notifications(fields=fields, only_new=only_new, only_unread=only_unread, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->search_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **only_new** | **bool**| Boolean value indicating wether return only the new notifications received after the last view date tracked using &#x60;POST /notifications/viewed&#x60;   | [optional] 
 **only_unread** | **bool**| Boolean value indicating wether return only the unread notifications  | [optional] 
 **page** | **int**| The page number (zero-based) of the search. The default value is zero.  | [optional] 
 **page_size** | **int**| The maximum number of records that will be returned on the search. The default value is 40. The maximum number of returned results is configured in Cyclos, and even if more than that is requested, it will be limited by that setting.  | [optional] 

### Return type

[**list[Notification]**](Notification.md)

### Authorization

[accessClient](../README.md#accessClient), [basic](../README.md#basic), [session](../README.md#session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_notification**
> Notification view_notification(id, fields=fields)

Returns the notification details.

Returns the notification details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
id = 'id_example' # str | The object identification
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns the notification details.
    api_response = api_instance.view_notification(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->view_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

