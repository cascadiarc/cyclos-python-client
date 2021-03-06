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


class PaymentError(object):
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
        'code': 'PaymentErrorCode',
        'currency': 'Currency',
        'max_amount': 'BigDecimal',
        'max_payments': 'int',
        'pos_error': 'PosError'
    }

    attribute_map = {
        'code': 'code',
        'currency': 'currency',
        'max_amount': 'maxAmount',
        'max_payments': 'maxPayments',
        'pos_error': 'posError'
    }

    def __init__(self, code=None, currency=None, max_amount=None, max_payments=None, pos_error=None, _configuration=None):  # noqa: E501
        """PaymentError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._currency = None
        self._max_amount = None
        self._max_payments = None
        self._pos_error = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if currency is not None:
            self.currency = currency
        if max_amount is not None:
            self.max_amount = max_amount
        if max_payments is not None:
            self.max_payments = max_payments
        if pos_error is not None:
            self.pos_error = pos_error

    @property
    def code(self):
        """Gets the code of this PaymentError.  # noqa: E501

        Application-specific error codes for a payment error  Possible values are: * dailyAmountExceeded: The maximum amount allowed per day was exceeded.   * dailyPaymentsExceeded: The maximum count of payments allowed per day was exceeded. * destinationUpperLimitReached: The upper balance limit of the destination account was exceeded. * insufficientBalance: The account selected for the payment does not have enough balance * monthlyAmountExceeded: The maximum amount allowed per month was exceeded. * monthlyPaymentsExceeded: The maximum count of payments allowed per month was exceeded. * pos: A POS exception has happened when performing this payment. See the `posError` field for more details.    * timeBetweenPaymentsNotMet: The minimum time between payments was not met. * unexpected: An unexpected error has occurred. See the `exceptionType` and `exceptionMessage` fields for the internal information. * weeklyAmountExceeded: The maximum amount allowed per week was exceeded. * weeklyPaymentsExceeded: The maximum count of payments allowed per week was exceeded.   # noqa: E501

        :return: The code of this PaymentError.  # noqa: E501
        :rtype: PaymentErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PaymentError.

        Application-specific error codes for a payment error  Possible values are: * dailyAmountExceeded: The maximum amount allowed per day was exceeded.   * dailyPaymentsExceeded: The maximum count of payments allowed per day was exceeded. * destinationUpperLimitReached: The upper balance limit of the destination account was exceeded. * insufficientBalance: The account selected for the payment does not have enough balance * monthlyAmountExceeded: The maximum amount allowed per month was exceeded. * monthlyPaymentsExceeded: The maximum count of payments allowed per month was exceeded. * pos: A POS exception has happened when performing this payment. See the `posError` field for more details.    * timeBetweenPaymentsNotMet: The minimum time between payments was not met. * unexpected: An unexpected error has occurred. See the `exceptionType` and `exceptionMessage` fields for the internal information. * weeklyAmountExceeded: The maximum amount allowed per week was exceeded. * weeklyPaymentsExceeded: The maximum count of payments allowed per week was exceeded.   # noqa: E501

        :param code: The code of this PaymentError.  # noqa: E501
        :type: PaymentErrorCode
        """

        self._code = code

    @property
    def currency(self):
        """Gets the currency of this PaymentError.  # noqa: E501

        Currency reference. Only if `code` is `dailyAmountExceeded`, `weeklyAmountExceeded` or `monthlyAmountExceeded`             # noqa: E501

        :return: The currency of this PaymentError.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentError.

        Currency reference. Only if `code` is `dailyAmountExceeded`, `weeklyAmountExceeded` or `monthlyAmountExceeded`             # noqa: E501

        :param currency: The currency of this PaymentError.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def max_amount(self):
        """Gets the max_amount of this PaymentError.  # noqa: E501

        The maximum amount. Only if `code` is `dailyAmountExceeded`, `weeklyAmountExceeded` or `monthlyAmountExceeded`             # noqa: E501

        :return: The max_amount of this PaymentError.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._max_amount

    @max_amount.setter
    def max_amount(self, max_amount):
        """Sets the max_amount of this PaymentError.

        The maximum amount. Only if `code` is `dailyAmountExceeded`, `weeklyAmountExceeded` or `monthlyAmountExceeded`             # noqa: E501

        :param max_amount: The max_amount of this PaymentError.  # noqa: E501
        :type: BigDecimal
        """

        self._max_amount = max_amount

    @property
    def max_payments(self):
        """Gets the max_payments of this PaymentError.  # noqa: E501

        The maximum payments count. Only if `code` is `dailyPaymentsExceeded`, `weeklyPaymentsExceeded` or `monthlyPaymentsExceeded`             # noqa: E501

        :return: The max_payments of this PaymentError.  # noqa: E501
        :rtype: int
        """
        return self._max_payments

    @max_payments.setter
    def max_payments(self, max_payments):
        """Sets the max_payments of this PaymentError.

        The maximum payments count. Only if `code` is `dailyPaymentsExceeded`, `weeklyPaymentsExceeded` or `monthlyPaymentsExceeded`             # noqa: E501

        :param max_payments: The max_payments of this PaymentError.  # noqa: E501
        :type: int
        """

        self._max_payments = max_payments

    @property
    def pos_error(self):
        """Gets the pos_error of this PaymentError.  # noqa: E501

        The POS error details. Only if `code` is `pos`             # noqa: E501

        :return: The pos_error of this PaymentError.  # noqa: E501
        :rtype: PosError
        """
        return self._pos_error

    @pos_error.setter
    def pos_error(self, pos_error):
        """Sets the pos_error of this PaymentError.

        The POS error details. Only if `code` is `pos`             # noqa: E501

        :param pos_error: The pos_error of this PaymentError.  # noqa: E501
        :type: PosError
        """

        self._pos_error = pos_error

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
        if issubclass(PaymentError, dict):
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
        if not isinstance(other, PaymentError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentError):
            return True

        return self.to_dict() != other.to_dict()
