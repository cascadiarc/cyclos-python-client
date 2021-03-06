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


class InputError(object):
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
        'code': 'InputErrorCode',
        'general_errors': 'list[str]',
        'properties': 'list[str]',
        'property_errors': 'dict(str, list[str])',
        'custom_fields': 'list[str]',
        'custom_field_errors': 'dict(str, list[str])',
        'max_items': 'int',
        'max_file_size': 'int',
        'value': 'str',
        'name': 'str',
        'errors': 'dict(str, InputError)',
        'indexed_errors': 'dict(str, list[InputError])'
    }

    attribute_map = {
        'code': 'code',
        'general_errors': 'generalErrors',
        'properties': 'properties',
        'property_errors': 'propertyErrors',
        'custom_fields': 'customFields',
        'custom_field_errors': 'customFieldErrors',
        'max_items': 'maxItems',
        'max_file_size': 'maxFileSize',
        'value': 'value',
        'name': 'name',
        'errors': 'errors',
        'indexed_errors': 'indexedErrors'
    }

    def __init__(self, code=None, general_errors=None, properties=None, property_errors=None, custom_fields=None, custom_field_errors=None, max_items=None, max_file_size=None, value=None, name=None, errors=None, indexed_errors=None, _configuration=None):  # noqa: E501
        """InputError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._general_errors = None
        self._properties = None
        self._property_errors = None
        self._custom_fields = None
        self._custom_field_errors = None
        self._max_items = None
        self._max_file_size = None
        self._value = None
        self._name = None
        self._errors = None
        self._indexed_errors = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if general_errors is not None:
            self.general_errors = general_errors
        if properties is not None:
            self.properties = properties
        if property_errors is not None:
            self.property_errors = property_errors
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if custom_field_errors is not None:
            self.custom_field_errors = custom_field_errors
        if max_items is not None:
            self.max_items = max_items
        if max_file_size is not None:
            self.max_file_size = max_file_size
        if value is not None:
            self.value = value
        if name is not None:
            self.name = name
        if errors is not None:
            self.errors = errors
        if indexed_errors is not None:
            self.indexed_errors = indexed_errors

    @property
    def code(self):
        """Gets the code of this InputError.  # noqa: E501

        Error codes for 422 Unprocessable entity HTTP status. It means there was an error with the input sent to the operation.  Possible values are: * aggregated: Represents an aggregation of other input errors * dataConversion: Some data conversion has failed. For example, when sending a date with an invalid format * fileUploadSize: An uploaded file size exceeds the maximum allowed  * maxItems: There was an attempt to create an item, but the maximum number of allowed items was exceeded * missingParameter: Missing a required request parameter * queryParse: A full-text query keywords contained an invalid text * validation: One or more of the fields sent contains invalid values   # noqa: E501

        :return: The code of this InputError.  # noqa: E501
        :rtype: InputErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InputError.

        Error codes for 422 Unprocessable entity HTTP status. It means there was an error with the input sent to the operation.  Possible values are: * aggregated: Represents an aggregation of other input errors * dataConversion: Some data conversion has failed. For example, when sending a date with an invalid format * fileUploadSize: An uploaded file size exceeds the maximum allowed  * maxItems: There was an attempt to create an item, but the maximum number of allowed items was exceeded * missingParameter: Missing a required request parameter * queryParse: A full-text query keywords contained an invalid text * validation: One or more of the fields sent contains invalid values   # noqa: E501

        :param code: The code of this InputError.  # noqa: E501
        :type: InputErrorCode
        """

        self._code = code

    @property
    def general_errors(self):
        """Gets the general_errors of this InputError.  # noqa: E501

        A list of errors that cannot be attributed to a specific property. Only returned if `code` is `validation`.   # noqa: E501

        :return: The general_errors of this InputError.  # noqa: E501
        :rtype: list[str]
        """
        return self._general_errors

    @general_errors.setter
    def general_errors(self, general_errors):
        """Sets the general_errors of this InputError.

        A list of errors that cannot be attributed to a specific property. Only returned if `code` is `validation`.   # noqa: E501

        :param general_errors: The general_errors of this InputError.  # noqa: E501
        :type: list[str]
        """

        self._general_errors = general_errors

    @property
    def properties(self):
        """Gets the properties of this InputError.  # noqa: E501

        An array of properties which contains errors, in the order they were processed. As `propertyErrors` is an object (without a guaranteed order for its keys) the original order would be lost otherwise. Only returned if `code` is `validation`.   # noqa: E501

        :return: The properties of this InputError.  # noqa: E501
        :rtype: list[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this InputError.

        An array of properties which contains errors, in the order they were processed. As `propertyErrors` is an object (without a guaranteed order for its keys) the original order would be lost otherwise. Only returned if `code` is `validation`.   # noqa: E501

        :param properties: The properties of this InputError.  # noqa: E501
        :type: list[str]
        """

        self._properties = properties

    @property
    def property_errors(self):
        """Gets the property_errors of this InputError.  # noqa: E501

        An object keyed by property name, whose values are lists of errors for that property. Only returned if `code` is `validation`.   # noqa: E501

        :return: The property_errors of this InputError.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._property_errors

    @property_errors.setter
    def property_errors(self, property_errors):
        """Sets the property_errors of this InputError.

        An object keyed by property name, whose values are lists of errors for that property. Only returned if `code` is `validation`.   # noqa: E501

        :param property_errors: The property_errors of this InputError.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._property_errors = property_errors

    @property
    def custom_fields(self):
        """Gets the custom_fields of this InputError.  # noqa: E501

        An array of custom field internal names which contains errors, in the order they were processed. As `propertyErrors` is an object (without a guaranteed order for its keys) the original order would be lost otherwise. Only returned if `code` is `validation`.   # noqa: E501

        :return: The custom_fields of this InputError.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this InputError.

        An array of custom field internal names which contains errors, in the order they were processed. As `propertyErrors` is an object (without a guaranteed order for its keys) the original order would be lost otherwise. Only returned if `code` is `validation`.   # noqa: E501

        :param custom_fields: The custom_fields of this InputError.  # noqa: E501
        :type: list[str]
        """

        self._custom_fields = custom_fields

    @property
    def custom_field_errors(self):
        """Gets the custom_field_errors of this InputError.  # noqa: E501

        An object keyed by custom field internal name, whose values are lists of errors for that custom field. Only returned if `code` is `validation`.   # noqa: E501

        :return: The custom_field_errors of this InputError.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._custom_field_errors

    @custom_field_errors.setter
    def custom_field_errors(self, custom_field_errors):
        """Sets the custom_field_errors of this InputError.

        An object keyed by custom field internal name, whose values are lists of errors for that custom field. Only returned if `code` is `validation`.   # noqa: E501

        :param custom_field_errors: The custom_field_errors of this InputError.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._custom_field_errors = custom_field_errors

    @property
    def max_items(self):
        """Gets the max_items of this InputError.  # noqa: E501

        The maximum allowed items. Only returned if `code` is `maxItems`.   # noqa: E501

        :return: The max_items of this InputError.  # noqa: E501
        :rtype: int
        """
        return self._max_items

    @max_items.setter
    def max_items(self, max_items):
        """Sets the max_items of this InputError.

        The maximum allowed items. Only returned if `code` is `maxItems`.   # noqa: E501

        :param max_items: The max_items of this InputError.  # noqa: E501
        :type: int
        """

        self._max_items = max_items

    @property
    def max_file_size(self):
        """Gets the max_file_size of this InputError.  # noqa: E501

        The maximum file size, in bytes, allowed for uploads. Only returned if `code` is `fileUploadSize`.   # noqa: E501

        :return: The max_file_size of this InputError.  # noqa: E501
        :rtype: int
        """
        return self._max_file_size

    @max_file_size.setter
    def max_file_size(self, max_file_size):
        """Sets the max_file_size of this InputError.

        The maximum file size, in bytes, allowed for uploads. Only returned if `code` is `fileUploadSize`.   # noqa: E501

        :param max_file_size: The max_file_size of this InputError.  # noqa: E501
        :type: int
        """

        self._max_file_size = max_file_size

    @property
    def value(self):
        """Gets the value of this InputError.  # noqa: E501

        The value that failed conversion to the expected data type, or the original full-text query keywords that failed parsing. Only returned if `code` is either `dataConversion` or `queryParse`.   # noqa: E501

        :return: The value of this InputError.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InputError.

        The value that failed conversion to the expected data type, or the original full-text query keywords that failed parsing. Only returned if `code` is either `dataConversion` or `queryParse`.   # noqa: E501

        :param value: The value of this InputError.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def name(self):
        """Gets the name of this InputError.  # noqa: E501

        The name of the required request parameter Only returned if `code` is `missingParameter`.   # noqa: E501

        :return: The name of this InputError.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputError.

        The name of the required request parameter Only returned if `code` is `missingParameter`.   # noqa: E501

        :param name: The name of this InputError.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def errors(self):
        """Gets the errors of this InputError.  # noqa: E501

        The aggregated `InputError`s for each regular property, that is, those that have a single input. Only returned if `code` is `aggregated`.   # noqa: E501

        :return: The errors of this InputError.  # noqa: E501
        :rtype: dict(str, InputError)
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InputError.

        The aggregated `InputError`s for each regular property, that is, those that have a single input. Only returned if `code` is `aggregated`.   # noqa: E501

        :param errors: The errors of this InputError.  # noqa: E501
        :type: dict(str, InputError)
        """

        self._errors = errors

    @property
    def indexed_errors(self):
        """Gets the indexed_errors of this InputError.  # noqa: E501

        The aggregated `InputError`s for each list property, that is, those that have a list of inputs. It is guaranteed that the indexes in the input array correspond to the indexes in the corresponding value. The positions with no errors will contain `null`. Only returned if `code` is `aggregated`.   # noqa: E501

        :return: The indexed_errors of this InputError.  # noqa: E501
        :rtype: dict(str, list[InputError])
        """
        return self._indexed_errors

    @indexed_errors.setter
    def indexed_errors(self, indexed_errors):
        """Sets the indexed_errors of this InputError.

        The aggregated `InputError`s for each list property, that is, those that have a list of inputs. It is guaranteed that the indexes in the input array correspond to the indexes in the corresponding value. The positions with no errors will contain `null`. Only returned if `code` is `aggregated`.   # noqa: E501

        :param indexed_errors: The indexed_errors of this InputError.  # noqa: E501
        :type: dict(str, list[InputError])
        """

        self._indexed_errors = indexed_errors

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
        if issubclass(InputError, dict):
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
        if not isinstance(other, InputError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputError):
            return True

        return self.to_dict() != other.to_dict()
