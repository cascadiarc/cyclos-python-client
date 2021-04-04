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


class OperationsPermissions(object):
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
        'user': 'list[OperationPermissions]',
        'system': 'list[OperationPermissions]'
    }

    attribute_map = {
        'user': 'user',
        'system': 'system'
    }

    def __init__(self, user=None, system=None, _configuration=None):  # noqa: E501
        """OperationsPermissions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user = None
        self._system = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if system is not None:
            self.system = system

    @property
    def user(self):
        """Gets the user of this OperationsPermissions.  # noqa: E501

        Permissions over custom operations applied to the authenticated user, with `scope` = `user`.   # noqa: E501

        :return: The user of this OperationsPermissions.  # noqa: E501
        :rtype: list[OperationPermissions]
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OperationsPermissions.

        Permissions over custom operations applied to the authenticated user, with `scope` = `user`.   # noqa: E501

        :param user: The user of this OperationsPermissions.  # noqa: E501
        :type: list[OperationPermissions]
        """

        self._user = user

    @property
    def system(self):
        """Gets the system of this OperationsPermissions.  # noqa: E501

        Custom operations the authenticated has access, with `scope` = `system`. Only returned for administrators.   # noqa: E501

        :return: The system of this OperationsPermissions.  # noqa: E501
        :rtype: list[OperationPermissions]
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this OperationsPermissions.

        Custom operations the authenticated has access, with `scope` = `system`. Only returned for administrators.   # noqa: E501

        :param system: The system of this OperationsPermissions.  # noqa: E501
        :type: list[OperationPermissions]
        """

        self._system = system

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
        if issubclass(OperationsPermissions, dict):
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
        if not isinstance(other, OperationsPermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OperationsPermissions):
            return True

        return self.to_dict() != other.to_dict()
