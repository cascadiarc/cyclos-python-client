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


class ShoppingCartCheckoutError(object):
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
        'code': 'ShoppingCartCheckoutErrorCode',
        'shopping_cart_error': 'ShoppingCartError'
    }

    attribute_map = {
        'code': 'code',
        'shopping_cart_error': 'shoppingCartError'
    }

    def __init__(self, code=None, shopping_cart_error=None, _configuration=None):  # noqa: E501
        """ShoppingCartCheckoutError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._shopping_cart_error = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if shopping_cart_error is not None:
            self.shopping_cart_error = shopping_cart_error

    @property
    def code(self):
        """Gets the code of this ShoppingCartCheckoutError.  # noqa: E501

        Possible errors when checking out a shopping cart. Possible values are: * insufficientBalance: The origin account of the selected payment type used to make the amount reservation does not have enough balance. * products: There was an error related to the products contained in he shopping cart. * unexpected: An unexpected error has occurred. See the `exceptionType` and `exceptionMessage` fields for the internal information.   # noqa: E501

        :return: The code of this ShoppingCartCheckoutError.  # noqa: E501
        :rtype: ShoppingCartCheckoutErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShoppingCartCheckoutError.

        Possible errors when checking out a shopping cart. Possible values are: * insufficientBalance: The origin account of the selected payment type used to make the amount reservation does not have enough balance. * products: There was an error related to the products contained in he shopping cart. * unexpected: An unexpected error has occurred. See the `exceptionType` and `exceptionMessage` fields for the internal information.   # noqa: E501

        :param code: The code of this ShoppingCartCheckoutError.  # noqa: E501
        :type: ShoppingCartCheckoutErrorCode
        """

        self._code = code

    @property
    def shopping_cart_error(self):
        """Gets the shopping_cart_error of this ShoppingCartCheckoutError.  # noqa: E501

        The `ShoppingCartError` generated when the products in the cart were being validated.  Only if `code` is `products`.   # noqa: E501

        :return: The shopping_cart_error of this ShoppingCartCheckoutError.  # noqa: E501
        :rtype: ShoppingCartError
        """
        return self._shopping_cart_error

    @shopping_cart_error.setter
    def shopping_cart_error(self, shopping_cart_error):
        """Sets the shopping_cart_error of this ShoppingCartCheckoutError.

        The `ShoppingCartError` generated when the products in the cart were being validated.  Only if `code` is `products`.   # noqa: E501

        :param shopping_cart_error: The shopping_cart_error of this ShoppingCartCheckoutError.  # noqa: E501
        :type: ShoppingCartError
        """

        self._shopping_cart_error = shopping_cart_error

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
        if issubclass(ShoppingCartCheckoutError, dict):
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
        if not isinstance(other, ShoppingCartCheckoutError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShoppingCartCheckoutError):
            return True

        return self.to_dict() != other.to_dict()