# MobileBaseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cyclos_version** | **str** | The version of the Cyclos server | [optional] 
**current_client_time** | **datetime** | The current client time according to the server | [optional] 
**number_format** | [**NumberFormatEnum**](NumberFormatEnum.md) | The format for numbers Possible values are: * commaAsDecimal: 9.999,99 * periodAsDecimal: 9,999.99  | [optional] 
**date_format** | [**DateFormatEnum**](DateFormatEnum.md) | The format for dates Possible values are: * dmyDash: DD-MM-YYYY * dmyPeriod: DD.MM.YYYY * dmySlash: DD/MM/YYYY * mdyDash: MM-DD-YYYY * mdyPeriod: MM.DD.YYYY * mdySlash: MM/DD/YYYY * ymdDash: YYYY-MM-DD * ymdPeriod: YYYY.MM.DD * ymdSlash: YYYY/MM/DD  | [optional] 
**time_format** | [**TimeFormatEnum**](TimeFormatEnum.md) | The format for times Possible values are: * h12: 12-hour with AM/PM indicator * h24: 24-hour  | [optional] 
**locale** | **str** | The current locale | [optional] 
**root_url** | **str** | The main URL set in the configuration | [optional] 
**theme** | [**ThemeUIElement**](ThemeUIElement.md) | The mobile theme. Only returned when changed. | [optional] 
**translations** | [**MobileTranslations**](MobileTranslations.md) | The mobile translations. Only returned when changed. | [optional] 
**max_image_width** | **int** | Maximum width (in pixels) for uploaded images | [optional] 
**max_image_height** | **int** | Maximum height (in pixels) for uploaded images | [optional] 
**max_upload_size** | **int** | Maximum size (in bytes) for uploaded files | [optional] 
**jpeg_quality** | **int** | Quality for JPEG image types (higher means better quality) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


