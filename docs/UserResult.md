# UserResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user&#39;s full name | [optional] 
**username** | **str** | The user&#39;s login name | [optional] 
**email** | **str** | The user&#39;s e-mail | [optional] 
**address** | [**Address**](Address.md) | Address to be placed on map. Is only returned when the search result type is &#x60;map&#x60;.  | [optional] 
**distance** | **float** | Only returned when there is a base location to calculate the distance from. The unit (kilometers or miles) depends on configuration.  | [optional] 
**custom_values** | **dict(str, str)** | Holds the values for custom fields, keyed by field internal name or id. The format of the value depends on the custom field type. Example: &#x60;{..., \&quot;customValues\&quot;: {\&quot;gender\&quot;: \&quot;male\&quot;, \&quot;birthDate\&quot;: \&quot;1980-10-27\&quot;}}&#x60;  | [optional] 
**phone** | **str** | First phone number, used when phone is marked on products to be returned on user list  | [optional] 
**account_number** | **str** | First account number, used when account number is marked on products to be returned on user list  | [optional] 
**group** | [**EntityReference**](EntityReference.md) | The user group. Only returned when the &#x60;includeGroup&#x60; parameter is set to &#x60;true&#x60; and the current user can see other users&#39; groups.  | [optional] 
**group_set** | [**EntityReference**](EntityReference.md) | The user group. Only returned when the &#x60;includeGroupSet&#x60; parameter is set to &#x60;true&#x60; and the current user can see other users&#39; group set.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


