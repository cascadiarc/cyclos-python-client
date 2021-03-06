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


class GeneralOperatorsQueryFilters(object):
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
        'user_groups': 'list[str]',
        'broker': 'str'
    }

    attribute_map = {
        'user_groups': 'userGroups',
        'broker': 'broker'
    }

    def __init__(self, user_groups=None, broker=None, _configuration=None):  # noqa: E501
        """GeneralOperatorsQueryFilters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_groups = None
        self._broker = None
        self.discriminator = None

        if user_groups is not None:
            self.user_groups = user_groups
        if broker is not None:
            self.broker = broker

    @property
    def user_groups(self):
        """Gets the user_groups of this GeneralOperatorsQueryFilters.  # noqa: E501

        Either id or internal names of user groups / group sets  # noqa: E501

        :return: The user_groups of this GeneralOperatorsQueryFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this GeneralOperatorsQueryFilters.

        Either id or internal names of user groups / group sets  # noqa: E501

        :param user_groups: The user_groups of this GeneralOperatorsQueryFilters.  # noqa: E501
        :type: list[str]
        """

        self._user_groups = user_groups

    @property
    def broker(self):
        """Gets the broker of this GeneralOperatorsQueryFilters.  # noqa: E501

        Either id or a principal (login name, e-mail, etc) of the user broker  # noqa: E501

        :return: The broker of this GeneralOperatorsQueryFilters.  # noqa: E501
        :rtype: str
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        """Sets the broker of this GeneralOperatorsQueryFilters.

        Either id or a principal (login name, e-mail, etc) of the user broker  # noqa: E501

        :param broker: The broker of this GeneralOperatorsQueryFilters.  # noqa: E501
        :type: str
        """

        self._broker = broker

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
        if issubclass(GeneralOperatorsQueryFilters, dict):
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
        if not isinstance(other, GeneralOperatorsQueryFilters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneralOperatorsQueryFilters):
            return True

        return self.to_dict() != other.to_dict()
