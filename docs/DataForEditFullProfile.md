# DataForEditFullProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** | Contains the formatting of the user according to the  configuration. Is only returned if no profile fields are marked to return in user list  | [optional] 
**short_display** | **str** | Contains the short formatting of the user according to the configuration. Is only returned if no profile fields are marked to return in user list  | [optional] 
**confirmation_password_input** | [**PasswordInput**](PasswordInput.md) | If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).  | [optional] 
**user_configuration** | [**BasicUserDataForEdit**](BasicUserDataForEdit.md) | Data for editing the basic fields | [optional] 
**user** | [**UserEdit**](UserEdit.md) | User model which can be modified and sent back | [optional] 
**phone_configuration** | [**PhoneConfigurationForUserProfile**](PhoneConfigurationForUserProfile.md) | Configuration data regarding phones | [optional] 
**land_line_phones** | [**list[PhoneEditWithId]**](PhoneEditWithId.md) | The existing land-line phones that can be modified and posted back  | [optional] 
**mobile_phones** | [**list[PhoneEditWithId]**](PhoneEditWithId.md) | The existing mobile phones that can be modified and posted back  | [optional] 
**address_configuration** | [**AddressConfigurationForUserProfile**](AddressConfigurationForUserProfile.md) | Configuration data regarding addresses | [optional] 
**addresses** | [**list[AddressEditWithId]**](AddressEditWithId.md) | The existing addresses that can be modified and posted back  | [optional] 
**contact_info_configuration** | [**ContactInfoConfigurationForUserProfile**](ContactInfoConfigurationForUserProfile.md) | Configuration data regarding additional contacts | [optional] 
**contact_infos** | [**list[ContactInfoEditWithId]**](ContactInfoEditWithId.md) | The existing additional contacts that can be modified and posted back  | [optional] 
**contact_info_binary_values** | [**dict(str, ContactInfoBinaryValuesForUserProfile)**](ContactInfoBinaryValuesForUserProfile.md) | Values for images and binary custom fields for additional contacts  | [optional] 
**image_configuration** | [**ImageConfigurationForUserProfile**](ImageConfigurationForUserProfile.md) | Configuration data regarding images | [optional] 
**images** | [**list[Image]**](Image.md) | All current user images | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


