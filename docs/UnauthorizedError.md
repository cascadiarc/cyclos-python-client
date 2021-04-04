# UnauthorizedError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**UnauthorizedErrorCode**](UnauthorizedErrorCode.md) | Error codes for 401 Unauthorized HTTP status.  Possible values are: * invalidAccessClient: The access client used for access is invalid * invalidChannelUsage: Attempt to login on a stateless-only channel, or use stateless in a stateful-only channel, or invoke as guest in a channel configuration which is only for users * invalidNetwork: Attempt to access a network that has been disabled * loggedOut: The session token used for access is invalid * login: Either user identification (principal) or password are invalid. May have additional information, such as the user / password status * missingAuthorization: Attempt to access an operation as guest, but the operation requires authentication * remoteAddressBlocked: The IP address being used for access has been blocked by exceeding tries with invalid users * unauthorizedAddress: The user cannot access the system using an IP address that is not white-listed * unauthorizedUrl: The user&#39;s configuration demands access using a specific URL, and this access is being done using another one  | [optional] 
**user_status** | [**UserStatusEnum**](UserStatusEnum.md) | May only returned when &#x60;code&#x60; is &#x60;login&#x60;. Possible values are: * active: The user is active and can use the system normally. * blocked: The user has been blocked from accessing the system. Other users still see him/her. * disabled: The user has been disabled - he/she cannot access the system and is invisible by other users. * pending: The user registration is pending a confirmation. Probably the user has received an e-mail with a link that must be followed to complete the activation. The user is invisible by other users. * purged: The user was permanently removed and had all his private data removed. Only transactions are kept for historical reasons. * removed: The user was permanently removed. It&#39;s profile is kept for historical purposes.  | [optional] 
**password_status** | [**PasswordStatusEnum**](PasswordStatusEnum.md) | May only returned when &#x60;code&#x60; is &#x60;login&#x60;. Possible values are: * active: The password is active and valid * disabled: The password has been manually disabled * expired: The password is expired * indefinitelyBlocked: The password is blocked by exceeding the maximum attempts until it is manually unblocked * neverCreated: The password has never been created for the user * pending: The password was manually allowed (by admins) for the user to generate it, but it was not yet generated (never used for manual passwords) * reset: The password has been reset (can be used for login but must then be changed) * temporarilyBlocked: The password is temporarily blocked by exceeding the maximum attempts  | [optional] 
**missing_secondary_password** | [**PasswordType**](PasswordType.md) | May only returned when &#x60;code&#x60; is &#x60;login&#x60; and there is a secondary access password defined for the channel.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

