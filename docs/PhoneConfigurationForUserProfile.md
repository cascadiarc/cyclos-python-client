# PhoneConfigurationForUserProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_phone** | [**PhoneNew**](PhoneNew.md) | Contains a template with default values for a new mobile phone  | [optional] 
**land_line_phone** | [**PhoneNew**](PhoneNew.md) | Contains a template the default values for a new land-line phone  | [optional] 
**mobile_availability** | [**AvailabilityEnum**](AvailabilityEnum.md) | The availability for mobile phones Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required  | [optional] 
**land_line_availability** | [**AvailabilityEnum**](AvailabilityEnum.md) | The availability for land-line phones Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required  | [optional] 
**edit** | **bool** | Can edit phones? | [optional] 
**manage_privacy** | **bool** | Can manage the privacy of phones? | [optional] 
**max_land_lines** | **int** | The maximum number of land-line phones the user can own | [optional] 
**max_mobiles** | **int** | The maximum number of mobile phones the user can own | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


