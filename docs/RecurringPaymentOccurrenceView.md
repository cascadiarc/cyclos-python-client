# RecurringPaymentOccurrenceView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The occurrence number. | [optional] 
**_date** | **datetime** | The occurrence date. | [optional] 
**amount** | [**BigDecimal**](BigDecimal.md) | The installment amount | [optional] 
**status** | [**RecurringPaymentOccurrenceStatusEnum**](RecurringPaymentOccurrenceStatusEnum.md) | The status of a recurring payment occurrence Possible values are: * failed: The occurrence has failed processing (probably because there was not enough funds in the payer account) * processed: The occurrence was correctly processed, generating a transfer  | [optional] 
**by** | [**User**](User.md) | The user that performed an status change. For example, who manually paid, settled or canceled an open installment  | [optional] 
**transfer_id** | **str** | Only if the occurrence was processed, contains the internal identifier of the generated transfer.  | [optional] 
**transaction_number** | **str** | Only if the occurrence was processed, contains the transaction number of the generated transfer.  | [optional] 
**transfer_date** | **datetime** | The date the occurrence was processed. It might happen that the occurrence has first failed, then later processed  | [optional] 
**can_process** | **bool** | Can the authenticated user process this failed occurrence? | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


