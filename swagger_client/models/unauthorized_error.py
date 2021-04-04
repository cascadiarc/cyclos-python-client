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


class UnauthorizedError(object):
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
        'code': 'UnauthorizedErrorCode',
        'user_status': 'UserStatusEnum',
        'password_status': 'PasswordStatusEnum',
        'missing_secondary_password': 'PasswordType'
    }

    attribute_map = {
        'code': 'code',
        'user_status': 'userStatus',
        'password_status': 'passwordStatus',
        'missing_secondary_password': 'missingSecondaryPassword'
    }

    def __init__(self, code=None, user_status=None, password_status=None, missing_secondary_password=None, _configuration=None):  # noqa: E501
        """UnauthorizedError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._user_status = None
        self._password_status = None
        self._missing_secondary_password = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if user_status is not None:
            self.user_status = user_status
        if password_status is not None:
            self.password_status = password_status
        if missing_secondary_password is not None:
            self.missing_secondary_password = missing_secondary_password

    @property
    def code(self):
        """Gets the code of this UnauthorizedError.  # noqa: E501

        Error codes for 401 Unauthorized HTTP status.  Possible values are: * invalidAccessClient: The access client used for access is invalid * invalidChannelUsage: Attempt to login on a stateless-only channel, or use stateless in a stateful-only channel, or invoke as guest in a channel configuration which is only for users * invalidNetwork: Attempt to access a network that has been disabled * loggedOut: The session token used for access is invalid * login: Either user identification (principal) or password are invalid. May have additional information, such as the user / password status * missingAuthorization: Attempt to access an operation as guest, but the operation requires authentication * remoteAddressBlocked: The IP address being used for access has been blocked by exceeding tries with invalid users * unauthorizedAddress: The user cannot access the system using an IP address that is not white-listed * unauthorizedUrl: The user's configuration demands access using a specific URL, and this access is being done using another one   # noqa: E501

        :return: The code of this UnauthorizedError.  # noqa: E501
        :rtype: UnauthorizedErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this UnauthorizedError.

        Error codes for 401 Unauthorized HTTP status.  Possible values are: * invalidAccessClient: The access client used for access is invalid * invalidChannelUsage: Attempt to login on a stateless-only channel, or use stateless in a stateful-only channel, or invoke as guest in a channel configuration which is only for users * invalidNetwork: Attempt to access a network that has been disabled * loggedOut: The session token used for access is invalid * login: Either user identification (principal) or password are invalid. May have additional information, such as the user / password status * missingAuthorization: Attempt to access an operation as guest, but the operation requires authentication * remoteAddressBlocked: The IP address being used for access has been blocked by exceeding tries with invalid users * unauthorizedAddress: The user cannot access the system using an IP address that is not white-listed * unauthorizedUrl: The user's configuration demands access using a specific URL, and this access is being done using another one   # noqa: E501

        :param code: The code of this UnauthorizedError.  # noqa: E501
        :type: UnauthorizedErrorCode
        """

        self._code = code

    @property
    def user_status(self):
        """Gets the user_status of this UnauthorizedError.  # noqa: E501

        May only returned when `code` is `login`. Possible values are: * active: The user is active and can use the system normally. * blocked: The user has been blocked from accessing the system. Other users still see him/her. * disabled: The user has been disabled - he/she cannot access the system and is invisible by other users. * pending: The user registration is pending a confirmation. Probably the user has received an e-mail with a link that must be followed to complete the activation. The user is invisible by other users. * purged: The user was permanently removed and had all his private data removed. Only transactions are kept for historical reasons. * removed: The user was permanently removed. It's profile is kept for historical purposes.   # noqa: E501

        :return: The user_status of this UnauthorizedError.  # noqa: E501
        :rtype: UserStatusEnum
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status):
        """Sets the user_status of this UnauthorizedError.

        May only returned when `code` is `login`. Possible values are: * active: The user is active and can use the system normally. * blocked: The user has been blocked from accessing the system. Other users still see him/her. * disabled: The user has been disabled - he/she cannot access the system and is invisible by other users. * pending: The user registration is pending a confirmation. Probably the user has received an e-mail with a link that must be followed to complete the activation. The user is invisible by other users. * purged: The user was permanently removed and had all his private data removed. Only transactions are kept for historical reasons. * removed: The user was permanently removed. It's profile is kept for historical purposes.   # noqa: E501

        :param user_status: The user_status of this UnauthorizedError.  # noqa: E501
        :type: UserStatusEnum
        """

        self._user_status = user_status

    @property
    def password_status(self):
        """Gets the password_status of this UnauthorizedError.  # noqa: E501

        May only returned when `code` is `login`. Possible values are: * active: The password is active and valid * disabled: The password has been manually disabled * expired: The password is expired * indefinitelyBlocked: The password is blocked by exceeding the maximum attempts until it is manually unblocked * neverCreated: The password has never been created for the user * pending: The password was manually allowed (by admins) for the user to generate it, but it was not yet generated (never used for manual passwords) * reset: The password has been reset (can be used for login but must then be changed) * temporarilyBlocked: The password is temporarily blocked by exceeding the maximum attempts   # noqa: E501

        :return: The password_status of this UnauthorizedError.  # noqa: E501
        :rtype: PasswordStatusEnum
        """
        return self._password_status

    @password_status.setter
    def password_status(self, password_status):
        """Sets the password_status of this UnauthorizedError.

        May only returned when `code` is `login`. Possible values are: * active: The password is active and valid * disabled: The password has been manually disabled * expired: The password is expired * indefinitelyBlocked: The password is blocked by exceeding the maximum attempts until it is manually unblocked * neverCreated: The password has never been created for the user * pending: The password was manually allowed (by admins) for the user to generate it, but it was not yet generated (never used for manual passwords) * reset: The password has been reset (can be used for login but must then be changed) * temporarilyBlocked: The password is temporarily blocked by exceeding the maximum attempts   # noqa: E501

        :param password_status: The password_status of this UnauthorizedError.  # noqa: E501
        :type: PasswordStatusEnum
        """

        self._password_status = password_status

    @property
    def missing_secondary_password(self):
        """Gets the missing_secondary_password of this UnauthorizedError.  # noqa: E501

        May only returned when `code` is `login` and there is a secondary access password defined for the channel.   # noqa: E501

        :return: The missing_secondary_password of this UnauthorizedError.  # noqa: E501
        :rtype: PasswordType
        """
        return self._missing_secondary_password

    @missing_secondary_password.setter
    def missing_secondary_password(self, missing_secondary_password):
        """Sets the missing_secondary_password of this UnauthorizedError.

        May only returned when `code` is `login` and there is a secondary access password defined for the channel.   # noqa: E501

        :param missing_secondary_password: The missing_secondary_password of this UnauthorizedError.  # noqa: E501
        :type: PasswordType
        """

        self._missing_secondary_password = missing_secondary_password

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
        if issubclass(UnauthorizedError, dict):
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
        if not isinstance(other, UnauthorizedError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnauthorizedError):
            return True

        return self.to_dict() != other.to_dict()