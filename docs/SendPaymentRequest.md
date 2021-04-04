# SendPaymentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_date** | **datetime** | The payment request expiration date. Required, unless the expiration date is configured in the payment type to be hidden from users. | [optional] 
**scheduling** | [**PaymentRequestSchedulingEnum**](PaymentRequestSchedulingEnum.md) | Determines how a payment request is scheduled. When not specified, the payment request is processed directly. Possible values are: * direct: The scheduled payment won&#39;t be scheduled, but paid directly * scheduled: The scheduled payment will be scheduled, once accepting, triggering a given number of installments  | [optional] 
**first_installment_is_immediate** | **bool** | Indicates whether the first installment should be immediately processed once the scheduled payment is accepted. Used only if &#x60;scheduling&#x60; is &#x60;scheduled&#x60;. When not explicitly set to &#x60;false&#x60; will process the first installment immediately.  | [optional] 
**installments_count** | **int** | Represents the number of installments. When not specified, assumes a single installment. Used only if &#x60;scheduling&#x60; is &#x60;scheduled&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


