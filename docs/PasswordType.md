# PasswordType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_global** | **bool** | Indicates whether this password type is defined in global mode (&#x60;true&#x60;) or in a network (&#x60;false&#x60;)  | [optional] 
**mode** | [**PasswordModeEnum**](PasswordModeEnum.md) | Indicates how a password is handled Possible values are: * generated: Passwords are always generated * manual: Passwords are manually typed by users * otp: One Time Passwords. are always generated and can be used only once * script: Passwords are not stored in Cyclos, but handed-over for a script to verify them.  Is normally used to implement single-sign-on with other apps.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


