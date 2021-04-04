# RunOperationResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_type** | [**OperationResultTypeEnum**](OperationResultTypeEnum.md) | The kind of data a custom operation execution is expected to return Possible values are: * externalRedirect: The main execution returns an URL for another service. Then a second execution is expected when this other service redirects the client back to Cyclos * fileDownload: Returns a file, which can be downloaded * notification: Returns a text to be displayed as a simple notification * plainText: Returns a plain text to be displayed in a page, and optionally printed * resultPage: Returns a page or list of results, which should be displayed in a table like any other search / list * richText: Returns an HTML formatted text to be displayed in a page, and optionally printed * url: The result should be an URL to which the client should be redirected to  | [optional] 
**title** | **str** | The text title. May be returned only if &#x60;resultType&#x60; is either &#x60;plainText&#x60;, &#x60;richText&#x60; or &#x60;resultPage&#x60;.  | [optional] 
**content** | **str** | The execution result content. Only returned if &#x60;resultType&#x60; is either &#x60;plainText&#x60; or  &#x60;richText&#x60;.  | [optional] 
**notification** | **str** | The execution result as string that should be shown as a notification. Only returned if &#x60;resultType&#x60; is &#x60;notification&#x60;.  | [optional] 
**notification_level** | [**NotificationLevelEnum**](NotificationLevelEnum.md) | Only returned if &#x60;resultType&#x60; is &#x60;notification&#x60;. Possible values are: * error: An error message, when some operation went wrong   * information: A general informative message * warning: A warning message, when special caution is required  | [optional] 
**url** | **str** | The execution result as an URL, to which the client should be redirected. Only returned if &#x60;resultType&#x60; is either &#x60;externalRedirect&#x60; or &#x60;url&#x60;.  | [optional] 
**back_to** | [**EntityReference**](EntityReference.md) | Either the id or internal name of the custom operation to go back after run the operation.  | [optional] 
**back_to_root** | **bool** | A boolean value indicating if the client application must go back to the page that originated the custom  operation executions.       | [optional] 
**re_run** | **bool** | A boolean value indicating if the custom operation we went back to or the current action container operation must be re-run before display it.  | [optional] 
**auto_run_action_id** | **str** | If it is present, it indicates the id of the action that should be executed automatically.  | [optional] 
**columns** | [**list[RunOperationResultColumn]**](RunOperationResultColumn.md) | Contains the definitions for each column in the result. Only returned if &#x60;resultType&#x60; is &#x60;resultPage&#x60;.   | [optional] 
**rows** | [**list[RunOperationResultRow]**](RunOperationResultRow.md) | Each row is an object containing the cells for that row, keyed by each column&#39;s &#x60;property&#x60;. Only returned if &#x60;resultType&#x60; is &#x60;resultPage&#x60;.  | [optional] 
**actions** | [**list[RunOperationAction]**](RunOperationAction.md) | Actions are other internal custom operations that can be executed from this custom operation. The returned parameters should be passed to the server when running this action.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


