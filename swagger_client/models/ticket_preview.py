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


class TicketPreview(object):
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
        'cancel_url': 'str',
        'success_url': 'str'
    }

    attribute_map = {
        'cancel_url': 'cancelUrl',
        'success_url': 'successUrl'
    }

    def __init__(self, cancel_url=None, success_url=None, _configuration=None):  # noqa: E501
        """TicketPreview - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cancel_url = None
        self._success_url = None
        self.discriminator = None

        if cancel_url is not None:
            self.cancel_url = cancel_url
        if success_url is not None:
            self.success_url = success_url

    @property
    def cancel_url(self):
        """Gets the cancel_url of this TicketPreview.  # noqa: E501

        The URL to redirect when canceling the accept ticket flow  # noqa: E501

        :return: The cancel_url of this TicketPreview.  # noqa: E501
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """Sets the cancel_url of this TicketPreview.

        The URL to redirect when canceling the accept ticket flow  # noqa: E501

        :param cancel_url: The cancel_url of this TicketPreview.  # noqa: E501
        :type: str
        """

        self._cancel_url = cancel_url

    @property
    def success_url(self):
        """Gets the success_url of this TicketPreview.  # noqa: E501

        The URL to redirect after successfully accepting a ticket  # noqa: E501

        :return: The success_url of this TicketPreview.  # noqa: E501
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """Sets the success_url of this TicketPreview.

        The URL to redirect after successfully accepting a ticket  # noqa: E501

        :param success_url: The success_url of this TicketPreview.  # noqa: E501
        :type: str
        """

        self._success_url = success_url

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
        if issubclass(TicketPreview, dict):
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
        if not isinstance(other, TicketPreview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TicketPreview):
            return True

        return self.to_dict() != other.to_dict()
