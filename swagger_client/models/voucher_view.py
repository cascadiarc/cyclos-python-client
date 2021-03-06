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


class VoucherView(object):
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
        'title': 'str',
        'description': 'str',
        'creation_type': 'VoucherCreationTypeEnum',
        'buy': 'Transaction',
        'redeem_date': 'datetime',
        'redeem': 'Transaction',
        'can_cancel': 'bool',
        'cancel_action': 'VoucherCancelActionEnum',
        'show_configuration': 'bool',
        'show_qr_code': 'bool',
        'redeem_after_date_reached': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'creation_type': 'creationType',
        'buy': 'buy',
        'redeem_date': 'redeemDate',
        'redeem': 'redeem',
        'can_cancel': 'canCancel',
        'cancel_action': 'cancelAction',
        'show_configuration': 'showConfiguration',
        'show_qr_code': 'showQrCode',
        'redeem_after_date_reached': 'redeemAfterDateReached'
    }

    def __init__(self, title=None, description=None, creation_type=None, buy=None, redeem_date=None, redeem=None, can_cancel=None, cancel_action=None, show_configuration=None, show_qr_code=None, redeem_after_date_reached=None, _configuration=None):  # noqa: E501
        """VoucherView - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._title = None
        self._description = None
        self._creation_type = None
        self._buy = None
        self._redeem_date = None
        self._redeem = None
        self._can_cancel = None
        self._cancel_action = None
        self._show_configuration = None
        self._show_qr_code = None
        self._redeem_after_date_reached = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if creation_type is not None:
            self.creation_type = creation_type
        if buy is not None:
            self.buy = buy
        if redeem_date is not None:
            self.redeem_date = redeem_date
        if redeem is not None:
            self.redeem = redeem
        if can_cancel is not None:
            self.can_cancel = can_cancel
        if cancel_action is not None:
            self.cancel_action = cancel_action
        if show_configuration is not None:
            self.show_configuration = show_configuration
        if show_qr_code is not None:
            self.show_qr_code = show_qr_code
        if redeem_after_date_reached is not None:
            self.redeem_after_date_reached = redeem_after_date_reached

    @property
    def title(self):
        """Gets the title of this VoucherView.  # noqa: E501

        The voucher title when it was created.  # noqa: E501

        :return: The title of this VoucherView.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this VoucherView.

        The voucher title when it was created.  # noqa: E501

        :param title: The title of this VoucherView.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this VoucherView.  # noqa: E501

        The voucher description when it was created.  # noqa: E501

        :return: The description of this VoucherView.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VoucherView.

        The voucher description when it was created.  # noqa: E501

        :param description: The description of this VoucherView.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def creation_type(self):
        """Gets the creation_type of this VoucherView.  # noqa: E501

        Indicates how a voucher was created Possible values are: * bought: The voucher was bought by an user * generated: The voucher was generated by an administrator   # noqa: E501

        :return: The creation_type of this VoucherView.  # noqa: E501
        :rtype: VoucherCreationTypeEnum
        """
        return self._creation_type

    @creation_type.setter
    def creation_type(self, creation_type):
        """Sets the creation_type of this VoucherView.

        Indicates how a voucher was created Possible values are: * bought: The voucher was bought by an user * generated: The voucher was generated by an administrator   # noqa: E501

        :param creation_type: The creation_type of this VoucherView.  # noqa: E501
        :type: VoucherCreationTypeEnum
        """

        self._creation_type = creation_type

    @property
    def buy(self):
        """Gets the buy of this VoucherView.  # noqa: E501

        The transaction which bought this voucher, if any and visible.   # noqa: E501

        :return: The buy of this VoucherView.  # noqa: E501
        :rtype: Transaction
        """
        return self._buy

    @buy.setter
    def buy(self, buy):
        """Sets the buy of this VoucherView.

        The transaction which bought this voucher, if any and visible.   # noqa: E501

        :param buy: The buy of this VoucherView.  # noqa: E501
        :type: Transaction
        """

        self._buy = buy

    @property
    def redeem_date(self):
        """Gets the redeem_date of this VoucherView.  # noqa: E501

        The date the voucher was redeemer, if any.  # noqa: E501

        :return: The redeem_date of this VoucherView.  # noqa: E501
        :rtype: datetime
        """
        return self._redeem_date

    @redeem_date.setter
    def redeem_date(self, redeem_date):
        """Sets the redeem_date of this VoucherView.

        The date the voucher was redeemer, if any.  # noqa: E501

        :param redeem_date: The redeem_date of this VoucherView.  # noqa: E501
        :type: datetime
        """

        self._redeem_date = redeem_date

    @property
    def redeem(self):
        """Gets the redeem of this VoucherView.  # noqa: E501

        The transaction which redeemed this voucher, if any and visible.   # noqa: E501

        :return: The redeem of this VoucherView.  # noqa: E501
        :rtype: Transaction
        """
        return self._redeem

    @redeem.setter
    def redeem(self, redeem):
        """Sets the redeem of this VoucherView.

        The transaction which redeemed this voucher, if any and visible.   # noqa: E501

        :param redeem: The redeem of this VoucherView.  # noqa: E501
        :type: Transaction
        """

        self._redeem = redeem

    @property
    def can_cancel(self):
        """Gets the can_cancel of this VoucherView.  # noqa: E501

        (Deprecated) Can the authenticated user cancel this voucher?  # noqa: E501

        :return: The can_cancel of this VoucherView.  # noqa: E501
        :rtype: bool
        """
        return self._can_cancel

    @can_cancel.setter
    def can_cancel(self, can_cancel):
        """Sets the can_cancel of this VoucherView.

        (Deprecated) Can the authenticated user cancel this voucher?  # noqa: E501

        :param can_cancel: The can_cancel of this VoucherView.  # noqa: E501
        :type: bool
        """

        self._can_cancel = can_cancel

    @property
    def cancel_action(self):
        """Gets the cancel_action of this VoucherView.  # noqa: E501

        Indicates what happens if a voucher is canceled, if it can be canceled Possible values are: * cancelAndRefund: A single bought voucher is canceled and the amount is refunded * cancelGenerated: Cancels a single generated voucher * cancelPendingPack: Cancels more than one bought vouchers whose buy payment is pending authorization * cancelPendingSingle: Cancels a single bought vouchers whose buy payment is pending authorization   # noqa: E501

        :return: The cancel_action of this VoucherView.  # noqa: E501
        :rtype: VoucherCancelActionEnum
        """
        return self._cancel_action

    @cancel_action.setter
    def cancel_action(self, cancel_action):
        """Sets the cancel_action of this VoucherView.

        Indicates what happens if a voucher is canceled, if it can be canceled Possible values are: * cancelAndRefund: A single bought voucher is canceled and the amount is refunded * cancelGenerated: Cancels a single generated voucher * cancelPendingPack: Cancels more than one bought vouchers whose buy payment is pending authorization * cancelPendingSingle: Cancels a single bought vouchers whose buy payment is pending authorization   # noqa: E501

        :param cancel_action: The cancel_action of this VoucherView.  # noqa: E501
        :type: VoucherCancelActionEnum
        """

        self._cancel_action = cancel_action

    @property
    def show_configuration(self):
        """Gets the show_configuration of this VoucherView.  # noqa: E501

        Should the voucher configuration be shown to users? This flag is `true` when there are multiple available configurations.   # noqa: E501

        :return: The show_configuration of this VoucherView.  # noqa: E501
        :rtype: bool
        """
        return self._show_configuration

    @show_configuration.setter
    def show_configuration(self, show_configuration):
        """Sets the show_configuration of this VoucherView.

        Should the voucher configuration be shown to users? This flag is `true` when there are multiple available configurations.   # noqa: E501

        :param show_configuration: The show_configuration of this VoucherView.  # noqa: E501
        :type: bool
        """

        self._show_configuration = show_configuration

    @property
    def show_qr_code(self):
        """Gets the show_qr_code of this VoucherView.  # noqa: E501

        Should the voucher token be shown as QR-code for users?  # noqa: E501

        :return: The show_qr_code of this VoucherView.  # noqa: E501
        :rtype: bool
        """
        return self._show_qr_code

    @show_qr_code.setter
    def show_qr_code(self, show_qr_code):
        """Sets the show_qr_code of this VoucherView.

        Should the voucher token be shown as QR-code for users?  # noqa: E501

        :param show_qr_code: The show_qr_code of this VoucherView.  # noqa: E501
        :type: bool
        """

        self._show_qr_code = show_qr_code

    @property
    def redeem_after_date_reached(self):
        """Gets the redeem_after_date_reached of this VoucherView.  # noqa: E501

        Should the voucher be available to be redeemed?  # noqa: E501

        :return: The redeem_after_date_reached of this VoucherView.  # noqa: E501
        :rtype: bool
        """
        return self._redeem_after_date_reached

    @redeem_after_date_reached.setter
    def redeem_after_date_reached(self, redeem_after_date_reached):
        """Sets the redeem_after_date_reached of this VoucherView.

        Should the voucher be available to be redeemed?  # noqa: E501

        :param redeem_after_date_reached: The redeem_after_date_reached of this VoucherView.  # noqa: E501
        :type: bool
        """

        self._redeem_after_date_reached = redeem_after_date_reached

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
        if issubclass(VoucherView, dict):
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
        if not isinstance(other, VoucherView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VoucherView):
            return True

        return self.to_dict() != other.to_dict()
