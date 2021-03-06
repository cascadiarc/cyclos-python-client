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


class ChangePassword(object):
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
        'old_password': 'str',
        'new_password': 'str',
        'check_confirmation': 'bool',
        'new_password_confirmation': 'str',
        'force_change': 'bool'
    }

    attribute_map = {
        'old_password': 'oldPassword',
        'new_password': 'newPassword',
        'check_confirmation': 'checkConfirmation',
        'new_password_confirmation': 'newPasswordConfirmation',
        'force_change': 'forceChange'
    }

    def __init__(self, old_password=None, new_password=None, check_confirmation=None, new_password_confirmation=None, force_change=None, _configuration=None):  # noqa: E501
        """ChangePassword - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._old_password = None
        self._new_password = None
        self._check_confirmation = None
        self._new_password_confirmation = None
        self._force_change = None
        self.discriminator = None

        if old_password is not None:
            self.old_password = old_password
        if new_password is not None:
            self.new_password = new_password
        if check_confirmation is not None:
            self.check_confirmation = check_confirmation
        if new_password_confirmation is not None:
            self.new_password_confirmation = new_password_confirmation
        if force_change is not None:
            self.force_change = force_change

    @property
    def old_password(self):
        """Gets the old_password of this ChangePassword.  # noqa: E501

        The current password value. Required when the user is changing his own password. Not used when admins / brokers are changing the password of a user they manage.   # noqa: E501

        :return: The old_password of this ChangePassword.  # noqa: E501
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this ChangePassword.

        The current password value. Required when the user is changing his own password. Not used when admins / brokers are changing the password of a user they manage.   # noqa: E501

        :param old_password: The old_password of this ChangePassword.  # noqa: E501
        :type: str
        """

        self._old_password = old_password

    @property
    def new_password(self):
        """Gets the new_password of this ChangePassword.  # noqa: E501

        The new password value. Required.  # noqa: E501

        :return: The new_password of this ChangePassword.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ChangePassword.

        The new password value. Required.  # noqa: E501

        :param new_password: The new_password of this ChangePassword.  # noqa: E501
        :type: str
        """

        self._new_password = new_password

    @property
    def check_confirmation(self):
        """Gets the check_confirmation of this ChangePassword.  # noqa: E501

        Depending on the client, if a confirm password field is shown to users, it might be useful to check the confirmation password value on the server. This way, if there are other validation exceptions, they are all shown together. In this case, this field should be set to `true` and the `confirmationValue` should be passed in with the user input. However, in cases where clients just want to register a user with a password non interactively (like in a bulk registration), passing the password value twice is not desirable. In such cases, this field can be left empty (or set to `false`), and the `newPasswordConfirmation` will be ignored.   # noqa: E501

        :return: The check_confirmation of this ChangePassword.  # noqa: E501
        :rtype: bool
        """
        return self._check_confirmation

    @check_confirmation.setter
    def check_confirmation(self, check_confirmation):
        """Sets the check_confirmation of this ChangePassword.

        Depending on the client, if a confirm password field is shown to users, it might be useful to check the confirmation password value on the server. This way, if there are other validation exceptions, they are all shown together. In this case, this field should be set to `true` and the `confirmationValue` should be passed in with the user input. However, in cases where clients just want to register a user with a password non interactively (like in a bulk registration), passing the password value twice is not desirable. In such cases, this field can be left empty (or set to `false`), and the `newPasswordConfirmation` will be ignored.   # noqa: E501

        :param check_confirmation: The check_confirmation of this ChangePassword.  # noqa: E501
        :type: bool
        """

        self._check_confirmation = check_confirmation

    @property
    def new_password_confirmation(self):
        """Gets the new_password_confirmation of this ChangePassword.  # noqa: E501

        The new password confirmation value. Is ignored unless `checkConfirmation` is set to `true`.   # noqa: E501

        :return: The new_password_confirmation of this ChangePassword.  # noqa: E501
        :rtype: str
        """
        return self._new_password_confirmation

    @new_password_confirmation.setter
    def new_password_confirmation(self, new_password_confirmation):
        """Sets the new_password_confirmation of this ChangePassword.

        The new password confirmation value. Is ignored unless `checkConfirmation` is set to `true`.   # noqa: E501

        :param new_password_confirmation: The new_password_confirmation of this ChangePassword.  # noqa: E501
        :type: str
        """

        self._new_password_confirmation = new_password_confirmation

    @property
    def force_change(self):
        """Gets the force_change of this ChangePassword.  # noqa: E501

        Indicates whether the new password needs to be changed on the next login. Only used when admins / brokers are changing the password of a user they manage.   # noqa: E501

        :return: The force_change of this ChangePassword.  # noqa: E501
        :rtype: bool
        """
        return self._force_change

    @force_change.setter
    def force_change(self, force_change):
        """Sets the force_change of this ChangePassword.

        Indicates whether the new password needs to be changed on the next login. Only used when admins / brokers are changing the password of a user they manage.   # noqa: E501

        :param force_change: The force_change of this ChangePassword.  # noqa: E501
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
        if issubclass(ChangePassword, dict):
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
        if not isinstance(other, ChangePassword):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangePassword):
            return True

        return self.to_dict() != other.to_dict()
