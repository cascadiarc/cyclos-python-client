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


class UserQueryFilters(object):
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
        'ignore_profile_fields_in_list': 'bool',
        'exclude_contacts': 'bool',
        'statuses': 'list[UserStatusEnum]',
        'roles': 'list[RoleEnum]',
        'order_by': 'UserOrderByEnum'
    }

    attribute_map = {
        'ignore_profile_fields_in_list': 'ignoreProfileFieldsInList',
        'exclude_contacts': 'excludeContacts',
        'statuses': 'statuses',
        'roles': 'roles',
        'order_by': 'orderBy'
    }

    def __init__(self, ignore_profile_fields_in_list=None, exclude_contacts=None, statuses=None, roles=None, order_by=None, _configuration=None):  # noqa: E501
        """UserQueryFilters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ignore_profile_fields_in_list = None
        self._exclude_contacts = None
        self._statuses = None
        self._roles = None
        self._order_by = None
        self.discriminator = None

        if ignore_profile_fields_in_list is not None:
            self.ignore_profile_fields_in_list = ignore_profile_fields_in_list
        if exclude_contacts is not None:
            self.exclude_contacts = exclude_contacts
        if statuses is not None:
            self.statuses = statuses
        if roles is not None:
            self.roles = roles
        if order_by is not None:
            self.order_by = order_by

    @property
    def ignore_profile_fields_in_list(self):
        """Gets the ignore_profile_fields_in_list of this UserQueryFilters.  # noqa: E501

        When set to `true`, instead of returning users with corresponding profile fields set on list, will return them with `display` and `shortDisplay`.    # noqa: E501

        :return: The ignore_profile_fields_in_list of this UserQueryFilters.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_profile_fields_in_list

    @ignore_profile_fields_in_list.setter
    def ignore_profile_fields_in_list(self, ignore_profile_fields_in_list):
        """Sets the ignore_profile_fields_in_list of this UserQueryFilters.

        When set to `true`, instead of returning users with corresponding profile fields set on list, will return them with `display` and `shortDisplay`.    # noqa: E501

        :param ignore_profile_fields_in_list: The ignore_profile_fields_in_list of this UserQueryFilters.  # noqa: E501
        :type: bool
        """

        self._ignore_profile_fields_in_list = ignore_profile_fields_in_list

    @property
    def exclude_contacts(self):
        """Gets the exclude_contacts of this UserQueryFilters.  # noqa: E501

        When set to `true` will not return any user that is already a contact of the currently authenticated user.   # noqa: E501

        :return: The exclude_contacts of this UserQueryFilters.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_contacts

    @exclude_contacts.setter
    def exclude_contacts(self, exclude_contacts):
        """Sets the exclude_contacts of this UserQueryFilters.

        When set to `true` will not return any user that is already a contact of the currently authenticated user.   # noqa: E501

        :param exclude_contacts: The exclude_contacts of this UserQueryFilters.  # noqa: E501
        :type: bool
        """

        self._exclude_contacts = exclude_contacts

    @property
    def statuses(self):
        """Gets the statuses of this UserQueryFilters.  # noqa: E501

        The possible statuses for an user Possibles values for each array element are: * active: The user is active and can use the system normally. * blocked: The user has been blocked from accessing the system. Other users still see him/her. * disabled: The user has been disabled - he/she cannot access the system and is invisible by other users. * pending: The user registration is pending a confirmation. Probably the user has received an e-mail with a link that must be followed to complete the activation. The user is invisible by other users. * purged: The user was permanently removed and had all his private data removed. Only transactions are kept for historical reasons. * removed: The user was permanently removed. It's profile is kept for historical purposes.   # noqa: E501

        :return: The statuses of this UserQueryFilters.  # noqa: E501
        :rtype: list[UserStatusEnum]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this UserQueryFilters.

        The possible statuses for an user Possibles values for each array element are: * active: The user is active and can use the system normally. * blocked: The user has been blocked from accessing the system. Other users still see him/her. * disabled: The user has been disabled - he/she cannot access the system and is invisible by other users. * pending: The user registration is pending a confirmation. Probably the user has received an e-mail with a link that must be followed to complete the activation. The user is invisible by other users. * purged: The user was permanently removed and had all his private data removed. Only transactions are kept for historical reasons. * removed: The user was permanently removed. It's profile is kept for historical purposes.   # noqa: E501

        :param statuses: The statuses of this UserQueryFilters.  # noqa: E501
        :type: list[UserStatusEnum]
        """

        self._statuses = statuses

    @property
    def roles(self):
        """Gets the roles of this UserQueryFilters.  # noqa: E501

        The main role the user has. Possibles values for each array element are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \"sub-user\" created by a member to manage his data.   # noqa: E501

        :return: The roles of this UserQueryFilters.  # noqa: E501
        :rtype: list[RoleEnum]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserQueryFilters.

        The main role the user has. Possibles values for each array element are: * administrator: A user who can manage the system and other users. * broker: A user who can manage other users. * member: A regular user who can manage operators.  * operator: A \"sub-user\" created by a member to manage his data.   # noqa: E501

        :param roles: The roles of this UserQueryFilters.  # noqa: E501
        :type: list[RoleEnum]
        """

        self._roles = roles

    @property
    def order_by(self):
        """Gets the order_by of this UserQueryFilters.  # noqa: E501

        Possible options for ordering the results of an user search. Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * creationDate: Newly registered users are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * random: Users will be randomly returned * relevance: This is the default if keywords are used. Best matching users come first.   # noqa: E501

        :return: The order_by of this UserQueryFilters.  # noqa: E501
        :rtype: UserOrderByEnum
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this UserQueryFilters.

        Possible options for ordering the results of an user search. Possible values are: * alphabeticallyAsc: Users are ordered by name (or whatever field is set to format users) in ascending order. * alphabeticallyDesc: Users are ordered by name (or whatever field is set to format users) in descending order. * creationDate: Newly registered users are returned first. * distance: Only useful when providing a location, will return nearer advertisements first. * random: Users will be randomly returned * relevance: This is the default if keywords are used. Best matching users come first.   # noqa: E501

        :param order_by: The order_by of this UserQueryFilters.  # noqa: E501
        :type: UserOrderByEnum
        """

        self._order_by = order_by

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
        if issubclass(UserQueryFilters, dict):
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
        if not isinstance(other, UserQueryFilters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserQueryFilters):
            return True

        return self.to_dict() != other.to_dict()