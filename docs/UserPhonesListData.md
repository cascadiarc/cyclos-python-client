# UserPhonesListData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_manage** | **bool** | Can the authenticated user manage phones of this user? | [optional] 
**can_create_land_line** | **bool** | Can the authenticated user create new land-line phones for this user?  | [optional] 
**can_create_mobile** | **bool** | Can the authenticated user create new mobile phones for this user?  | [optional] 
**sms_enabled** | **bool** | Indicates whether outbound SMS is enabled in Cyclos | [optional] 
**can_verify** | **bool** | Can the authenticated user verify mobile phones of this user?  | [optional] 
**can_enable_for_sms** | **bool** | Can the authenticated user enable / disable mobile phones of this user to send / receive SMS?  | [optional] 
**max_mobile_phones** | **int** | Indicates the maximum number of mobile phones this user can have. Is only returned when &#x60;canManage&#x60; is &#x60;true&#x60;.  | [optional] 
**max_land_line_phones** | **int** | Indicates the maximum number of land line (fixed) phones this user can have. Is only returned when &#x60;canManage&#x60; is &#x60;true&#x60;.  | [optional] 
**land_line_availability** | [**AvailabilityEnum**](AvailabilityEnum.md) | The availability for land-line phones Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required  | [optional] 
**mobile_availability** | [**AvailabilityEnum**](AvailabilityEnum.md) | The availability for mobile phones Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required  | [optional] 
**phones** | [**list[PhoneResult]**](PhoneResult.md) | The list of (visible) phones | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


