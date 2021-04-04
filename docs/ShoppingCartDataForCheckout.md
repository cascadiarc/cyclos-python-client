# ShoppingCartDataForCheckout

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cart** | [**ShoppingCartView**](ShoppingCartView.md) | The cart containing the currency and items. | [optional] 
**payment_types** | [**list[TransferType]**](TransferType.md) | Contains the allowed payment types. | [optional] 
**delivery_methods** | [**list[AdDeliveryMethod]**](AdDeliveryMethod.md) | The list of delivery method commons to all of the products added to the  shopping cart ordered by name.  | [optional] 
**address_configuration** | [**AddressConfiguration**](AddressConfiguration.md) | Configuration data for addresses. | [optional] 
**confirmation_password_input** | [**PasswordInput**](PasswordInput.md) | If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).  | [optional] 
**addresses** | [**list[Address]**](Address.md) | The addresses the logged user (i.e the buyer) has.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


