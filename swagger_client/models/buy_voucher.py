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


class BuyVoucher(object):
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
        'count': 'int',
        'amount': 'BigDecimal',
        'type': 'str',
        'custom_values': 'dict(str, str)'
    }

    attribute_map = {
        'count': 'count',
        'amount': 'amount',
        'type': 'type',
        'custom_values': 'customValues'
    }

    def __init__(self, count=None, amount=None, type=None, custom_values=None, _configuration=None):  # noqa: E501
        """BuyVoucher - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._amount = None
        self._type = None
        self._custom_values = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if amount is not None:
            self.amount = amount
        if type is not None:
            self.type = type
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def count(self):
        """Gets the count of this BuyVoucher.  # noqa: E501

        The number of vouchers to buy. Defaults to 1.  # noqa: E501

        :return: The count of this BuyVoucher.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BuyVoucher.

        The number of vouchers to buy. Defaults to 1.  # noqa: E501

        :param count: The count of this BuyVoucher.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def amount(self):
        """Gets the amount of this BuyVoucher.  # noqa: E501

        The amount per voucher  # noqa: E501

        :return: The amount of this BuyVoucher.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BuyVoucher.

        The amount per voucher  # noqa: E501

        :param amount: The amount of this BuyVoucher.  # noqa: E501
        :type: BigDecimal
        """

        self._amount = amount

    @property
    def type(self):
        """Gets the type of this BuyVoucher.  # noqa: E501

        Either the `id` or `internalName` of the voucher type   # noqa: E501

        :return: The type of this BuyVoucher.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BuyVoucher.

        Either the `id` or `internalName` of the voucher type   # noqa: E501

        :param type: The type of this BuyVoucher.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def custom_values(self):
        """Gets the custom_values of this BuyVoucher.  # noqa: E501

        Holds the payment custom field values, keyed by field internal name or id. The format of the value depends on the custom field type.   # noqa: E501

        :return: The custom_values of this BuyVoucher.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this BuyVoucher.

        Holds the payment custom field values, keyed by field internal name or id. The format of the value depends on the custom field type.   # noqa: E501

        :param custom_values: The custom_values of this BuyVoucher.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_values = custom_values

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
        if issubclass(BuyVoucher, dict):
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
        if not isinstance(other, BuyVoucher):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BuyVoucher):
            return True

        return self.to_dict() != other.to_dict()
