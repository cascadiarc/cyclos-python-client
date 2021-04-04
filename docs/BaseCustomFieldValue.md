# BaseCustomFieldValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** | The field value if the field type is either &#x60;string&#x60;, &#x60;text&#x60;, &#x60;richText&#x60; or &#x60;url&#x60;.  | [optional] 
**date_value** | **datetime** | The field value if the field type is &#x60;date&#x60;.  | [optional] 
**boolean_value** | **bool** | The field value if the field type is &#x60;boolean&#x60;.  | [optional] 
**integer_value** | **int** | The field value if the field type is &#x60;integer&#x60;.  | [optional] 
**decimal_value** | [**BigDecimal**](BigDecimal.md) | The field value if the field type is &#x60;decimal&#x60;.  | [optional] 
**enumerated_values** | [**list[CustomFieldPossibleValue]**](CustomFieldPossibleValue.md) | The field value if the field type is either &#x60;singleSelection&#x60; or &#x60;multiSelection&#x60;. For single selections will either be an empty array or an array with a single element  | [optional] 
**dynamic_value** | [**CustomFieldDynamicValue**](CustomFieldDynamicValue.md) | The field value if the field type is &#x60;dynamicSelection&#x60;.  | [optional] 
**file_values** | [**list[StoredFile]**](StoredFile.md) | The field value if the field type is &#x60;file&#x60;  | [optional] 
**image_values** | [**list[Image]**](Image.md) | The field value if the field type is &#x60;image&#x60;  | [optional] 
**linked_entity_value** | **object** | (Deprecated) The field value if the field type is &#x60;linkedEntity&#x60;.  | [optional] 
**ad_value** | [**Ad**](Ad.md) | The field value if the field type is &#x60;linkedEntity&#x60; and the linked entity type is &#x60;advertisement&#x60;. If the currently set record is not accessible by the logged user, only the &#x60;name&#x60; field is sent, which contains the advertisement title.  | [optional] 
**transaction_value** | [**Transaction**](Transaction.md) | The field value if the field type is &#x60;linkedEntity&#x60; and the linked entity type is &#x60;transaction&#x60;. If the currently set transaction is not accessible by the logged user, only the &#x60;display&#x60; field is sent.  | [optional] 
**transfer_value** | [**Transfer**](Transfer.md) | The field value if the field type is &#x60;linkedEntity&#x60; and the linked entity type is &#x60;transfer&#x60;. If the currently set transfer is not accessible by the logged user, only the &#x60;display&#x60; field is sent.  | [optional] 
**record_value** | [**Record**](Record.md) | The field value if the field type is &#x60;linkedEntity&#x60; and the linked entity type is &#x60;record&#x60;. If the currently set record is not accessible by the logged user, only the &#x60;display&#x60; field is sent.  | [optional] 
**user_value** | [**User**](User.md) | The field value if the field type is &#x60;linkedEntity&#x60; and the linked entity type is &#x60;user&#x60;. If the currently set user is not accessible by the logged user, only a limited set of fields is sent, namely &#x60;display&#x60; and &#x60;shortDisplay&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


