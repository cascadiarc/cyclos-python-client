# RecordView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RecordTypeDetailed**](RecordTypeDetailed.md) | The record type | [optional] 
**user** | [**User**](User.md) | The user which owns this record, only returned if &#x60;kind&#x60; is &#x60;user&#x60;  | [optional] 
**creation_date** | **datetime** | The record creation date | [optional] 
**created_by** | [**User**](User.md) | Reference to the user that created the record | [optional] 
**last_modification_date** | **datetime** | The record last modification date | [optional] 
**last_modified_by** | [**User**](User.md) | Reference to the user that last modified the record | [optional] 
**custom_values** | [**list[RecordCustomFieldValue]**](RecordCustomFieldValue.md) | The list of custom field values this record has | [optional] 
**edit** | **bool** | Can the authenticated user edit this record? | [optional] 
**remove** | **bool** | Can the authenticated user remove this record? | [optional] 
**operations** | [**list[Operation]**](Operation.md) | List of runnable custom operations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


