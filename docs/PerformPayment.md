# PerformPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduling** | [**PaymentSchedulingEnum**](PaymentSchedulingEnum.md) | Determines how a payment is scheduled. When not specified, direct payments are performed. Possible values are: * direct: The payment won&#39;t be scheduled, but paid directly * recurring: The payment will be recurring, repeated either by a limited number of occurrences or until cancel * scheduled: The payment will be scheduled, either to a single future date or multiple installments  | [optional] 
**installments_count** | **int** | Represents the number of installments. When not specified, assumes a single installment. Used only if &#x60;scheduling&#x60; is &#x60;scheduled&#x60;. Can be used together with &#x60;installmentsCount&#x60; as an alternative to providing individual &#x60;installments&#x60; definitions.  | [optional] 
**first_installment_date** | **datetime** | Represents the first installment date. When not specified, assumes the first installment is processed instantly. Used only if &#x60;scheduling&#x60; is &#x60;scheduled&#x60;. Can be used together with &#x60;installmentsCount&#x60; as an alternative to providing individual &#x60;installments&#x60; definitions.  | [optional] 
**installments** | [**list[PerformScheduledPaymentInstallment]**](PerformScheduledPaymentInstallment.md) | An array containing individual installments definitions, allowing full control over generated installments. Used only if &#x60;scheduling&#x60; is &#x60;scheduled&#x60;.  | [optional] 
**occurrences_count** | **int** | Represents the number of occurrences in a recurring payment. When not provided, the payment will be repeated until it is manually canceled. Used only if &#x60;scheduling&#x60; is &#x60;recurring&#x60;.  | [optional] 
**first_occurrence_date** | **datetime** | Represents the first occurrence date for a recurring payment. If none is given, it is assumed that the first occurrence is immediate. Used only if &#x60;scheduling&#x60; is &#x60;recurring&#x60;.  | [optional] 
**occurrence_interval** | [**TimeInterval**](TimeInterval.md) | Defines the interval between payment occurrences. If none is given, it is assumed 1 month between occurrences. Used only if &#x60;scheduling&#x60; is &#x60;recurring&#x60;.  | [optional] 
**nfc_challence** | **str** | If this payment is performed with a NFC token, must be the challenge (as returned by the server) encrypted by the NFC chip, encoded in HEX form (2 hex chars per byte).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


