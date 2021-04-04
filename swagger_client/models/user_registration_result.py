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


class UserRegistrationResult(object):
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
        'user': 'User',
        'status': 'UserRegistrationStatusEnum',
        'generated_passwords': 'list[EntityReference]',
        'root_url': 'str',
        'principals': 'list[UserRegistrationPrincipal]'
    }

    attribute_map = {
        'user': 'user',
        'status': 'status',
        'generated_passwords': 'generatedPasswords',
        'root_url': 'rootUrl',
        'principals': 'principals'
    }

    def __init__(self, user=None, status=None, generated_passwords=None, root_url=None, principals=None, _configuration=None):  # noqa: E501
        """UserRegistrationResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user = None
        self._status = None
        self._generated_passwords = None
        self._root_url = None
        self._principals = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if status is not None:
            self.status = status
        if generated_passwords is not None:
            self.generated_passwords = generated_passwords
        if root_url is not None:
            self.root_url = root_url
        if principals is not None:
            self.principals = principals

    @property
    def user(self):
        """Gets the user of this UserRegistrationResult.  # noqa: E501

        The user that has just been registered  # noqa: E501

        :return: The user of this UserRegistrationResult.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserRegistrationResult.

        The user that has just been registered  # noqa: E501

        :param user: The user of this UserRegistrationResult.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def status(self):
        """Gets the status of this UserRegistrationResult.  # noqa: E501

        The status of the user after the registration Possible values are: * active: The user is initially active * emailValidation: The user has received an e-mail, with a link to verify the e-mail address. Once verified, the registration will be complete * inactive: The user is initially inactive, and an administrator needs to manually activate the user   # noqa: E501

        :return: The status of this UserRegistrationResult.  # noqa: E501
        :rtype: UserRegistrationStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserRegistrationResult.

        The status of the user after the registration Possible values are: * active: The user is initially active * emailValidation: The user has received an e-mail, with a link to verify the e-mail address. Once verified, the registration will be complete * inactive: The user is initially inactive, and an administrator needs to manually activate the user   # noqa: E501

        :param status: The status of this UserRegistrationResult.  # noqa: E501
        :type: UserRegistrationStatusEnum
        """

        self._status = status

    @property
    def generated_passwords(self):
        """Gets the generated_passwords of this UserRegistrationResult.  # noqa: E501

        The types of passwords that were generated  # noqa: E501

        :return: The generated_passwords of this UserRegistrationResult.  # noqa: E501
        :rtype: list[EntityReference]
        """
        return self._generated_passwords

    @generated_passwords.setter
    def generated_passwords(self, generated_passwords):
        """Sets the generated_passwords of this UserRegistrationResult.

        The types of passwords that were generated  # noqa: E501

        :param generated_passwords: The generated_passwords of this UserRegistrationResult.  # noqa: E501
        :type: list[EntityReference]
        """

        self._generated_passwords = generated_passwords

    @property
    def root_url(self):
        """Gets the root_url of this UserRegistrationResult.  # noqa: E501

        The root URL that can be used to access the web interface  # noqa: E501

        :return: The root_url of this UserRegistrationResult.  # noqa: E501
        :rtype: str
        """
        return self._root_url

    @root_url.setter
    def root_url(self, root_url):
        """Sets the root_url of this UserRegistrationResult.

        The root URL that can be used to access the web interface  # noqa: E501

        :param root_url: The root_url of this UserRegistrationResult.  # noqa: E501
        :type: str
        """

        self._root_url = root_url

    @property
    def principals(self):
        """Gets the principals of this UserRegistrationResult.  # noqa: E501

        Contains information about each user principal (identification) and the channels that can be accessed using it   # noqa: E501

        :return: The principals of this UserRegistrationResult.  # noqa: E501
        :rtype: list[UserRegistrationPrincipal]
        """
        return self._principals

    @principals.setter
    def principals(self, principals):
        """Sets the principals of this UserRegistrationResult.

        Contains information about each user principal (identification) and the channels that can be accessed using it   # noqa: E501

        :param principals: The principals of this UserRegistrationResult.  # noqa: E501
        :type: list[UserRegistrationPrincipal]
        """

        self._principals = principals

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
        if issubclass(UserRegistrationResult, dict):
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
        if not isinstance(other, UserRegistrationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserRegistrationResult):
            return True

        return self.to_dict() != other.to_dict()
