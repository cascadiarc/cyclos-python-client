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


class SearchByDistanceData(object):
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
        'addresses': 'list[Address]',
        'distance_unit': 'DistanceEnum',
        'default_values': 'dict(str, str)'
    }

    attribute_map = {
        'addresses': 'addresses',
        'distance_unit': 'distanceUnit',
        'default_values': 'defaultValues'
    }

    def __init__(self, addresses=None, distance_unit=None, default_values=None, _configuration=None):  # noqa: E501
        """SearchByDistanceData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._addresses = None
        self._distance_unit = None
        self._default_values = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if distance_unit is not None:
            self.distance_unit = distance_unit
        if default_values is not None:
            self.default_values = default_values

    @property
    def addresses(self):
        """Gets the addresses of this SearchByDistanceData.  # noqa: E501

        The list of addresses owned by the authenticated user  # noqa: E501

        :return: The addresses of this SearchByDistanceData.  # noqa: E501
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this SearchByDistanceData.

        The list of addresses owned by the authenticated user  # noqa: E501

        :param addresses: The addresses of this SearchByDistanceData.  # noqa: E501
        :type: list[Address]
        """

        self._addresses = addresses

    @property
    def distance_unit(self):
        """Gets the distance_unit of this SearchByDistanceData.  # noqa: E501

        Unit for measuring distances Possible values are: * kilometer: Unit representing kilometers * mile: Unit representing miles    # noqa: E501

        :return: The distance_unit of this SearchByDistanceData.  # noqa: E501
        :rtype: DistanceEnum
        """
        return self._distance_unit

    @distance_unit.setter
    def distance_unit(self, distance_unit):
        """Sets the distance_unit of this SearchByDistanceData.

        Unit for measuring distances Possible values are: * kilometer: Unit representing kilometers * mile: Unit representing miles    # noqa: E501

        :param distance_unit: The distance_unit of this SearchByDistanceData.  # noqa: E501
        :type: DistanceEnum
        """

        self._distance_unit = distance_unit

    @property
    def default_values(self):
        """Gets the default_values of this SearchByDistanceData.  # noqa: E501

        The default values, keyed by field name, for address fields  # noqa: E501

        :return: The default_values of this SearchByDistanceData.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """Sets the default_values of this SearchByDistanceData.

        The default values, keyed by field name, for address fields  # noqa: E501

        :param default_values: The default_values of this SearchByDistanceData.  # noqa: E501
        :type: dict(str, str)
        """

        self._default_values = default_values

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
        if issubclass(SearchByDistanceData, dict):
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
        if not isinstance(other, SearchByDistanceData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchByDistanceData):
            return True

        return self.to_dict() != other.to_dict()