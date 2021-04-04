# TransactionTypeData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**Currency**](Currency.md) | The payment type currency | [optional] 
**fixed_amount** | [**BigDecimal**](BigDecimal.md) | The only allowed amount if the payment type uses a fixed amount  | [optional] 
**allows_recurring_payments** | **bool** | Can payments of this type be made recurring?  | [optional] 
**max_installments** | **int** | The maximum allowed installments. If it is zero, no kind of scheduled payments is allowed. If it is 1, a single future date can be used.  | [optional] 
**requires_description** | **bool** | The transaction description can be either required, or optional, depending on this setting. | [optional] 
**description_availability** | [**AvailabilityEnum**](AvailabilityEnum.md) | The availability for the transaction description           Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required  | [optional] 
**default_expiration_date** | **datetime** | The default expiration date, according to the configuration. Only for payment requests. | [optional] 
**hide_expiration_date** | **bool** | Whether the expiration date should be hidden from users, Only for payment requests. | [optional] 
**custom_fields** | [**list[CustomFieldDetailed]**](CustomFieldDetailed.md) | The custom fields related to this payment type | [optional] 
**a_rate** | [**BigDecimal**](BigDecimal.md) | The balance aging counter used for this payment. Only for payments.  | [optional] 
**d_rate** | [**BigDecimal**](BigDecimal.md) | The balance maturity used for this payment. Only for payments.  | [optional] 
**d_rate_creation_value** | [**BigDecimal**](BigDecimal.md) | The initial value for the balance maturity on this payment type. Only for payments.  | [optional] 
**limited_awaiting_authorization** | **bool** | Only for payments. | [optional] 
**no_negatives_maturity_policy** | **bool** | Only for payments. | [optional] 
**maturity_policy** | [**MaturityPolicyEnum**](MaturityPolicyEnum.md) | Only for payments. Possible values are: * always: The payment can always be performed, regardless its maturity * history: It the balance maturity ever reached zero in the past, that balance can be used on payment. If later on the maturity went above zero, that new balance cannot be used. Is normally used in conjunction with the maturity table, so the user can pick the balance from past maturity * zero: The payment can only be performed if the current maturity is zero  | [optional] 
**max_amount_by_maturity_policy** | [**BigDecimal**](BigDecimal.md) | The maximum amount that can be performed when &#x60;maturityPolicy&#x60; is &#x60;history&#x60;. It corresponds to the maturity table entry indicated by &#x60;maturityTableWinnerId&#x60;. Only for payments.  | [optional] 
**maturity_table_winner_id** | **str** | When &#x60;maturityPolicy&#x60; is &#x60;history&#x60;, contains the id of the maturity table entry that granted. Only for payments.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


