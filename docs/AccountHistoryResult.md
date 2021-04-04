# AccountHistoryResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_date** | **datetime** | The transfer date and time | [optional] 
**amount** | [**BigDecimal**](BigDecimal.md) | The transfer amount. May be positive or negative. | [optional] 
**related_account** | [**AccountWithOwner**](AccountWithOwner.md) | The account that either received / sent the balance | [optional] 
**type** | [**TransferType**](TransferType.md) | The transfer type | [optional] 
**description** | **str** | The transaction description. Is optional. | [optional] 
**transaction_number** | **str** | The transaction number identifying this balance transfer. The currency configuration has the definition on whether transaction numbers are enabled and which format they have.  | [optional] 
**custom_values** | **dict(str, str)** | Holds the custom field values, keyed by field internal name or id. The format of the value depends on the custom field type. In order to lookup the custom fields, use the &#x60;GET /{owner}/accounts/{accountType}/data-for-history&#x60; operation, and lookup each field by either internal name (if configured) or id. Example: &#x60;{..., \&quot;customValues\&quot;: {\&quot;linkedAccount\&quot;: \&quot;123456789\&quot;}}&#x60;  | [optional] 
**transaction** | [**Transaction**](Transaction.md) | If this balance transfer was originated from a transaction (like a payment or scheduled payment), contains the reference to this transaction.  | [optional] 
**statuses** | **dict(str, str)** | contains the current status internal name or id, keyed by the flow internal name or id  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


