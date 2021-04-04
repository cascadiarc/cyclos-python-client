# TokenDetailed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TokenStatusEnum**](TokenStatusEnum.md) | The possible statuses for a token Possible values are: * activationExpired: The token has exceeded the activation deadline. * active: The token is active and can be used. * blocked: The token is blocked from being used. * canceled: The token is canceled and cannot be used. * expired: The token has exceeded the expiration date. * pending: The token has been assigned to an user, but it&#39;s still pending for activation. * unassigned: The token is not assigned to an user.  | [optional] 
**user** | [**User**](User.md) | The assigned user. Only if status is not &#x60;unassigned&#x60;. | [optional] 
**activation_date** | **datetime** | When the owner user activated the token.  | [optional] 
**creation_date** | **datetime** | The creation date. | [optional] 
**expiry_date** | **datetime** | The expiration date. Only if the corresponding token type defines an expiration period. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


