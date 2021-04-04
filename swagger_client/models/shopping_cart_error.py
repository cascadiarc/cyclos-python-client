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


class ShoppingCartError(object):
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
        'code': 'ShoppingCartErrorCode',
        'ad': 'WebshopAd',
        'seller': 'User'
    }

    attribute_map = {
        'code': 'code',
        'ad': 'ad',
        'seller': 'seller'
    }

    def __init__(self, code=None, ad=None, seller=None, _configuration=None):  # noqa: E501
        """ShoppingCartError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._ad = None
        self._seller = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if ad is not None:
            self.ad = ad
        if seller is not None:
            self.seller = seller

    @property
    def code(self):
        """Gets the code of this ShoppingCartError.  # noqa: E501

        Possible errors when interacting with a shopping cart. Possible values are: * canNotBuyFromSeller: The authenticated user is not visible by the webshop's seller * notEnoughStock: There is not enough stock of the webshop ad to fulfill the requested quantity * unexpected: An unexpected error has occurred. See the `exceptionType` and `exceptionMessage` fields for the internal information.    # noqa: E501

        :return: The code of this ShoppingCartError.  # noqa: E501
        :rtype: ShoppingCartErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShoppingCartError.

        Possible errors when interacting with a shopping cart. Possible values are: * canNotBuyFromSeller: The authenticated user is not visible by the webshop's seller * notEnoughStock: There is not enough stock of the webshop ad to fulfill the requested quantity * unexpected: An unexpected error has occurred. See the `exceptionType` and `exceptionMessage` fields for the internal information.    # noqa: E501

        :param code: The code of this ShoppingCartError.  # noqa: E501
        :type: ShoppingCartErrorCode
        """

        self._code = code

    @property
    def ad(self):
        """Gets the ad of this ShoppingCartError.  # noqa: E501

        The webshop ad for which there is not enough stock.  Only if `code` is `notEnoughStock`   # noqa: E501

        :return: The ad of this ShoppingCartError.  # noqa: E501
        :rtype: WebshopAd
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """Sets the ad of this ShoppingCartError.

        The webshop ad for which there is not enough stock.  Only if `code` is `notEnoughStock`   # noqa: E501

        :param ad: The ad of this ShoppingCartError.  # noqa: E501
        :type: WebshopAd
        """

        self._ad = ad

    @property
    def seller(self):
        """Gets the seller of this ShoppingCartError.  # noqa: E501

        The seller whose webshop ad can not be bought. Only if `code` is `canNotBuyFromSeller`   # noqa: E501

        :return: The seller of this ShoppingCartError.  # noqa: E501
        :rtype: User
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this ShoppingCartError.

        The seller whose webshop ad can not be bought. Only if `code` is `canNotBuyFromSeller`   # noqa: E501

        :param seller: The seller of this ShoppingCartError.  # noqa: E501
        :type: User
        """

        self._seller = seller

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
        if issubclass(ShoppingCartError, dict):
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
        if not isinstance(other, ShoppingCartError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShoppingCartError):
            return True

        return self.to_dict() != other.to_dict()
