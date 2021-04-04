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


class BasicProfileFieldInput(object):
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
        'field': 'BasicProfileFieldEnum',
        'mask': 'str',
        'example': 'str'
    }

    attribute_map = {
        'field': 'field',
        'mask': 'mask',
        'example': 'example'
    }

    def __init__(self, field=None, mask=None, example=None, _configuration=None):  # noqa: E501
        """BasicProfileFieldInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._field = None
        self._mask = None
        self._example = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if mask is not None:
            self.mask = mask
        if example is not None:
            self.example = example

    @property
    def field(self):
        """Gets the field of this BasicProfileFieldInput.  # noqa: E501

        The basic field this refers to Possible values are: * accountNumber: Account number * address: Address * email: E-mail * image: Image * name: Full name * phone: Phone (either mobile or land-line) * username: Login name   # noqa: E501

        :return: The field of this BasicProfileFieldInput.  # noqa: E501
        :rtype: BasicProfileFieldEnum
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this BasicProfileFieldInput.

        The basic field this refers to Possible values are: * accountNumber: Account number * address: Address * email: E-mail * image: Image * name: Full name * phone: Phone (either mobile or land-line) * username: Login name   # noqa: E501

        :param field: The field of this BasicProfileFieldInput.  # noqa: E501
        :type: BasicProfileFieldEnum
        """

        self._field = field

    @property
    def mask(self):
        """Gets the mask of this BasicProfileFieldInput.  # noqa: E501

        If this field has a mask used for input, contains this mask. Currently only the account number can (optionally) have one.   # noqa: E501

        :return: The mask of this BasicProfileFieldInput.  # noqa: E501
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this BasicProfileFieldInput.

        If this field has a mask used for input, contains this mask. Currently only the account number can (optionally) have one.   # noqa: E501

        :param mask: The mask of this BasicProfileFieldInput.  # noqa: E501
        :type: str
        """

        self._mask = mask

    @property
    def example(self):
        """Gets the example of this BasicProfileFieldInput.  # noqa: E501

        If this field has an example value, holds that example   # noqa: E501

        :return: The example of this BasicProfileFieldInput.  # noqa: E501
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this BasicProfileFieldInput.

        If this field has an example value, holds that example   # noqa: E501

        :param example: The example of this BasicProfileFieldInput.  # noqa: E501
        :type: str
        """

        self._example = example

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
        if issubclass(BasicProfileFieldInput, dict):
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
        if not isinstance(other, BasicProfileFieldInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasicProfileFieldInput):
            return True

        return self.to_dict() != other.to_dict()
