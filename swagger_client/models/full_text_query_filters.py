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


class FullTextQueryFilters(object):
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
        'keywords': 'str',
        'profile_fields': 'list[str]'
    }

    attribute_map = {
        'keywords': 'keywords',
        'profile_fields': 'profileFields'
    }

    def __init__(self, keywords=None, profile_fields=None, _configuration=None):  # noqa: E501
        """FullTextQueryFilters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._keywords = None
        self._profile_fields = None
        self.discriminator = None

        if keywords is not None:
            self.keywords = keywords
        if profile_fields is not None:
            self.profile_fields = profile_fields

    @property
    def keywords(self):
        """Gets the keywords of this FullTextQueryFilters.  # noqa: E501

        Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.   # noqa: E501

        :return: The keywords of this FullTextQueryFilters.  # noqa: E501
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this FullTextQueryFilters.

        Textual search keywords. Sometimes, like in user search, the fields matched depends on what is configured on the products.   # noqa: E501

        :param keywords: The keywords of this FullTextQueryFilters.  # noqa: E501
        :type: str
        """

        self._keywords = keywords

    @property
    def profile_fields(self):
        """Gets the profile_fields of this FullTextQueryFilters.  # noqa: E501

        User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, `profileFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, `profileFields=field1:valueA|valueB`. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `profileFields=rank:bronze|silver,birthDate:2000-01-01|2001-12-31` would match results whose custom field with internal name 'rank' is either bronze or silver, and whose 'birthDate' is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `profileFields=birthDate:|2001-12-31`.  The basic profile fields have one of the following identifiers:  * `name` or `fullName`: Full name;  * `username`, `loginName` or `login`: Login name;  * `email`: E-mail;  * `phone`: Phone;  * `accountNumber`, `account`: Account number;  * `image`: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the `addressFieldsInSearch` field in the corresponding result from a data-for-search request.   The specific address fields are:  * `address`: Searches on any address field (not a specific field);  * `address.address`: Searches on the fields that represent the   street address, which are `addressLine1`,    `addressLine2`,   `street`,   `buildingNumber` and   `complement`. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * `address.zip`: Searches for matching zip (postal) code;  * `address.poBox`: Searches for matching postal box;  * `address.neighborhood`: Searches by neighborhood;  * `address.city`: Searches by city;  * `address.region`: Searches by region (or state);  * `address.country`: Searches by ISO 3166-1 alpha-2 country code.   A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `profileFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `profileFields=dynamic:'business`.   # noqa: E501

        :return: The profile_fields of this FullTextQueryFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._profile_fields

    @profile_fields.setter
    def profile_fields(self, profile_fields):
        """Sets the profile_fields of this FullTextQueryFilters.

        User profile fields, both basic (full name, login name, phone, e-mail, etc) and custom fields, that are used for search. Is a comma-separated array, where each part consists in two parts: the internal name (or custom field id) of the field, and a value, both separated by : (colon). For example, `profileFields=field1:value1,field2:value2`. Sometimes multiple values are accepted. In this case, the multiple values are separated by pipes. For example, `profileFields=field1:valueA|valueB`. The accepted fields depend on the products the authenticated user has. Enumerated fields accept multiple values, while numeric and date fields also accept ranges, which are two values, pipe-separated. For example, `profileFields=rank:bronze|silver,birthDate:2000-01-01|2001-12-31` would match results whose custom field with internal name 'rank' is either bronze or silver, and whose 'birthDate' is between January 1, 2000 and December 31, 2001. To specify a single bound in ranges (like birth dates before December 31, 2001), use a pipe in one of the values, like `profileFields=birthDate:|2001-12-31`.  The basic profile fields have one of the following identifiers:  * `name` or `fullName`: Full name;  * `username`, `loginName` or `login`: Login name;  * `email`: E-mail;  * `phone`: Phone;  * `accountNumber`, `account`: Account number;  * `image`: Image (accepts a boolean value, indicating that either it   is required that users either have images or not).  If address is an allowed profile field for search, specific address fields may be searched. The allowed ones are normally returned as the `addressFieldsInSearch` field in the corresponding result from a data-for-search request.   The specific address fields are:  * `address`: Searches on any address field (not a specific field);  * `address.address`: Searches on the fields that represent the   street address, which are `addressLine1`,    `addressLine2`,   `street`,   `buildingNumber` and   `complement`. Note that normally only a   subset of them should be enabled in the configuration (either line   1 / 2 or street + number + complement);  * `address.zip`: Searches for matching zip (postal) code;  * `address.poBox`: Searches for matching postal box;  * `address.neighborhood`: Searches by neighborhood;  * `address.city`: Searches by city;  * `address.region`: Searches by region (or state);  * `address.country`: Searches by ISO 3166-1 alpha-2 country code.   A note for dynamic custom fields: If a script is used to generate possible values for search, the list will be returned in the  corresponding data, and it is sent as a pipe-separated list of values (not labels). For example: `profileFields=dynamic:a|b|c`. However, it is also possible to perform a keywords-like (full-text) search using the dynamic value label. In this case a single value, prefixed by single quotes should be used. For example: `profileFields=dynamic:'business`.   # noqa: E501

        :param profile_fields: The profile_fields of this FullTextQueryFilters.  # noqa: E501
        :type: list[str]
        """

        self._profile_fields = profile_fields

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
        if issubclass(FullTextQueryFilters, dict):
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
        if not isinstance(other, FullTextQueryFilters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullTextQueryFilters):
            return True

        return self.to_dict() != other.to_dict()