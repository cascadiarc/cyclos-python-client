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


class ScheduledPaymentInstallmentPreview(object):
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
        'number': 'int',
        'due_date': 'datetime',
        'total_amount': 'BigDecimal',
        'main_amount': 'BigDecimal',
        'fees': 'list[TransferFeePreview]'
    }

    attribute_map = {
        'number': 'number',
        'due_date': 'dueDate',
        'total_amount': 'totalAmount',
        'main_amount': 'mainAmount',
        'fees': 'fees'
    }

    def __init__(self, number=None, due_date=None, total_amount=None, main_amount=None, fees=None, _configuration=None):  # noqa: E501
        """ScheduledPaymentInstallmentPreview - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._number = None
        self._due_date = None
        self._total_amount = None
        self._main_amount = None
        self._fees = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if due_date is not None:
            self.due_date = due_date
        if total_amount is not None:
            self.total_amount = total_amount
        if main_amount is not None:
            self.main_amount = main_amount
        if fees is not None:
            self.fees = fees

    @property
    def number(self):
        """Gets the number of this ScheduledPaymentInstallmentPreview.  # noqa: E501

        The installment number  # noqa: E501

        :return: The number of this ScheduledPaymentInstallmentPreview.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ScheduledPaymentInstallmentPreview.

        The installment number  # noqa: E501

        :param number: The number of this ScheduledPaymentInstallmentPreview.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def due_date(self):
        """Gets the due_date of this ScheduledPaymentInstallmentPreview.  # noqa: E501

        The installment due date  # noqa: E501

        :return: The due_date of this ScheduledPaymentInstallmentPreview.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this ScheduledPaymentInstallmentPreview.

        The installment due date  # noqa: E501

        :param due_date: The due_date of this ScheduledPaymentInstallmentPreview.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def total_amount(self):
        """Gets the total_amount of this ScheduledPaymentInstallmentPreview.  # noqa: E501

        The final total installment amount  # noqa: E501

        :return: The total_amount of this ScheduledPaymentInstallmentPreview.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this ScheduledPaymentInstallmentPreview.

        The final total installment amount  # noqa: E501

        :param total_amount: The total_amount of this ScheduledPaymentInstallmentPreview.  # noqa: E501
        :type: BigDecimal
        """

        self._total_amount = total_amount

    @property
    def main_amount(self):
        """Gets the main_amount of this ScheduledPaymentInstallmentPreview.  # noqa: E501

        Depending on the configured fees, it could happen that the main amount is deducted from fees amount. This reflects the new main amount. If no fees deduct, it will be the same as `totalAmount`.   # noqa: E501

        :return: The main_amount of this ScheduledPaymentInstallmentPreview.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._main_amount

    @main_amount.setter
    def main_amount(self, main_amount):
        """Sets the main_amount of this ScheduledPaymentInstallmentPreview.

        Depending on the configured fees, it could happen that the main amount is deducted from fees amount. This reflects the new main amount. If no fees deduct, it will be the same as `totalAmount`.   # noqa: E501

        :param main_amount: The main_amount of this ScheduledPaymentInstallmentPreview.  # noqa: E501
        :type: BigDecimal
        """

        self._main_amount = main_amount

    @property
    def fees(self):
        """Gets the fees of this ScheduledPaymentInstallmentPreview.  # noqa: E501

        Only returned for direct payments. Contains the fees that would be paid by the payer if the payment is confirmed.   # noqa: E501

        :return: The fees of this ScheduledPaymentInstallmentPreview.  # noqa: E501
        :rtype: list[TransferFeePreview]
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this ScheduledPaymentInstallmentPreview.

        Only returned for direct payments. Contains the fees that would be paid by the payer if the payment is confirmed.   # noqa: E501

        :param fees: The fees of this ScheduledPaymentInstallmentPreview.  # noqa: E501
        :type: list[TransferFeePreview]
        """

        self._fees = fees

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
        if issubclass(ScheduledPaymentInstallmentPreview, dict):
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
        if not isinstance(other, ScheduledPaymentInstallmentPreview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduledPaymentInstallmentPreview):
            return True

        return self.to_dict() != other.to_dict()
