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


class BankingPermissions(object):
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
        'accounts': 'list[AccountPermissions]',
        'payments': 'PaymentsPermissions',
        'authorizations': 'TransactionAuthorizationsPermissions',
        'scheduled_payments': 'ScheduledPaymentsPermissions',
        'recurring_payments': 'RecurringPaymentsPermissions',
        'external_payments': 'ExternalPaymentsPermissions',
        'payment_requests': 'PaymentRequestsPermissions',
        'tickets': 'TicketsPermissions'
    }

    attribute_map = {
        'accounts': 'accounts',
        'payments': 'payments',
        'authorizations': 'authorizations',
        'scheduled_payments': 'scheduledPayments',
        'recurring_payments': 'recurringPayments',
        'external_payments': 'externalPayments',
        'payment_requests': 'paymentRequests',
        'tickets': 'tickets'
    }

    def __init__(self, accounts=None, payments=None, authorizations=None, scheduled_payments=None, recurring_payments=None, external_payments=None, payment_requests=None, tickets=None, _configuration=None):  # noqa: E501
        """BankingPermissions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accounts = None
        self._payments = None
        self._authorizations = None
        self._scheduled_payments = None
        self._recurring_payments = None
        self._external_payments = None
        self._payment_requests = None
        self._tickets = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if payments is not None:
            self.payments = payments
        if authorizations is not None:
            self.authorizations = authorizations
        if scheduled_payments is not None:
            self.scheduled_payments = scheduled_payments
        if recurring_payments is not None:
            self.recurring_payments = recurring_payments
        if external_payments is not None:
            self.external_payments = external_payments
        if payment_requests is not None:
            self.payment_requests = payment_requests
        if tickets is not None:
            self.tickets = tickets

    @property
    def accounts(self):
        """Gets the accounts of this BankingPermissions.  # noqa: E501

        Permissions over each owned account  # noqa: E501

        :return: The accounts of this BankingPermissions.  # noqa: E501
        :rtype: list[AccountPermissions]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this BankingPermissions.

        Permissions over each owned account  # noqa: E501

        :param accounts: The accounts of this BankingPermissions.  # noqa: E501
        :type: list[AccountPermissions]
        """

        self._accounts = accounts

    @property
    def payments(self):
        """Gets the payments of this BankingPermissions.  # noqa: E501

        Payments permissions  # noqa: E501

        :return: The payments of this BankingPermissions.  # noqa: E501
        :rtype: PaymentsPermissions
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this BankingPermissions.

        Payments permissions  # noqa: E501

        :param payments: The payments of this BankingPermissions.  # noqa: E501
        :type: PaymentsPermissions
        """

        self._payments = payments

    @property
    def authorizations(self):
        """Gets the authorizations of this BankingPermissions.  # noqa: E501

        Transaction authorization permissions  # noqa: E501

        :return: The authorizations of this BankingPermissions.  # noqa: E501
        :rtype: TransactionAuthorizationsPermissions
        """
        return self._authorizations

    @authorizations.setter
    def authorizations(self, authorizations):
        """Sets the authorizations of this BankingPermissions.

        Transaction authorization permissions  # noqa: E501

        :param authorizations: The authorizations of this BankingPermissions.  # noqa: E501
        :type: TransactionAuthorizationsPermissions
        """

        self._authorizations = authorizations

    @property
    def scheduled_payments(self):
        """Gets the scheduled_payments of this BankingPermissions.  # noqa: E501

        Scheduled payments permissions  # noqa: E501

        :return: The scheduled_payments of this BankingPermissions.  # noqa: E501
        :rtype: ScheduledPaymentsPermissions
        """
        return self._scheduled_payments

    @scheduled_payments.setter
    def scheduled_payments(self, scheduled_payments):
        """Sets the scheduled_payments of this BankingPermissions.

        Scheduled payments permissions  # noqa: E501

        :param scheduled_payments: The scheduled_payments of this BankingPermissions.  # noqa: E501
        :type: ScheduledPaymentsPermissions
        """

        self._scheduled_payments = scheduled_payments

    @property
    def recurring_payments(self):
        """Gets the recurring_payments of this BankingPermissions.  # noqa: E501

        Recurring payments permissions  # noqa: E501

        :return: The recurring_payments of this BankingPermissions.  # noqa: E501
        :rtype: RecurringPaymentsPermissions
        """
        return self._recurring_payments

    @recurring_payments.setter
    def recurring_payments(self, recurring_payments):
        """Sets the recurring_payments of this BankingPermissions.

        Recurring payments permissions  # noqa: E501

        :param recurring_payments: The recurring_payments of this BankingPermissions.  # noqa: E501
        :type: RecurringPaymentsPermissions
        """

        self._recurring_payments = recurring_payments

    @property
    def external_payments(self):
        """Gets the external_payments of this BankingPermissions.  # noqa: E501

        External payments permissions  # noqa: E501

        :return: The external_payments of this BankingPermissions.  # noqa: E501
        :rtype: ExternalPaymentsPermissions
        """
        return self._external_payments

    @external_payments.setter
    def external_payments(self, external_payments):
        """Sets the external_payments of this BankingPermissions.

        External payments permissions  # noqa: E501

        :param external_payments: The external_payments of this BankingPermissions.  # noqa: E501
        :type: ExternalPaymentsPermissions
        """

        self._external_payments = external_payments

    @property
    def payment_requests(self):
        """Gets the payment_requests of this BankingPermissions.  # noqa: E501

        Payment requests permissions  # noqa: E501

        :return: The payment_requests of this BankingPermissions.  # noqa: E501
        :rtype: PaymentRequestsPermissions
        """
        return self._payment_requests

    @payment_requests.setter
    def payment_requests(self, payment_requests):
        """Sets the payment_requests of this BankingPermissions.

        Payment requests permissions  # noqa: E501

        :param payment_requests: The payment_requests of this BankingPermissions.  # noqa: E501
        :type: PaymentRequestsPermissions
        """

        self._payment_requests = payment_requests

    @property
    def tickets(self):
        """Gets the tickets of this BankingPermissions.  # noqa: E501

        Tickets permissions  # noqa: E501

        :return: The tickets of this BankingPermissions.  # noqa: E501
        :rtype: TicketsPermissions
        """
        return self._tickets

    @tickets.setter
    def tickets(self, tickets):
        """Sets the tickets of this BankingPermissions.

        Tickets permissions  # noqa: E501

        :param tickets: The tickets of this BankingPermissions.  # noqa: E501
        :type: TicketsPermissions
        """

        self._tickets = tickets

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
        if issubclass(BankingPermissions, dict):
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
        if not isinstance(other, BankingPermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BankingPermissions):
            return True

        return self.to_dict() != other.to_dict()