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


class AccountHistoryStatus(object):
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
        'begin_date': 'datetime',
        'balance_at_begin': 'BigDecimal',
        'end_date': 'datetime',
        'balance_at_end': 'BigDecimal',
        'incoming': 'AmountSummary',
        'outgoing': 'AmountSummary',
        'net_inflow': 'BigDecimal'
    }

    attribute_map = {
        'begin_date': 'beginDate',
        'balance_at_begin': 'balanceAtBegin',
        'end_date': 'endDate',
        'balance_at_end': 'balanceAtEnd',
        'incoming': 'incoming',
        'outgoing': 'outgoing',
        'net_inflow': 'netInflow'
    }

    def __init__(self, begin_date=None, balance_at_begin=None, end_date=None, balance_at_end=None, incoming=None, outgoing=None, net_inflow=None, _configuration=None):  # noqa: E501
        """AccountHistoryStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._begin_date = None
        self._balance_at_begin = None
        self._end_date = None
        self._balance_at_end = None
        self._incoming = None
        self._outgoing = None
        self._net_inflow = None
        self.discriminator = None

        if begin_date is not None:
            self.begin_date = begin_date
        if balance_at_begin is not None:
            self.balance_at_begin = balance_at_begin
        if end_date is not None:
            self.end_date = end_date
        if balance_at_end is not None:
            self.balance_at_end = balance_at_end
        if incoming is not None:
            self.incoming = incoming
        if outgoing is not None:
            self.outgoing = outgoing
        if net_inflow is not None:
            self.net_inflow = net_inflow

    @property
    def begin_date(self):
        """Gets the begin_date of this AccountHistoryStatus.  # noqa: E501

        The reference begin date  # noqa: E501

        :return: The begin_date of this AccountHistoryStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this AccountHistoryStatus.

        The reference begin date  # noqa: E501

        :param begin_date: The begin_date of this AccountHistoryStatus.  # noqa: E501
        :type: datetime
        """

        self._begin_date = begin_date

    @property
    def balance_at_begin(self):
        """Gets the balance_at_begin of this AccountHistoryStatus.  # noqa: E501

        The raw balance at the beginning of the informed period  # noqa: E501

        :return: The balance_at_begin of this AccountHistoryStatus.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._balance_at_begin

    @balance_at_begin.setter
    def balance_at_begin(self, balance_at_begin):
        """Sets the balance_at_begin of this AccountHistoryStatus.

        The raw balance at the beginning of the informed period  # noqa: E501

        :param balance_at_begin: The balance_at_begin of this AccountHistoryStatus.  # noqa: E501
        :type: BigDecimal
        """

        self._balance_at_begin = balance_at_begin

    @property
    def end_date(self):
        """Gets the end_date of this AccountHistoryStatus.  # noqa: E501

        The reference end date  # noqa: E501

        :return: The end_date of this AccountHistoryStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this AccountHistoryStatus.

        The reference end date  # noqa: E501

        :param end_date: The end_date of this AccountHistoryStatus.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def balance_at_end(self):
        """Gets the balance_at_end of this AccountHistoryStatus.  # noqa: E501

        The raw balance at the end of the informed period  # noqa: E501

        :return: The balance_at_end of this AccountHistoryStatus.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._balance_at_end

    @balance_at_end.setter
    def balance_at_end(self, balance_at_end):
        """Sets the balance_at_end of this AccountHistoryStatus.

        The raw balance at the end of the informed period  # noqa: E501

        :param balance_at_end: The balance_at_end of this AccountHistoryStatus.  # noqa: E501
        :type: BigDecimal
        """

        self._balance_at_end = balance_at_end

    @property
    def incoming(self):
        """Gets the incoming of this AccountHistoryStatus.  # noqa: E501

        The summary of incoming transfers  # noqa: E501

        :return: The incoming of this AccountHistoryStatus.  # noqa: E501
        :rtype: AmountSummary
        """
        return self._incoming

    @incoming.setter
    def incoming(self, incoming):
        """Sets the incoming of this AccountHistoryStatus.

        The summary of incoming transfers  # noqa: E501

        :param incoming: The incoming of this AccountHistoryStatus.  # noqa: E501
        :type: AmountSummary
        """

        self._incoming = incoming

    @property
    def outgoing(self):
        """Gets the outgoing of this AccountHistoryStatus.  # noqa: E501

        The summary of outgoing transfers  # noqa: E501

        :return: The outgoing of this AccountHistoryStatus.  # noqa: E501
        :rtype: AmountSummary
        """
        return self._outgoing

    @outgoing.setter
    def outgoing(self, outgoing):
        """Sets the outgoing of this AccountHistoryStatus.

        The summary of outgoing transfers  # noqa: E501

        :param outgoing: The outgoing of this AccountHistoryStatus.  # noqa: E501
        :type: AmountSummary
        """

        self._outgoing = outgoing

    @property
    def net_inflow(self):
        """Gets the net_inflow of this AccountHistoryStatus.  # noqa: E501

        The raw difference between incoming and outgoing transfers in the informed period    # noqa: E501

        :return: The net_inflow of this AccountHistoryStatus.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._net_inflow

    @net_inflow.setter
    def net_inflow(self, net_inflow):
        """Sets the net_inflow of this AccountHistoryStatus.

        The raw difference between incoming and outgoing transfers in the informed period    # noqa: E501

        :param net_inflow: The net_inflow of this AccountHistoryStatus.  # noqa: E501
        :type: BigDecimal
        """

        self._net_inflow = net_inflow

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
        if issubclass(AccountHistoryStatus, dict):
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
        if not isinstance(other, AccountHistoryStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountHistoryStatus):
            return True

        return self.to_dict() != other.to_dict()
