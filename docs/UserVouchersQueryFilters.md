# UserVouchersQueryFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_range** | [**list[BigDecimal]**](BigDecimal.md) | The minimum / maximum voucher amount  | [optional] 
**creation_period** | **list[datetime]** | The minimum / maximum voucher creation date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**expiration_period** | **list[datetime]** | The minimum / maximum voucher expiration date Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**redeem_period** | **list[datetime]** | The minimum / maximum voucher redeem date Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**token** | **str** | The voucher token (with or without mask) | [optional] 
**types** | **list[str]** | The ids or internal names of voucher types | [optional] 
**statuses** | [**list[VoucherStatusEnum]**](VoucherStatusEnum.md) | The voucher statuses Possibles values for each array element are: * canceled: The voucher was canceled, and cannot be further used * expired: The voucher has expired without being redeemed * open: The voucher has been generated / bought, and is open * pending: The voucher has been bought, and the corresponding payment is pending for authorization * redeemed: The voucher has been redeemed, and the corresponding payment was done  | [optional] 
**relation** | [**VoucherRelationEnum**](VoucherRelationEnum.md) | Indicates the relation used to filter the vouchers. Possible values are: * bought: A voucher the user has bought * redeemed: A voucher the user has redeemed  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


