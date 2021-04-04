# DataForLogin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_password_type** | [**EntityReference**](EntityReference.md) | The password type used for login access  | [optional] 
**principal_types** | [**list[PrincipalTypeInput]**](PrincipalTypeInput.md) | The identification methods accepted for login | [optional] 
**default_principal_type** | **str** | The internal name of the identification method that is marked as default for the current channel configuration. This is optional, and if there is no default, all possible identification methods will be attempted for login.  | [optional] 
**extra_forgot_password_principal_types** | [**list[PrincipalTypeInput]**](PrincipalTypeInput.md) | The additional identification methods also accepted for the  forgotten password request.  | [optional] 
**login_password_input** | [**PasswordInput**](PasswordInput.md) | Contains data for the password used on login | [optional] 
**forgot_password_captcha_provider** | [**CaptchaProviderEnum**](CaptchaProviderEnum.md) | If the forgot password request requires a captcha, will be the  provider used to request one. Otherwise will be null. Possible values are: * internal: Default provider using images  | [optional] 
**forgot_password_mediums** | [**list[SendMediumEnum]**](SendMediumEnum.md) | If the forgot password request is enabled, returns the mediums the user can choose to receive the confirmation key or code.  If nothing is returned, forgot password is not enabled. Possibles values for each array element are: * email: The user will receive an email with the information * sms: The user will receive a sms with the information (only if there is at least one phone enabled for sms)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


