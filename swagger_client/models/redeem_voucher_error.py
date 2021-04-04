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


class RedeemVoucherError(object):
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
        'code': 'RedeemVoucherErrorCode',
        'voucher_status': 'VoucherStatusEnum',
        'allowed_days': 'list[WeekDayEnum]',
        'redeem_after_date': 'datetime',
        'payment_error': 'PaymentError'
    }

    attribute_map = {
        'code': 'code',
        'voucher_status': 'voucherStatus',
        'allowed_days': 'allowedDays',
        'redeem_after_date': 'redeemAfterDate',
        'payment_error': 'paymentError'
    }

    def __init__(self, code=None, voucher_status=None, allowed_days=None, redeem_after_date=None, payment_error=None, _configuration=None):  # noqa: E501
        """RedeemVoucherError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._voucher_status = None
        self._allowed_days = None
        self._redeem_after_date = None
        self._payment_error = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if voucher_status is not None:
            self.voucher_status = voucher_status
        if allowed_days is not None:
            self.allowed_days = allowed_days
        if redeem_after_date is not None:
            self.redeem_after_date = redeem_after_date
        if payment_error is not None:
            self.payment_error = payment_error

    @property
    def code(self):
        """Gets the code of this RedeemVoucherError.  # noqa: E501

        Possible errors when redeeming a voucher Possible values are: * notAllowedForUser: This user cannot redeem this voucher * notAllowedForVoucher: This voucher cannot be redeemed * notAllowedToday: This voucher cannot be redeemed today  * notAllowedYet: The redeem period for this voucher has not arrived yet * payment: There was an error when performing the payment * unexpected: An unexpected error has occurred. See the `exceptionType` and `exceptionMessage` fields for the internal information. * userBlocked: The user has been blocked by exceeding redeem tries   # noqa: E501

        :return: The code of this RedeemVoucherError.  # noqa: E501
        :rtype: RedeemVoucherErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RedeemVoucherError.

        Possible errors when redeeming a voucher Possible values are: * notAllowedForUser: This user cannot redeem this voucher * notAllowedForVoucher: This voucher cannot be redeemed * notAllowedToday: This voucher cannot be redeemed today  * notAllowedYet: The redeem period for this voucher has not arrived yet * payment: There was an error when performing the payment * unexpected: An unexpected error has occurred. See the `exceptionType` and `exceptionMessage` fields for the internal information. * userBlocked: The user has been blocked by exceeding redeem tries   # noqa: E501

        :param code: The code of this RedeemVoucherError.  # noqa: E501
        :type: RedeemVoucherErrorCode
        """

        self._code = code

    @property
    def voucher_status(self):
        """Gets the voucher_status of this RedeemVoucherError.  # noqa: E501

        Only if `code` is `notAllowedForVoucher` Possible values are: * canceled: The voucher was canceled, and cannot be further used * expired: The voucher has expired without being redeemed * open: The voucher has been generated / bought, and is open * pending: The voucher has been bought, and the corresponding payment is pending for authorization * redeemed: The voucher has been redeemed, and the corresponding payment was done   # noqa: E501

        :return: The voucher_status of this RedeemVoucherError.  # noqa: E501
        :rtype: VoucherStatusEnum
        """
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, voucher_status):
        """Sets the voucher_status of this RedeemVoucherError.

        Only if `code` is `notAllowedForVoucher` Possible values are: * canceled: The voucher was canceled, and cannot be further used * expired: The voucher has expired without being redeemed * open: The voucher has been generated / bought, and is open * pending: The voucher has been bought, and the corresponding payment is pending for authorization * redeemed: The voucher has been redeemed, and the corresponding payment was done   # noqa: E501

        :param voucher_status: The voucher_status of this RedeemVoucherError.  # noqa: E501
        :type: VoucherStatusEnum
        """

        self._voucher_status = voucher_status

    @property
    def allowed_days(self):
        """Gets the allowed_days of this RedeemVoucherError.  # noqa: E501

        Only if `code` is `notAllowedToday` Possibles values for each array element are: * fri: Friday * mon: Monday * sat: Saturday * sun: Sunday * thu: Thursday * tue: Tuesday * wed: Wednesday   # noqa: E501

        :return: The allowed_days of this RedeemVoucherError.  # noqa: E501
        :rtype: list[WeekDayEnum]
        """
        return self._allowed_days

    @allowed_days.setter
    def allowed_days(self, allowed_days):
        """Sets the allowed_days of this RedeemVoucherError.

        Only if `code` is `notAllowedToday` Possibles values for each array element are: * fri: Friday * mon: Monday * sat: Saturday * sun: Sunday * thu: Thursday * tue: Tuesday * wed: Wednesday   # noqa: E501

        :param allowed_days: The allowed_days of this RedeemVoucherError.  # noqa: E501
        :type: list[WeekDayEnum]
        """

        self._allowed_days = allowed_days

    @property
    def redeem_after_date(self):
        """Gets the redeem_after_date of this RedeemVoucherError.  # noqa: E501

        Indicates the date after which this voucher can be redeemed. Only if `code` is `notAllowedYet`.   # noqa: E501

        :return: The redeem_after_date of this RedeemVoucherError.  # noqa: E501
        :rtype: datetime
        """
        return self._redeem_after_date

    @redeem_after_date.setter
    def redeem_after_date(self, redeem_after_date):
        """Sets the redeem_after_date of this RedeemVoucherError.

        Indicates the date after which this voucher can be redeemed. Only if `code` is `notAllowedYet`.   # noqa: E501

        :param redeem_after_date: The redeem_after_date of this RedeemVoucherError.  # noqa: E501
        :type: datetime
        """

        self._redeem_after_date = redeem_after_date

    @property
    def payment_error(self):
        """Gets the payment_error of this RedeemVoucherError.  # noqa: E501

        The `PaymentError` generated when the voucher payment was being created. Only if `code` is `payment`.   # noqa: E501

        :return: The payment_error of this RedeemVoucherError.  # noqa: E501
        :rtype: PaymentError
        """
        return self._payment_error

    @payment_error.setter
    def payment_error(self, payment_error):
        """Sets the payment_error of this RedeemVoucherError.

        The `PaymentError` generated when the voucher payment was being created. Only if `code` is `payment`.   # noqa: E501

        :param payment_error: The payment_error of this RedeemVoucherError.  # noqa: E501
        :type: PaymentError
        """

        self._payment_error = payment_error

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
        if issubclass(RedeemVoucherError, dict):
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
        if not isinstance(other, RedeemVoucherError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RedeemVoucherError):
            return True

        return self.to_dict() != other.to_dict()
