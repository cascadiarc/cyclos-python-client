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


class UserMarketplacePermissions(object):
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
        'view_advertisements': 'bool',
        'manage_advertisements': 'bool',
        'view_webshop': 'bool',
        'manage_webshop': 'bool',
        'view_purchases': 'bool',
        'view_sales': 'bool'
    }

    attribute_map = {
        'view_advertisements': 'viewAdvertisements',
        'manage_advertisements': 'manageAdvertisements',
        'view_webshop': 'viewWebshop',
        'manage_webshop': 'manageWebshop',
        'view_purchases': 'viewPurchases',
        'view_sales': 'viewSales'
    }

    def __init__(self, view_advertisements=None, manage_advertisements=None, view_webshop=None, manage_webshop=None, view_purchases=None, view_sales=None, _configuration=None):  # noqa: E501
        """UserMarketplacePermissions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._view_advertisements = None
        self._manage_advertisements = None
        self._view_webshop = None
        self._manage_webshop = None
        self._view_purchases = None
        self._view_sales = None
        self.discriminator = None

        if view_advertisements is not None:
            self.view_advertisements = view_advertisements
        if manage_advertisements is not None:
            self.manage_advertisements = manage_advertisements
        if view_webshop is not None:
            self.view_webshop = view_webshop
        if manage_webshop is not None:
            self.manage_webshop = manage_webshop
        if view_purchases is not None:
            self.view_purchases = view_purchases
        if view_sales is not None:
            self.view_sales = view_sales

    @property
    def view_advertisements(self):
        """Gets the view_advertisements of this UserMarketplacePermissions.  # noqa: E501

        Can view simple advertisements?  # noqa: E501

        :return: The view_advertisements of this UserMarketplacePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._view_advertisements

    @view_advertisements.setter
    def view_advertisements(self, view_advertisements):
        """Sets the view_advertisements of this UserMarketplacePermissions.

        Can view simple advertisements?  # noqa: E501

        :param view_advertisements: The view_advertisements of this UserMarketplacePermissions.  # noqa: E501
        :type: bool
        """

        self._view_advertisements = view_advertisements

    @property
    def manage_advertisements(self):
        """Gets the manage_advertisements of this UserMarketplacePermissions.  # noqa: E501

        Can manage simple advertisements?  # noqa: E501

        :return: The manage_advertisements of this UserMarketplacePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._manage_advertisements

    @manage_advertisements.setter
    def manage_advertisements(self, manage_advertisements):
        """Sets the manage_advertisements of this UserMarketplacePermissions.

        Can manage simple advertisements?  # noqa: E501

        :param manage_advertisements: The manage_advertisements of this UserMarketplacePermissions.  # noqa: E501
        :type: bool
        """

        self._manage_advertisements = manage_advertisements

    @property
    def view_webshop(self):
        """Gets the view_webshop of this UserMarketplacePermissions.  # noqa: E501

        Can view webshop advertisements?  # noqa: E501

        :return: The view_webshop of this UserMarketplacePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._view_webshop

    @view_webshop.setter
    def view_webshop(self, view_webshop):
        """Sets the view_webshop of this UserMarketplacePermissions.

        Can view webshop advertisements?  # noqa: E501

        :param view_webshop: The view_webshop of this UserMarketplacePermissions.  # noqa: E501
        :type: bool
        """

        self._view_webshop = view_webshop

    @property
    def manage_webshop(self):
        """Gets the manage_webshop of this UserMarketplacePermissions.  # noqa: E501

        Can manage webshop advertisements?  # noqa: E501

        :return: The manage_webshop of this UserMarketplacePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._manage_webshop

    @manage_webshop.setter
    def manage_webshop(self, manage_webshop):
        """Sets the manage_webshop of this UserMarketplacePermissions.

        Can manage webshop advertisements?  # noqa: E501

        :param manage_webshop: The manage_webshop of this UserMarketplacePermissions.  # noqa: E501
        :type: bool
        """

        self._manage_webshop = manage_webshop

    @property
    def view_purchases(self):
        """Gets the view_purchases of this UserMarketplacePermissions.  # noqa: E501

        Can view the purchases?  # noqa: E501

        :return: The view_purchases of this UserMarketplacePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._view_purchases

    @view_purchases.setter
    def view_purchases(self, view_purchases):
        """Sets the view_purchases of this UserMarketplacePermissions.

        Can view the purchases?  # noqa: E501

        :param view_purchases: The view_purchases of this UserMarketplacePermissions.  # noqa: E501
        :type: bool
        """

        self._view_purchases = view_purchases

    @property
    def view_sales(self):
        """Gets the view_sales of this UserMarketplacePermissions.  # noqa: E501

        Can view the sales?  # noqa: E501

        :return: The view_sales of this UserMarketplacePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._view_sales

    @view_sales.setter
    def view_sales(self, view_sales):
        """Sets the view_sales of this UserMarketplacePermissions.

        Can view the sales?  # noqa: E501

        :param view_sales: The view_sales of this UserMarketplacePermissions.  # noqa: E501
        :type: bool
        """

        self._view_sales = view_sales

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
        if issubclass(UserMarketplacePermissions, dict):
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
        if not isinstance(other, UserMarketplacePermissions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserMarketplacePermissions):
            return True

        return self.to_dict() != other.to_dict()
