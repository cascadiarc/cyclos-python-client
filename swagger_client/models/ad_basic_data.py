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


class AdBasicData(object):
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
        'custom_fields': 'list[CustomFieldDetailed]',
        'requires_authorization': 'bool',
        'categories': 'list[AdCategoryWithChildren]',
        'addresses': 'list[Address]'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'requires_authorization': 'requiresAuthorization',
        'categories': 'categories',
        'addresses': 'addresses'
    }

    def __init__(self, custom_fields=None, requires_authorization=None, categories=None, addresses=None, _configuration=None):  # noqa: E501
        """AdBasicData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_fields = None
        self._requires_authorization = None
        self._categories = None
        self._addresses = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if requires_authorization is not None:
            self.requires_authorization = requires_authorization
        if categories is not None:
            self.categories = categories
        if addresses is not None:
            self.addresses = addresses

    @property
    def custom_fields(self):
        """Gets the custom_fields of this AdBasicData.  # noqa: E501

        The possible advertisement custom fields   # noqa: E501

        :return: The custom_fields of this AdBasicData.  # noqa: E501
        :rtype: list[CustomFieldDetailed]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this AdBasicData.

        The possible advertisement custom fields   # noqa: E501

        :param custom_fields: The custom_fields of this AdBasicData.  # noqa: E501
        :type: list[CustomFieldDetailed]
        """

        self._custom_fields = custom_fields

    @property
    def requires_authorization(self):
        """Gets the requires_authorization of this AdBasicData.  # noqa: E501

        Indicates whether advertisements require an authorization from the administration in order to be published for other users to see   # noqa: E501

        :return: The requires_authorization of this AdBasicData.  # noqa: E501
        :rtype: bool
        """
        return self._requires_authorization

    @requires_authorization.setter
    def requires_authorization(self, requires_authorization):
        """Sets the requires_authorization of this AdBasicData.

        Indicates whether advertisements require an authorization from the administration in order to be published for other users to see   # noqa: E501

        :param requires_authorization: The requires_authorization of this AdBasicData.  # noqa: E501
        :type: bool
        """

        self._requires_authorization = requires_authorization

    @property
    def categories(self):
        """Gets the categories of this AdBasicData.  # noqa: E501

        The advertisement categoriesn each with its children, forming a tree   # noqa: E501

        :return: The categories of this AdBasicData.  # noqa: E501
        :rtype: list[AdCategoryWithChildren]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this AdBasicData.

        The advertisement categoriesn each with its children, forming a tree   # noqa: E501

        :param categories: The categories of this AdBasicData.  # noqa: E501
        :type: list[AdCategoryWithChildren]
        """

        self._categories = categories

    @property
    def addresses(self):
        """Gets the addresses of this AdBasicData.  # noqa: E501

        The addresses of the advertisement owner, so specific ones can be linked to the advertisement.   # noqa: E501

        :return: The addresses of this AdBasicData.  # noqa: E501
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this AdBasicData.

        The addresses of the advertisement owner, so specific ones can be linked to the advertisement.   # noqa: E501

        :param addresses: The addresses of this AdBasicData.  # noqa: E501
        :type: list[Address]
        """

        self._addresses = addresses

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
        if issubclass(AdBasicData, dict):
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
        if not isinstance(other, AdBasicData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdBasicData):
            return True

        return self.to_dict() != other.to_dict()
