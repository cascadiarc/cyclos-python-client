# UserView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**RoleEnum**](RoleEnum.md) | The main role the user has. Possible values are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \&quot;sub-user\&quot; created by a member to manage his data.  | [optional] 
**name** | **str** | The user&#39;s full name | [optional] 
**username** | **str** | The user&#39;s login name | [optional] 
**email** | **str** | The user&#39;s e-mail | [optional] 
**custom_values** | [**list[UserCustomFieldValue]**](UserCustomFieldValue.md) | The list of custom field values this user has | [optional] 
**group** | [**EntityReference**](EntityReference.md) | Reference to the user group. Is only returned if the authenticated user has permission to see groups   | [optional] 
**group_set** | [**EntityReference**](EntityReference.md) | Reference to the user group set. Is only returned if the authenticated user has permission to see group sets and the user group is in a group set   | [optional] 
**additional_images** | [**list[Image]**](Image.md) | Holds the images other than the primary image, which is returned in the &#x60;image&#x60; field  | [optional] 
**addresses** | [**list[AddressView]**](AddressView.md) | Visible addresses | [optional] 
**phones** | [**list[PhoneView]**](PhoneView.md) | Visible phones | [optional] 
**contact_infos** | [**list[ContactInfoDetailed]**](ContactInfoDetailed.md) | Visible additional contact information | [optional] 
**contact** | [**ContactView**](ContactView.md) | When this user is in the contact list of the currently logged user, returns data about the contact relation. When not returned, this user is no in the logged user&#39;s contact list.  | [optional] 
**registration_date** | **datetime** | The date the user was registered. Only returned if the logged user manages the given used.  | [optional] 
**activation_date** | **datetime** | The date the user was made active the first time. Only returned if the logged user manages the given used.  | [optional] 
**online** | **bool** | Indicates whether the given user is logged-in to the system. Only returned if the logged user manages the given used.  | [optional] 
**last_login** | **datetime** | The last time the user logged in, or null if never logged in. Only returned if the logged user manages the given used.  | [optional] 
**first_login** | **datetime** | The first time the user logged in, or null if never logged in. Only returned if the logged user manages the given used.  | [optional] 
**permissions** | [**UserPermissions**](UserPermissions.md) | Permissions the authenticated has over this user | [optional] 
**brokers** | [**list[BrokerView]**](BrokerView.md) | Visible brokers | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


