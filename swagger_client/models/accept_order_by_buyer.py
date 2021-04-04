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


class AcceptOrderByBuyer(object):
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
        'payment_type': 'str'
    }

    attribute_map = {
        'payment_type': 'paymentType'
    }

    def __init__(self, payment_type=None, _configuration=None):  # noqa: E501
        """AcceptOrderByBuyer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._payment_type = None
        self.discriminator = None

        if payment_type is not None:
            self.payment_type = payment_type

    @property
    def payment_type(self):
        """Gets the payment_type of this AcceptOrderByBuyer.  # noqa: E501

        Either the internal name or id of the selected payment type (if any).   # noqa: E501

        :return: The payment_type of this AcceptOrderByBuyer.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this AcceptOrderByBuyer.

        Either the internal name or id of the selected payment type (if any).   # noqa: E501

        :param payment_type: The payment_type of this AcceptOrderByBuyer.  # noqa: E501
        :type: str
        """

        self._payment_type = payment_type

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
        if issubclass(AcceptOrderByBuyer, dict):
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
        if not isinstance(other, AcceptOrderByBuyer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AcceptOrderByBuyer):
            return True

        return self.to_dict() != other.to_dict()
