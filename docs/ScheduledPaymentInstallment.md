# ScheduledPaymentInstallment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The installment number. | [optional] 
**due_date** | **datetime** | The installment due date. | [optional] 
**amount** | [**BigDecimal**](BigDecimal.md) | The installment amount | [optional] 
**status** | [**ScheduledPaymentInstallmentStatusEnum**](ScheduledPaymentInstallmentStatusEnum.md) | The status of a scheduled payment installment Possible values are: * blocked: The installment is blocked, and won&#39;t be automatically processed on its due date * canceled: The installment was canceled * failed: The installment processing failed, for example, because there was no funds in the source account * processed: The installment was processed, generating a transfer * scheduled: The installment is scheduled for a future date * settled: The installment was marked as settled by the receiver  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


