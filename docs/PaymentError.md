# PaymentError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**PaymentErrorCode**](PaymentErrorCode.md) | Application-specific error codes for a payment error  Possible values are: * dailyAmountExceeded: The maximum amount allowed per day was exceeded.   * dailyPaymentsExceeded: The maximum count of payments allowed per day was exceeded. * destinationUpperLimitReached: The upper balance limit of the destination account was exceeded. * insufficientBalance: The account selected for the payment does not have enough balance * monthlyAmountExceeded: The maximum amount allowed per month was exceeded. * monthlyPaymentsExceeded: The maximum count of payments allowed per month was exceeded. * pos: A POS exception has happened when performing this payment. See the &#x60;posError&#x60; field for more details.    * timeBetweenPaymentsNotMet: The minimum time between payments was not met. * unexpected: An unexpected error has occurred. See the &#x60;exceptionType&#x60; and &#x60;exceptionMessage&#x60; fields for the internal information. * weeklyAmountExceeded: The maximum amount allowed per week was exceeded. * weeklyPaymentsExceeded: The maximum count of payments allowed per week was exceeded.  | [optional] 
**currency** | [**Currency**](Currency.md) | Currency reference. Only if &#x60;code&#x60; is &#x60;dailyAmountExceeded&#x60;, &#x60;weeklyAmountExceeded&#x60; or &#x60;monthlyAmountExceeded&#x60;            | [optional] 
**max_amount** | [**BigDecimal**](BigDecimal.md) | The maximum amount. Only if &#x60;code&#x60; is &#x60;dailyAmountExceeded&#x60;, &#x60;weeklyAmountExceeded&#x60; or &#x60;monthlyAmountExceeded&#x60;            | [optional] 
**max_payments** | **int** | The maximum payments count. Only if &#x60;code&#x60; is &#x60;dailyPaymentsExceeded&#x60;, &#x60;weeklyPaymentsExceeded&#x60; or &#x60;monthlyPaymentsExceeded&#x60;            | [optional] 
**pos_error** | [**PosError**](PosError.md) | The POS error details. Only if &#x60;code&#x60; is &#x60;pos&#x60;            | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


