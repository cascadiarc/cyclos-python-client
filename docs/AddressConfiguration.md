# AddressConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_map** | **bool** | Indicates whether maps are enabled in Cyclos | [optional] 
**enabled_fields** | [**list[AddressFieldEnum]**](AddressFieldEnum.md) | Contains the address fields that are enabled in Cyclos Possibles values for each array element are: * addressLine1: The first line of the descriptive address * addressLine2: The second line of the descriptive address * buildingNumber: The numeric identifier for a land parcel, house, building or other * city: The city name * complement: The complement (like apartment number)   * country: The country, represented as 2-letter, uppercase, ISO 3166-1 code * neighborhood: The neighborhood name  * poBox: The post-office box, is an uniquely addressable box * region: The region or state * street: The street name * zip: A zip code that identifies a specific geographic (postal) delivery area  | [optional] 
**required_fields** | [**list[AddressFieldEnum]**](AddressFieldEnum.md) | Contains the address fields that are required in Cyclos Possibles values for each array element are: * addressLine1: The first line of the descriptive address * addressLine2: The second line of the descriptive address * buildingNumber: The numeric identifier for a land parcel, house, building or other * city: The city name * complement: The complement (like apartment number)   * country: The country, represented as 2-letter, uppercase, ISO 3166-1 code * neighborhood: The neighborhood name  * poBox: The post-office box, is an uniquely addressable box * region: The region or state * street: The street name * zip: A zip code that identifies a specific geographic (postal) delivery area  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


