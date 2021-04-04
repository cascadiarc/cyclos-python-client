# coding: utf-8

"""
    Cyclos 4.11.5 API

    The REST API for Cyclos 4.11.5  # noqa: E501

    OpenAPI spec version: 4.11.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class BaseAuth(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user': 'User',
        'language': 'VersionedEntity',
        '_global': 'bool',
        'role': 'RoleEnum',
        'system_administrator': 'bool',
        'alias_operator': 'bool',
        'permissions': 'Permissions',
        'session_token': 'str',
        'access_client': 'EntityReference',
        'principal_type': 'EntityReference',
        'principal': 'str',
        'password_type': 'PasswordType',
        'secondary_password_type': 'PasswordType',
        'expired_password': 'bool',
        'pending_agreements': 'bool',
        'expired_secondary_password': 'bool',
        'pending_secondary_password': 'bool'
    }

    attribute_map = {
        'user': 'user',
        'language': 'language',
        '_global': 'global',
        'role': 'role',
        'system_administrator': 'systemAdministrator',
        'alias_operator': 'aliasOperator',
        'permissions': 'permissions',
        'session_token': 'sessionToken',
        'access_client': 'accessClient',
        'principal_type': 'principalType',
        'principal': 'principal',
        'password_type': 'passwordType',
        'secondary_password_type': 'secondaryPasswordType',
        'expired_password': 'expiredPassword',
        'pending_agreements': 'pendingAgreements',
        'expired_secondary_password': 'expiredSecondaryPassword',
        'pending_secondary_password': 'pendingSecondaryPassword'
    }

    def __init__(self, user=None, language=None, _global=None, role=None, system_administrator=None, alias_operator=None, permissions=None, session_token=None, access_client=None, principal_type=None, principal=None, password_type=None, secondary_password_type=None, expired_password=None, pending_agreements=None, expired_secondary_password=None, pending_secondary_password=None, _configuration=None):  # noqa: E501
        """BaseAuth - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user = None
        self._language = None
        self.__global = None
        self._role = None
        self._system_administrator = None
        self._alias_operator = None
        self._permissions = None
        self._session_token = None
        self._access_client = None
        self._principal_type = None
        self._principal = None
        self._password_type = None
        self._secondary_password_type = None
        self._expired_password = None
        self._pending_agreements = None
        self._expired_secondary_password = None
        self._pending_secondary_password = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if language is not None:
            self.language = language
        if _global is not None:
            self._global = _global
        if role is not None:
            self.role = role
        if system_administrator is not None:
            self.system_administrator = system_administrator
        if alias_operator is not None:
            self.alias_operator = alias_operator
        if permissions is not None:
            self.permissions = permissions
        if session_token is not None:
            self.session_token = session_token
        if access_client is not None:
            self.access_client = access_client
        if principal_type is not None:
            self.principal_type = principal_type
        if principal is not None:
            self.principal = principal
        if password_type is not None:
            self.password_type = password_type
        if secondary_password_type is not None:
            self.secondary_password_type = secondary_password_type
        if expired_password is not None:
            self.expired_password = expired_password
        if pending_agreements is not None:
            self.pending_agreements = pending_agreements
        if expired_secondary_password is not None:
            self.expired_secondary_password = expired_secondary_password
        if pending_secondary_password is not None:
            self.pending_secondary_password = pending_secondary_password

    @property
    def user(self):
        """Gets the user of this BaseAuth.  # noqa: E501

        The authenticated user, if any.  # noqa: E501

        :return: The user of this BaseAuth.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BaseAuth.

        The authenticated user, if any.  # noqa: E501

        :param user: The user of this BaseAuth.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def language(self):
        """Gets the language of this BaseAuth.  # noqa: E501

        The current language version  # noqa: E501

        :return: The language of this BaseAuth.  # noqa: E501
        :rtype: VersionedEntity
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this BaseAuth.

        The current language version  # noqa: E501

        :param language: The language of this BaseAuth.  # noqa: E501
        :type: VersionedEntity
        """

        self._language = language

    @property
    def _global(self):
        """Gets the _global of this BaseAuth.  # noqa: E501

        Indicates whether this user belongs to global mode. Only returned if there is an authenticated user.   # noqa: E501

        :return: The _global of this BaseAuth.  # noqa: E501
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this BaseAuth.

        Indicates whether this user belongs to global mode. Only returned if there is an authenticated user.   # noqa: E501

        :param _global: The _global of this BaseAuth.  # noqa: E501
        :type: bool
        """

        self.__global = _global

    @property
    def role(self):
        """Gets the role of this BaseAuth.  # noqa: E501

        The main user role. Only returned if there is an authenticated user. Possible values are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \"sub-user\" created by a member to manage his data.   # noqa: E501

        :return: The role of this BaseAuth.  # noqa: E501
        :rtype: RoleEnum
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this BaseAuth.

        The main user role. Only returned if there is an authenticated user. Possible values are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \"sub-user\" created by a member to manage his data.   # noqa: E501

        :param role: The role of this BaseAuth.  # noqa: E501
        :type: RoleEnum
        """

        self._role = role

    @property
    def system_administrator(self):
        """Gets the system_administrator of this BaseAuth.  # noqa: E501

        Indicates whether this user is a system administrator, that is, either belongs to the global system administrators group or to the network system administrators group. Only returned if `role` is `administrator`.   # noqa: E501

        :return: The system_administrator of this BaseAuth.  # noqa: E501
        :rtype: bool
        """
        return self._system_administrator

    @system_administrator.setter
    def system_administrator(self, system_administrator):
        """Sets the system_administrator of this BaseAuth.

        Indicates whether this user is a system administrator, that is, either belongs to the global system administrators group or to the network system administrators group. Only returned if `role` is `administrator`.   # noqa: E501

        :param system_administrator: The system_administrator of this BaseAuth.  # noqa: E501
        :type: bool
        """

        self._system_administrator = system_administrator

    @property
    def alias_operator(self):
        """Gets the alias_operator of this BaseAuth.  # noqa: E501

        Indicates whether this user is an operator which is an alias of his owner member, that is, has all member permissions, and is not restricted to an operator group. Only returned if `role` is `operator`.   # noqa: E501

        :return: The alias_operator of this BaseAuth.  # noqa: E501
        :rtype: bool
        """
        return self._alias_operator

    @alias_operator.setter
    def alias_operator(self, alias_operator):
        """Sets the alias_operator of this BaseAuth.

        Indicates whether this user is an operator which is an alias of his owner member, that is, has all member permissions, and is not restricted to an operator group. Only returned if `role` is `operator`.   # noqa: E501

        :param alias_operator: The alias_operator of this BaseAuth.  # noqa: E501
        :type: bool
        """

        self._alias_operator = alias_operator

    @property
    def permissions(self):
        """Gets the permissions of this BaseAuth.  # noqa: E501

        The granted permissions for the authenticated user or guest  # noqa: E501

        :return: The permissions of this BaseAuth.  # noqa: E501
        :rtype: Permissions
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this BaseAuth.

        The granted permissions for the authenticated user or guest  # noqa: E501

        :param permissions: The permissions of this BaseAuth.  # noqa: E501
        :type: Permissions
        """

        self._permissions = permissions

    @property
    def session_token(self):
        """Gets the session_token of this BaseAuth.  # noqa: E501

        A token that must be passed in on the Session-Token header on subsequent requests instead of the login name and password. Only returned if using a session authentication.   # noqa: E501

        :return: The session_token of this BaseAuth.  # noqa: E501
        :rtype: str
        """
        return self._session_token

    @session_token.setter
    def session_token(self, session_token):
        """Sets the session_token of this BaseAuth.

        A token that must be passed in on the Session-Token header on subsequent requests instead of the login name and password. Only returned if using a session authentication.   # noqa: E501

        :param session_token: The session_token of this BaseAuth.  # noqa: E501
        :type: str
        """

        self._session_token = session_token

    @property
    def access_client(self):
        """Gets the access_client of this BaseAuth.  # noqa: E501

        Only returned when authenticated as access client, contains  information about it   # noqa: E501

        :return: The access_client of this BaseAuth.  # noqa: E501
        :rtype: EntityReference
        """
        return self._access_client

    @access_client.setter
    def access_client(self, access_client):
        """Sets the access_client of this BaseAuth.

        Only returned when authenticated as access client, contains  information about it   # noqa: E501

        :param access_client: The access_client of this BaseAuth.  # noqa: E501
        :type: EntityReference
        """

        self._access_client = access_client

    @property
    def principal_type(self):
        """Gets the principal_type of this BaseAuth.  # noqa: E501

        Returns a reference to the principal type used for authentication. May be some of the built-in types (login name, e-mail, mobile phone or account number), a profile field, a token type or an access client type   # noqa: E501

        :return: The principal_type of this BaseAuth.  # noqa: E501
        :rtype: EntityReference
        """
        return self._principal_type

    @principal_type.setter
    def principal_type(self, principal_type):
        """Sets the principal_type of this BaseAuth.

        Returns a reference to the principal type used for authentication. May be some of the built-in types (login name, e-mail, mobile phone or account number), a profile field, a token type or an access client type   # noqa: E501

        :param principal_type: The principal_type of this BaseAuth.  # noqa: E501
        :type: EntityReference
        """

        self._principal_type = principal_type

    @property
    def principal(self):
        """Gets the principal of this BaseAuth.  # noqa: E501

        The principal (user identification) used on authentication. Can be the value of the login name, e-mail, account number, custom field or token used on authentication or at the moment of login. Is not returned when the authentication was performed via access client.   # noqa: E501

        :return: The principal of this BaseAuth.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this BaseAuth.

        The principal (user identification) used on authentication. Can be the value of the login name, e-mail, account number, custom field or token used on authentication or at the moment of login. Is not returned when the authentication was performed via access client.   # noqa: E501

        :param principal: The principal of this BaseAuth.  # noqa: E501
        :type: str
        """

        self._principal = principal

    @property
    def password_type(self):
        """Gets the password_type of this BaseAuth.  # noqa: E501

        Returns a reference to the password type used on this channel.   # noqa: E501

        :return: The password_type of this BaseAuth.  # noqa: E501
        :rtype: PasswordType
        """
        return self._password_type

    @password_type.setter
    def password_type(self, password_type):
        """Sets the password_type of this BaseAuth.

        Returns a reference to the password type used on this channel.   # noqa: E501

        :param password_type: The password_type of this BaseAuth.  # noqa: E501
        :type: PasswordType
        """

        self._password_type = password_type

    @property
    def secondary_password_type(self):
        """Gets the secondary_password_type of this BaseAuth.  # noqa: E501

        Returns a reference to the secondary password type used on this channel, if any.   # noqa: E501

        :return: The secondary_password_type of this BaseAuth.  # noqa: E501
        :rtype: PasswordType
        """
        return self._secondary_password_type

    @secondary_password_type.setter
    def secondary_password_type(self, secondary_password_type):
        """Sets the secondary_password_type of this BaseAuth.

        Returns a reference to the secondary password type used on this channel, if any.   # noqa: E501

        :param secondary_password_type: The secondary_password_type of this BaseAuth.  # noqa: E501
        :type: PasswordType
        """

        self._secondary_password_type = secondary_password_type

    @property
    def expired_password(self):
        """Gets the expired_password of this BaseAuth.  # noqa: E501

        Returns whether the current access password is expired. If so, the user will have to change the password, or all other actions will be denied.   # noqa: E501

        :return: The expired_password of this BaseAuth.  # noqa: E501
        :rtype: bool
        """
        return self._expired_password

    @expired_password.setter
    def expired_password(self, expired_password):
        """Sets the expired_password of this BaseAuth.

        Returns whether the current access password is expired. If so, the user will have to change the password, or all other actions will be denied.   # noqa: E501

        :param expired_password: The expired_password of this BaseAuth.  # noqa: E501
        :type: bool
        """

        self._expired_password = expired_password

    @property
    def pending_agreements(self):
        """Gets the pending_agreements of this BaseAuth.  # noqa: E501

        Returns whether the current user has some agreements pending accept. If so, a call to GET /agreements/pending should be performed to get the content of the pending agreements, and then a POST  /agreements/pending{id_or_internal_name} to accept each agreement.   # noqa: E501

        :return: The pending_agreements of this BaseAuth.  # noqa: E501
        :rtype: bool
        """
        return self._pending_agreements

    @pending_agreements.setter
    def pending_agreements(self, pending_agreements):
        """Sets the pending_agreements of this BaseAuth.

        Returns whether the current user has some agreements pending accept. If so, a call to GET /agreements/pending should be performed to get the content of the pending agreements, and then a POST  /agreements/pending{id_or_internal_name} to accept each agreement.   # noqa: E501

        :param pending_agreements: The pending_agreements of this BaseAuth.  # noqa: E501
        :type: bool
        """

        self._pending_agreements = pending_agreements

    @property
    def expired_secondary_password(self):
        """Gets the expired_secondary_password of this BaseAuth.  # noqa: E501

        Returns whether the current secondary access password is expired. If so, the user will have to change the password, or all other actions will be denied.   # noqa: E501

        :return: The expired_secondary_password of this BaseAuth.  # noqa: E501
        :rtype: bool
        """
        return self._expired_secondary_password

    @expired_secondary_password.setter
    def expired_secondary_password(self, expired_secondary_password):
        """Sets the expired_secondary_password of this BaseAuth.

        Returns whether the current secondary access password is expired. If so, the user will have to change the password, or all other actions will be denied.   # noqa: E501

        :param expired_secondary_password: The expired_secondary_password of this BaseAuth.  # noqa: E501
        :type: bool
        """

        self._expired_secondary_password = expired_secondary_password

    @property
    def pending_secondary_password(self):
        """Gets the pending_secondary_password of this BaseAuth.  # noqa: E501

        Returns whether the current session requires a secondary password. If so, the user will have to validate it using its secondary access  password, otherwise, all other actions will be denied.   # noqa: E501

        :return: The pending_secondary_password of this BaseAuth.  # noqa: E501
        :rtype: bool
        """
        return self._pending_secondary_password

    @pending_secondary_password.setter
    def pending_secondary_password(self, pending_secondary_password):
        """Sets the pending_secondary_password of this BaseAuth.

        Returns whether the current session requires a secondary password. If so, the user will have to validate it using its secondary access  password, otherwise, all other actions will be denied.   # noqa: E501

        :param pending_secondary_password: The pending_secondary_password of this BaseAuth.  # noqa: E501
        :type: bool
        """

        self._pending_secondary_password = pending_secondary_password

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BaseAuth, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BaseAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseAuth):
            return True

        return self.to_dict() != other.to_dict()
