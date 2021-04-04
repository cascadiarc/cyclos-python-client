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


class AdDeliveryMethod(object):
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
        'charge_type': 'AdDeliveryMethodChargeEnum',
        'delivery_time': 'TimeInterval',
        'description': 'str',
        'charge_amount': 'BigDecimal'
    }

    attribute_map = {
        'charge_type': 'chargeType',
        'delivery_time': 'deliveryTime',
        'description': 'description',
        'charge_amount': 'chargeAmount'
    }

    def __init__(self, charge_type=None, delivery_time=None, description=None, charge_amount=None, _configuration=None):  # noqa: E501
        """AdDeliveryMethod - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._charge_type = None
        self._delivery_time = None
        self._description = None
        self._charge_amount = None
        self.discriminator = None

        if charge_type is not None:
            self.charge_type = charge_type
        if delivery_time is not None:
            self.delivery_time = delivery_time
        if description is not None:
            self.description = description
        if charge_amount is not None:
            self.charge_amount = charge_amount

    @property
    def charge_type(self):
        """Gets the charge_type of this AdDeliveryMethod.  # noqa: E501

        The possible charge types for a delivery method of a webshop ad. Possible values are: * fixed: The delivery method charge is fixed set by the seller. * negotiated: The delivery method charge can be be negotiated between the seller and the buyer.   # noqa: E501

        :return: The charge_type of this AdDeliveryMethod.  # noqa: E501
        :rtype: AdDeliveryMethodChargeEnum
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this AdDeliveryMethod.

        The possible charge types for a delivery method of a webshop ad. Possible values are: * fixed: The delivery method charge is fixed set by the seller. * negotiated: The delivery method charge can be be negotiated between the seller and the buyer.   # noqa: E501

        :param charge_type: The charge_type of this AdDeliveryMethod.  # noqa: E501
        :type: AdDeliveryMethodChargeEnum
        """

        self._charge_type = charge_type

    @property
    def delivery_time(self):
        """Gets the delivery_time of this AdDeliveryMethod.  # noqa: E501

        The delivery time.  # noqa: E501

        :return: The delivery_time of this AdDeliveryMethod.  # noqa: E501
        :rtype: TimeInterval
        """
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, delivery_time):
        """Sets the delivery_time of this AdDeliveryMethod.

        The delivery time.  # noqa: E501

        :param delivery_time: The delivery_time of this AdDeliveryMethod.  # noqa: E501
        :type: TimeInterval
        """

        self._delivery_time = delivery_time

    @property
    def description(self):
        """Gets the description of this AdDeliveryMethod.  # noqa: E501

        Description of the delivery method (if any).  # noqa: E501

        :return: The description of this AdDeliveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AdDeliveryMethod.

        Description of the delivery method (if any).  # noqa: E501

        :param description: The description of this AdDeliveryMethod.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def charge_amount(self):
        """Gets the charge_amount of this AdDeliveryMethod.  # noqa: E501

        The delivery method charge amount. Required if `chargeType` is  `fixed`.   # noqa: E501

        :return: The charge_amount of this AdDeliveryMethod.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, charge_amount):
        """Sets the charge_amount of this AdDeliveryMethod.

        The delivery method charge amount. Required if `chargeType` is  `fixed`.   # noqa: E501

        :param charge_amount: The charge_amount of this AdDeliveryMethod.  # noqa: E501
        :type: BigDecimal
        """

        self._charge_amount = charge_amount

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
        if issubclass(AdDeliveryMethod, dict):
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
        if not isinstance(other, AdDeliveryMethod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdDeliveryMethod):
            return True

        return self.to_dict() != other.to_dict()