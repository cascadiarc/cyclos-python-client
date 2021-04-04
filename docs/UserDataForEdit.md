# UserDataForEdit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**User**](User.md) | Additional details to the user being edited | [optional] 
**user** | [**UserEdit**](UserEdit.md) | The object that can be altered and posted back to save the user  | [optional] 
**confirmation_password_input** | [**PasswordInput**](PasswordInput.md) | If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


