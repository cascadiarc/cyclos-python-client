# UserWithBalanceResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**BigDecimal**](BigDecimal.md) | The raw account balance | [optional] 
**balance_level** | [**BalanceLevelEnum**](BalanceLevelEnum.md) | Contains the possible balance levels on the users with balances search  Possible values are: * high: High balance, above the medium balance range upper bound * low: Low balance, below the medium balance range lower bound * medium: Medium balance, between the lower and upper bounds of the medium balance range  | [optional] 
**negative_since** | **datetime** | The date since the account has been negative | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


