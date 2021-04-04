# AccountPermissions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**AccountWithCurrency**](AccountWithCurrency.md) | The account | [optional] 
**visible** | **bool** | Whether the account also is visible for the logged user or, if false means it is only accessible. A non visible account still is operative, i.e the user could make/receive payments from/to it  (i.e is accessible) but can not make a transfers history search for it.  | [optional] 
**system_payments** | [**list[RelatedTransferType]**](RelatedTransferType.md) | Payment types allowed to be performed to system accounts. | [optional] 
**user_payments** | [**list[RelatedTransferType]**](RelatedTransferType.md) | Payment types allowed to be performed to other users | [optional] 
**self_payments** | [**list[RelatedTransferType]**](RelatedTransferType.md) | Payment types allowed to be performed to other self accounts. Only returned for user accounts.  | [optional] 
**pos_payments** | [**list[RelatedTransferType]**](RelatedTransferType.md) | Payment types allowed to be used on POS (receive payments from other users). Only returned for user accounts.          | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


