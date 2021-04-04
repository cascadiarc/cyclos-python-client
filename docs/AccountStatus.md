# AccountStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**BigDecimal**](BigDecimal.md) | The raw account balance | [optional] 
**credit_limit** | [**BigDecimal**](BigDecimal.md) | The maximum negative balance an account may get | [optional] 
**upper_credit_limit** | [**BigDecimal**](BigDecimal.md) | The maximum positive balance an account may get | [optional] 
**reserved_amount** | [**BigDecimal**](BigDecimal.md) | The reserved amount is part of the raw balance, but cannot be used for payments because of some other events, like payments pending authorization, confirmed webshop orders, scheduled payments (when configured to reserve the total amount) and so on.  | [optional] 
**available_balance** | [**BigDecimal**](BigDecimal.md) | The available balance to be used, taking into account the raw balance, credit limit and reserved amount   | [optional] 
**negative_since** | **datetime** | If the account is negative, contains the date since it became so   | [optional] 
**a_rate** | [**BigDecimal**](BigDecimal.md) | The balance aging counter | [optional] 
**d_rate** | [**BigDecimal**](BigDecimal.md) | The balance maturity | [optional] 
**rate_balance_correction** | [**BigDecimal**](BigDecimal.md) |  | [optional] 
**virtual_rated_balance** | [**BigDecimal**](BigDecimal.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


