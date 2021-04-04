# AdDataForSearch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**list[Group]**](Group.md) | The groups the authenticated user can use to filter users. Admins can always filter by groups, while users depend on a permission, which can be to only view group sets, only groups or none.  | [optional] 
**default_groups** | **list[str]** | The internal names (or ids, if missing) of the groups which should be presented by default on user search  | [optional] 
**query** | [**AdQueryFilters**](AdQueryFilters.md) | Default query filters to search advertisements  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


