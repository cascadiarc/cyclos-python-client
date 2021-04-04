# OperationDataForRun

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_information_text** | **str** | A message to be displayed to the user when displaying the page  results. Only returned if &#x60;resultType&#x60; is &#x60;resultPage&#x60;.  | [optional] 
**custom_submit_label** | **str** | A label to be shown on the submit button. When not returned, a generic &#39;Submit&#39; should be displayed.  | [optional] 
**form_parameters** | [**list[CustomFieldDetailed]**](CustomFieldDetailed.md) | The custom fields which are used in a form as parameters for the operation execution.  | [optional] 
**confirmation_password_input** | [**PasswordInput**](PasswordInput.md) | If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).  | [optional] 
**row_action** | [**OperationRowActionEnum**](OperationRowActionEnum.md) | The action that should be performed when the user clicks a row in the results table Possible values are: * location: Navigate to a standard Cyclos location * operation: Run an internal custom operation, which is set on the custom operation itself * url: Navigate to an arbitrary URL, which is set in the custom operation itself  | [optional] 
**search_automatically** | **bool** | Should the operation be immediately executed by the third party client software when first presenting the form to the user  (when &#x60;true&#x60;) or only when the user clicks submit (when &#x60;false&#x60;)? Only returned if &#x60;resultType&#x60; is &#x60;resultPage&#x60;.  | [optional] 
**row_location** | **str** | The location to which the client should be redirected when selecting a row in the results table. Only returned if &#x60;resultType&#x60; is &#x60;resultPage&#x60; and &#x60;rowAction&#x60; is &#x60;location&#x60;.  | [optional] 
**row_operation** | [**Operation**](Operation.md) | The custom operation that should be executed when clicking a row. Only returned if &#x60;resultType&#x60; is &#x60;resultPage&#x60; and &#x60;rowAction&#x60; is &#x60;operation&#x60;.  | [optional] 
**row_url** | **str** | The URL the client should be redirected when clicking a row. Only returned if &#x60;resultType&#x60; is &#x60;resultPage&#x60; and &#x60;rowAction&#x60; is &#x60;url&#x60;.  | [optional] 
**row_parameters** | **list[str]** | The names of parameters belonging to each custom operation result that should be passed as parameter to the custom operation or URL which is executed when selecting a row in the table. Only returned if &#x60;resultType&#x60; is &#x60;resultPage&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


