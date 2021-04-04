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


class NfcExternalAuthenticateResult(object):
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
        'cyclos_challenge': 'str',
        'session_key': 'str'
    }

    attribute_map = {
        'cyclos_challenge': 'cyclosChallenge',
        'session_key': 'sessionKey'
    }

    def __init__(self, cyclos_challenge=None, session_key=None, _configuration=None):  # noqa: E501
        """NfcExternalAuthenticateResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cyclos_challenge = None
        self._session_key = None
        self.discriminator = None

        if cyclos_challenge is not None:
            self.cyclos_challenge = cyclos_challenge
        if session_key is not None:
            self.session_key = session_key

    @property
    def cyclos_challenge(self):
        """Gets the cyclos_challenge of this NfcExternalAuthenticateResult.  # noqa: E501

        The Cyclos-generated challenge encoded as hex. This challenge has to be encrypted by the NFC tag   # noqa: E501

        :return: The cyclos_challenge of this NfcExternalAuthenticateResult.  # noqa: E501
        :rtype: str
        """
        return self._cyclos_challenge

    @cyclos_challenge.setter
    def cyclos_challenge(self, cyclos_challenge):
        """Sets the cyclos_challenge of this NfcExternalAuthenticateResult.

        The Cyclos-generated challenge encoded as hex. This challenge has to be encrypted by the NFC tag   # noqa: E501

        :param cyclos_challenge: The cyclos_challenge of this NfcExternalAuthenticateResult.  # noqa: E501
        :type: str
        """

        self._cyclos_challenge = cyclos_challenge

    @property
    def session_key(self):
        """Gets the session_key of this NfcExternalAuthenticateResult.  # noqa: E501

        The session key to be used on subsequent NFC operations, encoded as hex   # noqa: E501

        :return: The session_key of this NfcExternalAuthenticateResult.  # noqa: E501
        :rtype: str
        """
        return self._session_key

    @session_key.setter
    def session_key(self, session_key):
        """Sets the session_key of this NfcExternalAuthenticateResult.

        The session key to be used on subsequent NFC operations, encoded as hex   # noqa: E501

        :param session_key: The session_key of this NfcExternalAuthenticateResult.  # noqa: E501
        :type: str
        """

        self._session_key = session_key

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
        if issubclass(NfcExternalAuthenticateResult, dict):
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
        if not isinstance(other, NfcExternalAuthenticateResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NfcExternalAuthenticateResult):
            return True

        return self.to_dict() != other.to_dict()