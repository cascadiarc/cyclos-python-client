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


class OperationPermissions(object):
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
        'operation': 'Operation',
        'run': 'bool'
    }

    attribute_map = {
        'operation': 'operation',
        'run': 'run'
    }

    def __init__(self, operation=None, run=None, _configuration=None):  # noqa: E501
        """OperationPermissions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operation = None
        self._run = None
        self.discriminator = None

        if operation is not None:
            self.operation = operation
        if run is not None:
            self.run = run

    @property
    def operation(self):
        """Gets the operation of this OperationPermissions.  # noqa: E501

        The custom operation  # noqa: E501

        :return: The operation of this OperationPermissions.  # noqa: E501
        :rtype: Operation
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this OperationPermissions.

        The custom operation  # noqa: E501

        :param operation: The operation of this OperationPermissions.  # noqa: E501
        :type: Operation
        """

        self._operation = operation

    @property
    def run(self):
        """Gets the run of this OperationPermissions.  # noqa: E501

        Can run this operation?  # noqa: E501

        :return: The run of this OperationPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this OperationPermissions.

        Can run this operation?  # noqa: E501

        :param run: The run of this OperationPermissions.  # noqa: E501
        :type: bool
        """

        self._run = run

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
        if issubclass(OperationPermissions, dict):
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
        if not isinstance(other, OperationPermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OperationPermissions):
            return True

        return self.to_dict() != other.to_dict()
