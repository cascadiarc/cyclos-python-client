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


class ContactDataForEdit(object):
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
        'editable_fields': 'list[str]',
        'contact': 'ContactEdit',
        'binary_values': 'CustomFieldBinaryValues'
    }

    attribute_map = {
        'editable_fields': 'editableFields',
        'contact': 'contact',
        'binary_values': 'binaryValues'
    }

    def __init__(self, editable_fields=None, contact=None, binary_values=None, _configuration=None):  # noqa: E501
        """ContactDataForEdit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._editable_fields = None
        self._contact = None
        self._binary_values = None
        self.discriminator = None

        if editable_fields is not None:
            self.editable_fields = editable_fields
        if contact is not None:
            self.contact = contact
        if binary_values is not None:
            self.binary_values = binary_values

    @property
    def editable_fields(self):
        """Gets the editable_fields of this ContactDataForEdit.  # noqa: E501

        The internal names of custom fields that can be edited  # noqa: E501

        :return: The editable_fields of this ContactDataForEdit.  # noqa: E501
        :rtype: list[str]
        """
        return self._editable_fields

    @editable_fields.setter
    def editable_fields(self, editable_fields):
        """Sets the editable_fields of this ContactDataForEdit.

        The internal names of custom fields that can be edited  # noqa: E501

        :param editable_fields: The editable_fields of this ContactDataForEdit.  # noqa: E501
        :type: list[str]
        """

        self._editable_fields = editable_fields

    @property
    def contact(self):
        """Gets the contact of this ContactDataForEdit.  # noqa: E501

        The contact that is being edited. This value can be modified and sent back to `PUT /contact/{id}`   # noqa: E501

        :return: The contact of this ContactDataForEdit.  # noqa: E501
        :rtype: ContactEdit
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this ContactDataForEdit.

        The contact that is being edited. This value can be modified and sent back to `PUT /contact/{id}`   # noqa: E501

        :param contact: The contact of this ContactDataForEdit.  # noqa: E501
        :type: ContactEdit
        """

        self._contact = contact

    @property
    def binary_values(self):
        """Gets the binary_values of this ContactDataForEdit.  # noqa: E501

        Holds the current values for file / image custom fields as lists of `StoredFile`s / `Image`s.   # noqa: E501

        :return: The binary_values of this ContactDataForEdit.  # noqa: E501
        :rtype: CustomFieldBinaryValues
        """
        return self._binary_values

    @binary_values.setter
    def binary_values(self, binary_values):
        """Sets the binary_values of this ContactDataForEdit.

        Holds the current values for file / image custom fields as lists of `StoredFile`s / `Image`s.   # noqa: E501

        :param binary_values: The binary_values of this ContactDataForEdit.  # noqa: E501
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
        if issubclass(ContactDataForEdit, dict):
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
        if not isinstance(other, ContactDataForEdit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactDataForEdit):
            return True

        return self.to_dict() != other.to_dict()
