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


class PasswordRegistration(object):
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
        'type': 'str',
        'value': 'str',
        'check_confirmation': 'bool',
        'confirmation_value': 'str',
        'force_change': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'check_confirmation': 'checkConfirmation',
        'confirmation_value': 'confirmationValue',
        'force_change': 'forceChange'
    }

    def __init__(self, type=None, value=None, check_confirmation=None, confirmation_value=None, force_change=None, _configuration=None):  # noqa: E501
        """PasswordRegistration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._value = None
        self._check_confirmation = None
        self._confirmation_value = None
        self._force_change = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if check_confirmation is not None:
            self.check_confirmation = check_confirmation
        if confirmation_value is not None:
            self.confirmation_value = confirmation_value
        if force_change is not None:
            self.force_change = force_change

    @property
    def type(self):
        """Gets the type of this PasswordRegistration.  # noqa: E501

        The password type  # noqa: E501

        :return: The type of this PasswordRegistration.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PasswordRegistration.

        The password type  # noqa: E501

        :param type: The type of this PasswordRegistration.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this PasswordRegistration.  # noqa: E501

        The password value  # noqa: E501

        :return: The value of this PasswordRegistration.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PasswordRegistration.

        The password value  # noqa: E501

        :param value: The value of this PasswordRegistration.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def check_confirmation(self):
        """Gets the check_confirmation of this PasswordRegistration.  # noqa: E501

        Depending on the client, if a confirm password field is shown to users, it might be useful to check the confirmation password value on the server. This way, if there are other validation exceptions, they are all shown together. In this case, this field should be set to `true` and the `confirmationValue` should be passed in with the user input. However, in cases where clients just want to register a user with a password non interactively (like in a bulk registration), passing the password value twice is not desirable. In such cases, this field can be left empty (or set to `false`), and the `confirmationValue` will be ignored.   # noqa: E501

        :return: The check_confirmation of this PasswordRegistration.  # noqa: E501
        :rtype: bool
        """
        return self._check_confirmation

    @check_confirmation.setter
    def check_confirmation(self, check_confirmation):
        """Sets the check_confirmation of this PasswordRegistration.

        Depending on the client, if a confirm password field is shown to users, it might be useful to check the confirmation password value on the server. This way, if there are other validation exceptions, they are all shown together. In this case, this field should be set to `true` and the `confirmationValue` should be passed in with the user input. However, in cases where clients just want to register a user with a password non interactively (like in a bulk registration), passing the password value twice is not desirable. In such cases, this field can be left empty (or set to `false`), and the `confirmationValue` will be ignored.   # noqa: E501

        :param check_confirmation: The check_confirmation of this PasswordRegistration.  # noqa: E501
        :type: bool
        """

        self._check_confirmation = check_confirmation

    @property
    def confirmation_value(self):
        """Gets the confirmation_value of this PasswordRegistration.  # noqa: E501

        The password confirmation value. Is ignored unless `checkConfirmation` is set to `true`.   # noqa: E501

        :return: The confirmation_value of this PasswordRegistration.  # noqa: E501
        :rtype: str
        """
        return self._confirmation_value

    @confirmation_value.setter
    def confirmation_value(self, confirmation_value):
        """Sets the confirmation_value of this PasswordRegistration.

        The password confirmation value. Is ignored unless `checkConfirmation` is set to `true`.   # noqa: E501

        :param confirmation_value: The confirmation_value of this PasswordRegistration.  # noqa: E501
        :type: str
        """

        self._confirmation_value = confirmation_value

    @property
    def force_change(self):
        """Gets the force_change of this PasswordRegistration.  # noqa: E501

        When set to true will force the user to change it after the first login   # noqa: E501

        :return: The force_change of this PasswordRegistration.  # noqa: E501
        :rtype: bool
        """
        return self._force_change

    @force_change.setter
    def force_change(self, force_change):
        """Sets the force_change of this PasswordRegistration.

        When set to true will force the user to change it after the first login   # noqa: E501

        :param force_change: The force_change of this PasswordRegistration.  # noqa: E501
        :type: bool
        """

        self._force_change = force_change

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
        if issubclass(PasswordRegistration, dict):
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
        if not isinstance(other, PasswordRegistration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PasswordRegistration):
            return True

        return self.to_dict() != other.to_dict()
