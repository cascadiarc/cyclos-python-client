# TransactionPreview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation_message** | **str** | If configured in the payment type, is a message to be shown to the user before confirming the transaction  | [optional] 
**confirmation_password_input** | [**PasswordInput**](PasswordInput.md) | If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).  | [optional] 
**payment_type** | [**TransferType**](TransferType.md) | The payment type reference | [optional] 
**currency** | [**Currency**](Currency.md) | The currency of the payment | [optional] 
**from_account** | [**AccountWithOwner**](AccountWithOwner.md) | A reference to the origin account | [optional] 
**total_amount** | [**BigDecimal**](BigDecimal.md) | The final amount charged to the payer including fees. | [optional] 
**custom_values** | [**list[CustomFieldValue]**](CustomFieldValue.md) | The list of custom field values, in a detailed view | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


