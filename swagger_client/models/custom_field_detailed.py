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


class CustomFieldDetailed(object):
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
        'size': 'CustomFieldSizeEnum',
        'pattern': 'str',
        'required': 'bool',
        'all_selected_label': 'str',
        'default_value': 'str',
        'possible_value_categories': 'list[EntityReference]',
        'has_values_list': 'bool',
        'possible_values': 'list[CustomFieldPossibleValue]',
        'dynamic_values': 'list[CustomFieldDynamicValue]',
        'string_values': 'list[str]',
        'date_values': 'list[datetime]',
        'integer_values': 'list[int]',
        'decimal_values': 'list[BigDecimal]',
        'ad_values': 'list[Ad]',
        'transaction_values': 'list[Transaction]',
        'transfer_values': 'list[Transfer]',
        'record_values': 'list[Record]',
        'user_values': 'list[User]',
        'max_files': 'int',
        'mime_types': 'list[str]',
        'allowed_mime_types': 'list[FileMimeTypeEnum]',
        'other_mime_types': 'list[str]'
    }

    attribute_map = {
        'information_text': 'informationText',
        'size': 'size',
        'pattern': 'pattern',
        'required': 'required',
        'all_selected_label': 'allSelectedLabel',
        'default_value': 'defaultValue',
        'possible_value_categories': 'possibleValueCategories',
        'has_values_list': 'hasValuesList',
        'possible_values': 'possibleValues',
        'dynamic_values': 'dynamicValues',
        'string_values': 'stringValues',
        'date_values': 'dateValues',
        'integer_values': 'integerValues',
        'decimal_values': 'decimalValues',
        'ad_values': 'adValues',
        'transaction_values': 'transactionValues',
        'transfer_values': 'transferValues',
        'record_values': 'recordValues',
        'user_values': 'userValues',
        'max_files': 'maxFiles',
        'mime_types': 'mimeTypes',
        'allowed_mime_types': 'allowedMimeTypes',
        'other_mime_types': 'otherMimeTypes'
    }

    def __init__(self, information_text=None, size=None, pattern=None, required=None, all_selected_label=None, default_value=None, possible_value_categories=None, has_values_list=None, possible_values=None, dynamic_values=None, string_values=None, date_values=None, integer_values=None, decimal_values=None, ad_values=None, transaction_values=None, transfer_values=None, record_values=None, user_values=None, max_files=None, mime_types=None, allowed_mime_types=None, other_mime_types=None, _configuration=None):  # noqa: E501
        """CustomFieldDetailed - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._information_text = None
        self._size = None
        self._pattern = None
        self._required = None
        self._all_selected_label = None
        self._default_value = None
        self._possible_value_categories = None
        self._has_values_list = None
        self._possible_values = None
        self._dynamic_values = None
        self._string_values = None
        self._date_values = None
        self._integer_values = None
        self._decimal_values = None
        self._ad_values = None
        self._transaction_values = None
        self._transfer_values = None
        self._record_values = None
        self._user_values = None
        self._max_files = None
        self._mime_types = None
        self._allowed_mime_types = None
        self._other_mime_types = None
        self.discriminator = None

        if information_text is not None:
            self.information_text = information_text
        if size is not None:
            self.size = size
        if pattern is not None:
            self.pattern = pattern
        if required is not None:
            self.required = required
        if all_selected_label is not None:
            self.all_selected_label = all_selected_label
        if default_value is not None:
            self.default_value = default_value
        if possible_value_categories is not None:
            self.possible_value_categories = possible_value_categories
        if has_values_list is not None:
            self.has_values_list = has_values_list
        if possible_values is not None:
            self.possible_values = possible_values
        if dynamic_values is not None:
            self.dynamic_values = dynamic_values
        if string_values is not None:
            self.string_values = string_values
        if date_values is not None:
            self.date_values = date_values
        if integer_values is not None:
            self.integer_values = integer_values
        if decimal_values is not None:
            self.decimal_values = decimal_values
        if ad_values is not None:
            self.ad_values = ad_values
        if transaction_values is not None:
            self.transaction_values = transaction_values
        if transfer_values is not None:
            self.transfer_values = transfer_values
        if record_values is not None:
            self.record_values = record_values
        if user_values is not None:
            self.user_values = user_values
        if max_files is not None:
            self.max_files = max_files
        if mime_types is not None:
            self.mime_types = mime_types
        if allowed_mime_types is not None:
            self.allowed_mime_types = allowed_mime_types
        if other_mime_types is not None:
            self.other_mime_types = other_mime_types

    @property
    def information_text(self):
        """Gets the information_text of this CustomFieldDetailed.  # noqa: E501

        Additional text that can be shown to the user as a hint of this field   # noqa: E501

        :return: The information_text of this CustomFieldDetailed.  # noqa: E501
        :rtype: str
        """
        return self._information_text

    @information_text.setter
    def information_text(self, information_text):
        """Sets the information_text of this CustomFieldDetailed.

        Additional text that can be shown to the user as a hint of this field   # noqa: E501

        :param information_text: The information_text of this CustomFieldDetailed.  # noqa: E501
        :type: str
        """

        self._information_text = information_text

    @property
    def size(self):
        """Gets the size of this CustomFieldDetailed.  # noqa: E501

        The size of the widget that should be rendered Possible values are: * full: The widget should occupy 100% of the available area * large: A large widget * medium: A medium widget * small: A small widget * tiny: A very small widget   # noqa: E501

        :return: The size of this CustomFieldDetailed.  # noqa: E501
        :rtype: CustomFieldSizeEnum
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CustomFieldDetailed.

        The size of the widget that should be rendered Possible values are: * full: The widget should occupy 100% of the available area * large: A large widget * medium: A medium widget * small: A small widget * tiny: A very small widget   # noqa: E501

        :param size: The size of this CustomFieldDetailed.  # noqa: E501
        :type: CustomFieldSizeEnum
        """

        self._size = size

    @property
    def pattern(self):
        """Gets the pattern of this CustomFieldDetailed.  # noqa: E501

        The (optional) mask to be applied to string values  # noqa: E501

        :return: The pattern of this CustomFieldDetailed.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this CustomFieldDetailed.

        The (optional) mask to be applied to string values  # noqa: E501

        :param pattern: The pattern of this CustomFieldDetailed.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def required(self):
        """Gets the required of this CustomFieldDetailed.  # noqa: E501

        Indicates whether this field is required  # noqa: E501

        :return: The required of this CustomFieldDetailed.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this CustomFieldDetailed.

        Indicates whether this field is required  # noqa: E501

        :param required: The required of this CustomFieldDetailed.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def all_selected_label(self):
        """Gets the all_selected_label of this CustomFieldDetailed.  # noqa: E501

        The label to be shown when all values are selected for a  multi selection field.   # noqa: E501

        :return: The all_selected_label of this CustomFieldDetailed.  # noqa: E501
        :rtype: str
        """
        return self._all_selected_label

    @all_selected_label.setter
    def all_selected_label(self, all_selected_label):
        """Sets the all_selected_label of this CustomFieldDetailed.

        The label to be shown when all values are selected for a  multi selection field.   # noqa: E501

        :param all_selected_label: The all_selected_label of this CustomFieldDetailed.  # noqa: E501
        :type: str
        """

        self._all_selected_label = all_selected_label

    @property
    def default_value(self):
        """Gets the default_value of this CustomFieldDetailed.  # noqa: E501

        The value that should be suggested as default. For multi selection will be a comma-separated string with possible values ids or internal names.   # noqa: E501

        :return: The default_value of this CustomFieldDetailed.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this CustomFieldDetailed.

        The value that should be suggested as default. For multi selection will be a comma-separated string with possible values ids or internal names.   # noqa: E501

        :param default_value: The default_value of this CustomFieldDetailed.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def possible_value_categories(self):
        """Gets the possible_value_categories of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field is enumerated (single or multi select). Contains the possible value categories.   # noqa: E501

        :return: The possible_value_categories of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[EntityReference]
        """
        return self._possible_value_categories

    @possible_value_categories.setter
    def possible_value_categories(self, possible_value_categories):
        """Sets the possible_value_categories of this CustomFieldDetailed.

        Only applicable when the custom field is enumerated (single or multi select). Contains the possible value categories.   # noqa: E501

        :param possible_value_categories: The possible_value_categories of this CustomFieldDetailed.  # noqa: E501
        :type: list[EntityReference]
        """

        self._possible_value_categories = possible_value_categories

    @property
    def has_values_list(self):
        """Gets the has_values_list of this CustomFieldDetailed.  # noqa: E501

        Returns whether this custom field has a list of possible values, according to its type.   # noqa: E501

        :return: The has_values_list of this CustomFieldDetailed.  # noqa: E501
        :rtype: bool
        """
        return self._has_values_list

    @has_values_list.setter
    def has_values_list(self, has_values_list):
        """Sets the has_values_list of this CustomFieldDetailed.

        Returns whether this custom field has a list of possible values, according to its type.   # noqa: E501

        :param has_values_list: The has_values_list of this CustomFieldDetailed.  # noqa: E501
        :type: bool
        """

        self._has_values_list = has_values_list

    @property
    def possible_values(self):
        """Gets the possible_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field is enumerated (single or multi selection). Contains the possible values for selection. Each value may or may not have a category. When they have, it will be a string pointing to the internal name (if available) or id of the possible value category, which can be looked up in the categories property.   # noqa: E501

        :return: The possible_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[CustomFieldPossibleValue]
        """
        return self._possible_values

    @possible_values.setter
    def possible_values(self, possible_values):
        """Sets the possible_values of this CustomFieldDetailed.

        Only applicable when the custom field is enumerated (single or multi selection). Contains the possible values for selection. Each value may or may not have a category. When they have, it will be a string pointing to the internal name (if available) or id of the possible value category, which can be looked up in the categories property.   # noqa: E501

        :param possible_values: The possible_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[CustomFieldPossibleValue]
        """

        self._possible_values = possible_values

    @property
    def dynamic_values(self):
        """Gets the dynamic_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field is dynamic selection. Contains the script-generated possible values.   # noqa: E501

        :return: The dynamic_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[CustomFieldDynamicValue]
        """
        return self._dynamic_values

    @dynamic_values.setter
    def dynamic_values(self, dynamic_values):
        """Sets the dynamic_values of this CustomFieldDetailed.

        Only applicable when the custom field is dynamic selection. Contains the script-generated possible values.   # noqa: E501

        :param dynamic_values: The dynamic_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[CustomFieldDynamicValue]
        """

        self._dynamic_values = dynamic_values

    @property
    def string_values(self):
        """Gets the string_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field type is `string` and `hasValuesList` is `true`. Contains the possible string values.   # noqa: E501

        :return: The string_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[str]
        """
        return self._string_values

    @string_values.setter
    def string_values(self, string_values):
        """Sets the string_values of this CustomFieldDetailed.

        Only applicable when the custom field type is `string` and `hasValuesList` is `true`. Contains the possible string values.   # noqa: E501

        :param string_values: The string_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[str]
        """

        self._string_values = string_values

    @property
    def date_values(self):
        """Gets the date_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field type is `date` and `hasValuesList` is `true`. Contains the possible date values.   # noqa: E501

        :return: The date_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._date_values

    @date_values.setter
    def date_values(self, date_values):
        """Sets the date_values of this CustomFieldDetailed.

        Only applicable when the custom field type is `date` and `hasValuesList` is `true`. Contains the possible date values.   # noqa: E501

        :param date_values: The date_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[datetime]
        """

        self._date_values = date_values

    @property
    def integer_values(self):
        """Gets the integer_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field type is `integer` and `hasValuesList` is `true`. Contains the possible integer values.   # noqa: E501

        :return: The integer_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[int]
        """
        return self._integer_values

    @integer_values.setter
    def integer_values(self, integer_values):
        """Sets the integer_values of this CustomFieldDetailed.

        Only applicable when the custom field type is `integer` and `hasValuesList` is `true`. Contains the possible integer values.   # noqa: E501

        :param integer_values: The integer_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[int]
        """

        self._integer_values = integer_values

    @property
    def decimal_values(self):
        """Gets the decimal_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field type is `decimal` and `hasValuesList` is `true`. Contains the possible decimal values.   # noqa: E501

        :return: The decimal_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[BigDecimal]
        """
        return self._decimal_values

    @decimal_values.setter
    def decimal_values(self, decimal_values):
        """Sets the decimal_values of this CustomFieldDetailed.

        Only applicable when the custom field type is `decimal` and `hasValuesList` is `true`. Contains the possible decimal values.   # noqa: E501

        :param decimal_values: The decimal_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[BigDecimal]
        """

        self._decimal_values = decimal_values

    @property
    def ad_values(self):
        """Gets the ad_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field is linked entity of type `advertisement` and `hasValuesList` is `true`. Contains the possible advertisements.   # noqa: E501

        :return: The ad_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[Ad]
        """
        return self._ad_values

    @ad_values.setter
    def ad_values(self, ad_values):
        """Sets the ad_values of this CustomFieldDetailed.

        Only applicable when the custom field is linked entity of type `advertisement` and `hasValuesList` is `true`. Contains the possible advertisements.   # noqa: E501

        :param ad_values: The ad_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[Ad]
        """

        self._ad_values = ad_values

    @property
    def transaction_values(self):
        """Gets the transaction_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field is linked entity of type `transaction` and `hasValuesList` is `true`. Contains the possible transactions.   # noqa: E501

        :return: The transaction_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[Transaction]
        """
        return self._transaction_values

    @transaction_values.setter
    def transaction_values(self, transaction_values):
        """Sets the transaction_values of this CustomFieldDetailed.

        Only applicable when the custom field is linked entity of type `transaction` and `hasValuesList` is `true`. Contains the possible transactions.   # noqa: E501

        :param transaction_values: The transaction_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[Transaction]
        """

        self._transaction_values = transaction_values

    @property
    def transfer_values(self):
        """Gets the transfer_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field is linked entity of type `transfer` and `hasValuesList` is `true`. Contains the possible transfers.   # noqa: E501

        :return: The transfer_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[Transfer]
        """
        return self._transfer_values

    @transfer_values.setter
    def transfer_values(self, transfer_values):
        """Sets the transfer_values of this CustomFieldDetailed.

        Only applicable when the custom field is linked entity of type `transfer` and `hasValuesList` is `true`. Contains the possible transfers.   # noqa: E501

        :param transfer_values: The transfer_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[Transfer]
        """

        self._transfer_values = transfer_values

    @property
    def record_values(self):
        """Gets the record_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field is linked entity of type `record` and `hasValuesList` is `true`. Contains the possible records.   # noqa: E501

        :return: The record_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[Record]
        """
        return self._record_values

    @record_values.setter
    def record_values(self, record_values):
        """Sets the record_values of this CustomFieldDetailed.

        Only applicable when the custom field is linked entity of type `record` and `hasValuesList` is `true`. Contains the possible records.   # noqa: E501

        :param record_values: The record_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[Record]
        """

        self._record_values = record_values

    @property
    def user_values(self):
        """Gets the user_values of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field is linked entity of type `user` and `hasValuesList` is `true`. Contains the possible users.   # noqa: E501

        :return: The user_values of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[User]
        """
        return self._user_values

    @user_values.setter
    def user_values(self, user_values):
        """Sets the user_values of this CustomFieldDetailed.

        Only applicable when the custom field is linked entity of type `user` and `hasValuesList` is `true`. Contains the possible users.   # noqa: E501

        :param user_values: The user_values of this CustomFieldDetailed.  # noqa: E501
        :type: list[User]
        """

        self._user_values = user_values

    @property
    def max_files(self):
        """Gets the max_files of this CustomFieldDetailed.  # noqa: E501

        Only applicable when the custom field type is  `file` or `image`. The maximun files that can be uploaded   # noqa: E501

        :return: The max_files of this CustomFieldDetailed.  # noqa: E501
        :rtype: int
        """
        return self._max_files

    @max_files.setter
    def max_files(self, max_files):
        """Sets the max_files of this CustomFieldDetailed.

        Only applicable when the custom field type is  `file` or `image`. The maximun files that can be uploaded   # noqa: E501

        :param max_files: The max_files of this CustomFieldDetailed.  # noqa: E501
        :type: int
        """

        self._max_files = max_files

    @property
    def mime_types(self):
        """Gets the mime_types of this CustomFieldDetailed.  # noqa: E501

        The allowed mime types for binary custom fields. Only applicable when the custom field type is either  `file` or `image`    # noqa: E501

        :return: The mime_types of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[str]
        """
        return self._mime_types

    @mime_types.setter
    def mime_types(self, mime_types):
        """Sets the mime_types of this CustomFieldDetailed.

        The allowed mime types for binary custom fields. Only applicable when the custom field type is either  `file` or `image`    # noqa: E501

        :param mime_types: The mime_types of this CustomFieldDetailed.  # noqa: E501
        :type: list[str]
        """

        self._mime_types = mime_types

    @property
    def allowed_mime_types(self):
        """Gets the allowed_mime_types of this CustomFieldDetailed.  # noqa: E501

        (deprecated) Only applicable when the custom field type is  `file`. Contains the possible built-in mime types allowed for the file being  uploaded   # noqa: E501

        :return: The allowed_mime_types of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[FileMimeTypeEnum]
        """
        return self._allowed_mime_types

    @allowed_mime_types.setter
    def allowed_mime_types(self, allowed_mime_types):
        """Sets the allowed_mime_types of this CustomFieldDetailed.

        (deprecated) Only applicable when the custom field type is  `file`. Contains the possible built-in mime types allowed for the file being  uploaded   # noqa: E501

        :param allowed_mime_types: The allowed_mime_types of this CustomFieldDetailed.  # noqa: E501
        :type: list[FileMimeTypeEnum]
        """

        self._allowed_mime_types = allowed_mime_types

    @property
    def other_mime_types(self):
        """Gets the other_mime_types of this CustomFieldDetailed.  # noqa: E501

        (deprecated) Only applicable when the custom field type is  `file`and the `others` option was selected in `allowedMimeTypes`. Contains the other mime types allowed for the file being uploaded    # noqa: E501

        :return: The other_mime_types of this CustomFieldDetailed.  # noqa: E501
        :rtype: list[str]
        """
        return self._other_mime_types

    @other_mime_types.setter
    def other_mime_types(self, other_mime_types):
        """Sets the other_mime_types of this CustomFieldDetailed.

        (deprecated) Only applicable when the custom field type is  `file`and the `others` option was selected in `allowedMimeTypes`. Contains the other mime types allowed for the file being uploaded    # noqa: E501

        :param other_mime_types: The other_mime_types of this CustomFieldDetailed.  # noqa: E501
        :type: list[str]
        """

        self._other_mime_types = other_mime_types

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
        if issubclass(CustomFieldDetailed, dict):
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
        if not isinstance(other, CustomFieldDetailed):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomFieldDetailed):
            return True

        return self.to_dict() != other.to_dict()
