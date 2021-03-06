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


class NotificationTypeEnum(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ADAUTHORIZED = "adAuthorized"
    ADEXPIRED = "adExpired"
    ADINTERESTNOTIFICATION = "adInterestNotification"
    ADPENDINGAUTHORIZATION = "adPendingAuthorization"
    ADPENDINGBYADMINAUTHORIZATION = "adPendingByAdminAuthorization"
    ADQUESTIONANSWERED = "adQuestionAnswered"
    ADQUESTIONCREATED = "adQuestionCreated"
    ADREJECTED = "adRejected"
    ALLNONSMSPERFORMEDPAYMENTS = "allNonSmsPerformedPayments"
    APPLICATIONERROR = "applicationError"
    ARTICLEOUTOFSTOCK = "articleOutOfStock"
    AUTHORIZEDPAYMENTCANCELED = "authorizedPaymentCanceled"
    AUTHORIZEDPAYMENTDENIED = "authorizedPaymentDenied"
    AUTHORIZEDPAYMENTSUCCEEDED = "authorizedPaymentSucceeded"
    BOUGHTVOUCHERSABOUTTOEXPIRE = "boughtVouchersAboutToExpire"
    BOUGHTVOUCHERSEXPIRATIONDATECHANGED = "boughtVouchersExpirationDateChanged"
    BOUGHTVOUCHERSEXPIRED = "boughtVouchersExpired"
    BROKERASSIGNED = "brokerAssigned"
    BROKERUNASSIGNED = "brokerUnassigned"
    EXTERNALPAYMENTEXPIRED = "externalPaymentExpired"
    EXTERNALPAYMENTPERFORMEDFAILED = "externalPaymentPerformedFailed"
    EXTERNALPAYMENTRECEIVEDFAILED = "externalPaymentReceivedFailed"
    EXTERNALUSERPAYMENTEXPIRED = "externalUserPaymentExpired"
    EXTERNALUSERPAYMENTPERFORMEDFAILED = "externalUserPaymentPerformedFailed"
    FEEDBACKCHANGED = "feedbackChanged"
    FEEDBACKCREATED = "feedbackCreated"
    FEEDBACKEXPIRATIONREMINDER = "feedbackExpirationReminder"
    FEEDBACKOPTIONAL = "feedbackOptional"
    FEEDBACKREPLYCREATED = "feedbackReplyCreated"
    FEEDBACKREQUIRED = "feedbackRequired"
    GENERATEDVOUCHERSABOUTTOEXPIRE = "generatedVouchersAboutToExpire"
    GENERATEDVOUCHERSEXPIRED = "generatedVouchersExpired"
    INCOMINGRECURRINGPAYMENTCANCELED = "incomingRecurringPaymentCanceled"
    INCOMINGRECURRINGPAYMENTFAILED = "incomingRecurringPaymentFailed"
    INCOMINGRECURRINGPAYMENTRECEIVED = "incomingRecurringPaymentReceived"
    INCOMINGSCHEDULEDPAYMENTCANCELED = "incomingScheduledPaymentCanceled"
    INCOMINGSCHEDULEDPAYMENTFAILED = "incomingScheduledPaymentFailed"
    INCOMINGSCHEDULEDPAYMENTRECEIVED = "incomingScheduledPaymentReceived"
    LIMITCHANGE = "limitChange"
    LOWSTOCKQUANTITY = "lowStockQuantity"
    MAXSMSPERMONTHREACHED = "maxSmsPerMonthReached"
    MEMBERASSIGNED = "memberAssigned"
    MEMBERUNASSIGNED = "memberUnassigned"
    NETWORKCREATED = "networkCreated"
    NEWTOKEN = "newToken"
    NEWTOKENPENDINGACTIVATION = "newTokenPendingActivation"
    OPERATORAUTHORIZEDPAYMENTAPPROVEDSTILLPENDING = "operatorAuthorizedPaymentApprovedStillPending"
    OPERATORAUTHORIZEDPAYMENTCANCELED = "operatorAuthorizedPaymentCanceled"
    OPERATORAUTHORIZEDPAYMENTDENIED = "operatorAuthorizedPaymentDenied"
    OPERATORAUTHORIZEDPAYMENTSUCCEEDED = "operatorAuthorizedPaymentSucceeded"
    OPERATORPAYMENTAWAITINGAUTHORIZATION = "operatorPaymentAwaitingAuthorization"
    ORDERCANCELEDBUYER = "orderCanceledBuyer"
    ORDERCANCELEDSELLER = "orderCanceledSeller"
    ORDERCREATED = "orderCreated"
    ORDERPAYMENTCANCELEDBUYER = "orderPaymentCanceledBuyer"
    ORDERPAYMENTCANCELEDSELLER = "orderPaymentCanceledSeller"
    ORDERPAYMENTDENIEDBUYER = "orderPaymentDeniedBuyer"
    ORDERPAYMENTDENIEDSELLER = "orderPaymentDeniedSeller"
    ORDERPENDINGAUTHORIZATIONBUYER = "orderPendingAuthorizationBuyer"
    ORDERPENDINGAUTHORIZATIONSELLER = "orderPendingAuthorizationSeller"
    ORDERPENDINGBUYER = "orderPendingBuyer"
    ORDERPENDINGDELIVERYDATABUYER = "orderPendingDeliveryDataBuyer"
    ORDERPENDINGDELIVERYDATASELLER = "orderPendingDeliveryDataSeller"
    ORDERREALIZEDBUYER = "orderRealizedBuyer"
    ORDERREALIZEDSELLER = "orderRealizedSeller"
    ORDERREJECTEDBYBUYER = "orderRejectedByBuyer"
    ORDERREJECTEDBYSELLER = "orderRejectedBySeller"
    PASSWORDSTATUSCHANGED = "passwordStatusChanged"
    PAYMENTAWAITINGADMINAUTHORIZATION = "paymentAwaitingAdminAuthorization"
    PAYMENTAWAITINGAUTHORIZATION = "paymentAwaitingAuthorization"
    PAYMENTPERFORMED = "paymentPerformed"
    PAYMENTRECEIVED = "paymentReceived"
    PAYMENTREQUESTCANCELED = "paymentRequestCanceled"
    PAYMENTREQUESTDENIED = "paymentRequestDenied"
    PAYMENTREQUESTEXPIRATIONDATECHANGED = "paymentRequestExpirationDateChanged"
    PAYMENTREQUESTEXPIRED = "paymentRequestExpired"
    PAYMENTREQUESTPROCESSED = "paymentRequestProcessed"
    PAYMENTREQUESTRECEIVED = "paymentRequestReceived"
    RECURRINGPAYMENTFAILED = "recurringPaymentFailed"
    RECURRINGPAYMENTOCCURRENCEPROCESSED = "recurringPaymentOccurrenceProcessed"
    REFERENCECHANGED = "referenceChanged"
    REFERENCECREATED = "referenceCreated"
    SALEPENDINGBUYER = "salePendingBuyer"
    SALEREALIZEDBUYER = "saleRealizedBuyer"
    SALEREJECTEDSELLER = "saleRejectedSeller"
    SCHEDULEDPAYMENTFAILED = "scheduledPaymentFailed"
    SCHEDULEDPAYMENTINSTALLMENTPROCESSED = "scheduledPaymentInstallmentProcessed"
    SCHEDULEDPAYMENTREQUESTFAILED = "scheduledPaymentRequestFailed"
    SMSPERFORMEDPAYMENT = "smsPerformedPayment"
    SYSTEMALERT = "systemAlert"
    TICKETWEBHOOKFAILED = "ticketWebhookFailed"
    TOKENSTATUSCHANGED = "tokenStatusChanged"
    USERALERT = "userAlert"
    USERIMPORT = "userImport"
    USERREGISTRATION = "userRegistration"
    USERSTATUSCHANGED = "userStatusChanged"
    VOUCHERBUYINGABOUTTOEXPIRE = "voucherBuyingAboutToExpire"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self, _configuration=None):  # noqa: E501
        """NotificationTypeEnum - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration
        self.discriminator = None

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
        if issubclass(NotificationTypeEnum, dict):
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
        if not isinstance(other, NotificationTypeEnum):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationTypeEnum):
            return True

        return self.to_dict() != other.to_dict()
