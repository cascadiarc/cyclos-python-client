# ImagesListData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_manage** | **bool** | Does the authenticated user has permission to manage these images?  | [optional] 
**can_create** | **bool** | Does the authenticated user has permission to create a new image?  | [optional] 
**max_images** | **int** | The maximum number of images allowed | [optional] 
**availability** | [**AvailabilityEnum**](AvailabilityEnum.md) | The availability for images Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required  | [optional] 
**images** | [**list[Image]**](Image.md) | The list of images | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


