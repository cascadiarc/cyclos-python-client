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


class DataForTransaction(object):
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
        'accounts': 'list[AccountWithStatus]',
        'from_kind': 'AccountKind',
        'from_user': 'User',
        'to_kind': 'AccountKind',
        'to_user': 'User',
        'payment_type_data': 'TransactionTypeData',
        'payment_types': 'list[TransferTypeWithCurrency]',
        'allow_autocomplete': 'bool',
        'allow_contacts': 'bool',
        'allowed_users': 'list[User]',
        'principal_types': 'list[PrincipalTypeInput]',
        'default_id_method': 'IdentificationMethodEnum',
        'default_principal_type': 'str'
    }

    attribute_map = {
        'accounts': 'accounts',
        'from_kind': 'fromKind',
        'from_user': 'fromUser',
        'to_kind': 'toKind',
        'to_user': 'toUser',
        'payment_type_data': 'paymentTypeData',
        'payment_types': 'paymentTypes',
        'allow_autocomplete': 'allowAutocomplete',
        'allow_contacts': 'allowContacts',
        'allowed_users': 'allowedUsers',
        'principal_types': 'principalTypes',
        'default_id_method': 'defaultIdMethod',
        'default_principal_type': 'defaultPrincipalType'
    }

    def __init__(self, accounts=None, from_kind=None, from_user=None, to_kind=None, to_user=None, payment_type_data=None, payment_types=None, allow_autocomplete=None, allow_contacts=None, allowed_users=None, principal_types=None, default_id_method=None, default_principal_type=None, _configuration=None):  # noqa: E501
        """DataForTransaction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accounts = None
        self._from_kind = None
        self._from_user = None
        self._to_kind = None
        self._to_user = None
        self._payment_type_data = None
        self._payment_types = None
        self._allow_autocomplete = None
        self._allow_contacts = None
        self._allowed_users = None
        self._principal_types = None
        self._default_id_method = None
        self._default_principal_type = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if from_kind is not None:
            self.from_kind = from_kind
        if from_user is not None:
            self.from_user = from_user
        if to_kind is not None:
            self.to_kind = to_kind
        if to_user is not None:
            self.to_user = to_user
        if payment_type_data is not None:
            self.payment_type_data = payment_type_data
        if payment_types is not None:
            self.payment_types = payment_types
        if allow_autocomplete is not None:
            self.allow_autocomplete = allow_autocomplete
        if allow_contacts is not None:
            self.allow_contacts = allow_contacts
        if allowed_users is not None:
            self.allowed_users = allowed_users
        if principal_types is not None:
            self.principal_types = principal_types
        if default_id_method is not None:
            self.default_id_method = default_id_method
        if default_principal_type is not None:
            self.default_principal_type = default_principal_type

    @property
    def accounts(self):
        """Gets the accounts of this DataForTransaction.  # noqa: E501

        Only returned when the payment type is not selected. Contains the possible accounts which can be used either as source (when performing the payment) or destination (when receiving the payment, on POS).   # noqa: E501

        :return: The accounts of this DataForTransaction.  # noqa: E501
        :rtype: list[AccountWithStatus]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this DataForTransaction.

        Only returned when the payment type is not selected. Contains the possible accounts which can be used either as source (when performing the payment) or destination (when receiving the payment, on POS).   # noqa: E501

        :param accounts: The accounts of this DataForTransaction.  # noqa: E501
        :type: list[AccountWithStatus]
        """

        self._accounts = accounts

    @property
    def from_kind(self):
        """Gets the from_kind of this DataForTransaction.  # noqa: E501

        Indicates the account kind that will perform the payment  # noqa: E501

        :return: The from_kind of this DataForTransaction.  # noqa: E501
        :rtype: AccountKind
        """
        return self._from_kind

    @from_kind.setter
    def from_kind(self, from_kind):
        """Sets the from_kind of this DataForTransaction.

        Indicates the account kind that will perform the payment  # noqa: E501

        :param from_kind: The from_kind of this DataForTransaction.  # noqa: E501
        :type: AccountKind
        """

        self._from_kind = from_kind

    @property
    def from_user(self):
        """Gets the from_user of this DataForTransaction.  # noqa: E501

        Only returned if `fromKind` is `user`. Is the payer user.   # noqa: E501

        :return: The from_user of this DataForTransaction.  # noqa: E501
        :rtype: User
        """
        return self._from_user

    @from_user.setter
    def from_user(self, from_user):
        """Sets the from_user of this DataForTransaction.

        Only returned if `fromKind` is `user`. Is the payer user.   # noqa: E501

        :param from_user: The from_user of this DataForTransaction.  # noqa: E501
        :type: User
        """

        self._from_user = from_user

    @property
    def to_kind(self):
        """Gets the to_kind of this DataForTransaction.  # noqa: E501

        Indicates the account kind that will receive the payment  # noqa: E501

        :return: The to_kind of this DataForTransaction.  # noqa: E501
        :rtype: AccountKind
        """
        return self._to_kind

    @to_kind.setter
    def to_kind(self, to_kind):
        """Sets the to_kind of this DataForTransaction.

        Indicates the account kind that will receive the payment  # noqa: E501

        :param to_kind: The to_kind of this DataForTransaction.  # noqa: E501
        :type: AccountKind
        """

        self._to_kind = to_kind

    @property
    def to_user(self):
        """Gets the to_user of this DataForTransaction.  # noqa: E501

        Only returned if `toKind` is `user`. Is the payee user.   # noqa: E501

        :return: The to_user of this DataForTransaction.  # noqa: E501
        :rtype: User
        """
        return self._to_user

    @to_user.setter
    def to_user(self, to_user):
        """Sets the to_user of this DataForTransaction.

        Only returned if `toKind` is `user`. Is the payee user.   # noqa: E501

        :param to_user: The to_user of this DataForTransaction.  # noqa: E501
        :type: User
        """

        self._to_user = to_user

    @property
    def payment_type_data(self):
        """Gets the payment_type_data of this DataForTransaction.  # noqa: E501

        Contains the detailed data for the selected (or first) payment type   # noqa: E501

        :return: The payment_type_data of this DataForTransaction.  # noqa: E501
        :rtype: TransactionTypeData
        """
        return self._payment_type_data

    @payment_type_data.setter
    def payment_type_data(self, payment_type_data):
        """Sets the payment_type_data of this DataForTransaction.

        Contains the detailed data for the selected (or first) payment type   # noqa: E501

        :param payment_type_data: The payment_type_data of this DataForTransaction.  # noqa: E501
        :type: TransactionTypeData
        """

        self._payment_type_data = payment_type_data

    @property
    def payment_types(self):
        """Gets the payment_types of this DataForTransaction.  # noqa: E501

        Only returned when the payment type is not selected. Contains the allowed payment types for a payment between the selected from and to owners.   # noqa: E501

        :return: The payment_types of this DataForTransaction.  # noqa: E501
        :rtype: list[TransferTypeWithCurrency]
        """
        return self._payment_types

    @payment_types.setter
    def payment_types(self, payment_types):
        """Sets the payment_types of this DataForTransaction.

        Only returned when the payment type is not selected. Contains the allowed payment types for a payment between the selected from and to owners.   # noqa: E501

        :param payment_types: The payment_types of this DataForTransaction.  # noqa: E501
        :type: list[TransferTypeWithCurrency]
        """

        self._payment_types = payment_types

    @property
    def allow_autocomplete(self):
        """Gets the allow_autocomplete of this DataForTransaction.  # noqa: E501

        Only returned when no subject is selected. Indicates whether the payee can be obtaining by freely searching users   # noqa: E501

        :return: The allow_autocomplete of this DataForTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._allow_autocomplete

    @allow_autocomplete.setter
    def allow_autocomplete(self, allow_autocomplete):
        """Sets the allow_autocomplete of this DataForTransaction.

        Only returned when no subject is selected. Indicates whether the payee can be obtaining by freely searching users   # noqa: E501

        :param allow_autocomplete: The allow_autocomplete of this DataForTransaction.  # noqa: E501
        :type: bool
        """

        self._allow_autocomplete = allow_autocomplete

    @property
    def allow_contacts(self):
        """Gets the allow_contacts of this DataForTransaction.  # noqa: E501

        Only returned when no subject is selected. Indicates whether the payee can be obtaining from the contact list   # noqa: E501

        :return: The allow_contacts of this DataForTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._allow_contacts

    @allow_contacts.setter
    def allow_contacts(self, allow_contacts):
        """Sets the allow_contacts of this DataForTransaction.

        Only returned when no subject is selected. Indicates whether the payee can be obtaining from the contact list   # noqa: E501

        :param allow_contacts: The allow_contacts of this DataForTransaction.  # noqa: E501
        :type: bool
        """

        self._allow_contacts = allow_contacts

    @property
    def allowed_users(self):
        """Gets the allowed_users of this DataForTransaction.  # noqa: E501

        If the authorized user is a restricted operator, it may be that the owner user has defined exactly to which users the operator can pay. If this is the case, this will be the list with such users.   # noqa: E501

        :return: The allowed_users of this DataForTransaction.  # noqa: E501
        :rtype: list[User]
        """
        return self._allowed_users

    @allowed_users.setter
    def allowed_users(self, allowed_users):
        """Sets the allowed_users of this DataForTransaction.

        If the authorized user is a restricted operator, it may be that the owner user has defined exactly to which users the operator can pay. If this is the case, this will be the list with such users.   # noqa: E501

        :param allowed_users: The allowed_users of this DataForTransaction.  # noqa: E501
        :type: list[User]
        """

        self._allowed_users = allowed_users

    @property
    def principal_types(self):
        """Gets the principal_types of this DataForTransaction.  # noqa: E501

        Only returned when no subject is selected. The possible principal types that can be used to locate the payee   # noqa: E501

        :return: The principal_types of this DataForTransaction.  # noqa: E501
        :rtype: list[PrincipalTypeInput]
        """
        return self._principal_types

    @principal_types.setter
    def principal_types(self, principal_types):
        """Sets the principal_types of this DataForTransaction.

        Only returned when no subject is selected. The possible principal types that can be used to locate the payee   # noqa: E501

        :param principal_types: The principal_types of this DataForTransaction.  # noqa: E501
        :type: list[PrincipalTypeInput]
        """

        self._principal_types = principal_types

    @property
    def default_id_method(self):
        """Gets the default_id_method of this DataForTransaction.  # noqa: E501

        Only returned when no subject is selected. The default option for the identification method when performing a payment. Possible values are: * autocomplete: The client application should search for an user and pass in the id * contacts: The client application should access the contact list of the authenticated user and pass the id * principalType: The client application should pass in an identification (principal) of the user, such as login name, e-mail and so on   # noqa: E501

        :return: The default_id_method of this DataForTransaction.  # noqa: E501
        :rtype: IdentificationMethodEnum
        """
        return self._default_id_method

    @default_id_method.setter
    def default_id_method(self, default_id_method):
        """Sets the default_id_method of this DataForTransaction.

        Only returned when no subject is selected. The default option for the identification method when performing a payment. Possible values are: * autocomplete: The client application should search for an user and pass in the id * contacts: The client application should access the contact list of the authenticated user and pass the id * principalType: The client application should pass in an identification (principal) of the user, such as login name, e-mail and so on   # noqa: E501

        :param default_id_method: The default_id_method of this DataForTransaction.  # noqa: E501
        :type: IdentificationMethodEnum
        """

        self._default_id_method = default_id_method

    @property
    def default_principal_type(self):
        """Gets the default_principal_type of this DataForTransaction.  # noqa: E501

        Only returned when no subject is selected. If the `defaultIdMethod` is `principalType`, contains the internal name or id of the principal type that should be the default. If there is a default, the user should be provided with the option to choose which principal type he's using. If there is no default, all possible principal types will be attempted. In this case, the UI will normally not show the option for which principal type should be used.   # noqa: E501

        :return: The default_principal_type of this DataForTransaction.  # noqa: E501
        :rtype: str
        """
        return self._default_principal_type

    @default_principal_type.setter
    def default_principal_type(self, default_principal_type):
        """Sets the default_principal_type of this DataForTransaction.

        Only returned when no subject is selected. If the `defaultIdMethod` is `principalType`, contains the internal name or id of the principal type that should be the default. If there is a default, the user should be provided with the option to choose which principal type he's using. If there is no default, all possible principal types will be attempted. In this case, the UI will normally not show the option for which principal type should be used.   # noqa: E501

        :param default_principal_type: The default_principal_type of this DataForTransaction.  # noqa: E501
        :type: str
        """

        self._default_principal_type = default_principal_type

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
        if issubclass(DataForTransaction, dict):
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
        if not isinstance(other, DataForTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForTransaction):
            return True

        return self.to_dict() != other.to_dict()