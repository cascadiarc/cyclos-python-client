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


class ShoppingCartItem(object):
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
        'price_when_added': 'BigDecimal',
        'price': 'BigDecimal',
        'promotional_price': 'BigDecimal'
    }

    attribute_map = {
        'price_when_added': 'priceWhenAdded',
        'price': 'price',
        'promotional_price': 'promotionalPrice'
    }

    def __init__(self, price_when_added=None, price=None, promotional_price=None, _configuration=None):  # noqa: E501
        """ShoppingCartItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._price_when_added = None
        self._price = None
        self._promotional_price = None
        self.discriminator = None

        if price_when_added is not None:
            self.price_when_added = price_when_added
        if price is not None:
            self.price = price
        if promotional_price is not None:
            self.promotional_price = promotional_price

    @property
    def price_when_added(self):
        """Gets the price_when_added of this ShoppingCartItem.  # noqa: E501

        The current product price at the moment of add it to the shopping cart.  Be carefull, this could not be the same price finally charged at  check-out (e.g because the promotional period has finished).  It could be used to show a warning message to the client indicating  the price has changed if it is different from the current price of the `product`.   # noqa: E501

        :return: The price_when_added of this ShoppingCartItem.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._price_when_added

    @price_when_added.setter
    def price_when_added(self, price_when_added):
        """Sets the price_when_added of this ShoppingCartItem.

        The current product price at the moment of add it to the shopping cart.  Be carefull, this could not be the same price finally charged at  check-out (e.g because the promotional period has finished).  It could be used to show a warning message to the client indicating  the price has changed if it is different from the current price of the `product`.   # noqa: E501

        :param price_when_added: The price_when_added of this ShoppingCartItem.  # noqa: E501
        :type: BigDecimal
        """

        self._price_when_added = price_when_added

    @property
    def price(self):
        """Gets the price of this ShoppingCartItem.  # noqa: E501

        The regular price.  # noqa: E501

        :return: The price of this ShoppingCartItem.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ShoppingCartItem.

        The regular price.  # noqa: E501

        :param price: The price of this ShoppingCartItem.  # noqa: E501
        :type: BigDecimal
        """

        self._price = price

    @property
    def promotional_price(self):
        """Gets the promotional_price of this ShoppingCartItem.  # noqa: E501

        The promotional price (aka the current price). if it is present then  that is the current price that would be charged at check-out.  Otherwise would be the `price`.  Only present if it is defined and the promotional period has not  yet finished.    # noqa: E501

        :return: The promotional_price of this ShoppingCartItem.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._promotional_price

    @promotional_price.setter
    def promotional_price(self, promotional_price):
        """Sets the promotional_price of this ShoppingCartItem.

        The promotional price (aka the current price). if it is present then  that is the current price that would be charged at check-out.  Otherwise would be the `price`.  Only present if it is defined and the promotional period has not  yet finished.    # noqa: E501

        :param promotional_price: The promotional_price of this ShoppingCartItem.  # noqa: E501
        :type: BigDecimal
        """

        self._promotional_price = promotional_price

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
        if issubclass(ShoppingCartItem, dict):
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
        if not isinstance(other, ShoppingCartItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShoppingCartItem):
            return True

        return self.to_dict() != other.to_dict()
