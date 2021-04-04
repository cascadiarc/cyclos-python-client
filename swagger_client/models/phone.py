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


class Phone(object):
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
        'type': 'PhoneKind',
        'normalized_number': 'str'
    }

    attribute_map = {
        'name': 'name',
        'number': 'number',
        'extension': 'extension',
        'type': 'type',
        'normalized_number': 'normalizedNumber'
    }

    def __init__(self, name=None, number=None, extension=None, type=None, normalized_number=None, _configuration=None):  # noqa: E501
        """Phone - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._number = None
        self._extension = None
        self._type = None
        self._normalized_number = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if extension is not None:
            self.extension = extension
        if type is not None:
            self.type = type
        if normalized_number is not None:
            self.normalized_number = normalized_number

    @property
    def name(self):
        """Gets the name of this Phone.  # noqa: E501

        The phone name  # noqa: E501

        :return: The name of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Phone.

        The phone name  # noqa: E501

        :param name: The name of this Phone.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this Phone.  # noqa: E501

        The formatted number  # noqa: E501

        :return: The number of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Phone.

        The formatted number  # noqa: E501

        :param number: The number of this Phone.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def extension(self):
        """Gets the extension of this Phone.  # noqa: E501

        The number extension, only for landLine phones, and is only used if the phone configuration states that extensions are enabled.    # noqa: E501

        :return: The extension of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this Phone.

        The number extension, only for landLine phones, and is only used if the phone configuration states that extensions are enabled.    # noqa: E501

        :param extension: The extension of this Phone.  # noqa: E501
        :type: str
        """

        self._extension = extension

    @property
    def type(self):
        """Gets the type of this Phone.  # noqa: E501

        Type of phone Possible values are: * landLine: A landline phone * mobile: A mobile phone   # noqa: E501

        :return: The type of this Phone.  # noqa: E501
        :rtype: PhoneKind
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Phone.

        Type of phone Possible values are: * landLine: A landline phone * mobile: A mobile phone   # noqa: E501

        :param type: The type of this Phone.  # noqa: E501
        :type: PhoneKind
        """

        self._type = type

    @property
    def normalized_number(self):
        """Gets the normalized_number of this Phone.  # noqa: E501

        The number, normalized to the E.164 format  # noqa: E501

        :return: The normalized_number of this Phone.  # noqa: E501
        :rtype: str
        """
        return self._normalized_number

    @normalized_number.setter
    def normalized_number(self, normalized_number):
        """Sets the normalized_number of this Phone.

        The number, normalized to the E.164 format  # noqa: E501

        :param normalized_number: The normalized_number of this Phone.  # noqa: E501
        :type: str
        """

        self._normalized_number = normalized_number

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
        if issubclass(Phone, dict):
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
        if not isinstance(other, Phone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Phone):
            return True

        return self.to_dict() != other.to_dict()
