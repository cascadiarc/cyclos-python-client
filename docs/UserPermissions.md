# UserPermissions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserProfilePermissions**](UserProfilePermissions.md) | Permissions over the user profile | [optional] 
**contact** | [**UserContactPermissions**](UserContactPermissions.md) | Permissions over a contact | [optional] 
**marketplace** | [**UserMarketplacePermissions**](UserMarketplacePermissions.md) | Permissions over the user marketplace | [optional] 
**accounts** | [**list[AccountWithCurrency]**](AccountWithCurrency.md) | Accounts which can be viewed by the authenticated user | [optional] 
**payment** | [**UserPaymentPermissions**](UserPaymentPermissions.md) | Permissions for payments regarding this user | [optional] 
**records** | [**list[OwnerRecordPermissions]**](OwnerRecordPermissions.md) | Records types the authenticated user can view over the given user  | [optional] 
**operations** | [**list[Operation]**](Operation.md) | Custom operations the authenticated user can run over the given user  | [optional] 
**tokens** | [**list[TokenType]**](TokenType.md) | Tokens the authenticated user can view over the given user  | [optional] 
**personalize_nfc_tokens** | [**list[TokenType]**](TokenType.md) | NFC tokens the authenticated user can personalize for the given user  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


