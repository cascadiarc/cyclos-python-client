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


class BaseCustomFieldValue(object):
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
        'string_value': 'str',
        'date_value': 'datetime',
        'boolean_value': 'bool',
        'integer_value': 'int',
        'decimal_value': 'BigDecimal',
        'enumerated_values': 'list[CustomFieldPossibleValue]',
        'dynamic_value': 'CustomFieldDynamicValue',
        'file_values': 'list[StoredFile]',
        'image_values': 'list[Image]',
        'linked_entity_value': 'object',
        'ad_value': 'Ad',
        'transaction_value': 'Transaction',
        'transfer_value': 'Transfer',
        'record_value': 'Record',
        'user_value': 'User'
    }

    attribute_map = {
        'string_value': 'stringValue',
        'date_value': 'dateValue',
        'boolean_value': 'booleanValue',
        'integer_value': 'integerValue',
        'decimal_value': 'decimalValue',
        'enumerated_values': 'enumeratedValues',
        'dynamic_value': 'dynamicValue',
        'file_values': 'fileValues',
        'image_values': 'imageValues',
        'linked_entity_value': 'linkedEntityValue',
        'ad_value': 'adValue',
        'transaction_value': 'transactionValue',
        'transfer_value': 'transferValue',
        'record_value': 'recordValue',
        'user_value': 'userValue'
    }

    def __init__(self, string_value=None, date_value=None, boolean_value=None, integer_value=None, decimal_value=None, enumerated_values=None, dynamic_value=None, file_values=None, image_values=None, linked_entity_value=None, ad_value=None, transaction_value=None, transfer_value=None, record_value=None, user_value=None, _configuration=None):  # noqa: E501
        """BaseCustomFieldValue - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._string_value = None
        self._date_value = None
        self._boolean_value = None
        self._integer_value = None
        self._decimal_value = None
        self._enumerated_values = None
        self._dynamic_value = None
        self._file_values = None
        self._image_values = None
        self._linked_entity_value = None
        self._ad_value = None
        self._transaction_value = None
        self._transfer_value = None
        self._record_value = None
        self._user_value = None
        self.discriminator = None

        if string_value is not None:
            self.string_value = string_value
        if date_value is not None:
            self.date_value = date_value
        if boolean_value is not None:
            self.boolean_value = boolean_value
        if integer_value is not None:
            self.integer_value = integer_value
        if decimal_value is not None:
            self.decimal_value = decimal_value
        if enumerated_values is not None:
            self.enumerated_values = enumerated_values
        if dynamic_value is not None:
            self.dynamic_value = dynamic_value
        if file_values is not None:
            self.file_values = file_values
        if image_values is not None:
            self.image_values = image_values
        if linked_entity_value is not None:
            self.linked_entity_value = linked_entity_value
        if ad_value is not None:
            self.ad_value = ad_value
        if transaction_value is not None:
            self.transaction_value = transaction_value
        if transfer_value is not None:
            self.transfer_value = transfer_value
        if record_value is not None:
            self.record_value = record_value
        if user_value is not None:
            self.user_value = user_value

    @property
    def string_value(self):
        """Gets the string_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is either `string`, `text`, `richText` or `url`.   # noqa: E501

        :return: The string_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """Sets the string_value of this BaseCustomFieldValue.

        The field value if the field type is either `string`, `text`, `richText` or `url`.   # noqa: E501

        :param string_value: The string_value of this BaseCustomFieldValue.  # noqa: E501
        :type: str
        """

        self._string_value = string_value

    @property
    def date_value(self):
        """Gets the date_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `date`.   # noqa: E501

        :return: The date_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: datetime
        """
        return self._date_value

    @date_value.setter
    def date_value(self, date_value):
        """Sets the date_value of this BaseCustomFieldValue.

        The field value if the field type is `date`.   # noqa: E501

        :param date_value: The date_value of this BaseCustomFieldValue.  # noqa: E501
        :type: datetime
        """

        self._date_value = date_value

    @property
    def boolean_value(self):
        """Gets the boolean_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `boolean`.   # noqa: E501

        :return: The boolean_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: bool
        """
        return self._boolean_value

    @boolean_value.setter
    def boolean_value(self, boolean_value):
        """Sets the boolean_value of this BaseCustomFieldValue.

        The field value if the field type is `boolean`.   # noqa: E501

        :param boolean_value: The boolean_value of this BaseCustomFieldValue.  # noqa: E501
        :type: bool
        """

        self._boolean_value = boolean_value

    @property
    def integer_value(self):
        """Gets the integer_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `integer`.   # noqa: E501

        :return: The integer_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: int
        """
        return self._integer_value

    @integer_value.setter
    def integer_value(self, integer_value):
        """Sets the integer_value of this BaseCustomFieldValue.

        The field value if the field type is `integer`.   # noqa: E501

        :param integer_value: The integer_value of this BaseCustomFieldValue.  # noqa: E501
        :type: int
        """

        self._integer_value = integer_value

    @property
    def decimal_value(self):
        """Gets the decimal_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `decimal`.   # noqa: E501

        :return: The decimal_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._decimal_value

    @decimal_value.setter
    def decimal_value(self, decimal_value):
        """Sets the decimal_value of this BaseCustomFieldValue.

        The field value if the field type is `decimal`.   # noqa: E501

        :param decimal_value: The decimal_value of this BaseCustomFieldValue.  # noqa: E501
        :type: BigDecimal
        """

        self._decimal_value = decimal_value

    @property
    def enumerated_values(self):
        """Gets the enumerated_values of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is either `singleSelection` or `multiSelection`. For single selections will either be an empty array or an array with a single element   # noqa: E501

        :return: The enumerated_values of this BaseCustomFieldValue.  # noqa: E501
        :rtype: list[CustomFieldPossibleValue]
        """
        return self._enumerated_values

    @enumerated_values.setter
    def enumerated_values(self, enumerated_values):
        """Sets the enumerated_values of this BaseCustomFieldValue.

        The field value if the field type is either `singleSelection` or `multiSelection`. For single selections will either be an empty array or an array with a single element   # noqa: E501

        :param enumerated_values: The enumerated_values of this BaseCustomFieldValue.  # noqa: E501
        :type: list[CustomFieldPossibleValue]
        """

        self._enumerated_values = enumerated_values

    @property
    def dynamic_value(self):
        """Gets the dynamic_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `dynamicSelection`.   # noqa: E501

        :return: The dynamic_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: CustomFieldDynamicValue
        """
        return self._dynamic_value

    @dynamic_value.setter
    def dynamic_value(self, dynamic_value):
        """Sets the dynamic_value of this BaseCustomFieldValue.

        The field value if the field type is `dynamicSelection`.   # noqa: E501

        :param dynamic_value: The dynamic_value of this BaseCustomFieldValue.  # noqa: E501
        :type: CustomFieldDynamicValue
        """

        self._dynamic_value = dynamic_value

    @property
    def file_values(self):
        """Gets the file_values of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `file`   # noqa: E501

        :return: The file_values of this BaseCustomFieldValue.  # noqa: E501
        :rtype: list[StoredFile]
        """
        return self._file_values

    @file_values.setter
    def file_values(self, file_values):
        """Sets the file_values of this BaseCustomFieldValue.

        The field value if the field type is `file`   # noqa: E501

        :param file_values: The file_values of this BaseCustomFieldValue.  # noqa: E501
        :type: list[StoredFile]
        """

        self._file_values = file_values

    @property
    def image_values(self):
        """Gets the image_values of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `image`   # noqa: E501

        :return: The image_values of this BaseCustomFieldValue.  # noqa: E501
        :rtype: list[Image]
        """
        return self._image_values

    @image_values.setter
    def image_values(self, image_values):
        """Sets the image_values of this BaseCustomFieldValue.

        The field value if the field type is `image`   # noqa: E501

        :param image_values: The image_values of this BaseCustomFieldValue.  # noqa: E501
        :type: list[Image]
        """

        self._image_values = image_values

    @property
    def linked_entity_value(self):
        """Gets the linked_entity_value of this BaseCustomFieldValue.  # noqa: E501

        (Deprecated) The field value if the field type is `linkedEntity`.   # noqa: E501

        :return: The linked_entity_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: object
        """
        return self._linked_entity_value

    @linked_entity_value.setter
    def linked_entity_value(self, linked_entity_value):
        """Sets the linked_entity_value of this BaseCustomFieldValue.

        (Deprecated) The field value if the field type is `linkedEntity`.   # noqa: E501

        :param linked_entity_value: The linked_entity_value of this BaseCustomFieldValue.  # noqa: E501
        :type: object
        """

        self._linked_entity_value = linked_entity_value

    @property
    def ad_value(self):
        """Gets the ad_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `linkedEntity` and the linked entity type is `advertisement`. If the currently set record is not accessible by the logged user, only the `name` field is sent, which contains the advertisement title.   # noqa: E501

        :return: The ad_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: Ad
        """
        return self._ad_value

    @ad_value.setter
    def ad_value(self, ad_value):
        """Sets the ad_value of this BaseCustomFieldValue.

        The field value if the field type is `linkedEntity` and the linked entity type is `advertisement`. If the currently set record is not accessible by the logged user, only the `name` field is sent, which contains the advertisement title.   # noqa: E501

        :param ad_value: The ad_value of this BaseCustomFieldValue.  # noqa: E501
        :type: Ad
        """

        self._ad_value = ad_value

    @property
    def transaction_value(self):
        """Gets the transaction_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `linkedEntity` and the linked entity type is `transaction`. If the currently set transaction is not accessible by the logged user, only the `display` field is sent.   # noqa: E501

        :return: The transaction_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: Transaction
        """
        return self._transaction_value

    @transaction_value.setter
    def transaction_value(self, transaction_value):
        """Sets the transaction_value of this BaseCustomFieldValue.

        The field value if the field type is `linkedEntity` and the linked entity type is `transaction`. If the currently set transaction is not accessible by the logged user, only the `display` field is sent.   # noqa: E501

        :param transaction_value: The transaction_value of this BaseCustomFieldValue.  # noqa: E501
        :type: Transaction
        """

        self._transaction_value = transaction_value

    @property
    def transfer_value(self):
        """Gets the transfer_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `linkedEntity` and the linked entity type is `transfer`. If the currently set transfer is not accessible by the logged user, only the `display` field is sent.   # noqa: E501

        :return: The transfer_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: Transfer
        """
        return self._transfer_value

    @transfer_value.setter
    def transfer_value(self, transfer_value):
        """Sets the transfer_value of this BaseCustomFieldValue.

        The field value if the field type is `linkedEntity` and the linked entity type is `transfer`. If the currently set transfer is not accessible by the logged user, only the `display` field is sent.   # noqa: E501

        :param transfer_value: The transfer_value of this BaseCustomFieldValue.  # noqa: E501
        :type: Transfer
        """

        self._transfer_value = transfer_value

    @property
    def record_value(self):
        """Gets the record_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `linkedEntity` and the linked entity type is `record`. If the currently set record is not accessible by the logged user, only the `display` field is sent.   # noqa: E501

        :return: The record_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: Record
        """
        return self._record_value

    @record_value.setter
    def record_value(self, record_value):
        """Sets the record_value of this BaseCustomFieldValue.

        The field value if the field type is `linkedEntity` and the linked entity type is `record`. If the currently set record is not accessible by the logged user, only the `display` field is sent.   # noqa: E501

        :param record_value: The record_value of this BaseCustomFieldValue.  # noqa: E501
        :type: Record
        """

        self._record_value = record_value

    @property
    def user_value(self):
        """Gets the user_value of this BaseCustomFieldValue.  # noqa: E501

        The field value if the field type is `linkedEntity` and the linked entity type is `user`. If the currently set user is not accessible by the logged user, only a limited set of fields is sent, namely `display` and `shortDisplay`.   # noqa: E501

        :return: The user_value of this BaseCustomFieldValue.  # noqa: E501
        :rtype: User
        """
        return self._user_value

    @user_value.setter
    def user_value(self, user_value):
        """Sets the user_value of this BaseCustomFieldValue.

        The field value if the field type is `linkedEntity` and the linked entity type is `user`. If the currently set user is not accessible by the logged user, only a limited set of fields is sent, namely `display` and `shortDisplay`.   # noqa: E501

        :param user_value: The user_value of this BaseCustomFieldValue.  # noqa: E501
        :type: User
        """

        self._user_value = user_value

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
        if issubclass(BaseCustomFieldValue, dict):
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
        if not isinstance(other, BaseCustomFieldValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseCustomFieldValue):
            return True

        return self.to_dict() != other.to_dict()
