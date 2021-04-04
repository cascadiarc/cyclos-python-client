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


class BaseTransferDataForSearch(object):
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
        'transfer_status_flows': 'list[TransferStatusFlow]'
    }

    attribute_map = {
        'transfer_status_flows': 'transferStatusFlows'
    }

    def __init__(self, transfer_status_flows=None, _configuration=None):  # noqa: E501
        """BaseTransferDataForSearch - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transfer_status_flows = None
        self.discriminator = None

        if transfer_status_flows is not None:
            self.transfer_status_flows = transfer_status_flows

    @property
    def transfer_status_flows(self):
        """Gets the transfer_status_flows of this BaseTransferDataForSearch.  # noqa: E501

        References to the allowed transfer status flows for this account    # noqa: E501

        :return: The transfer_status_flows of this BaseTransferDataForSearch.  # noqa: E501
        :rtype: list[TransferStatusFlow]
        """
        return self._transfer_status_flows

    @transfer_status_flows.setter
    def transfer_status_flows(self, transfer_status_flows):
        """Sets the transfer_status_flows of this BaseTransferDataForSearch.

        References to the allowed transfer status flows for this account    # noqa: E501

        :param transfer_status_flows: The transfer_status_flows of this BaseTransferDataForSearch.  # noqa: E501
        :type: list[TransferStatusFlow]
        """

        self._transfer_status_flows = transfer_status_flows

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
        if issubclass(BaseTransferDataForSearch, dict):
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
        if not isinstance(other, BaseTransferDataForSearch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseTransferDataForSearch):
            return True

        return self.to_dict() != other.to_dict()