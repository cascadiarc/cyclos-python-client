# RedeemVoucherError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**RedeemVoucherErrorCode**](RedeemVoucherErrorCode.md) | Possible errors when redeeming a voucher Possible values are: * notAllowedForUser: This user cannot redeem this voucher * notAllowedForVoucher: This voucher cannot be redeemed * notAllowedToday: This voucher cannot be redeemed today  * notAllowedYet: The redeem period for this voucher has not arrived yet * payment: There was an error when performing the payment * unexpected: An unexpected error has occurred. See the &#x60;exceptionType&#x60; and &#x60;exceptionMessage&#x60; fields for the internal information. * userBlocked: The user has been blocked by exceeding redeem tries  | [optional] 
**voucher_status** | [**VoucherStatusEnum**](VoucherStatusEnum.md) | Only if &#x60;code&#x60; is &#x60;notAllowedForVoucher&#x60; Possible values are: * canceled: The voucher was canceled, and cannot be further used * expired: The voucher has expired without being redeemed * open: The voucher has been generated / bought, and is open * pending: The voucher has been bought, and the corresponding payment is pending for authorization * redeemed: The voucher has been redeemed, and the corresponding payment was done  | [optional] 
**allowed_days** | [**list[WeekDayEnum]**](WeekDayEnum.md) | Only if &#x60;code&#x60; is &#x60;notAllowedToday&#x60; Possibles values for each array element are: * fri: Friday * mon: Monday * sat: Saturday * sun: Sunday * thu: Thursday * tue: Tuesday * wed: Wednesday  | [optional] 
**redeem_after_date** | **datetime** | Indicates the date after which this voucher can be redeemed. Only if &#x60;code&#x60; is &#x60;notAllowedYet&#x60;.  | [optional] 
**payment_error** | [**PaymentError**](PaymentError.md) | The &#x60;PaymentError&#x60; generated when the voucher payment was being created. Only if &#x60;code&#x60; is &#x60;payment&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


