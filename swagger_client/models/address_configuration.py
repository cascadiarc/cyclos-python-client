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


class AddressConfiguration(object):
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
        'use_map': 'bool',
        'enabled_fields': 'list[AddressFieldEnum]',
        'required_fields': 'list[AddressFieldEnum]'
    }

    attribute_map = {
        'use_map': 'useMap',
        'enabled_fields': 'enabledFields',
        'required_fields': 'requiredFields'
    }

    def __init__(self, use_map=None, enabled_fields=None, required_fields=None, _configuration=None):  # noqa: E501
        """AddressConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._use_map = None
        self._enabled_fields = None
        self._required_fields = None
        self.discriminator = None

        if use_map is not None:
            self.use_map = use_map
        if enabled_fields is not None:
            self.enabled_fields = enabled_fields
        if required_fields is not None:
            self.required_fields = required_fields

    @property
    def use_map(self):
        """Gets the use_map of this AddressConfiguration.  # noqa: E501

        Indicates whether maps are enabled in Cyclos  # noqa: E501

        :return: The use_map of this AddressConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_map

    @use_map.setter
    def use_map(self, use_map):
        """Sets the use_map of this AddressConfiguration.

        Indicates whether maps are enabled in Cyclos  # noqa: E501

        :param use_map: The use_map of this AddressConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_map = use_map

    @property
    def enabled_fields(self):
        """Gets the enabled_fields of this AddressConfiguration.  # noqa: E501

        Contains the address fields that are enabled in Cyclos Possibles values for each array element are: * addressLine1: The first line of the descriptive address * addressLine2: The second line of the descriptive address * buildingNumber: The numeric identifier for a land parcel, house, building or other * city: The city name * complement: The complement (like apartment number)   * country: The country, represented as 2-letter, uppercase, ISO 3166-1 code * neighborhood: The neighborhood name  * poBox: The post-office box, is an uniquely addressable box * region: The region or state * street: The street name * zip: A zip code that identifies a specific geographic (postal) delivery area   # noqa: E501

        :return: The enabled_fields of this AddressConfiguration.  # noqa: E501
        :rtype: list[AddressFieldEnum]
        """
        return self._enabled_fields

    @enabled_fields.setter
    def enabled_fields(self, enabled_fields):
        """Sets the enabled_fields of this AddressConfiguration.

        Contains the address fields that are enabled in Cyclos Possibles values for each array element are: * addressLine1: The first line of the descriptive address * addressLine2: The second line of the descriptive address * buildingNumber: The numeric identifier for a land parcel, house, building or other * city: The city name * complement: The complement (like apartment number)   * country: The country, represented as 2-letter, uppercase, ISO 3166-1 code * neighborhood: The neighborhood name  * poBox: The post-office box, is an uniquely addressable box * region: The region or state * street: The street name * zip: A zip code that identifies a specific geographic (postal) delivery area   # noqa: E501

        :param enabled_fields: The enabled_fields of this AddressConfiguration.  # noqa: E501
        :type: list[AddressFieldEnum]
        """

        self._enabled_fields = enabled_fields

    @property
    def required_fields(self):
        """Gets the required_fields of this AddressConfiguration.  # noqa: E501

        Contains the address fields that are required in Cyclos Possibles values for each array element are: * addressLine1: The first line of the descriptive address * addressLine2: The second line of the descriptive address * buildingNumber: The numeric identifier for a land parcel, house, building or other * city: The city name * complement: The complement (like apartment number)   * country: The country, represented as 2-letter, uppercase, ISO 3166-1 code * neighborhood: The neighborhood name  * poBox: The post-office box, is an uniquely addressable box * region: The region or state * street: The street name * zip: A zip code that identifies a specific geographic (postal) delivery area   # noqa: E501

        :return: The required_fields of this AddressConfiguration.  # noqa: E501
        :rtype: list[AddressFieldEnum]
        """
        return self._required_fields

    @required_fields.setter
    def required_fields(self, required_fields):
        """Sets the required_fields of this AddressConfiguration.

        Contains the address fields that are required in Cyclos Possibles values for each array element are: * addressLine1: The first line of the descriptive address * addressLine2: The second line of the descriptive address * buildingNumber: The numeric identifier for a land parcel, house, building or other * city: The city name * complement: The complement (like apartment number)   * country: The country, represented as 2-letter, uppercase, ISO 3166-1 code * neighborhood: The neighborhood name  * poBox: The post-office box, is an uniquely addressable box * region: The region or state * street: The street name * zip: A zip code that identifies a specific geographic (postal) delivery area   # noqa: E501

        :param required_fields: The required_fields of this AddressConfiguration.  # noqa: E501
        :type: list[AddressFieldEnum]
        """

        self._required_fields = required_fields

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
        if issubclass(AddressConfiguration, dict):
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
        if not isinstance(other, AddressConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressConfiguration):
            return True

        return self.to_dict() != other.to_dict()