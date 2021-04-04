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


class AccountHistoryResult(object):
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
        '_date': 'datetime',
        'amount': 'BigDecimal',
        'related_account': 'AccountWithOwner',
        'type': 'TransferType',
        'description': 'str',
        'transaction_number': 'str',
        'custom_values': 'dict(str, str)',
        'transaction': 'Transaction',
        'statuses': 'dict(str, str)'
    }

    attribute_map = {
        '_date': 'date',
        'amount': 'amount',
        'related_account': 'relatedAccount',
        'type': 'type',
        'description': 'description',
        'transaction_number': 'transactionNumber',
        'custom_values': 'customValues',
        'transaction': 'transaction',
        'statuses': 'statuses'
    }

    def __init__(self, _date=None, amount=None, related_account=None, type=None, description=None, transaction_number=None, custom_values=None, transaction=None, statuses=None, _configuration=None):  # noqa: E501
        """AccountHistoryResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__date = None
        self._amount = None
        self._related_account = None
        self._type = None
        self._description = None
        self._transaction_number = None
        self._custom_values = None
        self._transaction = None
        self._statuses = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if amount is not None:
            self.amount = amount
        if related_account is not None:
            self.related_account = related_account
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if transaction_number is not None:
            self.transaction_number = transaction_number
        if custom_values is not None:
            self.custom_values = custom_values
        if transaction is not None:
            self.transaction = transaction
        if statuses is not None:
            self.statuses = statuses

    @property
    def _date(self):
        """Gets the _date of this AccountHistoryResult.  # noqa: E501

        The transfer date and time  # noqa: E501

        :return: The _date of this AccountHistoryResult.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AccountHistoryResult.

        The transfer date and time  # noqa: E501

        :param _date: The _date of this AccountHistoryResult.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def amount(self):
        """Gets the amount of this AccountHistoryResult.  # noqa: E501

        The transfer amount. May be positive or negative.  # noqa: E501

        :return: The amount of this AccountHistoryResult.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AccountHistoryResult.

        The transfer amount. May be positive or negative.  # noqa: E501

        :param amount: The amount of this AccountHistoryResult.  # noqa: E501
        :type: BigDecimal
        """

        self._amount = amount

    @property
    def related_account(self):
        """Gets the related_account of this AccountHistoryResult.  # noqa: E501

        The account that either received / sent the balance  # noqa: E501

        :return: The related_account of this AccountHistoryResult.  # noqa: E501
        :rtype: AccountWithOwner
        """
        return self._related_account

    @related_account.setter
    def related_account(self, related_account):
        """Sets the related_account of this AccountHistoryResult.

        The account that either received / sent the balance  # noqa: E501

        :param related_account: The related_account of this AccountHistoryResult.  # noqa: E501
        :type: AccountWithOwner
        """

        self._related_account = related_account

    @property
    def type(self):
        """Gets the type of this AccountHistoryResult.  # noqa: E501

        The transfer type  # noqa: E501

        :return: The type of this AccountHistoryResult.  # noqa: E501
        :rtype: TransferType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountHistoryResult.

        The transfer type  # noqa: E501

        :param type: The type of this AccountHistoryResult.  # noqa: E501
        :type: TransferType
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this AccountHistoryResult.  # noqa: E501

        The transaction description. Is optional.  # noqa: E501

        :return: The description of this AccountHistoryResult.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccountHistoryResult.

        The transaction description. Is optional.  # noqa: E501

        :param description: The description of this AccountHistoryResult.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def transaction_number(self):
        """Gets the transaction_number of this AccountHistoryResult.  # noqa: E501

        The transaction number identifying this balance transfer. The currency configuration has the definition on whether transaction numbers are enabled and which format they have.   # noqa: E501

        :return: The transaction_number of this AccountHistoryResult.  # noqa: E501
        :rtype: str
        """
        return self._transaction_number

    @transaction_number.setter
    def transaction_number(self, transaction_number):
        """Sets the transaction_number of this AccountHistoryResult.

        The transaction number identifying this balance transfer. The currency configuration has the definition on whether transaction numbers are enabled and which format they have.   # noqa: E501

        :param transaction_number: The transaction_number of this AccountHistoryResult.  # noqa: E501
        :type: str
        """

        self._transaction_number = transaction_number

    @property
    def custom_values(self):
        """Gets the custom_values of this AccountHistoryResult.  # noqa: E501

        Holds the custom field values, keyed by field internal name or id. The format of the value depends on the custom field type. In order to lookup the custom fields, use the `GET /{owner}/accounts/{accountType}/data-for-history` operation, and lookup each field by either internal name (if configured) or id. Example: `{..., \"customValues\": {\"linkedAccount\": \"123456789\"}}`   # noqa: E501

        :return: The custom_values of this AccountHistoryResult.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this AccountHistoryResult.

        Holds the custom field values, keyed by field internal name or id. The format of the value depends on the custom field type. In order to lookup the custom fields, use the `GET /{owner}/accounts/{accountType}/data-for-history` operation, and lookup each field by either internal name (if configured) or id. Example: `{..., \"customValues\": {\"linkedAccount\": \"123456789\"}}`   # noqa: E501

        :param custom_values: The custom_values of this AccountHistoryResult.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_values = custom_values

    @property
    def transaction(self):
        """Gets the transaction of this AccountHistoryResult.  # noqa: E501

        If this balance transfer was originated from a transaction (like a payment or scheduled payment), contains the reference to this transaction.   # noqa: E501

        :return: The transaction of this AccountHistoryResult.  # noqa: E501
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this AccountHistoryResult.

        If this balance transfer was originated from a transaction (like a payment or scheduled payment), contains the reference to this transaction.   # noqa: E501

        :param transaction: The transaction of this AccountHistoryResult.  # noqa: E501
        :type: Transaction
        """

        self._transaction = transaction

    @property
    def statuses(self):
        """Gets the statuses of this AccountHistoryResult.  # noqa: E501

        contains the current status internal name or id, keyed by the flow internal name or id   # noqa: E501

        :return: The statuses of this AccountHistoryResult.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this AccountHistoryResult.

        contains the current status internal name or id, keyed by the flow internal name or id   # noqa: E501

        :param statuses: The statuses of this AccountHistoryResult.  # noqa: E501
        :type: dict(str, str)
        """

        self._statuses = statuses

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
        if issubclass(AccountHistoryResult, dict):
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
        if not isinstance(other, AccountHistoryResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountHistoryResult):
            return True

        return self.to_dict() != other.to_dict()
