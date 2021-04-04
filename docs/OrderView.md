# OrderView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer** | [**User**](User.md) | The buyer of the order. | [optional] 
**seller** | [**User**](User.md) | The seller of the order. | [optional] 
**delivery_address** | [**Address**](Address.md) |  | [optional] 
**delivery_method_name** | **str** | The delivery method name. | [optional] 
**delivery_price** | [**BigDecimal**](BigDecimal.md) | The delivery method price. | [optional] 
**delivery_time** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**payment_type** | [**TransferType**](TransferType.md) |  | [optional] 
**items** | [**list[OrderItem]**](OrderItem.md) | The order items | [optional] 
**remarks** | **str** | The current order remarks (i.e those for check-out, accept  or reject).   | [optional] 
**sale** | **bool** | Is it a sale? | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


