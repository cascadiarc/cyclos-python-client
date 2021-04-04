# InputError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**InputErrorCode**](InputErrorCode.md) | Error codes for 422 Unprocessable entity HTTP status. It means there was an error with the input sent to the operation.  Possible values are: * aggregated: Represents an aggregation of other input errors * dataConversion: Some data conversion has failed. For example, when sending a date with an invalid format * fileUploadSize: An uploaded file size exceeds the maximum allowed  * maxItems: There was an attempt to create an item, but the maximum number of allowed items was exceeded * missingParameter: Missing a required request parameter * queryParse: A full-text query keywords contained an invalid text * validation: One or more of the fields sent contains invalid values  | [optional] 
**general_errors** | **list[str]** | A list of errors that cannot be attributed to a specific property. Only returned if &#x60;code&#x60; is &#x60;validation&#x60;.  | [optional] 
**properties** | **list[str]** | An array of properties which contains errors, in the order they were processed. As &#x60;propertyErrors&#x60; is an object (without a guaranteed order for its keys) the original order would be lost otherwise. Only returned if &#x60;code&#x60; is &#x60;validation&#x60;.  | [optional] 
**property_errors** | **dict(str, list[str])** | An object keyed by property name, whose values are lists of errors for that property. Only returned if &#x60;code&#x60; is &#x60;validation&#x60;.  | [optional] 
**custom_fields** | **list[str]** | An array of custom field internal names which contains errors, in the order they were processed. As &#x60;propertyErrors&#x60; is an object (without a guaranteed order for its keys) the original order would be lost otherwise. Only returned if &#x60;code&#x60; is &#x60;validation&#x60;.  | [optional] 
**custom_field_errors** | **dict(str, list[str])** | An object keyed by custom field internal name, whose values are lists of errors for that custom field. Only returned if &#x60;code&#x60; is &#x60;validation&#x60;.  | [optional] 
**max_items** | **int** | The maximum allowed items. Only returned if &#x60;code&#x60; is &#x60;maxItems&#x60;.  | [optional] 
**max_file_size** | **int** | The maximum file size, in bytes, allowed for uploads. Only returned if &#x60;code&#x60; is &#x60;fileUploadSize&#x60;.  | [optional] 
**value** | **str** | The value that failed conversion to the expected data type, or the original full-text query keywords that failed parsing. Only returned if &#x60;code&#x60; is either &#x60;dataConversion&#x60; or &#x60;queryParse&#x60;.  | [optional] 
**name** | **str** | The name of the required request parameter Only returned if &#x60;code&#x60; is &#x60;missingParameter&#x60;.  | [optional] 
**errors** | [**dict(str, InputError)**](InputError.md) | The aggregated &#x60;InputError&#x60;s for each regular property, that is, those that have a single input. Only returned if &#x60;code&#x60; is &#x60;aggregated&#x60;.  | [optional] 
**indexed_errors** | **dict(str, list[InputError])** | The aggregated &#x60;InputError&#x60;s for each list property, that is, those that have a list of inputs. It is guaranteed that the indexes in the input array correspond to the indexes in the corresponding value. The positions with no errors will contain &#x60;null&#x60;. Only returned if &#x60;code&#x60; is &#x60;aggregated&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


