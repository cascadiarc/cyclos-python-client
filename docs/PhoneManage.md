# PhoneManage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The phone name | [optional] 
**number** | **str** | The formatted number | [optional] 
**extension** | **str** | The number extension, only for landLine phones, and is only used if the phone configuration states that extensions are enabled.   | [optional] 
**hidden** | **bool** | Indicates whether this phone is hidden for other users (&#x60;true&#x60;) or visible to all users (&#x60;false&#x60;).  | [optional] 
**enabled_for_sms** | **bool** | Only applicable if this represents a mobile phone. Whether this mobile phone is enabled for SMS, both receiving notifications and sending SMS operations. Can only be set if the mobile phone is verified.  | [optional] 
**verified** | **bool** | Only applicable if this represents a mobile phone. Whether this mobile is verified. Can only be directly set by administrators. Regular users need to verify it.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


