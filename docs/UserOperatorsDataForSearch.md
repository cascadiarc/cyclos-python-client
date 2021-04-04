# UserOperatorsDataForSearch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_create_new** | **bool** | Indicates whether the authenticated user can create more operators  for the specified user  | [optional] 
**groups** | [**list[EntityReference]**](EntityReference.md) | The operator groups this user owns | [optional] 
**fields_in_list** | **list[str]** | The internal names of either basic or custom profile fields that are configured to be shown on the list. This actually defines the fields that will be loaded on the result. It is possible that no fields are configured to be returned on list. In this case, the result objects will have the &#39;display&#39; property loaded with what is configured to be the user formatting field(s).   | [optional] 
**basic_fields** | [**list[BasicProfileFieldInput]**](BasicProfileFieldInput.md) | The basic profile fields in the result list | [optional] 
**custom_fields** | [**list[CustomFieldDetailed]**](CustomFieldDetailed.md) | The custom profile fields in the result list | [optional] 
**query** | [**UserOperatorsQueryFilters**](UserOperatorsQueryFilters.md) | Default query filters to search a user&#39;s operators  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


