# BasicUserQueryFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users_to_exclude** | **list[str]** | Indicated the users to be excluded from the result  | [optional] 
**users_to_include** | **list[str]** | Indicated the users to be included in the result.  Any other user not present in this list will be excluded from the result.  | [optional] 
**activation_period** | **list[datetime]** | The minimum / maximum user activation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**creation_period** | **list[datetime]** | The minimum / maximum user creation date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**last_login_period** | **list[datetime]** | The minimum / maximum user last login date. Only taken into account if searching as administrator or managing broker. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**groups** | **list[str]** | Either id or internal names of groups / group sets | [optional] 
**brokers** | **list[str]** | Either id or a principal (login name, e-mail, etc) for brokers | [optional] 
**main_broker_only** | **bool** | When set to &#x60;true&#x60;, will match only users that have the brokers as set in the &#x60;brokers&#x60; parameter as main broker.   | [optional] 
**include_group** | **bool** | When set to &#x60;true&#x60; and the logged user has permission to view user groups, will return the &#x60;group&#x60; property on users.   | [optional] 
**include_group_set** | **bool** | When set to &#x60;true&#x60; and the logged user has permission to view user group sets, will return the &#x60;groupSet&#x60; property on users.   | [optional] 
**address_result** | [**UserAddressResultEnum**](UserAddressResultEnum.md) | Determines which address is returned on the search, if any. By default no addresses are returned. This option is useful for displaying results as locations on a map. In all cases only located addresses (those that have the geographical coordinates set) are returned. When returning all addresses, data related with multiple addresses is returned multiple times. Possible values are: * all: All addresses are returned. * nearest: The nearest address from the reference location is returned. Only usable if a reference coordinate (&#x60;latitude&#x60; and &#x60;longitude&#x60;) * none: Addresses are not returned. * primary: The primary (default) user address is returned  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


