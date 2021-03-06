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


class InternalTransactionPreview(object):
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
        'pending_authorization': 'bool',
        'to_account': 'AccountWithOwner'
    }

    attribute_map = {
        'pending_authorization': 'pendingAuthorization',
        'to_account': 'toAccount'
    }

    def __init__(self, pending_authorization=None, to_account=None, _configuration=None):  # noqa: E501
        """InternalTransactionPreview - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pending_authorization = None
        self._to_account = None
        self.discriminator = None

        if pending_authorization is not None:
            self.pending_authorization = pending_authorization
        if to_account is not None:
            self.to_account = to_account

    @property
    def pending_authorization(self):
        """Gets the pending_authorization of this InternalTransactionPreview.  # noqa: E501

        Indicates whether the transaction would be initially pending authorization in order to be processed   # noqa: E501

        :return: The pending_authorization of this InternalTransactionPreview.  # noqa: E501
        :rtype: bool
        """
        return self._pending_authorization

    @pending_authorization.setter
    def pending_authorization(self, pending_authorization):
        """Sets the pending_authorization of this InternalTransactionPreview.

        Indicates whether the transaction would be initially pending authorization in order to be processed   # noqa: E501

        :param pending_authorization: The pending_authorization of this InternalTransactionPreview.  # noqa: E501
        :type: bool
        """

        self._pending_authorization = pending_authorization

    @property
    def to_account(self):
        """Gets the to_account of this InternalTransactionPreview.  # noqa: E501

        A reference to the destination account  # noqa: E501

        :return: The to_account of this InternalTransactionPreview.  # noqa: E501
        :rtype: AccountWithOwner
        """
        return self._to_account

    @to_account.setter
    def to_account(self, to_account):
        """Sets the to_account of this InternalTransactionPreview.

        A reference to the destination account  # noqa: E501

        :param to_account: The to_account of this InternalTransactionPreview.  # noqa: E501
        :type: AccountWithOwner
        """

        self._to_account = to_account

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
        if issubclass(InternalTransactionPreview, dict):
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
        if not isinstance(other, InternalTransactionPreview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InternalTransactionPreview):
            return True

        return self.to_dict() != other.to_dict()
