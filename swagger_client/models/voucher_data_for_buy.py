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


class VoucherDataForBuy(object):
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
        'account': 'AccountWithStatus',
        'can_buy_multiple': 'bool',
        'fixed_amount': 'BigDecimal',
        'amount_range': 'DecimalRange',
        'minimum_time_to_redeem': 'TimeInterval'
    }

    attribute_map = {
        'account': 'account',
        'can_buy_multiple': 'canBuyMultiple',
        'fixed_amount': 'fixedAmount',
        'amount_range': 'amountRange',
        'minimum_time_to_redeem': 'minimumTimeToRedeem'
    }

    def __init__(self, account=None, can_buy_multiple=None, fixed_amount=None, amount_range=None, minimum_time_to_redeem=None, _configuration=None):  # noqa: E501
        """VoucherDataForBuy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account = None
        self._can_buy_multiple = None
        self._fixed_amount = None
        self._amount_range = None
        self._minimum_time_to_redeem = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if can_buy_multiple is not None:
            self.can_buy_multiple = can_buy_multiple
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if amount_range is not None:
            self.amount_range = amount_range
        if minimum_time_to_redeem is not None:
            self.minimum_time_to_redeem = minimum_time_to_redeem

    @property
    def account(self):
        """Gets the account of this VoucherDataForBuy.  # noqa: E501

        The account from which the buy will be debited  # noqa: E501

        :return: The account of this VoucherDataForBuy.  # noqa: E501
        :rtype: AccountWithStatus
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this VoucherDataForBuy.

        The account from which the buy will be debited  # noqa: E501

        :param account: The account of this VoucherDataForBuy.  # noqa: E501
        :type: AccountWithStatus
        """

        self._account = account

    @property
    def can_buy_multiple(self):
        """Gets the can_buy_multiple of this VoucherDataForBuy.  # noqa: E501

        If user can buy multiple vouchers at same time  # noqa: E501

        :return: The can_buy_multiple of this VoucherDataForBuy.  # noqa: E501
        :rtype: bool
        """
        return self._can_buy_multiple

    @can_buy_multiple.setter
    def can_buy_multiple(self, can_buy_multiple):
        """Sets the can_buy_multiple of this VoucherDataForBuy.

        If user can buy multiple vouchers at same time  # noqa: E501

        :param can_buy_multiple: The can_buy_multiple of this VoucherDataForBuy.  # noqa: E501
        :type: bool
        """

        self._can_buy_multiple = can_buy_multiple

    @property
    def fixed_amount(self):
        """Gets the fixed_amount of this VoucherDataForBuy.  # noqa: E501

        Returned if there is a fixed amount for bought vouchers. Is kept for backwards compatibility, because the `amountRange` is enough to return this information (when `min` and `max` are the same amount)   # noqa: E501

        :return: The fixed_amount of this VoucherDataForBuy.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        """Sets the fixed_amount of this VoucherDataForBuy.

        Returned if there is a fixed amount for bought vouchers. Is kept for backwards compatibility, because the `amountRange` is enough to return this information (when `min` and `max` are the same amount)   # noqa: E501

        :param fixed_amount: The fixed_amount of this VoucherDataForBuy.  # noqa: E501
        :type: BigDecimal
        """

        self._fixed_amount = fixed_amount

    @property
    def amount_range(self):
        """Gets the amount_range of this VoucherDataForBuy.  # noqa: E501

        Returned if there is a minimum / maximum amount for buying   # noqa: E501

        :return: The amount_range of this VoucherDataForBuy.  # noqa: E501
        :rtype: DecimalRange
        """
        return self._amount_range

    @amount_range.setter
    def amount_range(self, amount_range):
        """Sets the amount_range of this VoucherDataForBuy.

        Returned if there is a minimum / maximum amount for buying   # noqa: E501

        :param amount_range: The amount_range of this VoucherDataForBuy.  # noqa: E501
        :type: DecimalRange
        """

        self._amount_range = amount_range

    @property
    def minimum_time_to_redeem(self):
        """Gets the minimum_time_to_redeem of this VoucherDataForBuy.  # noqa: E501

        Returned if there is a minimum time to be elapsed before bought vouchers can be redeemed   # noqa: E501

        :return: The minimum_time_to_redeem of this VoucherDataForBuy.  # noqa: E501
        :rtype: TimeInterval
        """
        return self._minimum_time_to_redeem

    @minimum_time_to_redeem.setter
    def minimum_time_to_redeem(self, minimum_time_to_redeem):
        """Sets the minimum_time_to_redeem of this VoucherDataForBuy.

        Returned if there is a minimum time to be elapsed before bought vouchers can be redeemed   # noqa: E501

        :param minimum_time_to_redeem: The minimum_time_to_redeem of this VoucherDataForBuy.  # noqa: E501
        :type: TimeInterval
        """

        self._minimum_time_to_redeem = minimum_time_to_redeem

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
        if issubclass(VoucherDataForBuy, dict):
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
        if not isinstance(other, VoucherDataForBuy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VoucherDataForBuy):
            return True

        return self.to_dict() != other.to_dict()
