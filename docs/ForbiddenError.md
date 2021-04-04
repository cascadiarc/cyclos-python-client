# ForbiddenError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**ForbiddenErrorCode**](ForbiddenErrorCode.md) | Error codes for 403 Forbidden HTTP status.  Possible values are: * expiredPassword: The password being used has expired * illegalAction: Attempt to perform an action that is not allowed on this context * inaccessibleChannel: This channel cannot be accessed by the user  * inaccessiblePrincipal: The used identification method (principal type) cannot be used in this channel * indefinitelyBlocked: The password was indefinitely blocked by exceeding the allowed attempts  * invalidPassword: The password being used is invalid (normally the confirmation password) * operatorWithPendingAgreements: The operator cannot access because his owner member has pending agreements * pendingAgreements: There is at least one agreement which needs to be accepted in order to access the syste * permissionDenied: The operation was denied because a required permission was not granted * resetPassword: The password being used was manually reset * temporarilyBlocked: The password was temporarily blocked by exceeding the allowed attempts  | [optional] 
**password_type** | [**EntityReference**](EntityReference.md) | The password type of the failed password. Only sent if &#x60;code&#x60; is one of: - &#x60;invalidPassword&#x60; - &#x60;expiredPassword&#x60; - &#x60;temporarilyBlocked&#x60; - &#x60;indefinitelyBlocked&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


