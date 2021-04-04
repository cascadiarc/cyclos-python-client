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


class ShoppingCartDataForCheckout(object):
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
        'cart': 'ShoppingCartView',
        'payment_types': 'list[TransferType]',
        'delivery_methods': 'list[AdDeliveryMethod]',
        'address_configuration': 'AddressConfiguration',
        'confirmation_password_input': 'PasswordInput',
        'addresses': 'list[Address]'
    }

    attribute_map = {
        'cart': 'cart',
        'payment_types': 'paymentTypes',
        'delivery_methods': 'deliveryMethods',
        'address_configuration': 'addressConfiguration',
        'confirmation_password_input': 'confirmationPasswordInput',
        'addresses': 'addresses'
    }

    def __init__(self, cart=None, payment_types=None, delivery_methods=None, address_configuration=None, confirmation_password_input=None, addresses=None, _configuration=None):  # noqa: E501
        """ShoppingCartDataForCheckout - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cart = None
        self._payment_types = None
        self._delivery_methods = None
        self._address_configuration = None
        self._confirmation_password_input = None
        self._addresses = None
        self.discriminator = None

        if cart is not None:
            self.cart = cart
        if payment_types is not None:
            self.payment_types = payment_types
        if delivery_methods is not None:
            self.delivery_methods = delivery_methods
        if address_configuration is not None:
            self.address_configuration = address_configuration
        if confirmation_password_input is not None:
            self.confirmation_password_input = confirmation_password_input
        if addresses is not None:
            self.addresses = addresses

    @property
    def cart(self):
        """Gets the cart of this ShoppingCartDataForCheckout.  # noqa: E501

        The cart containing the currency and items.  # noqa: E501

        :return: The cart of this ShoppingCartDataForCheckout.  # noqa: E501
        :rtype: ShoppingCartView
        """
        return self._cart

    @cart.setter
    def cart(self, cart):
        """Sets the cart of this ShoppingCartDataForCheckout.

        The cart containing the currency and items.  # noqa: E501

        :param cart: The cart of this ShoppingCartDataForCheckout.  # noqa: E501
        :type: ShoppingCartView
        """

        self._cart = cart

    @property
    def payment_types(self):
        """Gets the payment_types of this ShoppingCartDataForCheckout.  # noqa: E501

        Contains the allowed payment types.  # noqa: E501

        :return: The payment_types of this ShoppingCartDataForCheckout.  # noqa: E501
        :rtype: list[TransferType]
        """
        return self._payment_types

    @payment_types.setter
    def payment_types(self, payment_types):
        """Sets the payment_types of this ShoppingCartDataForCheckout.

        Contains the allowed payment types.  # noqa: E501

        :param payment_types: The payment_types of this ShoppingCartDataForCheckout.  # noqa: E501
        :type: list[TransferType]
        """

        self._payment_types = payment_types

    @property
    def delivery_methods(self):
        """Gets the delivery_methods of this ShoppingCartDataForCheckout.  # noqa: E501

        The list of delivery method commons to all of the products added to the  shopping cart ordered by name.   # noqa: E501

        :return: The delivery_methods of this ShoppingCartDataForCheckout.  # noqa: E501
        :rtype: list[AdDeliveryMethod]
        """
        return self._delivery_methods

    @delivery_methods.setter
    def delivery_methods(self, delivery_methods):
        """Sets the delivery_methods of this ShoppingCartDataForCheckout.

        The list of delivery method commons to all of the products added to the  shopping cart ordered by name.   # noqa: E501

        :param delivery_methods: The delivery_methods of this ShoppingCartDataForCheckout.  # noqa: E501
        :type: list[AdDeliveryMethod]
        """

        self._delivery_methods = delivery_methods

    @property
    def address_configuration(self):
        """Gets the address_configuration of this ShoppingCartDataForCheckout.  # noqa: E501

        Configuration data for addresses.  # noqa: E501

        :return: The address_configuration of this ShoppingCartDataForCheckout.  # noqa: E501
        :rtype: AddressConfiguration
        """
        return self._address_configuration

    @address_configuration.setter
    def address_configuration(self, address_configuration):
        """Sets the address_configuration of this ShoppingCartDataForCheckout.

        Configuration data for addresses.  # noqa: E501

        :param address_configuration: The address_configuration of this ShoppingCartDataForCheckout.  # noqa: E501
        :type: AddressConfiguration
        """

        self._address_configuration = address_configuration

    @property
    def confirmation_password_input(self):
        """Gets the confirmation_password_input of this ShoppingCartDataForCheckout.  # noqa: E501

        If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).   # noqa: E501

        :return: The confirmation_password_input of this ShoppingCartDataForCheckout.  # noqa: E501
        :rtype: PasswordInput
        """
        return self._confirmation_password_input

    @confirmation_password_input.setter
    def confirmation_password_input(self, confirmation_password_input):
        """Sets the confirmation_password_input of this ShoppingCartDataForCheckout.

        If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).   # noqa: E501

        :param confirmation_password_input: The confirmation_password_input of this ShoppingCartDataForCheckout.  # noqa: E501
        :type: PasswordInput
        """

        self._confirmation_password_input = confirmation_password_input

    @property
    def addresses(self):
        """Gets the addresses of this ShoppingCartDataForCheckout.  # noqa: E501

        The addresses the logged user (i.e the buyer) has.   # noqa: E501

        :return: The addresses of this ShoppingCartDataForCheckout.  # noqa: E501
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this ShoppingCartDataForCheckout.

        The addresses the logged user (i.e the buyer) has.   # noqa: E501

        :param addresses: The addresses of this ShoppingCartDataForCheckout.  # noqa: E501
        :type: list[Address]
        """

        self._addresses = addresses

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
        if issubclass(ShoppingCartDataForCheckout, dict):
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
        if not isinstance(other, ShoppingCartDataForCheckout):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShoppingCartDataForCheckout):
            return True

        return self.to_dict() != other.to_dict()
