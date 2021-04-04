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


class BasicUserDataForEdit(object):
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
        'email_pending_validation': 'str',
        'binary_values': 'CustomFieldBinaryValues'
    }

    attribute_map = {
        'email_pending_validation': 'emailPendingValidation',
        'binary_values': 'binaryValues'
    }

    def __init__(self, email_pending_validation=None, binary_values=None, _configuration=None):  # noqa: E501
        """BasicUserDataForEdit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email_pending_validation = None
        self._binary_values = None
        self.discriminator = None

        if email_pending_validation is not None:
            self.email_pending_validation = email_pending_validation
        if binary_values is not None:
            self.binary_values = binary_values

    @property
    def email_pending_validation(self):
        """Gets the email_pending_validation of this BasicUserDataForEdit.  # noqa: E501

        The new e-mail address, which is still pending validation. Is only returned when e-mail validation is enabled for edit profile, and the user has changed the e-mail address.   # noqa: E501

        :return: The email_pending_validation of this BasicUserDataForEdit.  # noqa: E501
        :rtype: str
        """
        return self._email_pending_validation

    @email_pending_validation.setter
    def email_pending_validation(self, email_pending_validation):
        """Sets the email_pending_validation of this BasicUserDataForEdit.

        The new e-mail address, which is still pending validation. Is only returned when e-mail validation is enabled for edit profile, and the user has changed the e-mail address.   # noqa: E501

        :param email_pending_validation: The email_pending_validation of this BasicUserDataForEdit.  # noqa: E501
        :type: str
        """

        self._email_pending_validation = email_pending_validation

    @property
    def binary_values(self):
        """Gets the binary_values of this BasicUserDataForEdit.  # noqa: E501

        Holds the current values for file / image custom fields as lists of `StoredFile`s / `Image`s.   # noqa: E501

        :return: The binary_values of this BasicUserDataForEdit.  # noqa: E501
        :rtype: CustomFieldBinaryValues
        """
        return self._binary_values

    @binary_values.setter
    def binary_values(self, binary_values):
        """Sets the binary_values of this BasicUserDataForEdit.

        Holds the current values for file / image custom fields as lists of `StoredFile`s / `Image`s.   # noqa: E501

        :param binary_values: The binary_values of this BasicUserDataForEdit.  # noqa: E501
        :type: CustomFieldBinaryValues
        """

        self._binary_values = binary_values

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
        if issubclass(BasicUserDataForEdit, dict):
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
        if not isinstance(other, BasicUserDataForEdit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasicUserDataForEdit):
            return True

        return self.to_dict() != other.to_dict()