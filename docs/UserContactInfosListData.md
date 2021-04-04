# UserContactInfosListData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_manage** | **bool** | Indicates whether the additional contact informations can be managed by the authenticated user  | [optional] 
**can_create** | **bool** | Indicates whether new additional contact informations can be created by the authenticated user  | [optional] 
**max_contact_infos** | **int** | Indicates the maximum number of additional contact informations the user can have  | [optional] 
**availability** | [**AvailabilityEnum**](AvailabilityEnum.md) | The availability for additional contacts Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required  | [optional] 
**custom_fields** | [**list[CustomFieldDetailed]**](CustomFieldDetailed.md) | The list of additional contact informations custom fields | [optional] 
**contact_infos** | [**list[ContactInfoResult]**](ContactInfoResult.md) | The additional contact information list | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


