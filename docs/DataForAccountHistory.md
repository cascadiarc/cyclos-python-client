# DataForAccountHistory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**AccountWithCurrency**](AccountWithCurrency.md) | Information about this specific account | [optional] 
**transaction_number_mask** | **str** | If a transaction number is used for this account, is a pattern that represent it.  | [optional] 
**can_filter_by_direction** | **bool** | Whether the current user can use the direction filter by direction. In some cases, such as restricted operators that can only see incoming or outgoing payments, this flag will be &#x60;false&#x60;.  | [optional] 
**show_description_in_filters** | **bool** | Whether to show the description as filter or not | [optional] 
**show_description_in_list** | **bool** | Whether to show the description in the result list or not | [optional] 
**custom_fields_in_search** | [**list[CustomFieldDetailed]**](CustomFieldDetailed.md) | Detailed references for custom fields that are set to be used as search filters   | [optional] 
**custom_fields_in_list** | [**list[CustomField]**](CustomField.md) | Simple references for custom fields that are set to be used on the search result list   | [optional] 
**query** | [**AccountHistoryQueryFilters**](AccountHistoryQueryFilters.md) | Default query filters for the account history  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


