# WebshopAd

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_decimal_quantity** | **bool** | Indicates if the webshop ad allow enter a decimal value for the  quantity.  | [optional] 
**min_allowed_in_cart** | [**BigDecimal**](BigDecimal.md) | The minimum quantity allowed to be added in the shopping cart.  | [optional] 
**max_allowed_in_cart** | [**BigDecimal**](BigDecimal.md) | The maximum quantity allowed to be added in the shopping cart.   | [optional] 
**stock_quantity** | [**BigDecimal**](BigDecimal.md) | The stock disponibility. Only if &#x60;unlimitedStock&#x60; is false and the  &#39;Stock type&#39; was not marked as &#39;Not available&#39; (through the web  interface).  | [optional] 
**unlimited_stock** | **bool** | If true then it means there is always disponibility of the webshop ad. | [optional] 
**product_number** | **str** | The number assigned to the webshop ad. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


