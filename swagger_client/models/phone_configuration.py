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


class PhoneConfiguration(object):
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
        'country': 'str',
        'always_show_international_number': 'bool',
        'extension_enabled': 'bool',
        'sms_enabled': 'bool',
        'land_line_example': 'str',
        'mobile_example': 'str'
    }

    attribute_map = {
        'country': 'country',
        'always_show_international_number': 'alwaysShowInternationalNumber',
        'extension_enabled': 'extensionEnabled',
        'sms_enabled': 'smsEnabled',
        'land_line_example': 'landLineExample',
        'mobile_example': 'mobileExample'
    }

    def __init__(self, country=None, always_show_international_number=None, extension_enabled=None, sms_enabled=None, land_line_example=None, mobile_example=None, _configuration=None):  # noqa: E501
        """PhoneConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._country = None
        self._always_show_international_number = None
        self._extension_enabled = None
        self._sms_enabled = None
        self._land_line_example = None
        self._mobile_example = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if always_show_international_number is not None:
            self.always_show_international_number = always_show_international_number
        if extension_enabled is not None:
            self.extension_enabled = extension_enabled
        if sms_enabled is not None:
            self.sms_enabled = sms_enabled
        if land_line_example is not None:
            self.land_line_example = land_line_example
        if mobile_example is not None:
            self.mobile_example = mobile_example

    @property
    def country(self):
        """Gets the country of this PhoneConfiguration.  # noqa: E501

        The 2-letter country code used by default for numbers. Unless an international number is specified (using the `+` prefix), the phone number is assumed to belong to this country.   # noqa: E501

        :return: The country of this PhoneConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PhoneConfiguration.

        The 2-letter country code used by default for numbers. Unless an international number is specified (using the `+` prefix), the phone number is assumed to belong to this country.   # noqa: E501

        :param country: The country of this PhoneConfiguration.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def always_show_international_number(self):
        """Gets the always_show_international_number of this PhoneConfiguration.  # noqa: E501

        Indicates the it is configured to always format numbers using the international format. If set to false, numbers will be formatted in the national format.   # noqa: E501

        :return: The always_show_international_number of this PhoneConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._always_show_international_number

    @always_show_international_number.setter
    def always_show_international_number(self, always_show_international_number):
        """Sets the always_show_international_number of this PhoneConfiguration.

        Indicates the it is configured to always format numbers using the international format. If set to false, numbers will be formatted in the national format.   # noqa: E501

        :param always_show_international_number: The always_show_international_number of this PhoneConfiguration.  # noqa: E501
        :type: bool
        """

        self._always_show_international_number = always_show_international_number

    @property
    def extension_enabled(self):
        """Gets the extension_enabled of this PhoneConfiguration.  # noqa: E501

        Indicates whether the extension is enabled for land-line phones  # noqa: E501

        :return: The extension_enabled of this PhoneConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._extension_enabled

    @extension_enabled.setter
    def extension_enabled(self, extension_enabled):
        """Sets the extension_enabled of this PhoneConfiguration.

        Indicates whether the extension is enabled for land-line phones  # noqa: E501

        :param extension_enabled: The extension_enabled of this PhoneConfiguration.  # noqa: E501
        :type: bool
        """

        self._extension_enabled = extension_enabled

    @property
    def sms_enabled(self):
        """Gets the sms_enabled of this PhoneConfiguration.  # noqa: E501

        Indicates whether outbound SMS is enabled in Cyclos  # noqa: E501

        :return: The sms_enabled of this PhoneConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._sms_enabled

    @sms_enabled.setter
    def sms_enabled(self, sms_enabled):
        """Sets the sms_enabled of this PhoneConfiguration.

        Indicates whether outbound SMS is enabled in Cyclos  # noqa: E501

        :param sms_enabled: The sms_enabled of this PhoneConfiguration.  # noqa: E501
        :type: bool
        """

        self._sms_enabled = sms_enabled

    @property
    def land_line_example(self):
        """Gets the land_line_example of this PhoneConfiguration.  # noqa: E501

        An example phone number for a land-line phone  # noqa: E501

        :return: The land_line_example of this PhoneConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._land_line_example

    @land_line_example.setter
    def land_line_example(self, land_line_example):
        """Sets the land_line_example of this PhoneConfiguration.

        An example phone number for a land-line phone  # noqa: E501

        :param land_line_example: The land_line_example of this PhoneConfiguration.  # noqa: E501
        :type: str
        """

        self._land_line_example = land_line_example

    @property
    def mobile_example(self):
        """Gets the mobile_example of this PhoneConfiguration.  # noqa: E501

        An example phone number for a mobile phone  # noqa: E501

        :return: The mobile_example of this PhoneConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._mobile_example

    @mobile_example.setter
    def mobile_example(self, mobile_example):
        """Sets the mobile_example of this PhoneConfiguration.

        An example phone number for a mobile phone  # noqa: E501

        :param mobile_example: The mobile_example of this PhoneConfiguration.  # noqa: E501
        :type: str
        """

        self._mobile_example = mobile_example

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
        if issubclass(PhoneConfiguration, dict):
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
        if not isinstance(other, PhoneConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhoneConfiguration):
            return True

        return self.to_dict() != other.to_dict()