# ForgottenPasswordError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**ForgottenPasswordErrorCode**](ForgottenPasswordErrorCode.md) | Application-specific error codes for a ForgottenPassword error. Possible values are: * invalidSecurityAnswer: if the answer for the security question was incorrect. * unexpected: An unexpected error has occurred.   | [optional] 
**key_invalidated** | **bool** | Flag indicating if the key received on the forgotten password reset  request was invalidated because the maximum tries was reached.   Only if code is &#x60;invalidSecurityAnswer&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


