# BuyVoucherError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**BuyVoucherErrorCode**](BuyVoucherErrorCode.md) | Possible errors when buying a voucher Possible values are: * maxAmountForPeriod: The maximum allowed buy amount for a period (example, a month) has been exceeded * maxOpenAmount: The maximum open amount for this voucher type for the buyer user has been exceeded * maxTotalOpenAmount: The maximum total open amount for this voucher type, for all users, has been exceeded * notAllowedForUser: The user attempting to buy vouchers is not allowed to buy vouchers of this type * payment: There was an error when performing the payment * unexpected: An unexpected error has occurred. See the &#x60;exceptionType&#x60; and &#x60;exceptionMessage&#x60; fields for the internal information.  | [optional] 
**currency** | [**Currency**](Currency.md) | Currency reference. Only if &#x60;code&#x60; is &#x60;maxAmountForPeriod&#x60; or &#x60;maxTotalOpenAmount&#x60;            | [optional] 
**amount_left_for_buying** | [**BigDecimal**](BigDecimal.md) | Indicates the maximum amount the user can buy this time without exceeding the maximum. Only if &#x60;code&#x60; is &#x60;maxAmountForPeriod&#x60;.  | [optional] 
**date_allowed_again** | **datetime** | Indicates the date this user will be able to buy vouchers again for this type. Only if &#x60;code&#x60; is &#x60;maxAmountForPeriod&#x60;.  | [optional] 
**current_open_amount** | [**BigDecimal**](BigDecimal.md) | Indicates the current total amount that is open. Only if &#x60;code&#x60; is &#x60;maxOpenAmount&#x60; or &#x60;maxTotalOpenAmount&#x60;.  | [optional] 
**max_open_amount** | [**BigDecimal**](BigDecimal.md) | Indicates the maximum total open amount. Only if &#x60;code&#x60; is &#x60;maxOpenAmount&#x60; or &#x60;maxTotalOpenAmount&#x60;.  | [optional] 
**payment_error** | [**PaymentError**](PaymentError.md) | The &#x60;PaymentError&#x60; generated when the voucher payment was being created. Only if &#x60;code&#x60; is &#x60;payment&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


