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


class IncomingMessage(object):
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
        '_date': 'datetime',
        'category': 'EntityReference',
        'from_user': 'User',
        'subject': 'str',
        'body': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'category': 'category',
        'from_user': 'fromUser',
        'subject': 'subject',
        'body': 'body'
    }

    def __init__(self, _date=None, category=None, from_user=None, subject=None, body=None, _configuration=None):  # noqa: E501
        """IncomingMessage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__date = None
        self._category = None
        self._from_user = None
        self._subject = None
        self._body = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if category is not None:
            self.category = category
        if from_user is not None:
            self.from_user = from_user
        if subject is not None:
            self.subject = subject
        if body is not None:
            self.body = body

    @property
    def _date(self):
        """Gets the _date of this IncomingMessage.  # noqa: E501

        The message date  # noqa: E501

        :return: The _date of this IncomingMessage.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this IncomingMessage.

        The message date  # noqa: E501

        :param _date: The _date of this IncomingMessage.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def category(self):
        """Gets the category of this IncomingMessage.  # noqa: E501

        The message category, for messages from system  # noqa: E501

        :return: The category of this IncomingMessage.  # noqa: E501
        :rtype: EntityReference
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this IncomingMessage.

        The message category, for messages from system  # noqa: E501

        :param category: The category of this IncomingMessage.  # noqa: E501
        :type: EntityReference
        """

        self._category = category

    @property
    def from_user(self):
        """Gets the from_user of this IncomingMessage.  # noqa: E501

        The user that sent this message  # noqa: E501

        :return: The from_user of this IncomingMessage.  # noqa: E501
        :rtype: User
        """
        return self._from_user

    @from_user.setter
    def from_user(self, from_user):
        """Sets the from_user of this IncomingMessage.

        The user that sent this message  # noqa: E501

        :param from_user: The from_user of this IncomingMessage.  # noqa: E501
        :type: User
        """

        self._from_user = from_user

    @property
    def subject(self):
        """Gets the subject of this IncomingMessage.  # noqa: E501

        The message subject  # noqa: E501

        :return: The subject of this IncomingMessage.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this IncomingMessage.

        The message subject  # noqa: E501

        :param subject: The subject of this IncomingMessage.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def body(self):
        """Gets the body of this IncomingMessage.  # noqa: E501

        The message body  # noqa: E501

        :return: The body of this IncomingMessage.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this IncomingMessage.

        The message body  # noqa: E501

        :param body: The body of this IncomingMessage.  # noqa: E501
        :type: str
        """

        self._body = body

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
        if issubclass(IncomingMessage, dict):
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
        if not isinstance(other, IncomingMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IncomingMessage):
            return True

        return self.to_dict() != other.to_dict()
