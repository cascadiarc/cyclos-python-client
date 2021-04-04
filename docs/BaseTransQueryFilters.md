# BaseTransQueryFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_period** | **list[datetime]** | The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 
**transfer_filters** | **list[str]** | Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format &#x60;accountType.transferFilter&#x60;.  | [optional] 
**transfer_types** | **list[str]** | Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format &#x60;accountType.transferType&#x60;.  | [optional] 
**transaction_number** | **str** | The transaction number of the matching transfer  | [optional] 
**user** | **str** | Reference a user that should have either received / performed the transfer.  | [optional] 
**groups** | **list[str]** | Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.  | [optional] 
**by** | **str** | Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.  | [optional] 
**broker** | **str** | Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.  | [optional] 
**channels** | **list[str]** | Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.  | [optional] 
**excluded_ids** | **list[str]** | List of transfers ids to be excluded from the result.  | [optional] 
**access_clients** | **list[str]** | References to access clients (id or token) used to perform / receive the  transfer.  | [optional] 
**include_generated_by_access_client** | **bool** | Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a &#x60;ticket&#x60; or &#x60;paymentRequest&#x60; was processed then a new transfer will be generated.  | [optional] 
**from_current_access_client** | **bool** | Flag indicating whether to include only transfers by the current access client.  | [optional] 
**amount_range** | [**list[BigDecimal]**](BigDecimal.md) | The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


