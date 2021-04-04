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


class PasswordPermissions(object):
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
        'type': 'PasswordType',
        'change': 'bool',
        'enable': 'bool',
        'reset': 'bool',
        'unblock': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'change': 'change',
        'enable': 'enable',
        'reset': 'reset',
        'unblock': 'unblock'
    }

    def __init__(self, type=None, change=None, enable=None, reset=None, unblock=None, _configuration=None):  # noqa: E501
        """PasswordPermissions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._change = None
        self._enable = None
        self._reset = None
        self._unblock = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if change is not None:
            self.change = change
        if enable is not None:
            self.enable = enable
        if reset is not None:
            self.reset = reset
        if unblock is not None:
            self.unblock = unblock

    @property
    def type(self):
        """Gets the type of this PasswordPermissions.  # noqa: E501

        The password type  # noqa: E501

        :return: The type of this PasswordPermissions.  # noqa: E501
        :rtype: PasswordType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PasswordPermissions.

        The password type  # noqa: E501

        :param type: The type of this PasswordPermissions.  # noqa: E501
        :type: PasswordType
        """

        self._type = type

    @property
    def change(self):
        """Gets the change of this PasswordPermissions.  # noqa: E501

        Can change this password?  # noqa: E501

        :return: The change of this PasswordPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this PasswordPermissions.

        Can change this password?  # noqa: E501

        :param change: The change of this PasswordPermissions.  # noqa: E501
        :type: bool
        """

        self._change = change

    @property
    def enable(self):
        """Gets the enable of this PasswordPermissions.  # noqa: E501

        Can enable / disable this password?  # noqa: E501

        :return: The enable of this PasswordPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this PasswordPermissions.

        Can enable / disable this password?  # noqa: E501

        :param enable: The enable of this PasswordPermissions.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def reset(self):
        """Gets the reset of this PasswordPermissions.  # noqa: E501

        Can reset this password?  # noqa: E501

        :return: The reset of this PasswordPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._reset

    @reset.setter
    def reset(self, reset):
        """Sets the reset of this PasswordPermissions.

        Can reset this password?  # noqa: E501

        :param reset: The reset of this PasswordPermissions.  # noqa: E501
        :type: bool
        """

        self._reset = reset

    @property
    def unblock(self):
        """Gets the unblock of this PasswordPermissions.  # noqa: E501

        Can unblock this password if blocked by exceeding tries?  # noqa: E501

        :return: The unblock of this PasswordPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._unblock

    @unblock.setter
    def unblock(self, unblock):
        """Sets the unblock of this PasswordPermissions.

        Can unblock this password if blocked by exceeding tries?  # noqa: E501

        :param unblock: The unblock of this PasswordPermissions.  # noqa: E501
        :type: bool
        """

        self._unblock = unblock

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
        if issubclass(PasswordPermissions, dict):
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
        if not isinstance(other, PasswordPermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PasswordPermissions):
            return True

        return self.to_dict() != other.to_dict()