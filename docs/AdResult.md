# AdResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotional_price** | [**BigDecimal**](BigDecimal.md) | The promotional price, only returned if there is a promotional price set and the promotional period is active  | [optional] 
**address** | [**Address**](Address.md) | Address to be placed on map. Is only returned when the search result type is &#x60;map&#x60;.  | [optional] 
**distance** | **float** | Only returned when there is a base location to calculate the distance from. The unit (kilometers or miles) depends on configuration.  | [optional] 
**categories** | **list[str]** | Either internal name or id of categories this advertisement belongs to. In most cases an advertisement will have a single category, but this depends on the Cyclos configuration.  | [optional] 
**currency** | **str** | Either internal name or id of the advertisement&#39;s price currency  | [optional] 
**editable** | **bool** | Indicates if the advertisement can be edited according to the logged  user&#39;s permissions and advertisement status.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


