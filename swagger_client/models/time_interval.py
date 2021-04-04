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


class TimeInterval(object):
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
        'amount': 'int',
        'field': 'TimeFieldEnum'
    }

    attribute_map = {
        'amount': 'amount',
        'field': 'field'
    }

    def __init__(self, amount=None, field=None, _configuration=None):  # noqa: E501
        """TimeInterval - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount = None
        self._field = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if field is not None:
            self.field = field

    @property
    def amount(self):
        """Gets the amount of this TimeInterval.  # noqa: E501

        The amount of time units  # noqa: E501

        :return: The amount of this TimeInterval.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TimeInterval.

        The amount of time units  # noqa: E501

        :param amount: The amount of this TimeInterval.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def field(self):
        """Gets the field of this TimeInterval.  # noqa: E501

        Determines a time field, such as seconds, hours or months Possible values are: * days: Day(s) * hours: Hour(s) * millis: Millisecond(s) * minutes: Minute(s) * months: Month(s) * seconds: Second(s) * weeks: Week(s) * years: Year(s)   # noqa: E501

        :return: The field of this TimeInterval.  # noqa: E501
        :rtype: TimeFieldEnum
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this TimeInterval.

        Determines a time field, such as seconds, hours or months Possible values are: * days: Day(s) * hours: Hour(s) * millis: Millisecond(s) * minutes: Minute(s) * months: Month(s) * seconds: Second(s) * weeks: Week(s) * years: Year(s)   # noqa: E501

        :param field: The field of this TimeInterval.  # noqa: E501
        :type: TimeFieldEnum
        """

        self._field = field

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
        if issubclass(TimeInterval, dict):
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
        if not isinstance(other, TimeInterval):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeInterval):
            return True

        return self.to_dict() != other.to_dict()