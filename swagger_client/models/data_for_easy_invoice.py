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


class DataForEasyInvoice(object):
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
        'to': 'User',
        'amount': 'BigDecimal',
        'currency': 'Currency',
        'payment_type_data': 'TransactionTypeData',
        'payment_types': 'list[TransferTypeWithCurrency]',
        'custom_values': 'list[CustomFieldValue]'
    }

    attribute_map = {
        'to': 'to',
        'amount': 'amount',
        'currency': 'currency',
        'payment_type_data': 'paymentTypeData',
        'payment_types': 'paymentTypes',
        'custom_values': 'customValues'
    }

    def __init__(self, to=None, amount=None, currency=None, payment_type_data=None, payment_types=None, custom_values=None, _configuration=None):  # noqa: E501
        """DataForEasyInvoice - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._to = None
        self._amount = None
        self._currency = None
        self._payment_type_data = None
        self._payment_types = None
        self._custom_values = None
        self.discriminator = None

        if to is not None:
            self.to = to
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if payment_type_data is not None:
            self.payment_type_data = payment_type_data
        if payment_types is not None:
            self.payment_types = payment_types
        if custom_values is not None:
            self.custom_values = custom_values

    @property
    def to(self):
        """Gets the to of this DataForEasyInvoice.  # noqa: E501

        The destination user details. Is only returned if called with a logged user or if the user's group is visible to guests accoerding to the current configuration.    # noqa: E501

        :return: The to of this DataForEasyInvoice.  # noqa: E501
        :rtype: User
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this DataForEasyInvoice.

        The destination user details. Is only returned if called with a logged user or if the user's group is visible to guests accoerding to the current configuration.    # noqa: E501

        :param to: The to of this DataForEasyInvoice.  # noqa: E501
        :type: User
        """

        self._to = to

    @property
    def amount(self):
        """Gets the amount of this DataForEasyInvoice.  # noqa: E501

        The easy invoice amount  # noqa: E501

        :return: The amount of this DataForEasyInvoice.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DataForEasyInvoice.

        The easy invoice amount  # noqa: E501

        :param amount: The amount of this DataForEasyInvoice.  # noqa: E501
        :type: BigDecimal
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this DataForEasyInvoice.  # noqa: E501

        The easy invoice currency.  # noqa: E501

        :return: The currency of this DataForEasyInvoice.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this DataForEasyInvoice.

        The easy invoice currency.  # noqa: E501

        :param currency: The currency of this DataForEasyInvoice.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def payment_type_data(self):
        """Gets the payment_type_data of this DataForEasyInvoice.  # noqa: E501

        Contains the detailed data for the selected (or first) payment type. Only returned if there is a logged user. The custom fields will only contain those without a fixed value.   # noqa: E501

        :return: The payment_type_data of this DataForEasyInvoice.  # noqa: E501
        :rtype: TransactionTypeData
        """
        return self._payment_type_data

    @payment_type_data.setter
    def payment_type_data(self, payment_type_data):
        """Sets the payment_type_data of this DataForEasyInvoice.

        Contains the detailed data for the selected (or first) payment type. Only returned if there is a logged user. The custom fields will only contain those without a fixed value.   # noqa: E501

        :param payment_type_data: The payment_type_data of this DataForEasyInvoice.  # noqa: E501
        :type: TransactionTypeData
        """

        self._payment_type_data = payment_type_data

    @property
    def payment_types(self):
        """Gets the payment_types of this DataForEasyInvoice.  # noqa: E501

        Only returned if there is a logged user, and a specific payment type was not informed. Contains the allowed payment types to the given user.   # noqa: E501

        :return: The payment_types of this DataForEasyInvoice.  # noqa: E501
        :rtype: list[TransferTypeWithCurrency]
        """
        return self._payment_types

    @payment_types.setter
    def payment_types(self, payment_types):
        """Sets the payment_types of this DataForEasyInvoice.

        Only returned if there is a logged user, and a specific payment type was not informed. Contains the allowed payment types to the given user.   # noqa: E501

        :param payment_types: The payment_types of this DataForEasyInvoice.  # noqa: E501
        :type: list[TransferTypeWithCurrency]
        """

        self._payment_types = payment_types

    @property
    def custom_values(self):
        """Gets the custom_values of this DataForEasyInvoice.  # noqa: E501

        The list of custom field values with a fixed value, as requested.    # noqa: E501

        :return: The custom_values of this DataForEasyInvoice.  # noqa: E501
        :rtype: list[CustomFieldValue]
        """
        return self._custom_values

    @custom_values.setter
    def custom_values(self, custom_values):
        """Sets the custom_values of this DataForEasyInvoice.

        The list of custom field values with a fixed value, as requested.    # noqa: E501

        :param custom_values: The custom_values of this DataForEasyInvoice.  # noqa: E501
        :type: list[CustomFieldValue]
        """

        self._custom_values = custom_values

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
        if issubclass(DataForEasyInvoice, dict):
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
        if not isinstance(other, DataForEasyInvoice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForEasyInvoice):
            return True

        return self.to_dict() != other.to_dict()