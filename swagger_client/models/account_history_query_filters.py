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


class AccountHistoryQueryFilters(object):
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
        'custom_fields': 'list[str]',
        'direction': 'TransferDirectionEnum'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'direction': 'direction'
    }

    def __init__(self, custom_fields=None, direction=None, _configuration=None):  # noqa: E501
        """AccountHistoryQueryFilters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_fields = None
        self._direction = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if direction is not None:
            self.direction = direction

    @property
    def custom_fields(self):
        """Gets the custom_fields of this AccountHistoryQueryFilters.  # noqa: E501

        Transaction custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, `customFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields=field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `customFields=rank:bronze|silver,documentDate:2000-01-01|2001-12-31` would match results whose custom field with internal name `rank` is either `bronze` or `silver`, and whose `documentDate` is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `customFields=documentDate:|2001-12-31`.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `customFields=dynamic:a|b|c`. However, it is also possible to perform a partial-match search using the dynamic value label. In this case a single value, prefixed or enclosed by single quotes should be used. For example: `customFields=dynamic:'business` or `customFields=dynamic:'business'`.          # noqa: E501

        :return: The custom_fields of this AccountHistoryQueryFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this AccountHistoryQueryFilters.

        Transaction custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, `customFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields=field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `customFields=rank:bronze|silver,documentDate:2000-01-01|2001-12-31` would match results whose custom field with internal name `rank` is either `bronze` or `silver`, and whose `documentDate` is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `customFields=documentDate:|2001-12-31`.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `customFields=dynamic:a|b|c`. However, it is also possible to perform a partial-match search using the dynamic value label. In this case a single value, prefixed or enclosed by single quotes should be used. For example: `customFields=dynamic:'business` or `customFields=dynamic:'business'`.          # noqa: E501

        :param custom_fields: The custom_fields of this AccountHistoryQueryFilters.  # noqa: E501
        :type: list[str]
        """

        self._custom_fields = custom_fields

    @property
    def direction(self):
        """Gets the direction of this AccountHistoryQueryFilters.  # noqa: E501

        Indicates whether from an account POV a transfer is a credit or debit Possible values are: * credit: The transfer impacts the balance positively * debit: The transfer impacts the balance negatively   # noqa: E501

        :return: The direction of this AccountHistoryQueryFilters.  # noqa: E501
        :rtype: TransferDirectionEnum
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this AccountHistoryQueryFilters.

        Indicates whether from an account POV a transfer is a credit or debit Possible values are: * credit: The transfer impacts the balance positively * debit: The transfer impacts the balance negatively   # noqa: E501

        :param direction: The direction of this AccountHistoryQueryFilters.  # noqa: E501
        :type: TransferDirectionEnum
        """

        self._direction = direction

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
        if issubclass(AccountHistoryQueryFilters, dict):
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
        if not isinstance(other, AccountHistoryQueryFilters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountHistoryQueryFilters):
            return True

        return self.to_dict() != other.to_dict()