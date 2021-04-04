# ConflictError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**ConflictErrorCode**](ConflictErrorCode.md) | Error codes for 409 Conflict entity HTTP status  Possible values are: * constraintViolatedOnRemove: An attempt to remove some entity has failed, probably because that entity is in use, that is, is being referenced by some other entity.  * staleEntity: Failure in the optimistic lock. It means some entity was fetched for editing by 2 clients. Then they both saved it. The first one is successful, but the second one will fail. If you get this error, make sure the &#x60;version&#x60; field is being sent with the correct value, as fetched from the server.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


