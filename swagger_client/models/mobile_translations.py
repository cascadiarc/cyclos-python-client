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


class MobileTranslations(object):
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
        'locale': 'str',
        'translations': 'dict(str, str)',
        'countries': 'list[Country]'
    }

    attribute_map = {
        'locale': 'locale',
        'translations': 'translations',
        'countries': 'countries'
    }

    def __init__(self, locale=None, translations=None, countries=None, _configuration=None):  # noqa: E501
        """MobileTranslations - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._locale = None
        self._translations = None
        self._countries = None
        self.discriminator = None

        if locale is not None:
            self.locale = locale
        if translations is not None:
            self.translations = translations
        if countries is not None:
            self.countries = countries

    @property
    def locale(self):
        """Gets the locale of this MobileTranslations.  # noqa: E501

        The locale represented by this language, in either of the following formats: `<2-letter lowercase language code>` or `<2-letter lowercase language code>`_`<2-letter uppercase country code>`.   # noqa: E501

        :return: The locale of this MobileTranslations.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this MobileTranslations.

        The locale represented by this language, in either of the following formats: `<2-letter lowercase language code>` or `<2-letter lowercase language code>`_`<2-letter uppercase country code>`.   # noqa: E501

        :param locale: The locale of this MobileTranslations.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def translations(self):
        """Gets the translations of this MobileTranslations.  # noqa: E501

        The translation keys / values for the mobile application  # noqa: E501

        :return: The translations of this MobileTranslations.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._translations

    @translations.setter
    def translations(self, translations):
        """Sets the translations of this MobileTranslations.

        The translation keys / values for the mobile application  # noqa: E501

        :param translations: The translations of this MobileTranslations.  # noqa: E501
        :type: dict(str, str)
        """

        self._translations = translations

    @property
    def countries(self):
        """Gets the countries of this MobileTranslations.  # noqa: E501

        The list of countries, with translated display names. Whenever the translations are returned, the country list is returned as well.    # noqa: E501

        :return: The countries of this MobileTranslations.  # noqa: E501
        :rtype: list[Country]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this MobileTranslations.

        The list of countries, with translated display names. Whenever the translations are returned, the country list is returned as well.    # noqa: E501

        :param countries: The countries of this MobileTranslations.  # noqa: E501
        :type: list[Country]
        """

        self._countries = countries

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
        if issubclass(MobileTranslations, dict):
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
        if not isinstance(other, MobileTranslations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MobileTranslations):
            return True

        return self.to_dict() != other.to_dict()
