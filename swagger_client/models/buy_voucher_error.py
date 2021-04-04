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


class BuyVoucherError(object):
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
        'code': 'BuyVoucherErrorCode',
        'currency': 'Currency',
        'amount_left_for_buying': 'BigDecimal',
        'date_allowed_again': 'datetime',
        'current_open_amount': 'BigDecimal',
        'max_open_amount': 'BigDecimal',
        'payment_error': 'PaymentError'
    }

    attribute_map = {
        'code': 'code',
        'currency': 'currency',
        'amount_left_for_buying': 'amountLeftForBuying',
        'date_allowed_again': 'dateAllowedAgain',
        'current_open_amount': 'currentOpenAmount',
        'max_open_amount': 'maxOpenAmount',
        'payment_error': 'paymentError'
    }

    def __init__(self, code=None, currency=None, amount_left_for_buying=None, date_allowed_again=None, current_open_amount=None, max_open_amount=None, payment_error=None, _configuration=None):  # noqa: E501
        """BuyVoucherError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._currency = None
        self._amount_left_for_buying = None
        self._date_allowed_again = None
        self._current_open_amount = None
        self._max_open_amount = None
        self._payment_error = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if currency is not None:
            self.currency = currency
        if amount_left_for_buying is not None:
            self.amount_left_for_buying = amount_left_for_buying
        if date_allowed_again is not None:
            self.date_allowed_again = date_allowed_again
        if current_open_amount is not None:
            self.current_open_amount = current_open_amount
        if max_open_amount is not None:
            self.max_open_amount = max_open_amount
        if payment_error is not None:
            self.payment_error = payment_error

    @property
    def code(self):
        """Gets the code of this BuyVoucherError.  # noqa: E501

        Possible errors when buying a voucher Possible values are: * maxAmountForPeriod: The maximum allowed buy amount for a period (example, a month) has been exceeded * maxOpenAmount: The maximum open amount for this voucher type for the buyer user has been exceeded * maxTotalOpenAmount: The maximum total open amount for this voucher type, for all users, has been exceeded * notAllowedForUser: The user attempting to buy vouchers is not allowed to buy vouchers of this type * payment: There was an error when performing the payment * unexpected: An unexpected error has occurred. See the `exceptionType` and `exceptionMessage` fields for the internal information.   # noqa: E501

        :return: The code of this BuyVoucherError.  # noqa: E501
        :rtype: BuyVoucherErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BuyVoucherError.

        Possible errors when buying a voucher Possible values are: * maxAmountForPeriod: The maximum allowed buy amount for a period (example, a month) has been exceeded * maxOpenAmount: The maximum open amount for this voucher type for the buyer user has been exceeded * maxTotalOpenAmount: The maximum total open amount for this voucher type, for all users, has been exceeded * notAllowedForUser: The user attempting to buy vouchers is not allowed to buy vouchers of this type * payment: There was an error when performing the payment * unexpected: An unexpected error has occurred. See the `exceptionType` and `exceptionMessage` fields for the internal information.   # noqa: E501

        :param code: The code of this BuyVoucherError.  # noqa: E501
        :type: BuyVoucherErrorCode
        """

        self._code = code

    @property
    def currency(self):
        """Gets the currency of this BuyVoucherError.  # noqa: E501

        Currency reference. Only if `code` is `maxAmountForPeriod` or `maxTotalOpenAmount`             # noqa: E501

        :return: The currency of this BuyVoucherError.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this BuyVoucherError.

        Currency reference. Only if `code` is `maxAmountForPeriod` or `maxTotalOpenAmount`             # noqa: E501

        :param currency: The currency of this BuyVoucherError.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def amount_left_for_buying(self):
        """Gets the amount_left_for_buying of this BuyVoucherError.  # noqa: E501

        Indicates the maximum amount the user can buy this time without exceeding the maximum. Only if `code` is `maxAmountForPeriod`.   # noqa: E501

        :return: The amount_left_for_buying of this BuyVoucherError.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._amount_left_for_buying

    @amount_left_for_buying.setter
    def amount_left_for_buying(self, amount_left_for_buying):
        """Sets the amount_left_for_buying of this BuyVoucherError.

        Indicates the maximum amount the user can buy this time without exceeding the maximum. Only if `code` is `maxAmountForPeriod`.   # noqa: E501

        :param amount_left_for_buying: The amount_left_for_buying of this BuyVoucherError.  # noqa: E501
        :type: BigDecimal
        """

        self._amount_left_for_buying = amount_left_for_buying

    @property
    def date_allowed_again(self):
        """Gets the date_allowed_again of this BuyVoucherError.  # noqa: E501

        Indicates the date this user will be able to buy vouchers again for this type. Only if `code` is `maxAmountForPeriod`.   # noqa: E501

        :return: The date_allowed_again of this BuyVoucherError.  # noqa: E501
        :rtype: datetime
        """
        return self._date_allowed_again

    @date_allowed_again.setter
    def date_allowed_again(self, date_allowed_again):
        """Sets the date_allowed_again of this BuyVoucherError.

        Indicates the date this user will be able to buy vouchers again for this type. Only if `code` is `maxAmountForPeriod`.   # noqa: E501

        :param date_allowed_again: The date_allowed_again of this BuyVoucherError.  # noqa: E501
        :type: datetime
        """

        self._date_allowed_again = date_allowed_again

    @property
    def current_open_amount(self):
        """Gets the current_open_amount of this BuyVoucherError.  # noqa: E501

        Indicates the current total amount that is open. Only if `code` is `maxOpenAmount` or `maxTotalOpenAmount`.   # noqa: E501

        :return: The current_open_amount of this BuyVoucherError.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._current_open_amount

    @current_open_amount.setter
    def current_open_amount(self, current_open_amount):
        """Sets the current_open_amount of this BuyVoucherError.

        Indicates the current total amount that is open. Only if `code` is `maxOpenAmount` or `maxTotalOpenAmount`.   # noqa: E501

        :param current_open_amount: The current_open_amount of this BuyVoucherError.  # noqa: E501
        :type: BigDecimal
        """

        self._current_open_amount = current_open_amount

    @property
    def max_open_amount(self):
        """Gets the max_open_amount of this BuyVoucherError.  # noqa: E501

        Indicates the maximum total open amount. Only if `code` is `maxOpenAmount` or `maxTotalOpenAmount`.   # noqa: E501

        :return: The max_open_amount of this BuyVoucherError.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._max_open_amount

    @max_open_amount.setter
    def max_open_amount(self, max_open_amount):
        """Sets the max_open_amount of this BuyVoucherError.

        Indicates the maximum total open amount. Only if `code` is `maxOpenAmount` or `maxTotalOpenAmount`.   # noqa: E501

        :param max_open_amount: The max_open_amount of this BuyVoucherError.  # noqa: E501
        :type: BigDecimal
        """

        self._max_open_amount = max_open_amount

    @property
    def payment_error(self):
        """Gets the payment_error of this BuyVoucherError.  # noqa: E501

        The `PaymentError` generated when the voucher payment was being created. Only if `code` is `payment`.   # noqa: E501

        :return: The payment_error of this BuyVoucherError.  # noqa: E501
        :rtype: PaymentError
        """
        return self._payment_error

    @payment_error.setter
    def payment_error(self, payment_error):
        """Sets the payment_error of this BuyVoucherError.

        The `PaymentError` generated when the voucher payment was being created. Only if `code` is `payment`.   # noqa: E501

        :param payment_error: The payment_error of this BuyVoucherError.  # noqa: E501
        :type: PaymentError
        """

        self._payment_error = payment_error

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
        if issubclass(BuyVoucherError, dict):
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
        if not isinstance(other, BuyVoucherError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BuyVoucherError):
            return True

        return self.to_dict() != other.to_dict()