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


class BrokerView(object):
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
        'main_broker': 'bool',
        'since': 'datetime',
        'broker': 'User'
    }

    attribute_map = {
        'main_broker': 'mainBroker',
        'since': 'since',
        'broker': 'broker'
    }

    def __init__(self, main_broker=None, since=None, broker=None, _configuration=None):  # noqa: E501
        """BrokerView - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._main_broker = None
        self._since = None
        self._broker = None
        self.discriminator = None

        if main_broker is not None:
            self.main_broker = main_broker
        if since is not None:
            self.since = since
        if broker is not None:
            self.broker = broker

    @property
    def main_broker(self):
        """Gets the main_broker of this BrokerView.  # noqa: E501

        Indicates whether this broker is the main or not.  # noqa: E501

        :return: The main_broker of this BrokerView.  # noqa: E501
        :rtype: bool
        """
        return self._main_broker

    @main_broker.setter
    def main_broker(self, main_broker):
        """Sets the main_broker of this BrokerView.

        Indicates whether this broker is the main or not.  # noqa: E501

        :param main_broker: The main_broker of this BrokerView.  # noqa: E501
        :type: bool
        """

        self._main_broker = main_broker

    @property
    def since(self):
        """Gets the since of this BrokerView.  # noqa: E501

        Indicates when the brokerage relationship began.  # noqa: E501

        :return: The since of this BrokerView.  # noqa: E501
        :rtype: datetime
        """
        return self._since

    @since.setter
    def since(self, since):
        """Sets the since of this BrokerView.

        Indicates when the brokerage relationship began.  # noqa: E501

        :param since: The since of this BrokerView.  # noqa: E501
        :type: datetime
        """

        self._since = since

    @property
    def broker(self):
        """Gets the broker of this BrokerView.  # noqa: E501

        The broker user.  # noqa: E501

        :return: The broker of this BrokerView.  # noqa: E501
        :rtype: User
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        """Sets the broker of this BrokerView.

        The broker user.  # noqa: E501

        :param broker: The broker of this BrokerView.  # noqa: E501
        :type: User
        """

        self._broker = broker

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
        if issubclass(BrokerView, dict):
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
        if not isinstance(other, BrokerView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BrokerView):
            return True

        return self.to_dict() != other.to_dict()