# Transfer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** | The descriptive text for this transfer, according to the transfer type and currency configuration in Cyclos   | [optional] 
**_date** | **datetime** | The transfer date and time | [optional] 
**amount** | [**BigDecimal**](BigDecimal.md) | The transfer amount. May be positive or negative. | [optional] 
**type** | [**EntityReference**](EntityReference.md) | The transfer type | [optional] 
**currency** | [**Currency**](Currency.md) | The transfer currency | [optional] 
**_from** | [**AccountWithOwner**](AccountWithOwner.md) | The account that sent the balance | [optional] 
**to** | [**AccountWithOwner**](AccountWithOwner.md) | The account that received the balance | [optional] 
**transaction_number** | **str** | The transaction number identifying this balance transfer. The currency configuration has the definition on whether transaction numbers are enabled and which format they have.  | [optional] 
**statuses** | [**list[TransferStatus]**](TransferStatus.md) | Contains the current status for each status flow this transfer has  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


