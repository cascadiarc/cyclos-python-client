# CustomFieldDetailed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**information_text** | **str** | Additional text that can be shown to the user as a hint of this field  | [optional] 
**size** | [**CustomFieldSizeEnum**](CustomFieldSizeEnum.md) | The size of the widget that should be rendered Possible values are: * full: The widget should occupy 100% of the available area * large: A large widget * medium: A medium widget * small: A small widget * tiny: A very small widget  | [optional] 
**pattern** | **str** | The (optional) mask to be applied to string values | [optional] 
**required** | **bool** | Indicates whether this field is required | [optional] 
**all_selected_label** | **str** | The label to be shown when all values are selected for a  multi selection field.  | [optional] 
**default_value** | **str** | The value that should be suggested as default. For multi selection will be a comma-separated string with possible values ids or internal names.  | [optional] 
**possible_value_categories** | [**list[EntityReference]**](EntityReference.md) | Only applicable when the custom field is enumerated (single or multi select). Contains the possible value categories.  | [optional] 
**has_values_list** | **bool** | Returns whether this custom field has a list of possible values, according to its type.  | [optional] 
**possible_values** | [**list[CustomFieldPossibleValue]**](CustomFieldPossibleValue.md) | Only applicable when the custom field is enumerated (single or multi selection). Contains the possible values for selection. Each value may or may not have a category. When they have, it will be a string pointing to the internal name (if available) or id of the possible value category, which can be looked up in the categories property.  | [optional] 
**dynamic_values** | [**list[CustomFieldDynamicValue]**](CustomFieldDynamicValue.md) | Only applicable when the custom field is dynamic selection. Contains the script-generated possible values.  | [optional] 
**string_values** | **list[str]** | Only applicable when the custom field type is &#x60;string&#x60; and &#x60;hasValuesList&#x60; is &#x60;true&#x60;. Contains the possible string values.  | [optional] 
**date_values** | **list[datetime]** | Only applicable when the custom field type is &#x60;date&#x60; and &#x60;hasValuesList&#x60; is &#x60;true&#x60;. Contains the possible date values.  | [optional] 
**integer_values** | **list[int]** | Only applicable when the custom field type is &#x60;integer&#x60; and &#x60;hasValuesList&#x60; is &#x60;true&#x60;. Contains the possible integer values.  | [optional] 
**decimal_values** | [**list[BigDecimal]**](BigDecimal.md) | Only applicable when the custom field type is &#x60;decimal&#x60; and &#x60;hasValuesList&#x60; is &#x60;true&#x60;. Contains the possible decimal values.  | [optional] 
**ad_values** | [**list[Ad]**](Ad.md) | Only applicable when the custom field is linked entity of type &#x60;advertisement&#x60; and &#x60;hasValuesList&#x60; is &#x60;true&#x60;. Contains the possible advertisements.  | [optional] 
**transaction_values** | [**list[Transaction]**](Transaction.md) | Only applicable when the custom field is linked entity of type &#x60;transaction&#x60; and &#x60;hasValuesList&#x60; is &#x60;true&#x60;. Contains the possible transactions.  | [optional] 
**transfer_values** | [**list[Transfer]**](Transfer.md) | Only applicable when the custom field is linked entity of type &#x60;transfer&#x60; and &#x60;hasValuesList&#x60; is &#x60;true&#x60;. Contains the possible transfers.  | [optional] 
**record_values** | [**list[Record]**](Record.md) | Only applicable when the custom field is linked entity of type &#x60;record&#x60; and &#x60;hasValuesList&#x60; is &#x60;true&#x60;. Contains the possible records.  | [optional] 
**user_values** | [**list[User]**](User.md) | Only applicable when the custom field is linked entity of type &#x60;user&#x60; and &#x60;hasValuesList&#x60; is &#x60;true&#x60;. Contains the possible users.  | [optional] 
**max_files** | **int** | Only applicable when the custom field type is  &#x60;file&#x60; or &#x60;image&#x60;. The maximun files that can be uploaded  | [optional] 
**mime_types** | **list[str]** | The allowed mime types for binary custom fields. Only applicable when the custom field type is either  &#x60;file&#x60; or &#x60;image&#x60;   | [optional] 
**allowed_mime_types** | [**list[FileMimeTypeEnum]**](FileMimeTypeEnum.md) | (deprecated) Only applicable when the custom field type is  &#x60;file&#x60;. Contains the possible built-in mime types allowed for the file being  uploaded  | [optional] 
**other_mime_types** | **list[str]** | (deprecated) Only applicable when the custom field type is  &#x60;file&#x60;and the &#x60;others&#x60; option was selected in &#x60;allowedMimeTypes&#x60;. Contains the other mime types allowed for the file being uploaded   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


