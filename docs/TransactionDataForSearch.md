# TransactionDataForSearch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_types** | [**list[AccountType]**](AccountType.md) | Visible account types from the given owner | [optional] 
**can_view_authorized** | **bool** | Can the authenticated user view authorized transactions of this owner?   | [optional] 
**can_view_scheduled** | **bool** | Can the authenticated user view scheduled payments of this owner?   | [optional] 
**visible_kinds** | [**list[TransactionKind]**](TransactionKind.md) | Contains the transaction kinds the authenticated user can view over this owner.   | [optional] 
**query** | [**TransactionQueryFilters**](TransactionQueryFilters.md) | Default query filters for the transactions search  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


