# ClientView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ClientStatusEnum**](ClientStatusEnum.md) | The status of an access client Possible values are: * active: The access client is active, and can operate normally * blocked: The access client is blocked and cannot be used until it is unblocked * removed: The access client was removed, but had transactions, so couldn&#39;t be physically removed * unassigned: The access client is unassigned (disconnected) from an (remote) application  | [optional] 
**activation_date** | **datetime** | The date the client was activated | [optional] 
**confirmation_password_input** | [**PasswordInput**](PasswordInput.md) | If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).  | [optional] 
**can_get_activation_code** | **bool** | Can the authenticated user get the activation code, to later activate (assign) this client?  | [optional] 
**can_unassign** | **bool** | Can the authenticated user unassign this client? | [optional] 
**can_block** | **bool** | Can the authenticated user block this client? | [optional] 
**can_unblock** | **bool** | Can the authenticated user unblock this client? | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


