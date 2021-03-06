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


class PasswordStatusAndActions(object):
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
        'type': 'PasswordTypeWithDescription',
        'require_old_password_for_change': 'bool',
        'permissions': 'PasswordActions'
    }

    attribute_map = {
        'type': 'type',
        'require_old_password_for_change': 'requireOldPasswordForChange',
        'permissions': 'permissions'
    }

    def __init__(self, type=None, require_old_password_for_change=None, permissions=None, _configuration=None):  # noqa: E501
        """PasswordStatusAndActions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._require_old_password_for_change = None
        self._permissions = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if require_old_password_for_change is not None:
            self.require_old_password_for_change = require_old_password_for_change
        if permissions is not None:
            self.permissions = permissions

    @property
    def type(self):
        """Gets the type of this PasswordStatusAndActions.  # noqa: E501

        The password type along with the description  # noqa: E501

        :return: The type of this PasswordStatusAndActions.  # noqa: E501
        :rtype: PasswordTypeWithDescription
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PasswordStatusAndActions.

        The password type along with the description  # noqa: E501

        :param type: The type of this PasswordStatusAndActions.  # noqa: E501
        :type: PasswordTypeWithDescription
        """

        self._type = type

    @property
    def require_old_password_for_change(self):
        """Gets the require_old_password_for_change of this PasswordStatusAndActions.  # noqa: E501

        Indicates whether the `change` action, if enabled, requires the old password to be sent. This is the case when changing the password of the logged user, and the current password was ever set and is not currently expired / reset.   # noqa: E501

        :return: The require_old_password_for_change of this PasswordStatusAndActions.  # noqa: E501
        :rtype: bool
        """
        return self._require_old_password_for_change

    @require_old_password_for_change.setter
    def require_old_password_for_change(self, require_old_password_for_change):
        """Sets the require_old_password_for_change of this PasswordStatusAndActions.

        Indicates whether the `change` action, if enabled, requires the old password to be sent. This is the case when changing the password of the logged user, and the current password was ever set and is not currently expired / reset.   # noqa: E501

        :param require_old_password_for_change: The require_old_password_for_change of this PasswordStatusAndActions.  # noqa: E501
        :type: bool
        """

        self._require_old_password_for_change = require_old_password_for_change

    @property
    def permissions(self):
        """Gets the permissions of this PasswordStatusAndActions.  # noqa: E501

        The permissions over actions the authenticated user can perform on this password   # noqa: E501

        :return: The permissions of this PasswordStatusAndActions.  # noqa: E501
        :rtype: PasswordActions
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this PasswordStatusAndActions.

        The permissions over actions the authenticated user can perform on this password   # noqa: E501

        :param permissions: The permissions of this PasswordStatusAndActions.  # noqa: E501
        :type: PasswordActions
        """

        self._permissions = permissions

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
        if issubclass(PasswordStatusAndActions, dict):
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
        if not isinstance(other, PasswordStatusAndActions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PasswordStatusAndActions):
            return True

        return self.to_dict() != other.to_dict()
