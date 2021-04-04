# RecordBasicData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**RecordKind**](RecordKind.md) | The possible kinds of a record, which can either belong to system or to an user Possible values are: * system: The record belongs to the system, and is unrelated to an user * user: The record belongs to a specific user  | [optional] 
**type** | [**RecordTypeDetailed**](RecordTypeDetailed.md) | The record type | [optional] 
**fields** | [**list[RecordCustomFieldDetailed]**](RecordCustomFieldDetailed.md) | The record custom fields (either defined within this record type or shared fields linked with this record type)  | [optional] 
**user** | [**User**](User.md) | The record owner user. Only returned if &#x60;kind&#x60; is &#x60;user&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


