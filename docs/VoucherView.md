# VoucherView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The voucher title when it was created. | [optional] 
**description** | **str** | The voucher description when it was created. | [optional] 
**creation_type** | [**VoucherCreationTypeEnum**](VoucherCreationTypeEnum.md) | Indicates how a voucher was created Possible values are: * bought: The voucher was bought by an user * generated: The voucher was generated by an administrator  | [optional] 
**buy** | [**Transaction**](Transaction.md) | The transaction which bought this voucher, if any and visible.  | [optional] 
**redeem_date** | **datetime** | The date the voucher was redeemer, if any. | [optional] 
**redeem** | [**Transaction**](Transaction.md) | The transaction which redeemed this voucher, if any and visible.  | [optional] 
**can_cancel** | **bool** | (Deprecated) Can the authenticated user cancel this voucher? | [optional] 
**cancel_action** | [**VoucherCancelActionEnum**](VoucherCancelActionEnum.md) | Indicates what happens if a voucher is canceled, if it can be canceled Possible values are: * cancelAndRefund: A single bought voucher is canceled and the amount is refunded * cancelGenerated: Cancels a single generated voucher * cancelPendingPack: Cancels more than one bought vouchers whose buy payment is pending authorization * cancelPendingSingle: Cancels a single bought vouchers whose buy payment is pending authorization  | [optional] 
**show_configuration** | **bool** | Should the voucher configuration be shown to users? This flag is &#x60;true&#x60; when there are multiple available configurations.  | [optional] 
**show_qr_code** | **bool** | Should the voucher token be shown as QR-code for users? | [optional] 
**redeem_after_date_reached** | **bool** | Should the voucher be available to be redeemed? | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


