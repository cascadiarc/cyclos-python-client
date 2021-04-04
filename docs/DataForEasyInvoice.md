# DataForEasyInvoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | [**User**](User.md) | The destination user details. Is only returned if called with a logged user or if the user&#39;s group is visible to guests accoerding to the current configuration.   | [optional] 
**amount** | [**BigDecimal**](BigDecimal.md) | The easy invoice amount | [optional] 
**currency** | [**Currency**](Currency.md) | The easy invoice currency. | [optional] 
**payment_type_data** | [**TransactionTypeData**](TransactionTypeData.md) | Contains the detailed data for the selected (or first) payment type. Only returned if there is a logged user. The custom fields will only contain those without a fixed value.  | [optional] 
**payment_types** | [**list[TransferTypeWithCurrency]**](TransferTypeWithCurrency.md) | Only returned if there is a logged user, and a specific payment type was not informed. Contains the allowed payment types to the given user.  | [optional] 
**custom_values** | [**list[CustomFieldValue]**](CustomFieldValue.md) | The list of custom field values with a fixed value, as requested.   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


