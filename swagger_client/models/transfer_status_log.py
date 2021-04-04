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


class TransferStatusLog(object):
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
        'by': 'User',
        '_date': 'datetime',
        'status': 'EntityReference',
        'comments': 'str'
    }

    attribute_map = {
        'by': 'by',
        '_date': 'date',
        'status': 'status',
        'comments': 'comments'
    }

    def __init__(self, by=None, _date=None, status=None, comments=None, _configuration=None):  # noqa: E501
        """TransferStatusLog - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._by = None
        self.__date = None
        self._status = None
        self._comments = None
        self.discriminator = None

        if by is not None:
            self.by = by
        if _date is not None:
            self._date = _date
        if status is not None:
            self.status = status
        if comments is not None:
            self.comments = comments

    @property
    def by(self):
        """Gets the by of this TransferStatusLog.  # noqa: E501

        The user that performed the change  # noqa: E501

        :return: The by of this TransferStatusLog.  # noqa: E501
        :rtype: User
        """
        return self._by

    @by.setter
    def by(self, by):
        """Sets the by of this TransferStatusLog.

        The user that performed the change  # noqa: E501

        :param by: The by of this TransferStatusLog.  # noqa: E501
        :type: User
        """

        self._by = by

    @property
    def _date(self):
        """Gets the _date of this TransferStatusLog.  # noqa: E501

        The date / time the action was performed  # noqa: E501

        :return: The _date of this TransferStatusLog.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this TransferStatusLog.

        The date / time the action was performed  # noqa: E501

        :param _date: The _date of this TransferStatusLog.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def status(self):
        """Gets the status of this TransferStatusLog.  # noqa: E501

        The new status  # noqa: E501

        :return: The status of this TransferStatusLog.  # noqa: E501
        :rtype: EntityReference
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransferStatusLog.

        The new status  # noqa: E501

        :param status: The status of this TransferStatusLog.  # noqa: E501
        :type: EntityReference
        """

        self._status = status

    @property
    def comments(self):
        """Gets the comments of this TransferStatusLog.  # noqa: E501

        Comments provided by the user which performed the change   # noqa: E501

        :return: The comments of this TransferStatusLog.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this TransferStatusLog.

        Comments provided by the user which performed the change   # noqa: E501

        :param comments: The comments of this TransferStatusLog.  # noqa: E501
        :type: str
        """

        self._comments = comments

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
        if issubclass(TransferStatusLog, dict):
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
        if not isinstance(other, TransferStatusLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransferStatusLog):
            return True

        return self.to_dict() != other.to_dict()