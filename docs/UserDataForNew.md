# UserDataForNew

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_set_send_activation_email** | **bool** | Whether the current user is allowed to skip the activateion e-mail  | [optional] 
**generated_username** | **bool** | Indicates whether the login name is generated | [optional] 
**address_configuration** | [**AddressConfigurationForUserProfile**](AddressConfigurationForUserProfile.md) | Configuration for registering addresses | [optional] 
**phone_configuration** | [**PhoneConfigurationForUserProfile**](PhoneConfigurationForUserProfile.md) | Configuration for registering phones | [optional] 
**contact_info_configuration** | [**ContactInfoConfigurationForUserProfile**](ContactInfoConfigurationForUserProfile.md) | Configuration for registering additional contacts | [optional] 
**image_configuration** | [**ImageConfigurationForUserProfile**](ImageConfigurationForUserProfile.md) | Configuration for uploading images | [optional] 
**password_types** | [**list[PasswordTypeRegistration]**](PasswordTypeRegistration.md) | The password types that should be registered together with the user  | [optional] 
**captcha_type** | [**CaptchaProviderEnum**](CaptchaProviderEnum.md) | description: &gt;   The captcha provider used to requested a captcha for registration,   or null if no captcha is needed. Possible values are: * internal: Default provider using images  | [optional] 
**user** | [**UserNew**](UserNew.md) | The object that can be altered and posted back to register the user  | [optional] 
**agreements** | [**list[AgreementContent]**](AgreementContent.md) | The agreements that needs to be accepted by the user to be able to register. Only returned for public registrations.  | [optional] 
**security_questions** | [**list[EntityReference]**](EntityReference.md) | If enabled in the server, are the possible security questions the user can use to set the answer.  | [optional] 
**nfc_token_types** | [**list[EntityReference]**](EntityReference.md) | The NFC token types the authenticated user can parsonalize tags for the user being registered  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


