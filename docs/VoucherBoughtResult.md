# VoucherBoughtResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vouchers** | **list[str]** | The identifiers of all bought vouchers. | [optional] 
**voucher_status** | [**VoucherStatusEnum**](VoucherStatusEnum.md) | The status of all bought vouchers. Possible values are: * canceled: The voucher was canceled, and cannot be further used * expired: The voucher has expired without being redeemed * open: The voucher has been generated / bought, and is open * pending: The voucher has been bought, and the corresponding payment is pending for authorization * redeemed: The voucher has been redeemed, and the corresponding payment was done  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


