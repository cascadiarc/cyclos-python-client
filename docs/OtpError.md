# OtpError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**OtpErrorCode**](OtpErrorCode.md) | Application-specific error codes for an OTP error. Possible values are: * errorSendingSms: An error has occurred trying to send the OTP through SMS. * unexpected: An unexpected error has occurred.   | [optional] 
**sms_status** | [**OutboundSmsStatusEnum**](OutboundSmsStatusEnum.md) | Only if code is &#x60;errorSendingSms&#x60; Possible values are: * gatewayUreachable: Network problem, or gateway server down * invalid: The parameters for sending an SMS message were invalid * maxMessagesReached: The maximum SMS messages for the user (or guest) have been reached * rejected: The gateway has rejected the SMS message * success: The SMS message was successfully sent * timeout: Timeout while connecting or waiting for a gateway server reply * unexpected: An unexpected error has occurred  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


