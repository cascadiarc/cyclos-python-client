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


class RecordQueryFilters(object):
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
        'creation_period': 'list[datetime]'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'creation_period': 'creationPeriod'
    }

    def __init__(self, custom_fields=None, creation_period=None, _configuration=None):  # noqa: E501
        """RecordQueryFilters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_fields = None
        self._creation_period = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if creation_period is not None:
            self.creation_period = creation_period

    @property
    def custom_fields(self):
        """Gets the custom_fields of this RecordQueryFilters.  # noqa: E501

        Record custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, `customFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields=field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `customFields=tradeType:offer|search,extraDate:2000-01-01|2001-12-31` would match results whose custom field with internal name `tradeType` is either `offer` or `search`, and whose `extraDate` is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `customFields=extraDate:|2001-12-31`.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `customFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `customFields=dynamic:'business`.   # noqa: E501

        :return: The custom_fields of this RecordQueryFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this RecordQueryFilters.

        Record custom field values used as filters. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon).  For example, `customFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, customFields=field1:valueA|valueB. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `customFields=tradeType:offer|search,extraDate:2000-01-01|2001-12-31` would match results whose custom field with internal name `tradeType` is either `offer` or `search`, and whose `extraDate` is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `customFields=extraDate:|2001-12-31`.  A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `customFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `customFields=dynamic:'business`.   # noqa: E501

        :param custom_fields: The custom_fields of this RecordQueryFilters.  # noqa: E501
        :type: list[str]
        """

        self._custom_fields = custom_fields

    @property
    def creation_period(self):
        """Gets the creation_period of this RecordQueryFilters.  # noqa: E501

        The minimum / maximum record creation date   # noqa: E501

        :return: The creation_period of this RecordQueryFilters.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._creation_period

    @creation_period.setter
    def creation_period(self, creation_period):
        """Sets the creation_period of this RecordQueryFilters.

        The minimum / maximum record creation date   # noqa: E501

        :param creation_period: The creation_period of this RecordQueryFilters.  # noqa: E501
        :type: list[datetime]
        """

        self._creation_period = creation_period

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
        if issubclass(RecordQueryFilters, dict):
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
        if not isinstance(other, RecordQueryFilters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecordQueryFilters):
            return True

        return self.to_dict() != other.to_dict()
