# UserQueryFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_profile_fields_in_list** | **bool** | When set to &#x60;true&#x60;, instead of returning users with corresponding profile fields set on list, will return them with &#x60;display&#x60; and &#x60;shortDisplay&#x60;.   | [optional] 
**exclude_contacts** | **bool** | When set to &#x60;true&#x60; will not return any user that is already a contact of the currently authenticated user.  | [optional] 
**statuses** | [**list[UserStatusEnum]**](UserStatusEnum.md) | The possible statuses for an user Possibles values for each array element are: * active: The user is active and can use the system normally. * blocked: The user has been blocked from accessing the system. Other users still see him/her. * disabled: The user has been disabled - he/she cannot access the system and is invisible by other users. * pending: The user registration is pending a confirmation. Probably the user has received an e-mail with a link that must be followed to complete the activation. The user is invisible by other users. * purged: The user was permanently removed and had all his private data removed. Only transactions are kept for historical reasons. * removed: The user was permanently removed. It&#39;s profile is kept for historical purposes.  | [optional] 
**roles** | [**list[RoleEnum]**](RoleEnum.md) | The main role the user has. Possibles values for each array element are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \&quot;sub-user\&quot; created by a member to manage his data.  | [optional] 
**order_by** | [**UserOrderByEnum**](UserOrderByEnum.md) | Possible options for ordering the results of an user search. Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * creationDate: Newly registered users are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * random: Users will be randomly returned * relevance: This is the default if keywords are used. Best matching users come first.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


