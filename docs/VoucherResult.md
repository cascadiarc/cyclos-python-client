# VoucherResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer** | [**User**](User.md) | The voucher buyer. Is not returned when the voucher was generated or when searching for bought vouchers of a user.  | [optional] 
**creation_date** | **datetime** | The date a voucher was generated or bought | [optional] 
**expiration_date** | **datetime** | The date a voucher expires | [optional] 
**redeemer** | [**User**](User.md) | The voucher redeemer. Is not returned when the voucher was not yet redeemed or when searching for redeemed vouchers of a user.  | [optional] 
**redeem_date** | **datetime** | The date a voucher was redeemed (if so) | [optional] 
**redeem_after_date** | **datetime** | The date after which the voucher can be redeemed. Is only returned if the voucher &#x60;status&#x60; is &#x60;open&#x60;.  | [optional] 
**redeem_on_week_days** | [**list[WeekDayEnum]**](WeekDayEnum.md) | The days of the week a voucher can be redeemed. Is only returned if the voucher &#x60;status&#x60; is &#x60;open&#x60;. Possibles values for each array element are: * fri: Friday * mon: Monday * sat: Saturday * sun: Sunday * thu: Thursday * tue: Tuesday * wed: Wednesday  | [optional] 
**type** | [**VoucherType**](VoucherType.md) | The voucher type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


