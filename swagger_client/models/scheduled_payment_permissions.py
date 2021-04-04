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


class ScheduledPaymentPermissions(object):
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
        'block': 'bool',
        'unblock': 'bool',
        'cancel': 'bool',
        'settle': 'bool'
    }

    attribute_map = {
        'block': 'block',
        'unblock': 'unblock',
        'cancel': 'cancel',
        'settle': 'settle'
    }

    def __init__(self, block=None, unblock=None, cancel=None, settle=None, _configuration=None):  # noqa: E501
        """ScheduledPaymentPermissions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._block = None
        self._unblock = None
        self._cancel = None
        self._settle = None
        self.discriminator = None

        if block is not None:
            self.block = block
        if unblock is not None:
            self.unblock = unblock
        if cancel is not None:
            self.cancel = cancel
        if settle is not None:
            self.settle = settle

    @property
    def block(self):
        """Gets the block of this ScheduledPaymentPermissions.  # noqa: E501

        Can block the whole scheduled payment?  # noqa: E501

        :return: The block of this ScheduledPaymentPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this ScheduledPaymentPermissions.

        Can block the whole scheduled payment?  # noqa: E501

        :param block: The block of this ScheduledPaymentPermissions.  # noqa: E501
        :type: bool
        """

        self._block = block

    @property
    def unblock(self):
        """Gets the unblock of this ScheduledPaymentPermissions.  # noqa: E501

        Can unblock the whole scheduled payment?  # noqa: E501

        :return: The unblock of this ScheduledPaymentPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._unblock

    @unblock.setter
    def unblock(self, unblock):
        """Sets the unblock of this ScheduledPaymentPermissions.

        Can unblock the whole scheduled payment?  # noqa: E501

        :param unblock: The unblock of this ScheduledPaymentPermissions.  # noqa: E501
        :type: bool
        """

        self._unblock = unblock

    @property
    def cancel(self):
        """Gets the cancel of this ScheduledPaymentPermissions.  # noqa: E501

        Can cancel the whole scheduled payment?  # noqa: E501

        :return: The cancel of this ScheduledPaymentPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        """Sets the cancel of this ScheduledPaymentPermissions.

        Can cancel the whole scheduled payment?  # noqa: E501

        :param cancel: The cancel of this ScheduledPaymentPermissions.  # noqa: E501
        :type: bool
        """

        self._cancel = cancel

    @property
    def settle(self):
        """Gets the settle of this ScheduledPaymentPermissions.  # noqa: E501

        Can settle open installments?  # noqa: E501

        :return: The settle of this ScheduledPaymentPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._settle

    @settle.setter
    def settle(self, settle):
        """Sets the settle of this ScheduledPaymentPermissions.

        Can settle open installments?  # noqa: E501

        :param settle: The settle of this ScheduledPaymentPermissions.  # noqa: E501
        :type: bool
        """

        self._settle = settle

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
        if issubclass(ScheduledPaymentPermissions, dict):
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
        if not isinstance(other, ScheduledPaymentPermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduledPaymentPermissions):
            return True

        return self.to_dict() != other.to_dict()
