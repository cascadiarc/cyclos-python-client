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


class RecordSection(object):
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
        'information_text': 'str',
        'fields': 'list[str]'
    }

    attribute_map = {
        'information_text': 'informationText',
        'fields': 'fields'
    }

    def __init__(self, information_text=None, fields=None, _configuration=None):  # noqa: E501
        """RecordSection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._information_text = None
        self._fields = None
        self.discriminator = None

        if information_text is not None:
            self.information_text = information_text
        if fields is not None:
            self.fields = fields

    @property
    def information_text(self):
        """Gets the information_text of this RecordSection.  # noqa: E501

        An informative text that should be shown in the form. The text is formatted in HTML.   # noqa: E501

        :return: The information_text of this RecordSection.  # noqa: E501
        :rtype: str
        """
        return self._information_text

    @information_text.setter
    def information_text(self, information_text):
        """Sets the information_text of this RecordSection.

        An informative text that should be shown in the form. The text is formatted in HTML.   # noqa: E501

        :param information_text: The information_text of this RecordSection.  # noqa: E501
        :type: str
        """

        self._information_text = information_text

    @property
    def fields(self):
        """Gets the fields of this RecordSection.  # noqa: E501

        The internal names of the custom fields which are part of this section.   # noqa: E501

        :return: The fields of this RecordSection.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this RecordSection.

        The internal names of the custom fields which are part of this section.   # noqa: E501

        :param fields: The fields of this RecordSection.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

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
        if issubclass(RecordSection, dict):
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
        if not isinstance(other, RecordSection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecordSection):
            return True

        return self.to_dict() != other.to_dict()
