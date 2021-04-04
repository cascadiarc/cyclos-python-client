# AccountHistoryStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin_date** | **datetime** | The reference begin date | [optional] 
**balance_at_begin** | [**BigDecimal**](BigDecimal.md) | The raw balance at the beginning of the informed period | [optional] 
**end_date** | **datetime** | The reference end date | [optional] 
**balance_at_end** | [**BigDecimal**](BigDecimal.md) | The raw balance at the end of the informed period | [optional] 
**incoming** | [**AmountSummary**](AmountSummary.md) | The summary of incoming transfers | [optional] 
**outgoing** | [**AmountSummary**](AmountSummary.md) | The summary of outgoing transfers | [optional] 
**net_inflow** | [**BigDecimal**](BigDecimal.md) | The raw difference between incoming and outgoing transfers in the informed period   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


