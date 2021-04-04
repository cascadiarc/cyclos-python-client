# UsersWithBalanceQueryFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** | The account type | 
**balance_range** | **list[int]** | The minimum and / or maximum balance for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**last_incoming_transfer_period** | **list[datetime]** | The minimum / maximum date of the last incoming transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**last_outgoing_transfer_period** | **list[datetime]** | The minimum / maximum date of the last outgoing transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**negative_since_period** | **list[datetime]** | The minimum / maximum negative-since date for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**medium_balance_range** | **list[int]** | An array with 2 elements, describing the lower and upper medium balance bounds. If not specified, the range defined in the account type will be used. If that one is also not defined, there will be no definitions for balance levels. Both bounds need to be set as 2 element in the array, or it won&#39;t be considered.  | [optional] 
**order_by** | [**UsersWithBalanceOrderByEnum**](UsersWithBalanceOrderByEnum.md) | Contains the possible &#39;order by&#39; values when searching for users with balances  Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * balanceAsc: User are ordered by balance, lower balances first. * balanceDesc: User are ordered by balance, higher balances first.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


