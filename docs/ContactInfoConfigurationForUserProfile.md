# ContactInfoConfigurationForUserProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_info** | [**ContactInfoNew**](ContactInfoNew.md) | Contains the default values for a new additional contact | [optional] 
**availability** | [**AvailabilityEnum**](AvailabilityEnum.md) | The availability for additional contacts Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required  | [optional] 
**custom_fields** | [**list[CustomFieldDetailed]**](CustomFieldDetailed.md) | The custom fields for additional contact informations | [optional] 
**edit** | **bool** | Can the authenticated user edit additional contacts? | [optional] 
**manage_privacy** | **bool** | Can the authenticated user manage the privacy of additional contacts?  | [optional] 
**max_contact_infos** | **int** | The maximum number of additional contacts the user can own | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


