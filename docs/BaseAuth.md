# BaseAuth

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) | The authenticated user, if any. | [optional] 
**language** | [**VersionedEntity**](VersionedEntity.md) | The current language version | [optional] 
**_global** | **bool** | Indicates whether this user belongs to global mode. Only returned if there is an authenticated user.  | [optional] 
**role** | [**RoleEnum**](RoleEnum.md) | The main user role. Only returned if there is an authenticated user. Possible values are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \&quot;sub-user\&quot; created by a member to manage his data.  | [optional] 
**system_administrator** | **bool** | Indicates whether this user is a system administrator, that is, either belongs to the global system administrators group or to the network system administrators group. Only returned if &#x60;role&#x60; is &#x60;administrator&#x60;.  | [optional] 
**alias_operator** | **bool** | Indicates whether this user is an operator which is an alias of his owner member, that is, has all member permissions, and is not restricted to an operator group. Only returned if &#x60;role&#x60; is &#x60;operator&#x60;.  | [optional] 
**permissions** | [**Permissions**](Permissions.md) | The granted permissions for the authenticated user or guest | [optional] 
**session_token** | **str** | A token that must be passed in on the Session-Token header on subsequent requests instead of the login name and password. Only returned if using a session authentication.  | [optional] 
**access_client** | [**EntityReference**](EntityReference.md) | Only returned when authenticated as access client, contains  information about it  | [optional] 
**principal_type** | [**EntityReference**](EntityReference.md) | Returns a reference to the principal type used for authentication. May be some of the built-in types (login name, e-mail, mobile phone or account number), a profile field, a token type or an access client type  | [optional] 
**principal** | **str** | The principal (user identification) used on authentication. Can be the value of the login name, e-mail, account number, custom field or token used on authentication or at the moment of login. Is not returned when the authentication was performed via access client.  | [optional] 
**password_type** | [**PasswordType**](PasswordType.md) | Returns a reference to the password type used on this channel.  | [optional] 
**secondary_password_type** | [**PasswordType**](PasswordType.md) | Returns a reference to the secondary password type used on this channel, if any.  | [optional] 
**expired_password** | **bool** | Returns whether the current access password is expired. If so, the user will have to change the password, or all other actions will be denied.  | [optional] 
**pending_agreements** | **bool** | Returns whether the current user has some agreements pending accept. If so, a call to GET /agreements/pending should be performed to get the content of the pending agreements, and then a POST  /agreements/pending{id_or_internal_name} to accept each agreement.  | [optional] 
**expired_secondary_password** | **bool** | Returns whether the current secondary access password is expired. If so, the user will have to change the password, or all other actions will be denied.  | [optional] 
**pending_secondary_password** | **bool** | Returns whether the current session requires a secondary password. If so, the user will have to validate it using its secondary access  password, otherwise, all other actions will be denied.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


