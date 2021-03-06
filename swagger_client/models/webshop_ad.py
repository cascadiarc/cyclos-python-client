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


class WebshopAd(object):
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
        'allow_decimal_quantity': 'bool',
        'min_allowed_in_cart': 'BigDecimal',
        'max_allowed_in_cart': 'BigDecimal',
        'stock_quantity': 'BigDecimal',
        'unlimited_stock': 'bool',
        'product_number': 'str'
    }

    attribute_map = {
        'allow_decimal_quantity': 'allowDecimalQuantity',
        'min_allowed_in_cart': 'minAllowedInCart',
        'max_allowed_in_cart': 'maxAllowedInCart',
        'stock_quantity': 'stockQuantity',
        'unlimited_stock': 'unlimitedStock',
        'product_number': 'productNumber'
    }

    def __init__(self, allow_decimal_quantity=None, min_allowed_in_cart=None, max_allowed_in_cart=None, stock_quantity=None, unlimited_stock=None, product_number=None, _configuration=None):  # noqa: E501
        """WebshopAd - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_decimal_quantity = None
        self._min_allowed_in_cart = None
        self._max_allowed_in_cart = None
        self._stock_quantity = None
        self._unlimited_stock = None
        self._product_number = None
        self.discriminator = None

        if allow_decimal_quantity is not None:
            self.allow_decimal_quantity = allow_decimal_quantity
        if min_allowed_in_cart is not None:
            self.min_allowed_in_cart = min_allowed_in_cart
        if max_allowed_in_cart is not None:
            self.max_allowed_in_cart = max_allowed_in_cart
        if stock_quantity is not None:
            self.stock_quantity = stock_quantity
        if unlimited_stock is not None:
            self.unlimited_stock = unlimited_stock
        if product_number is not None:
            self.product_number = product_number

    @property
    def allow_decimal_quantity(self):
        """Gets the allow_decimal_quantity of this WebshopAd.  # noqa: E501

        Indicates if the webshop ad allow enter a decimal value for the  quantity.   # noqa: E501

        :return: The allow_decimal_quantity of this WebshopAd.  # noqa: E501
        :rtype: bool
        """
        return self._allow_decimal_quantity

    @allow_decimal_quantity.setter
    def allow_decimal_quantity(self, allow_decimal_quantity):
        """Sets the allow_decimal_quantity of this WebshopAd.

        Indicates if the webshop ad allow enter a decimal value for the  quantity.   # noqa: E501

        :param allow_decimal_quantity: The allow_decimal_quantity of this WebshopAd.  # noqa: E501
        :type: bool
        """

        self._allow_decimal_quantity = allow_decimal_quantity

    @property
    def min_allowed_in_cart(self):
        """Gets the min_allowed_in_cart of this WebshopAd.  # noqa: E501

        The minimum quantity allowed to be added in the shopping cart.   # noqa: E501

        :return: The min_allowed_in_cart of this WebshopAd.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._min_allowed_in_cart

    @min_allowed_in_cart.setter
    def min_allowed_in_cart(self, min_allowed_in_cart):
        """Sets the min_allowed_in_cart of this WebshopAd.

        The minimum quantity allowed to be added in the shopping cart.   # noqa: E501

        :param min_allowed_in_cart: The min_allowed_in_cart of this WebshopAd.  # noqa: E501
        :type: BigDecimal
        """

        self._min_allowed_in_cart = min_allowed_in_cart

    @property
    def max_allowed_in_cart(self):
        """Gets the max_allowed_in_cart of this WebshopAd.  # noqa: E501

        The maximum quantity allowed to be added in the shopping cart.    # noqa: E501

        :return: The max_allowed_in_cart of this WebshopAd.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._max_allowed_in_cart

    @max_allowed_in_cart.setter
    def max_allowed_in_cart(self, max_allowed_in_cart):
        """Sets the max_allowed_in_cart of this WebshopAd.

        The maximum quantity allowed to be added in the shopping cart.    # noqa: E501

        :param max_allowed_in_cart: The max_allowed_in_cart of this WebshopAd.  # noqa: E501
        :type: BigDecimal
        """

        self._max_allowed_in_cart = max_allowed_in_cart

    @property
    def stock_quantity(self):
        """Gets the stock_quantity of this WebshopAd.  # noqa: E501

        The stock disponibility. Only if `unlimitedStock` is false and the  'Stock type' was not marked as 'Not available' (through the web  interface).   # noqa: E501

        :return: The stock_quantity of this WebshopAd.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, stock_quantity):
        """Sets the stock_quantity of this WebshopAd.

        The stock disponibility. Only if `unlimitedStock` is false and the  'Stock type' was not marked as 'Not available' (through the web  interface).   # noqa: E501

        :param stock_quantity: The stock_quantity of this WebshopAd.  # noqa: E501
        :type: BigDecimal
        """

        self._stock_quantity = stock_quantity

    @property
    def unlimited_stock(self):
        """Gets the unlimited_stock of this WebshopAd.  # noqa: E501

        If true then it means there is always disponibility of the webshop ad.  # noqa: E501

        :return: The unlimited_stock of this WebshopAd.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited_stock

    @unlimited_stock.setter
    def unlimited_stock(self, unlimited_stock):
        """Sets the unlimited_stock of this WebshopAd.

        If true then it means there is always disponibility of the webshop ad.  # noqa: E501

        :param unlimited_stock: The unlimited_stock of this WebshopAd.  # noqa: E501
        :type: bool
        """

        self._unlimited_stock = unlimited_stock

    @property
    def product_number(self):
        """Gets the product_number of this WebshopAd.  # noqa: E501

        The number assigned to the webshop ad.  # noqa: E501

        :return: The product_number of this WebshopAd.  # noqa: E501
        :rtype: str
        """
        return self._product_number

    @product_number.setter
    def product_number(self, product_number):
        """Sets the product_number of this WebshopAd.

        The number assigned to the webshop ad.  # noqa: E501

        :param product_number: The product_number of this WebshopAd.  # noqa: E501
        :type: str
        """

        self._product_number = product_number

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
        if issubclass(WebshopAd, dict):
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
        if not isinstance(other, WebshopAd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebshopAd):
            return True

        return self.to_dict() != other.to_dict()
