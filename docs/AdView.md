# AdView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**list[AdCategoryWithParent]**](AdCategoryWithParent.md) | Either internal name or id of categories this advertisement belongs to. In most cases an advertisement will have a single category, but this depends on the Cyclos configuration.  | [optional] 
**custom_values** | [**list[CustomFieldValue]**](CustomFieldValue.md) | The list of custom field values this advertisement has | [optional] 
**currency** | [**Currency**](Currency.md) | The advertisement&#39;s price currency | [optional] 
**promotional_price** | [**BigDecimal**](BigDecimal.md) | The promotional price, to be applied on the promotional period is active  | [optional] 
**promotional_period** | [**DatePeriod**](DatePeriod.md) | The promotional period, the one when &#x60;promotionalPrice&#x60; is valid  | [optional] 
**promotional_period_active** | **bool** | Indicates whether the promotional period is active at the moment this data is returned  | [optional] 
**can_manage** | **bool** | Indicates if the authenticated user manage this advertisement | [optional] 
**can_buy** | **bool** | Indicates if the authenticated user can buy this webshop ad.  | [optional] 
**can_ask** | **bool** | Indicates if the authenticated user can ask questions about this advertisement.  | [optional] 
**questions_enabled** | **bool** | Indicates if the questions are anabled for the given advertisement. | [optional] 
**additional_images** | [**list[Image]**](Image.md) | Holds the images other than the primary image, which is returned in the &#x60;image&#x60; field  | [optional] 
**addresses** | [**list[Address]**](Address.md) | (Deprecated) The addresses (belonging to the advertisement&#39;s owner) where this  advertisement is available.  | [optional] 
**user_addresses** | [**list[Address]**](Address.md) | The addresses (belonging to the advertisement&#39;s owner) where this  advertisement is available.  | [optional] 
**ad_addresses** | [**list[Address]**](Address.md) | The custom addresses where this advertisement is available.  | [optional] 
**questions** | [**list[AdQuestionView]**](AdQuestionView.md) | The list of questions this advertisement has.  | [optional] 
**allow_decimal** | **bool** | if true then this webshop ad can be ordered specifying the quantity  as a decimal number.  | [optional] 
**delivery_methods** | [**list[AdDeliveryMethod]**](AdDeliveryMethod.md) | The available delivery methods for this webshop ad. | [optional] 
**max_allowed_in_cart** | [**BigDecimal**](BigDecimal.md) | The maximum quantity that can be specified in the shopping cart.  | [optional] 
**min_allowed_in_cart** | [**BigDecimal**](BigDecimal.md) | The minimum quantity that can be specified in the shopping cart.        | [optional] 
**product_number** | **str** | The product number according to the webshop settings. | [optional] 
**stock_quantity** | [**BigDecimal**](BigDecimal.md) | The stock disponibility. Only if &#x60;unlimitedStock&#x60; is false and the  &#39;Stock type&#39; was not marked as &#39;Not available&#39; (through the web  interface).  | [optional] 
**unlimited_stock** | **bool** | If true then it means there is always disponibility of the webshop ad. | [optional] 
**operations** | [**list[Operation]**](Operation.md) | List of runnable custom operations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


