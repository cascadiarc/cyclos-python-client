# ShoppingCartCheckoutError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**ShoppingCartCheckoutErrorCode**](ShoppingCartCheckoutErrorCode.md) | Possible errors when checking out a shopping cart. Possible values are: * insufficientBalance: The origin account of the selected payment type used to make the amount reservation does not have enough balance. * products: There was an error related to the products contained in he shopping cart. * unexpected: An unexpected error has occurred. See the &#x60;exceptionType&#x60; and &#x60;exceptionMessage&#x60; fields for the internal information.  | [optional] 
**shopping_cart_error** | [**ShoppingCartError**](ShoppingCartError.md) | The &#x60;ShoppingCartError&#x60; generated when the products in the cart were being validated.  Only if &#x60;code&#x60; is &#x60;products&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


