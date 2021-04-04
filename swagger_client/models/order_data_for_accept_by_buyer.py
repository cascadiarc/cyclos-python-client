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


class OrderDataForAcceptByBuyer(object):
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
        'payment_types': 'list[TransferType]',
        'confirmation_password_input': 'PasswordInput'
    }

    attribute_map = {
        'payment_types': 'paymentTypes',
        'confirmation_password_input': 'confirmationPasswordInput'
    }

    def __init__(self, payment_types=None, confirmation_password_input=None, _configuration=None):  # noqa: E501
        """OrderDataForAcceptByBuyer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._payment_types = None
        self._confirmation_password_input = None
        self.discriminator = None

        if payment_types is not None:
            self.payment_types = payment_types
        if confirmation_password_input is not None:
            self.confirmation_password_input = confirmation_password_input

    @property
    def payment_types(self):
        """Gets the payment_types of this OrderDataForAcceptByBuyer.  # noqa: E501

        Contains the allowed payment types.  # noqa: E501

        :return: The payment_types of this OrderDataForAcceptByBuyer.  # noqa: E501
        :rtype: list[TransferType]
        """
        return self._payment_types

    @payment_types.setter
    def payment_types(self, payment_types):
        """Sets the payment_types of this OrderDataForAcceptByBuyer.

        Contains the allowed payment types.  # noqa: E501

        :param payment_types: The payment_types of this OrderDataForAcceptByBuyer.  # noqa: E501
        :type: list[TransferType]
        """

        self._payment_types = payment_types

    @property
    def confirmation_password_input(self):
        """Gets the confirmation_password_input of this OrderDataForAcceptByBuyer.  # noqa: E501

        If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).   # noqa: E501

        :return: The confirmation_password_input of this OrderDataForAcceptByBuyer.  # noqa: E501
        :rtype: PasswordInput
        """
        return self._confirmation_password_input

    @confirmation_password_input.setter
    def confirmation_password_input(self, confirmation_password_input):
        """Sets the confirmation_password_input of this OrderDataForAcceptByBuyer.

        If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).   # noqa: E501

        :param confirmation_password_input: The confirmation_password_input of this OrderDataForAcceptByBuyer.  # noqa: E501
        :type: PasswordInput
        """

        self._confirmation_password_input = confirmation_password_input

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
        if issubclass(OrderDataForAcceptByBuyer, dict):
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
        if not isinstance(other, OrderDataForAcceptByBuyer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderDataForAcceptByBuyer):
            return True

        return self.to_dict() != other.to_dict()
