# PrincipalTypeInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field** | [**CustomFieldDetailed**](CustomFieldDetailed.md) | If this principal is based on a custom field, holds its definition  | [optional] 
**token_type** | [**TokenTypeEnum**](TokenTypeEnum.md) | If this principal is a token, contains its type Possible values are: * barcode: A barcode with the token * nfcDevice: A device (e.g. cell phone) with support for NFC * nfcTag: A NFC tag/card  * other: Any other type containing a token * qrcode: A QR code containing a token * swipe: A swipe/magnetic card containing the token  | [optional] 
**mask** | **str** | If this principal is either a token or account number, holds the (optional) mask which clients can use to input the value.  | [optional] 
**allow_manual_input** | **bool** | Only returned if &#x60;kind&#x60; is &#x60;token&#x60;. Specifies if the principal type allows enter manually the token value.  | [optional] 
**example** | **str** | If this principal is mobile phone, holds an example number.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


