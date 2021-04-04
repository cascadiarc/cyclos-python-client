# BadRequestError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**BadRequestErrorCode**](BadRequestErrorCode.md) | Error codes for 400 Bad request HTTP status  Possible values are: * general: Bad request format * json: Error in the JSON format  | [optional] 
**message** | **str** | A (technical) message explaining the problem | [optional] 
**line** | **int** | The request body line that shows the problem | [optional] 
**column** | **int** | The request body column that shows the problem | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


