# UserAddressesListData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_manage** | **bool** | Indicates whether the addresses can be managed by the authenticated user  | [optional] 
**can_create** | **bool** | Indicates whether the authenticated user can create a new address for this user  | [optional] 
**max_addresses** | **int** | Indicates the maximum number of addresses the user can have  | [optional] 
**availability** | [**AvailabilityEnum**](AvailabilityEnum.md) | The availability for addresses Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required  | [optional] 
**addresses** | [**list[AddressResult]**](AddressResult.md) | The address list | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


