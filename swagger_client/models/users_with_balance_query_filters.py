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


class UsersWithBalanceQueryFilters(object):
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
        'account_type': 'str',
        'balance_range': 'list[int]',
        'last_incoming_transfer_period': 'list[datetime]',
        'last_outgoing_transfer_period': 'list[datetime]',
        'negative_since_period': 'list[datetime]',
        'medium_balance_range': 'list[int]',
        'order_by': 'UsersWithBalanceOrderByEnum'
    }

    attribute_map = {
        'account_type': 'accountType',
        'balance_range': 'balanceRange',
        'last_incoming_transfer_period': 'lastIncomingTransferPeriod',
        'last_outgoing_transfer_period': 'lastOutgoingTransferPeriod',
        'negative_since_period': 'negativeSincePeriod',
        'medium_balance_range': 'mediumBalanceRange',
        'order_by': 'orderBy'
    }

    def __init__(self, account_type=None, balance_range=None, last_incoming_transfer_period=None, last_outgoing_transfer_period=None, negative_since_period=None, medium_balance_range=None, order_by=None, _configuration=None):  # noqa: E501
        """UsersWithBalanceQueryFilters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_type = None
        self._balance_range = None
        self._last_incoming_transfer_period = None
        self._last_outgoing_transfer_period = None
        self._negative_since_period = None
        self._medium_balance_range = None
        self._order_by = None
        self.discriminator = None

        self.account_type = account_type
        if balance_range is not None:
            self.balance_range = balance_range
        if last_incoming_transfer_period is not None:
            self.last_incoming_transfer_period = last_incoming_transfer_period
        if last_outgoing_transfer_period is not None:
            self.last_outgoing_transfer_period = last_outgoing_transfer_period
        if negative_since_period is not None:
            self.negative_since_period = negative_since_period
        if medium_balance_range is not None:
            self.medium_balance_range = medium_balance_range
        if order_by is not None:
            self.order_by = order_by

    @property
    def account_type(self):
        """Gets the account_type of this UsersWithBalanceQueryFilters.  # noqa: E501

        The account type  # noqa: E501

        :return: The account_type of this UsersWithBalanceQueryFilters.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this UsersWithBalanceQueryFilters.

        The account type  # noqa: E501

        :param account_type: The account_type of this UsersWithBalanceQueryFilters.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

    @property
    def balance_range(self):
        """Gets the balance_range of this UsersWithBalanceQueryFilters.  # noqa: E501

        The minimum and / or maximum balance for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :return: The balance_range of this UsersWithBalanceQueryFilters.  # noqa: E501
        :rtype: list[int]
        """
        return self._balance_range

    @balance_range.setter
    def balance_range(self, balance_range):
        """Sets the balance_range of this UsersWithBalanceQueryFilters.

        The minimum and / or maximum balance for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :param balance_range: The balance_range of this UsersWithBalanceQueryFilters.  # noqa: E501
        :type: list[int]
        """

        self._balance_range = balance_range

    @property
    def last_incoming_transfer_period(self):
        """Gets the last_incoming_transfer_period of this UsersWithBalanceQueryFilters.  # noqa: E501

        The minimum / maximum date of the last incoming transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :return: The last_incoming_transfer_period of this UsersWithBalanceQueryFilters.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._last_incoming_transfer_period

    @last_incoming_transfer_period.setter
    def last_incoming_transfer_period(self, last_incoming_transfer_period):
        """Sets the last_incoming_transfer_period of this UsersWithBalanceQueryFilters.

        The minimum / maximum date of the last incoming transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :param last_incoming_transfer_period: The last_incoming_transfer_period of this UsersWithBalanceQueryFilters.  # noqa: E501
        :type: list[datetime]
        """

        self._last_incoming_transfer_period = last_incoming_transfer_period

    @property
    def last_outgoing_transfer_period(self):
        """Gets the last_outgoing_transfer_period of this UsersWithBalanceQueryFilters.  # noqa: E501

        The minimum / maximum date of the last outgoing transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :return: The last_outgoing_transfer_period of this UsersWithBalanceQueryFilters.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._last_outgoing_transfer_period

    @last_outgoing_transfer_period.setter
    def last_outgoing_transfer_period(self, last_outgoing_transfer_period):
        """Sets the last_outgoing_transfer_period of this UsersWithBalanceQueryFilters.

        The minimum / maximum date of the last outgoing transfer for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :param last_outgoing_transfer_period: The last_outgoing_transfer_period of this UsersWithBalanceQueryFilters.  # noqa: E501
        :type: list[datetime]
        """

        self._last_outgoing_transfer_period = last_outgoing_transfer_period

    @property
    def negative_since_period(self):
        """Gets the negative_since_period of this UsersWithBalanceQueryFilters.  # noqa: E501

        The minimum / maximum negative-since date for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :return: The negative_since_period of this UsersWithBalanceQueryFilters.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._negative_since_period

    @negative_since_period.setter
    def negative_since_period(self, negative_since_period):
        """Sets the negative_since_period of this UsersWithBalanceQueryFilters.

        The minimum / maximum negative-since date for users to be returned. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :param negative_since_period: The negative_since_period of this UsersWithBalanceQueryFilters.  # noqa: E501
        :type: list[datetime]
        """

        self._negative_since_period = negative_since_period

    @property
    def medium_balance_range(self):
        """Gets the medium_balance_range of this UsersWithBalanceQueryFilters.  # noqa: E501

        An array with 2 elements, describing the lower and upper medium balance bounds. If not specified, the range defined in the account type will be used. If that one is also not defined, there will be no definitions for balance levels. Both bounds need to be set as 2 element in the array, or it won't be considered.   # noqa: E501

        :return: The medium_balance_range of this UsersWithBalanceQueryFilters.  # noqa: E501
        :rtype: list[int]
        """
        return self._medium_balance_range

    @medium_balance_range.setter
    def medium_balance_range(self, medium_balance_range):
        """Sets the medium_balance_range of this UsersWithBalanceQueryFilters.

        An array with 2 elements, describing the lower and upper medium balance bounds. If not specified, the range defined in the account type will be used. If that one is also not defined, there will be no definitions for balance levels. Both bounds need to be set as 2 element in the array, or it won't be considered.   # noqa: E501

        :param medium_balance_range: The medium_balance_range of this UsersWithBalanceQueryFilters.  # noqa: E501
        :type: list[int]
        """

        self._medium_balance_range = medium_balance_range

    @property
    def order_by(self):
        """Gets the order_by of this UsersWithBalanceQueryFilters.  # noqa: E501

        Contains the possible 'order by' values when searching for users with balances  Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * balanceAsc: User are ordered by balance, lower balances first. * balanceDesc: User are ordered by balance, higher balances first.   # noqa: E501

        :return: The order_by of this UsersWithBalanceQueryFilters.  # noqa: E501
        :rtype: UsersWithBalanceOrderByEnum
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this UsersWithBalanceQueryFilters.

        Contains the possible 'order by' values when searching for users with balances  Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * balanceAsc: User are ordered by balance, lower balances first. * balanceDesc: User are ordered by balance, higher balances first.   # noqa: E501

        :param order_by: The order_by of this UsersWithBalanceQueryFilters.  # noqa: E501
        :type: UsersWithBalanceOrderByEnum
        """

        self._order_by = order_by

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
        if issubclass(UsersWithBalanceQueryFilters, dict):
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
        if not isinstance(other, UsersWithBalanceQueryFilters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsersWithBalanceQueryFilters):
            return True

        return self.to_dict() != other.to_dict()
