# PasswordStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PasswordStatusEnum**](PasswordStatusEnum.md) | The password status Possible values are: * active: The password is active and valid * disabled: The password has been manually disabled * expired: The password is expired * indefinitelyBlocked: The password is blocked by exceeding the maximum attempts until it is manually unblocked * neverCreated: The password has never been created for the user * pending: The password was manually allowed (by admins) for the user to generate it, but it was not yet generated (never used for manual passwords) * reset: The password has been reset (can be used for login but must then be changed) * temporarilyBlocked: The password is temporarily blocked by exceeding the maximum attempts  | [optional] 
**_date** | **datetime** | The date this status took place | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


