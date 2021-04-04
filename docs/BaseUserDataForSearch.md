# BaseUserDataForSearch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_keywords** | **bool** | Indicates whether using keywords is allowed | [optional] 
**fields_in_search** | **list[str]** | The internal names of either basic or custom profile fields which  can be used as search filters (separated fields, not keywords)   | [optional] 
**address_fields_in_search** | [**list[AddressQueryFieldEnum]**](AddressQueryFieldEnum.md) | Fields which can be used when filtering by user address, by using the &#x60;address.&lt;addressField&gt;&#x60; name Possibles values for each array element are: * address: Filters by any field in the street address: &#x60;addressLine1&#x60;, &#x60;addressLine2&#x60;, &#x60;street&#x60;, &#x60;buildingNumber&#x60; or &#x60;complement&#x60;   * city: Filters by city name * country: Filters by country, represented as 2-letter, uppercase, ISO 3166-1 code (exact match) * neighborhood: Filters by neighborhood name  * poBox: Filters by post-office box (exact match) * region: Filters by region or state * zip: Filters by zip (postal) code (exact match)  | [optional] 
**basic_fields** | [**list[BasicProfileFieldInput]**](BasicProfileFieldInput.md) | The list of basic profile fields that can be used either as search filters (if the internal names are present in the &#x60;fieldsInSearch&#x60; property) or on the result list (if the internal names are present in the &#x60;fieldsInList&#x60; property)  | [optional] 
**custom_fields** | [**list[CustomFieldDetailed]**](CustomFieldDetailed.md) | The list of custom profile fields that can be used either as search filters (if the internal names are present in the &#x60;fieldsInSearch&#x60; property) or on the result list (if the internal names are present in the &#x60;fieldsInList&#x60; property)  | [optional] 
**groups** | [**list[Group]**](Group.md) | The groups the authenticated user can use to filter users. Admins can always filter by groups, while users depend on a permission, which can be to only view group sets, only groups or none.  | [optional] 
**search_by_distance_data** | [**SearchByDistanceData**](SearchByDistanceData.md) | Data for searching users by distance | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


