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


class ContactInfoDetailed(object):
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
        'custom_values': 'list[CustomFieldValue]',
        'operations': 'list[Operation]'
    }

    attribute_map = {
        'custom_values': 'customValues',
        'operations': 'operations'
    }

    def __init__(self, custom_values=None, operations=None, _configuration=None):  # noqa: E501
        """ContactInfoDetailed - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_values = None
        self._operations = None
        self.discriminator = None

        if custom_values is not None:
            self.custom_values = custom_values
        if operations is not None:
            self.operations = operations

    @property
    def custom_values(self):
        """Gets the custom_values of this ContactInfoDetailed.  # noqa: E501

        The list of custom field values on this additional contact information   # noqa: E501

        :return: The custom_values of this ContactInfoDetailed.  # noqa: E501
        :rtype: list[CustomFieldValue]
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this ContactInfoDetailed.

        The list of custom field values on this additional contact information   # noqa: E501

        :param custom_values: The custom_values of this ContactInfoDetailed.  # noqa: E501
        :type: list[CustomFieldValue]
        """

        self._custom_values = custom_values

    @property
    def operations(self):
        """Gets the operations of this ContactInfoDetailed.  # noqa: E501

        The list of custom operations the logged user can run over this additional contact information   # noqa: E501

        :return: The operations of this ContactInfoDetailed.  # noqa: E501
        :rtype: list[Operation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this ContactInfoDetailed.

        The list of custom operations the logged user can run over this additional contact information   # noqa: E501

        :param operations: The operations of this ContactInfoDetailed.  # noqa: E501
        :type: list[Operation]
        """

        self._operations = operations

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
        if issubclass(ContactInfoDetailed, dict):
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
        if not isinstance(other, ContactInfoDetailed):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactInfoDetailed):
            return True

        return self.to_dict() != other.to_dict()
