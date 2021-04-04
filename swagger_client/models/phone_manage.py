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


class PhoneManage(object):
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
        'name': 'str',
        'number': 'str',
        'extension': 'str',
        'hidden': 'bool',
        'enabled_for_sms': 'bool',
        'verified': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'number': 'number',
        'extension': 'extension',
        'hidden': 'hidden',
        'enabled_for_sms': 'enabledForSms',
        'verified': 'verified'
    }

    def __init__(self, name=None, number=None, extension=None, hidden=None, enabled_for_sms=None, verified=None, _configuration=None):  # noqa: E501
        """PhoneManage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._number = None
        self._extension = None
        self._hidden = None
        self._enabled_for_sms = None
        self._verified = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if extension is not None:
            self.extension = extension
        if hidden is not None:
            self.hidden = hidden
        if enabled_for_sms is not None:
            self.enabled_for_sms = enabled_for_sms
        if verified is not None:
            self.verified = verified

    @property
    def name(self):
        """Gets the name of this PhoneManage.  # noqa: E501

        The phone name  # noqa: E501

        :return: The name of this PhoneManage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhoneManage.

        The phone name  # noqa: E501

        :param name: The name of this PhoneManage.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this PhoneManage.  # noqa: E501

        The formatted number  # noqa: E501

        :return: The number of this PhoneManage.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PhoneManage.

        The formatted number  # noqa: E501

        :param number: The number of this PhoneManage.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def extension(self):
        """Gets the extension of this PhoneManage.  # noqa: E501

        The number extension, only for landLine phones, and is only used if the phone configuration states that extensions are enabled.    # noqa: E501

        :return: The extension of this PhoneManage.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this PhoneManage.

        The number extension, only for landLine phones, and is only used if the phone configuration states that extensions are enabled.    # noqa: E501

        :param extension: The extension of this PhoneManage.  # noqa: E501
        :type: str
        """

        self._extension = extension

    @property
    def hidden(self):
        """Gets the hidden of this PhoneManage.  # noqa: E501

        Indicates whether this phone is hidden for other users (`true`) or visible to all users (`false`).   # noqa: E501

        :return: The hidden of this PhoneManage.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this PhoneManage.

        Indicates whether this phone is hidden for other users (`true`) or visible to all users (`false`).   # noqa: E501

        :param hidden: The hidden of this PhoneManage.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def enabled_for_sms(self):
        """Gets the enabled_for_sms of this PhoneManage.  # noqa: E501

        Only applicable if this represents a mobile phone. Whether this mobile phone is enabled for SMS, both receiving notifications and sending SMS operations. Can only be set if the mobile phone is verified.   # noqa: E501

        :return: The enabled_for_sms of this PhoneManage.  # noqa: E501
        :rtype: bool
        """
        return self._enabled_for_sms

    @enabled_for_sms.setter
    def enabled_for_sms(self, enabled_for_sms):
        """Sets the enabled_for_sms of this PhoneManage.

        Only applicable if this represents a mobile phone. Whether this mobile phone is enabled for SMS, both receiving notifications and sending SMS operations. Can only be set if the mobile phone is verified.   # noqa: E501

        :param enabled_for_sms: The enabled_for_sms of this PhoneManage.  # noqa: E501
        :type: bool
        """

        self._enabled_for_sms = enabled_for_sms

    @property
    def verified(self):
        """Gets the verified of this PhoneManage.  # noqa: E501

        Only applicable if this represents a mobile phone. Whether this mobile is verified. Can only be directly set by administrators. Regular users need to verify it.   # noqa: E501

        :return: The verified of this PhoneManage.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this PhoneManage.

        Only applicable if this represents a mobile phone. Whether this mobile is verified. Can only be directly set by administrators. Regular users need to verify it.   # noqa: E501

        :param verified: The verified of this PhoneManage.  # noqa: E501
        :type: bool
        """

        self._verified = verified

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
        if issubclass(PhoneManage, dict):
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
        if not isinstance(other, PhoneManage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhoneManage):
            return True

        return self.to_dict() != other.to_dict()