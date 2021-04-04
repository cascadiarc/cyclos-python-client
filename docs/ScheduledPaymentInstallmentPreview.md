# ScheduledPaymentInstallmentPreview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The installment number | [optional] 
**due_date** | **datetime** | The installment due date | [optional] 
**total_amount** | [**BigDecimal**](BigDecimal.md) | The final total installment amount | [optional] 
**main_amount** | [**BigDecimal**](BigDecimal.md) | Depending on the configured fees, it could happen that the main amount is deducted from fees amount. This reflects the new main amount. If no fees deduct, it will be the same as &#x60;totalAmount&#x60;.  | [optional] 
**fees** | [**list[TransferFeePreview]**](TransferFeePreview.md) | Only returned for direct payments. Contains the fees that would be paid by the payer if the payment is confirmed.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


