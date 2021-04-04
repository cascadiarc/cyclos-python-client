# Operation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**OperationScopeEnum**](OperationScopeEnum.md) | The scope determines where does a custom operation can be executed Possible values are: * advertisement: A custom operation which is executed over an advertisement * bulkAction: A custom operation executed over a set of users (one at a time) * contact: A custom operation which is executed over a contact in a user&#39;s contact list * contactInfo: A custom operation which is executed over an additional contact information, which is part of the user profile * internal: A custom operation which is executed by another custom operation * menu: A custom operation which is visible in a custom menu item * record: A custom operation which is executed over a record * system: A general, system custom operation * transfer: A custom operation which is executed over a transfer * user: A custom operation over a single user  | [optional] 
**result_type** | [**OperationResultTypeEnum**](OperationResultTypeEnum.md) | The kind of data a custom operation execution is expected to return Possible values are: * externalRedirect: The main execution returns an URL for another service. Then a second execution is expected when this other service redirects the client back to Cyclos * fileDownload: Returns a file, which can be downloaded * notification: Returns a text to be displayed as a simple notification * plainText: Returns a plain text to be displayed in a page, and optionally printed * resultPage: Returns a page or list of results, which should be displayed in a table like any other search / list * richText: Returns an HTML formatted text to be displayed in a page, and optionally printed * url: The result should be an URL to which the client should be redirected to  | [optional] 
**icon** | **str** | The character that represents the icon in the Cyclos font | [optional] 
**label** | **str** | A representative label about the operation | [optional] 
**information_text** | **str** | A message to be displayed to the user when displaying the parameters form  | [optional] 
**confirmation_text** | **str** | A message to be shown to the user in order to confirm the operation execution  | [optional] 
**require_confirmation_password** | **bool** | Indicates whether this operation requires confirmation password  | [optional] 
**has_file_upload** | **bool** | Indicates whether this operation accepts a file upload as input  | [optional] 
**allow_export** | **bool** | Does this operation allows exporting the results as CSV? Only returned if &#x60;resultType&#x60; is &#x60;resultPage&#x60;  | [optional] 
**allow_print** | **bool** | Does this operation allows printing the results as PDF? Only returned if &#x60;resultType&#x60; is &#x60;resultPage&#x60;  | [optional] 
**missing_optional_parameters** | **list[str]** | The optional custom fields without a value. The front-end could opt-in to rely on the &#x60;showFormForMissingOptionalParameters&#x60; flag to wether show or not  an input form  | [optional] 
**missing_required_parameters** | **list[str]** | The required custom fields without a value.  This means the operation will fail with a validation error if the parameters present in this list are not  given when run it  | [optional] 
**show_form_for_missing_optional_parameters** | **bool** | Indicates whether a form to enter the missing optional parameters must be shown. Only returned if the &#x60;missingOptionalParameters&#x60; list is not empty and &#x60;scope&#x60; is  &#x60;internal&#x60;  | [optional] 
**can_run_directly** | **bool** | (Deprecated) Indicates whether this operation can be executed directly, without showing a form page. More specifically, this flag is true if: * There are no confirmation text nor informational text * File upload is not allowed * Confirmation password is not required * All required parameters were set * All optional parametes were set or, if not, the option to show the form in case of missing parameters is false.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


