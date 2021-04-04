# ShoppingCartError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**ShoppingCartErrorCode**](ShoppingCartErrorCode.md) | Possible errors when interacting with a shopping cart. Possible values are: * canNotBuyFromSeller: The authenticated user is not visible by the webshop&#39;s seller * notEnoughStock: There is not enough stock of the webshop ad to fulfill the requested quantity * unexpected: An unexpected error has occurred. See the &#x60;exceptionType&#x60; and &#x60;exceptionMessage&#x60; fields for the internal information.   | [optional] 
**ad** | [**WebshopAd**](WebshopAd.md) | The webshop ad for which there is not enough stock.  Only if &#x60;code&#x60; is &#x60;notEnoughStock&#x60;  | [optional] 
**seller** | [**User**](User.md) | The seller whose webshop ad can not be bought. Only if &#x60;code&#x60; is &#x60;canNotBuyFromSeller&#x60;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


