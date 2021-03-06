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


class Currency(object):
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
        'symbol': 'str',
        'prefix': 'str',
        'suffix': 'str',
        'transaction_number_pattern': 'str',
        'decimal_digits': 'int'
    }

    attribute_map = {
        'symbol': 'symbol',
        'prefix': 'prefix',
        'suffix': 'suffix',
        'transaction_number_pattern': 'transactionNumberPattern',
        'decimal_digits': 'decimalDigits'
    }

    def __init__(self, symbol=None, prefix=None, suffix=None, transaction_number_pattern=None, decimal_digits=None, _configuration=None):  # noqa: E501
        """Currency - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._symbol = None
        self._prefix = None
        self._suffix = None
        self._transaction_number_pattern = None
        self._decimal_digits = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if prefix is not None:
            self.prefix = prefix
        if suffix is not None:
            self.suffix = suffix
        if transaction_number_pattern is not None:
            self.transaction_number_pattern = transaction_number_pattern
        if decimal_digits is not None:
            self.decimal_digits = decimal_digits

    @property
    def symbol(self):
        """Gets the symbol of this Currency.  # noqa: E501

        The currency symbol  # noqa: E501

        :return: The symbol of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Currency.

        The currency symbol  # noqa: E501

        :param symbol: The symbol of this Currency.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def prefix(self):
        """Gets the prefix of this Currency.  # noqa: E501

        The currency prefix when formatting numbers  # noqa: E501

        :return: The prefix of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this Currency.

        The currency prefix when formatting numbers  # noqa: E501

        :param prefix: The prefix of this Currency.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def suffix(self):
        """Gets the suffix of this Currency.  # noqa: E501

        The currency suffix when formatting numbers  # noqa: E501

        :return: The suffix of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this Currency.

        The currency suffix when formatting numbers  # noqa: E501

        :param suffix: The suffix of this Currency.  # noqa: E501
        :type: str
        """

        self._suffix = suffix

    @property
    def transaction_number_pattern(self):
        """Gets the transaction_number_pattern of this Currency.  # noqa: E501

        If transaction number is enabled for this currency, contains the pattern which is expected, in case of rendering a field for users to type in a transaction number   # noqa: E501

        :return: The transaction_number_pattern of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._transaction_number_pattern

    @transaction_number_pattern.setter
    def transaction_number_pattern(self, transaction_number_pattern):
        """Sets the transaction_number_pattern of this Currency.

        If transaction number is enabled for this currency, contains the pattern which is expected, in case of rendering a field for users to type in a transaction number   # noqa: E501

        :param transaction_number_pattern: The transaction_number_pattern of this Currency.  # noqa: E501
        :type: str
        """

        self._transaction_number_pattern = transaction_number_pattern

    @property
    def decimal_digits(self):
        """Gets the decimal_digits of this Currency.  # noqa: E501

        The number of decimal digits used by this currency  # noqa: E501

        :return: The decimal_digits of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._decimal_digits

    @decimal_digits.setter
    def decimal_digits(self, decimal_digits):
        """Sets the decimal_digits of this Currency.

        The number of decimal digits used by this currency  # noqa: E501

        :param decimal_digits: The decimal_digits of this Currency.  # noqa: E501
        :type: int
        """

        self._decimal_digits = decimal_digits

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
        if issubclass(Currency, dict):
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
        if not isinstance(other, Currency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Currency):
            return True

        return self.to_dict() != other.to_dict()
