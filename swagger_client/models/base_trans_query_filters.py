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


class BaseTransQueryFilters(object):
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
        'date_period': 'list[datetime]',
        'transfer_filters': 'list[str]',
        'transfer_types': 'list[str]',
        'transaction_number': 'str',
        'user': 'str',
        'groups': 'list[str]',
        'by': 'str',
        'broker': 'str',
        'channels': 'list[str]',
        'excluded_ids': 'list[str]',
        'access_clients': 'list[str]',
        'include_generated_by_access_client': 'bool',
        'from_current_access_client': 'bool',
        'amount_range': 'list[BigDecimal]'
    }

    attribute_map = {
        'date_period': 'datePeriod',
        'transfer_filters': 'transferFilters',
        'transfer_types': 'transferTypes',
        'transaction_number': 'transactionNumber',
        'user': 'user',
        'groups': 'groups',
        'by': 'by',
        'broker': 'broker',
        'channels': 'channels',
        'excluded_ids': 'excludedIds',
        'access_clients': 'accessClients',
        'include_generated_by_access_client': 'includeGeneratedByAccessClient',
        'from_current_access_client': 'fromCurrentAccessClient',
        'amount_range': 'amountRange'
    }

    def __init__(self, date_period=None, transfer_filters=None, transfer_types=None, transaction_number=None, user=None, groups=None, by=None, broker=None, channels=None, excluded_ids=None, access_clients=None, include_generated_by_access_client=None, from_current_access_client=None, amount_range=None, _configuration=None):  # noqa: E501
        """BaseTransQueryFilters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._date_period = None
        self._transfer_filters = None
        self._transfer_types = None
        self._transaction_number = None
        self._user = None
        self._groups = None
        self._by = None
        self._broker = None
        self._channels = None
        self._excluded_ids = None
        self._access_clients = None
        self._include_generated_by_access_client = None
        self._from_current_access_client = None
        self._amount_range = None
        self.discriminator = None

        if date_period is not None:
            self.date_period = date_period
        if transfer_filters is not None:
            self.transfer_filters = transfer_filters
        if transfer_types is not None:
            self.transfer_types = transfer_types
        if transaction_number is not None:
            self.transaction_number = transaction_number
        if user is not None:
            self.user = user
        if groups is not None:
            self.groups = groups
        if by is not None:
            self.by = by
        if broker is not None:
            self.broker = broker
        if channels is not None:
            self.channels = channels
        if excluded_ids is not None:
            self.excluded_ids = excluded_ids
        if access_clients is not None:
            self.access_clients = access_clients
        if include_generated_by_access_client is not None:
            self.include_generated_by_access_client = include_generated_by_access_client
        if from_current_access_client is not None:
            self.from_current_access_client = from_current_access_client
        if amount_range is not None:
            self.amount_range = amount_range

    @property
    def date_period(self):
        """Gets the date_period of this BaseTransQueryFilters.  # noqa: E501

        The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :return: The date_period of this BaseTransQueryFilters.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._date_period

    @date_period.setter
    def date_period(self, date_period):
        """Sets the date_period of this BaseTransQueryFilters.

        The minimum / maximum transfer date. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :param date_period: The date_period of this BaseTransQueryFilters.  # noqa: E501
        :type: list[datetime]
        """

        self._date_period = date_period

    @property
    def transfer_filters(self):
        """Gets the transfer_filters of this BaseTransQueryFilters.  # noqa: E501

        Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format `accountType.transferFilter`.   # noqa: E501

        :return: The transfer_filters of this BaseTransQueryFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._transfer_filters

    @transfer_filters.setter
    def transfer_filters(self, transfer_filters):
        """Sets the transfer_filters of this BaseTransQueryFilters.

        Reference to the transfer filters, which filters transfers by type. May be either the internal id or qualified transfer filter internal name, in the format `accountType.transferFilter`.   # noqa: E501

        :param transfer_filters: The transfer_filters of this BaseTransQueryFilters.  # noqa: E501
        :type: list[str]
        """

        self._transfer_filters = transfer_filters

    @property
    def transfer_types(self):
        """Gets the transfer_types of this BaseTransQueryFilters.  # noqa: E501

        Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format `accountType.transferType`.   # noqa: E501

        :return: The transfer_types of this BaseTransQueryFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._transfer_types

    @transfer_types.setter
    def transfer_types(self, transfer_types):
        """Sets the transfer_types of this BaseTransQueryFilters.

        Reference to the transfer types for filter. May be either the internal id or qualified transfer type internal name, in the format `accountType.transferType`.   # noqa: E501

        :param transfer_types: The transfer_types of this BaseTransQueryFilters.  # noqa: E501
        :type: list[str]
        """

        self._transfer_types = transfer_types

    @property
    def transaction_number(self):
        """Gets the transaction_number of this BaseTransQueryFilters.  # noqa: E501

        The transaction number of the matching transfer   # noqa: E501

        :return: The transaction_number of this BaseTransQueryFilters.  # noqa: E501
        :rtype: str
        """
        return self._transaction_number

    @transaction_number.setter
    def transaction_number(self, transaction_number):
        """Sets the transaction_number of this BaseTransQueryFilters.

        The transaction number of the matching transfer   # noqa: E501

        :param transaction_number: The transaction_number of this BaseTransQueryFilters.  # noqa: E501
        :type: str
        """

        self._transaction_number = transaction_number

    @property
    def user(self):
        """Gets the user of this BaseTransQueryFilters.  # noqa: E501

        Reference a user that should have either received / performed the transfer.   # noqa: E501

        :return: The user of this BaseTransQueryFilters.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BaseTransQueryFilters.

        Reference a user that should have either received / performed the transfer.   # noqa: E501

        :param user: The user of this BaseTransQueryFilters.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def groups(self):
        """Gets the groups of this BaseTransQueryFilters.  # noqa: E501

        Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.   # noqa: E501

        :return: The groups of this BaseTransQueryFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this BaseTransQueryFilters.

        Reference to the user group used to perform / receive the transfer. Only taken into account if authenticated as administrator.   # noqa: E501

        :param groups: The groups of this BaseTransQueryFilters.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def by(self):
        """Gets the by of this BaseTransQueryFilters.  # noqa: E501

        Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.   # noqa: E501

        :return: The by of this BaseTransQueryFilters.  # noqa: E501
        :rtype: str
        """
        return self._by

    @by.setter
    def by(self, by):
        """Sets the by of this BaseTransQueryFilters.

        Reference to the user that was authenticated when the transfer was performed. Is only taken into account if authenticated as administrator.   # noqa: E501

        :param by: The by of this BaseTransQueryFilters.  # noqa: E501
        :type: str
        """

        self._by = by

    @property
    def broker(self):
        """Gets the broker of this BaseTransQueryFilters.  # noqa: E501

        Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.   # noqa: E501

        :return: The broker of this BaseTransQueryFilters.  # noqa: E501
        :rtype: str
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        """Sets the broker of this BaseTransQueryFilters.

        Reference to the broker of users involved in transfers. Is only taken into account if authenticated as administrator.   # noqa: E501

        :param broker: The broker of this BaseTransQueryFilters.  # noqa: E501
        :type: str
        """

        self._broker = broker

    @property
    def channels(self):
        """Gets the channels of this BaseTransQueryFilters.  # noqa: E501

        Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.   # noqa: E501

        :return: The channels of this BaseTransQueryFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this BaseTransQueryFilters.

        Reference to the channel used to perform / receive the transfer. Only taken into account if authenticated as administrator.   # noqa: E501

        :param channels: The channels of this BaseTransQueryFilters.  # noqa: E501
        :type: list[str]
        """

        self._channels = channels

    @property
    def excluded_ids(self):
        """Gets the excluded_ids of this BaseTransQueryFilters.  # noqa: E501

        List of transfers ids to be excluded from the result.   # noqa: E501

        :return: The excluded_ids of this BaseTransQueryFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded_ids

    @excluded_ids.setter
    def excluded_ids(self, excluded_ids):
        """Sets the excluded_ids of this BaseTransQueryFilters.

        List of transfers ids to be excluded from the result.   # noqa: E501

        :param excluded_ids: The excluded_ids of this BaseTransQueryFilters.  # noqa: E501
        :type: list[str]
        """

        self._excluded_ids = excluded_ids

    @property
    def access_clients(self):
        """Gets the access_clients of this BaseTransQueryFilters.  # noqa: E501

        References to access clients (id or token) used to perform / receive the  transfer.   # noqa: E501

        :return: The access_clients of this BaseTransQueryFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_clients

    @access_clients.setter
    def access_clients(self, access_clients):
        """Sets the access_clients of this BaseTransQueryFilters.

        References to access clients (id or token) used to perform / receive the  transfer.   # noqa: E501

        :param access_clients: The access_clients of this BaseTransQueryFilters.  # noqa: E501
        :type: list[str]
        """

        self._access_clients = access_clients

    @property
    def include_generated_by_access_client(self):
        """Gets the include_generated_by_access_client of this BaseTransQueryFilters.  # noqa: E501

        Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a `ticket` or `paymentRequest` was processed then a new transfer will be generated.   # noqa: E501

        :return: The include_generated_by_access_client of this BaseTransQueryFilters.  # noqa: E501
        :rtype: bool
        """
        return self._include_generated_by_access_client

    @include_generated_by_access_client.setter
    def include_generated_by_access_client(self, include_generated_by_access_client):
        """Sets the include_generated_by_access_client of this BaseTransQueryFilters.

        Flag indicating whether to include or not the generated transfer. Only valid if there is at least one access client specified. For example if a `ticket` or `paymentRequest` was processed then a new transfer will be generated.   # noqa: E501

        :param include_generated_by_access_client: The include_generated_by_access_client of this BaseTransQueryFilters.  # noqa: E501
        :type: bool
        """

        self._include_generated_by_access_client = include_generated_by_access_client

    @property
    def from_current_access_client(self):
        """Gets the from_current_access_client of this BaseTransQueryFilters.  # noqa: E501

        Flag indicating whether to include only transfers by the current access client.   # noqa: E501

        :return: The from_current_access_client of this BaseTransQueryFilters.  # noqa: E501
        :rtype: bool
        """
        return self._from_current_access_client

    @from_current_access_client.setter
    def from_current_access_client(self, from_current_access_client):
        """Sets the from_current_access_client of this BaseTransQueryFilters.

        Flag indicating whether to include only transfers by the current access client.   # noqa: E501

        :param from_current_access_client: The from_current_access_client of this BaseTransQueryFilters.  # noqa: E501
        :type: bool
        """

        self._from_current_access_client = from_current_access_client

    @property
    def amount_range(self):
        """Gets the amount_range of this BaseTransQueryFilters.  # noqa: E501

        The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :return: The amount_range of this BaseTransQueryFilters.  # noqa: E501
        :rtype: list[BigDecimal]
        """
        return self._amount_range

    @amount_range.setter
    def amount_range(self, amount_range):
        """Sets the amount_range of this BaseTransQueryFilters.

        The minimum / maximum amount. Is expressed an array, with the lower bound as first element, and the upper bound as second element. When only one element, will have just the lower bound. To specify only the upper bound, prefix the value with a comma.   # noqa: E501

        :param amount_range: The amount_range of this BaseTransQueryFilters.  # noqa: E501
        :type: list[BigDecimal]
        """

        self._amount_range = amount_range

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
        if issubclass(BaseTransQueryFilters, dict):
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
        if not isinstance(other, BaseTransQueryFilters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseTransQueryFilters):
            return True

        return self.to_dict() != other.to_dict()
