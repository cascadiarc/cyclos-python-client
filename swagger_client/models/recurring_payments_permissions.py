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


class RecurringPaymentsPermissions(object):
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
        'view': 'bool'
    }

    attribute_map = {
        'view': 'view'
    }

    def __init__(self, view=None, _configuration=None):  # noqa: E501
        """RecurringPaymentsPermissions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._view = None
        self.discriminator = None

        if view is not None:
            self.view = view

    @property
    def view(self):
        """Gets the view of this RecurringPaymentsPermissions.  # noqa: E501

        Can view recurring payments?  # noqa: E501

        :return: The view of this RecurringPaymentsPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this RecurringPaymentsPermissions.

        Can view recurring payments?  # noqa: E501

        :param view: The view of this RecurringPaymentsPermissions.  # noqa: E501
        :type: bool
        """

        self._view = view

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
        if issubclass(RecurringPaymentsPermissions, dict):
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
        if not isinstance(other, RecurringPaymentsPermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecurringPaymentsPermissions):
            return True

        return self.to_dict() != other.to_dict()
