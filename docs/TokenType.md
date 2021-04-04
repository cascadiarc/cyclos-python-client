# TokenType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physical_type** | [**PhysicalTokenTypeEnum**](PhysicalTokenTypeEnum.md) | The possible physical type for tokens. Determines how applications interact with hardware in order to read the token value. Possible values are: * barcode: A 1d barcode printed on a card * nfcDevice: A phone (or other device) with NFC support * nfcTag: A NFC tag, normally a DESFire NFC card * other: Other * qrCode: A QR-code * swipe: A swipe card  | [optional] 
**mask** | **str** | In case the token value is entered by users or formatted, this is the (optional) mask to be used.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


