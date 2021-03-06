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


class RecordTypeDetailed(object):
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
        'field_columns': 'int',
        'nowrap_labels': 'bool',
        'information_text': 'str',
        'sections': 'list[RecordSection]'
    }

    attribute_map = {
        'field_columns': 'fieldColumns',
        'nowrap_labels': 'nowrapLabels',
        'information_text': 'informationText',
        'sections': 'sections'
    }

    def __init__(self, field_columns=None, nowrap_labels=None, information_text=None, sections=None, _configuration=None):  # noqa: E501
        """RecordTypeDetailed - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._field_columns = None
        self._nowrap_labels = None
        self._information_text = None
        self._sections = None
        self.discriminator = None

        if field_columns is not None:
            self.field_columns = field_columns
        if nowrap_labels is not None:
            self.nowrap_labels = nowrap_labels
        if information_text is not None:
            self.information_text = information_text
        if sections is not None:
            self.sections = sections

    @property
    def field_columns(self):
        """Gets the field_columns of this RecordTypeDetailed.  # noqa: E501

        The number of columns which should be used to layout fields    # noqa: E501

        :return: The field_columns of this RecordTypeDetailed.  # noqa: E501
        :rtype: int
        """
        return self._field_columns

    @field_columns.setter
    def field_columns(self, field_columns):
        """Sets the field_columns of this RecordTypeDetailed.

        The number of columns which should be used to layout fields    # noqa: E501

        :param field_columns: The field_columns of this RecordTypeDetailed.  # noqa: E501
        :type: int
        """

        self._field_columns = field_columns

    @property
    def nowrap_labels(self):
        """Gets the nowrap_labels of this RecordTypeDetailed.  # noqa: E501

        Indicates whether labels in the form should be prevented from wrapping lines    # noqa: E501

        :return: The nowrap_labels of this RecordTypeDetailed.  # noqa: E501
        :rtype: bool
        """
        return self._nowrap_labels

    @nowrap_labels.setter
    def nowrap_labels(self, nowrap_labels):
        """Sets the nowrap_labels of this RecordTypeDetailed.

        Indicates whether labels in the form should be prevented from wrapping lines    # noqa: E501

        :param nowrap_labels: The nowrap_labels of this RecordTypeDetailed.  # noqa: E501
        :type: bool
        """

        self._nowrap_labels = nowrap_labels

    @property
    def information_text(self):
        """Gets the information_text of this RecordTypeDetailed.  # noqa: E501

        An informative text that should be shown in the form. The text is formatted in HTML.   # noqa: E501

        :return: The information_text of this RecordTypeDetailed.  # noqa: E501
        :rtype: str
        """
        return self._information_text

    @information_text.setter
    def information_text(self, information_text):
        """Sets the information_text of this RecordTypeDetailed.

        An informative text that should be shown in the form. The text is formatted in HTML.   # noqa: E501

        :param information_text: The information_text of this RecordTypeDetailed.  # noqa: E501
        :type: str
        """

        self._information_text = information_text

    @property
    def sections(self):
        """Gets the sections of this RecordTypeDetailed.  # noqa: E501

        The field sections in this record type    # noqa: E501

        :return: The sections of this RecordTypeDetailed.  # noqa: E501
        :rtype: list[RecordSection]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this RecordTypeDetailed.

        The field sections in this record type    # noqa: E501

        :param sections: The sections of this RecordTypeDetailed.  # noqa: E501
        :type: list[RecordSection]
        """

        self._sections = sections

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
        if issubclass(RecordTypeDetailed, dict):
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
        if not isinstance(other, RecordTypeDetailed):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecordTypeDetailed):
            return True

        return self.to_dict() != other.to_dict()
