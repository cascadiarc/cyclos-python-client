# swagger_client.FilesApi

All URIs are relative to *https://dev.leftcoastfs.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_raw_file**](FilesApi.md#delete_raw_file) | **DELETE** /files/{id} | Removes a file by id
[**get_raw_file_content**](FilesApi.md#get_raw_file_content) | **GET** /files/{id}/content | Returns the content of a raw file (temp or custom field value)
[**list_temp_files**](FilesApi.md#list_temp_files) | **GET** /files/temp | Lists temporary files related to the currently authenticated user or guest 
[**upload_temp_file**](FilesApi.md#upload_temp_file) | **POST** /files/temp | Adds a new temporary file for the currently authenticated user or guest. 
[**view_raw_file**](FilesApi.md#view_raw_file) | **GET** /files/{id} | Returns a file details by id


# **delete_raw_file**
> delete_raw_file(id)

Removes a file by id

Removes the file with id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesApi()
id = 'id_example' # str | The object identification

try:
    # Removes a file by id
    api_instance.delete_raw_file(id)
except ApiException as e:
    print("Exception when calling FilesApi->delete_raw_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_file_content**
> file get_raw_file_content(id)

Returns the content of a raw file (temp or custom field value)

Returns the content of either a temporary or a custom field value file 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesApi()
id = 'id_example' # str | The file identifier

try:
    # Returns the content of a raw file (temp or custom field value)
    api_response = api_instance.get_raw_file_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_raw_file_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The file identifier | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/html, text/css, text/yaml, text/javascript, text/csv, image/jpeg, image/gif, image/png, application/pdf, application/zip, image/svg+xml, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_temp_files**
> list[StoredFile] list_temp_files(fields=fields, guest_key=guest_key, custom_field=custom_field, custom_field_kind=custom_field_kind)

Lists temporary files related to the currently authenticated user or guest 

Returns all uploaded temporary files by the current user, or guest key. If the current request is as guest and no guest key is given, the IP address is used to match files. Using a key is recommended, because clients that move between WiFi and mobile connection or if the client is in a network with multiple outbound IP addresses, files won't be correctly matched without a key.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesApi()
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)
guest_key = 'guest_key_example' # str | This parameter is only taken into account if the current request is running as guest. It is the key passed by the client when uploading files. If no key is given, files are matched by remote address.   (optional)
custom_field = 'custom_field_example' # str | If the temp file will be used as the value of a custom field of type file then the corresponding custom field must be given (id or internal name). Otherwise this paremeter will be ignored.   (optional)
custom_field_kind = 'custom_field_kind_example' # str | If a custom field is given then its kind must be given too to allow find it. Possible values are: * contact: Contact fields. * contactInfo: Additional contact information fields. * custom_operation: Custom operation fields. * document: Document fields. * marketplace: Advertisements field. * record: Record fields. * transaction: Transaction fields. * user: User profile fields.  (optional)

try:
    # Lists temporary files related to the currently authenticated user or guest 
    api_response = api_instance.list_temp_files(fields=fields, guest_key=guest_key, custom_field=custom_field, custom_field_kind=custom_field_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->list_temp_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 
 **guest_key** | **str**| This parameter is only taken into account if the current request is running as guest. It is the key passed by the client when uploading files. If no key is given, files are matched by remote address.   | [optional] 
 **custom_field** | **str**| If the temp file will be used as the value of a custom field of type file then the corresponding custom field must be given (id or internal name). Otherwise this paremeter will be ignored.   | [optional] 
 **custom_field_kind** | **str**| If a custom field is given then its kind must be given too to allow find it. Possible values are: * contact: Contact fields. * contactInfo: Additional contact information fields. * custom_operation: Custom operation fields. * document: Document fields. * marketplace: Advertisements field. * record: Record fields. * transaction: Transaction fields. * user: User profile fields.  | [optional] 

### Return type

[**list[StoredFile]**](StoredFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_temp_file**
> str upload_temp_file(file, name=name, guest_key=guest_key, custom_field=custom_field, custom_field_kind=custom_field_kind)

Adds a new temporary file for the currently authenticated user or guest. 

Uploads a new temporary file. The returned id can later be used as value of a custom field of type file. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesApi()
file = '/path/to/file.txt' # file | The file being uploaded
name = 'name_example' # str | The name for the new file. If not informed will fall back to the original file name in the form data  (optional)
guest_key = 'guest_key_example' # str | This parameter is only taken into account if the current request is running as guest. It should be a reasonably unique key (for example, an UUID, device identifier or a reasonably large random string) which uniquely identifies the uploaded file as belonging to this \"session\". If no key is given, files uploaded as guest are matched by IP address. Using a key is recommended, because clients that move between WiFi and mobile connection or if the client is in a network with multiple outbound IP addresses, files won't be correctly matched without a key.    (optional)
custom_field = 'custom_field_example' # str | If the temp file will be used as the value of a custom field of type file then the corresponding custom field must be given (id or internal name). Otherwise this paremeter will be ignored.   (optional)
custom_field_kind = 'custom_field_kind_example' # str | If a custom field is given then its kind must be given too to allow find it. Possible values are: * contact: Contact fields. * contactInfo: Additional contact information fields. * custom_operation: Custom operation fields. * document: Document fields. * marketplace: Advertisements field. * record: Record fields. * transaction: Transaction fields. * user: User profile fields.  (optional)

try:
    # Adds a new temporary file for the currently authenticated user or guest. 
    api_response = api_instance.upload_temp_file(file, name=name, guest_key=guest_key, custom_field=custom_field, custom_field_kind=custom_field_kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->upload_temp_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The file being uploaded | 
 **name** | **str**| The name for the new file. If not informed will fall back to the original file name in the form data  | [optional] 
 **guest_key** | **str**| This parameter is only taken into account if the current request is running as guest. It should be a reasonably unique key (for example, an UUID, device identifier or a reasonably large random string) which uniquely identifies the uploaded file as belonging to this \&quot;session\&quot;. If no key is given, files uploaded as guest are matched by IP address. Using a key is recommended, because clients that move between WiFi and mobile connection or if the client is in a network with multiple outbound IP addresses, files won&#39;t be correctly matched without a key.    | [optional] 
 **custom_field** | **str**| If the temp file will be used as the value of a custom field of type file then the corresponding custom field must be given (id or internal name). Otherwise this paremeter will be ignored.   | [optional] 
 **custom_field_kind** | **str**| If a custom field is given then its kind must be given too to allow find it. Possible values are: * contact: Contact fields. * contactInfo: Additional contact information fields. * custom_operation: Custom operation fields. * document: Document fields. * marketplace: Advertisements field. * record: Record fields. * transaction: Transaction fields. * user: User profile fields.  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_raw_file**
> StoredFile view_raw_file(id, fields=fields)

Returns a file details by id

Returns metadata about a file given its id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesApi()
id = 'id_example' # str | The object identification
fields = ['fields_example'] # list[str] | Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: `a,b.b1,c.-c1,c.-c2` will return the fields `a`, `b` (containing only the `b1` field) and `c` (containing all its fields except for `c1` or `c2`).   (optional)

try:
    # Returns a file details by id
    api_response = api_instance.view_raw_file(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->view_raw_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The object identification | 
 **fields** | [**list[str]**](str.md)| Select which fields to include on returned data. If nothing is set, all object fields are returned. Unprefixed field names will be handled like a whitelist (only listed fields will be included), while names starting with a minus (-) or exclamation mark (!) will be handled as blacklist (listed fields will not be included). This works for nesting as well. For example: &#x60;a,b.b1,c.-c1,c.-c2&#x60; will return the fields &#x60;a&#x60;, &#x60;b&#x60; (containing only the &#x60;b1&#x60; field) and &#x60;c&#x60; (containing all its fields except for &#x60;c1&#x60; or &#x60;c2&#x60;).   | [optional] 

### Return type

[**StoredFile**](StoredFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

