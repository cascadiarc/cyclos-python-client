# Voucher

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**VoucherStatusEnum**](VoucherStatusEnum.md) | The voucher statuses Possible values are: * canceled: The voucher was canceled, and cannot be further used * expired: The voucher has expired without being redeemed * open: The voucher has been generated / bought, and is open * pending: The voucher has been bought, and the corresponding payment is pending for authorization * redeemed: The voucher has been redeemed, and the corresponding payment was done  | [optional] 
**amount** | [**BigDecimal**](BigDecimal.md) | The voucher amount | [optional] 
**token** | **str** | The voucher token | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


