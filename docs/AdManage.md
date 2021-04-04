# AdManage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The advertisement title | [optional] 
**description** | **str** | The advertisement description content, formatted as HTML  | [optional] 
**publication_period** | [**DatePeriod**](DatePeriod.md) | The date period this advertisement is published | [optional] 
**categories** | **list[str]** | Either internal name or id of categories this advertisement belongs to. In most cases an advertisement will have a single category, but this depends on the Cyclos configuration.  | [optional] 
**currency** | **str** | Either internal name or id of the advertisement&#39;s price currency  | [optional] 
**price** | [**BigDecimal**](BigDecimal.md) | The regular price | [optional] 
**promotional_price** | [**BigDecimal**](BigDecimal.md) | The promotional price, if any | [optional] 
**promotional_period** | [**DatePeriod**](DatePeriod.md) | The promotional period, the one when &#x60;promotionalPrice&#x60; is valid  | [optional] 
**custom_values** | **dict(str, str)** | Holds the custom field values, keyed by field internal name or id. The format of the value depends on the custom field type. Example: &#x60;{..., \&quot;customValues\&quot;: {\&quot;gender\&quot;: \&quot;male\&quot;, \&quot;birthDate\&quot;: \&quot;1980-10-27\&quot;}}&#x60;  | [optional] 
**addresses** | **list[str]** | Ids of addresses (belogining to the advertisement owner) this  advertisement is available at.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


