# BaseAdDataForSearch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible_kinds** | [**list[AdKind]**](AdKind.md) | The advertisement kinds that can be searched by the authenticated user Possibles values for each array element are: * simple: A simple advertisement that can be viewed, but not directly bought * webshop: An advertisement that is part of an webshop. Can be bought, there is stock management, etc.  | [optional] 
**categories** | [**list[AdCategoryWithChildren]**](AdCategoryWithChildren.md) | The advertisement categories each with its children, forming a tree  | [optional] 
**custom_fields** | [**list[CustomFieldDetailed]**](CustomFieldDetailed.md) | The list of custom fields that are either to be used as search filter (if its internal name is present on either  &#x60;fieldsInBasicSearch&#x60; or &#x60;fieldsInAdvancedSearch&#x60;) and / or in the result list (if its internal name is present on &#x60;fieldsInList&#x60;).   | [optional] 
**fields_in_basic_search** | **list[str]** | The internal names of the custom fields that should be used as search filters in the basic section (separated fields, not keywords)  | [optional] 
**fields_in_advanced_search** | **list[str]** | The internal names of the custom fields that should be used as search filters in the advanced section (separated fields, not keywords)  | [optional] 
**fields_in_list** | **list[str]** | The internal names of the custom fields that will be returned together with each advertisement, and should be shown in the result list. This feature is planned, but not yet available.  | [optional] 
**basic_profile_fields** | [**list[BasicProfileFieldInput]**](BasicProfileFieldInput.md) | The list of basic user profile fields that can be used as search filters. Only returned if searching user advertisements.  | [optional] 
**address_fields_in_search** | [**list[AddressQueryFieldEnum]**](AddressQueryFieldEnum.md) | Fields which can be used when filtering by user address, by using the &#x60;address.&lt;addressField&gt;&#x60; name Possibles values for each array element are: * address: Filters by any field in the street address: &#x60;addressLine1&#x60;, &#x60;addressLine2&#x60;, &#x60;street&#x60;, &#x60;buildingNumber&#x60; or &#x60;complement&#x60;   * city: Filters by city name * country: Filters by country, represented as 2-letter, uppercase, ISO 3166-1 code (exact match) * neighborhood: Filters by neighborhood name  * poBox: Filters by post-office box (exact match) * region: Filters by region or state * zip: Filters by zip (postal) code (exact match)  | [optional] 
**custom_profile_fields** | [**list[CustomFieldDetailed]**](CustomFieldDetailed.md) | The list of custom user profile fields that can be used as search filters. Only returned if searching user advertisements.  | [optional] 
**currencies** | [**list[Currency]**](Currency.md) | The currencies the authenticated user may use to filter by price   | [optional] 
**search_by_distance_data** | [**SearchByDistanceData**](SearchByDistanceData.md) | Data for searching advertisements by distance | [optional] 
**categories_display** | [**AdCategoriesDisplayEnum**](AdCategoriesDisplayEnum.md) | The category view configured for the logged user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


