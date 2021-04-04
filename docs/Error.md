# Error

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**ErrorKind**](ErrorKind.md) | Error types associated to the HTTP Status 500 Possible values are: * buyVoucher: An error has occurred when buying a voucher  * forgottenPassword: An error has occurred when changing a forgotten password. * general: An unexpected error has occurred * initializeNfc: An error has occurred when initializing a NFC token * nested: An error which has another internal error at a given property / index * nfcAuth: An error has occurred when making an external NFC authentication * otp: An error has occurred requesting an OTP * payment: An error has occurred when making a payment * personalizeNfc: An error has occurred when personalizing a NFC token * pos: An error has occurred when receiving a payment on a POS operation * redeemVoucher: An error has occurred when redeeming a voucher * shoppingCart: An error has occurred when interacting with a shopping cart. * shoppingCartCheckout: An error has occurred when checking out a shopping cart.  | [optional] 
**exception_type** | **str** | The server exception class name (not intended to be shown to  final users. Only for logging purposes)  | 
**exception_message** | **str** | The server exception message (not intended to be shown to  final users. Only for logging purposes)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


