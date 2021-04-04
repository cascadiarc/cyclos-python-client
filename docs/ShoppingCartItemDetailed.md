# ShoppingCartItemDetailed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_price** | [**BigDecimal**](BigDecimal.md) | The total price for this item, i.e the curent price of the product multiplied by its corresponding quantity.   | [optional] 
**availability** | [**ShoppingCartItemAvailabilityEnum**](ShoppingCartItemAvailabilityEnum.md) | The possible status of a webshop advertisement in relation to its availability  Possible values are: * available: The webshop advertisement is available and can be purchased * outOfStock: The webshop advertisement is now out of stock * unavailable: The webshop advertisement has been made unavailable and cannot be purchased anymore   | [optional] 
**quantity_adjustment** | [**ShoppingCartItemQuantityAdjustmentEnum**](ShoppingCartItemQuantityAdjustmentEnum.md) | The possible adjustments to a quantity-limited product added to shopping cart Possible values are: * max: The quantity was reduced to honor the maximum allowed quantity * min: The quantity was raised to honor the minimum allowed quantity * stock: The quantity was reduced to the maximum available stock quantity  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


