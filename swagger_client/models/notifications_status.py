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


class NotificationsStatus(object):
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
        'new_notifications': 'int',
        'unread_notifications': 'int',
        'last_view_date': 'datetime'
    }

    attribute_map = {
        'new_notifications': 'newNotifications',
        'unread_notifications': 'unreadNotifications',
        'last_view_date': 'lastViewDate'
    }

    def __init__(self, new_notifications=None, unread_notifications=None, last_view_date=None, _configuration=None):  # noqa: E501
        """NotificationsStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._new_notifications = None
        self._unread_notifications = None
        self._last_view_date = None
        self.discriminator = None

        if new_notifications is not None:
            self.new_notifications = new_notifications
        if unread_notifications is not None:
            self.unread_notifications = unread_notifications
        if last_view_date is not None:
            self.last_view_date = last_view_date

    @property
    def new_notifications(self):
        """Gets the new_notifications of this NotificationsStatus.  # noqa: E501

        Indicates the number of received notifications after the last view date (i.e `lastViewDate`).  # noqa: E501

        :return: The new_notifications of this NotificationsStatus.  # noqa: E501
        :rtype: int
        """
        return self._new_notifications

    @new_notifications.setter
    def new_notifications(self, new_notifications):
        """Sets the new_notifications of this NotificationsStatus.

        Indicates the number of received notifications after the last view date (i.e `lastViewDate`).  # noqa: E501

        :param new_notifications: The new_notifications of this NotificationsStatus.  # noqa: E501
        :type: int
        """

        self._new_notifications = new_notifications

    @property
    def unread_notifications(self):
        """Gets the unread_notifications of this NotificationsStatus.  # noqa: E501

        Indicates the total number of unread notifications.  # noqa: E501

        :return: The unread_notifications of this NotificationsStatus.  # noqa: E501
        :rtype: int
        """
        return self._unread_notifications

    @unread_notifications.setter
    def unread_notifications(self, unread_notifications):
        """Sets the unread_notifications of this NotificationsStatus.

        Indicates the total number of unread notifications.  # noqa: E501

        :param unread_notifications: The unread_notifications of this NotificationsStatus.  # noqa: E501
        :type: int
        """

        self._unread_notifications = unread_notifications

    @property
    def last_view_date(self):
        """Gets the last_view_date of this NotificationsStatus.  # noqa: E501

        The last view date tracked by the server through `POST /notifications/viewed`  # noqa: E501

        :return: The last_view_date of this NotificationsStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_view_date

    @last_view_date.setter
    def last_view_date(self, last_view_date):
        """Sets the last_view_date of this NotificationsStatus.

        The last view date tracked by the server through `POST /notifications/viewed`  # noqa: E501

        :param last_view_date: The last_view_date of this NotificationsStatus.  # noqa: E501
        :type: datetime
        """

        self._last_view_date = last_view_date

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
        if issubclass(NotificationsStatus, dict):
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
        if not isinstance(other, NotificationsStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationsStatus):
            return True

        return self.to_dict() != other.to_dict()
