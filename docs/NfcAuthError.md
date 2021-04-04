# NfcAuthError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**NfcAuthErrorCode**](NfcAuthErrorCode.md) | Application-specific error codes for an NFC authentication error  Possible values are: * pos: A POS exception has happened when trying to make an external authenticate. See the &#x60;posError&#x60; field for more details.   * unexpected: An unexpected error has occurred. See the &#x60;exceptionType&#x60; and &#x60;exceptionMessage&#x60; fields for the internal information.  | [optional] 
**pos_error** | [**PosError**](PosError.md) | The POS error details. Only if &#x60;code&#x60; is &#x60;pos&#x60;            | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


