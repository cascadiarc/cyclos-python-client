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


class PrincipalTypeInput(object):
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
        'custom_field': 'CustomFieldDetailed',
        'token_type': 'TokenTypeEnum',
        'mask': 'str',
        'allow_manual_input': 'bool',
        'example': 'str'
    }

    attribute_map = {
        'custom_field': 'customField',
        'token_type': 'tokenType',
        'mask': 'mask',
        'allow_manual_input': 'allowManualInput',
        'example': 'example'
    }

    def __init__(self, custom_field=None, token_type=None, mask=None, allow_manual_input=None, example=None, _configuration=None):  # noqa: E501
        """PrincipalTypeInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_field = None
        self._token_type = None
        self._mask = None
        self._allow_manual_input = None
        self._example = None
        self.discriminator = None

        if custom_field is not None:
            self.custom_field = custom_field
        if token_type is not None:
            self.token_type = token_type
        if mask is not None:
            self.mask = mask
        if allow_manual_input is not None:
            self.allow_manual_input = allow_manual_input
        if example is not None:
            self.example = example

    @property
    def custom_field(self):
        """Gets the custom_field of this PrincipalTypeInput.  # noqa: E501

        If this principal is based on a custom field, holds its definition   # noqa: E501

        :return: The custom_field of this PrincipalTypeInput.  # noqa: E501
        :rtype: CustomFieldDetailed
        """
        return self._custom_field

    @custom_field.setter
    def custom_field(self, custom_field):
        """Sets the custom_field of this PrincipalTypeInput.

        If this principal is based on a custom field, holds its definition   # noqa: E501

        :param custom_field: The custom_field of this PrincipalTypeInput.  # noqa: E501
        :type: CustomFieldDetailed
        """

        self._custom_field = custom_field

    @property
    def token_type(self):
        """Gets the token_type of this PrincipalTypeInput.  # noqa: E501

        If this principal is a token, contains its type Possible values are: * barcode: A barcode with the token * nfcDevice: A device (e.g. cell phone) with support for NFC * nfcTag: A NFC tag/card  * other: Any other type containing a token * qrcode: A QR code containing a token * swipe: A swipe/magnetic card containing the token   # noqa: E501

        :return: The token_type of this PrincipalTypeInput.  # noqa: E501
        :rtype: TokenTypeEnum
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this PrincipalTypeInput.

        If this principal is a token, contains its type Possible values are: * barcode: A barcode with the token * nfcDevice: A device (e.g. cell phone) with support for NFC * nfcTag: A NFC tag/card  * other: Any other type containing a token * qrcode: A QR code containing a token * swipe: A swipe/magnetic card containing the token   # noqa: E501

        :param token_type: The token_type of this PrincipalTypeInput.  # noqa: E501
        :type: TokenTypeEnum
        """

        self._token_type = token_type

    @property
    def mask(self):
        """Gets the mask of this PrincipalTypeInput.  # noqa: E501

        If this principal is either a token or account number, holds the (optional) mask which clients can use to input the value.   # noqa: E501

        :return: The mask of this PrincipalTypeInput.  # noqa: E501
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this PrincipalTypeInput.

        If this principal is either a token or account number, holds the (optional) mask which clients can use to input the value.   # noqa: E501

        :param mask: The mask of this PrincipalTypeInput.  # noqa: E501
        :type: str
        """

        self._mask = mask

    @property
    def allow_manual_input(self):
        """Gets the allow_manual_input of this PrincipalTypeInput.  # noqa: E501

        Only returned if `kind` is `token`. Specifies if the principal type allows enter manually the token value.   # noqa: E501

        :return: The allow_manual_input of this PrincipalTypeInput.  # noqa: E501
        :rtype: bool
        """
        return self._allow_manual_input

    @allow_manual_input.setter
    def allow_manual_input(self, allow_manual_input):
        """Sets the allow_manual_input of this PrincipalTypeInput.

        Only returned if `kind` is `token`. Specifies if the principal type allows enter manually the token value.   # noqa: E501

        :param allow_manual_input: The allow_manual_input of this PrincipalTypeInput.  # noqa: E501
        :type: bool
        """

        self._allow_manual_input = allow_manual_input

    @property
    def example(self):
        """Gets the example of this PrincipalTypeInput.  # noqa: E501

        If this principal is mobile phone, holds an example number.   # noqa: E501

        :return: The example of this PrincipalTypeInput.  # noqa: E501
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this PrincipalTypeInput.

        If this principal is mobile phone, holds an example number.   # noqa: E501

        :param example: The example of this PrincipalTypeInput.  # noqa: E501
        :type: str
        """

        self._example = example

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
        if issubclass(PrincipalTypeInput, dict):
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
        if not isinstance(other, PrincipalTypeInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrincipalTypeInput):
            return True

        return self.to_dict() != other.to_dict()
