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


class UserContactInfosListData(object):
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
        'can_manage': 'bool',
        'can_create': 'bool',
        'max_contact_infos': 'int',
        'availability': 'AvailabilityEnum',
        'custom_fields': 'list[CustomFieldDetailed]',
        'contact_infos': 'list[ContactInfoResult]'
    }

    attribute_map = {
        'can_manage': 'canManage',
        'can_create': 'canCreate',
        'max_contact_infos': 'maxContactInfos',
        'availability': 'availability',
        'custom_fields': 'customFields',
        'contact_infos': 'contactInfos'
    }

    def __init__(self, can_manage=None, can_create=None, max_contact_infos=None, availability=None, custom_fields=None, contact_infos=None, _configuration=None):  # noqa: E501
        """UserContactInfosListData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._can_manage = None
        self._can_create = None
        self._max_contact_infos = None
        self._availability = None
        self._custom_fields = None
        self._contact_infos = None
        self.discriminator = None

        if can_manage is not None:
            self.can_manage = can_manage
        if can_create is not None:
            self.can_create = can_create
        if max_contact_infos is not None:
            self.max_contact_infos = max_contact_infos
        if availability is not None:
            self.availability = availability
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if contact_infos is not None:
            self.contact_infos = contact_infos

    @property
    def can_manage(self):
        """Gets the can_manage of this UserContactInfosListData.  # noqa: E501

        Indicates whether the additional contact informations can be managed by the authenticated user   # noqa: E501

        :return: The can_manage of this UserContactInfosListData.  # noqa: E501
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        """Sets the can_manage of this UserContactInfosListData.

        Indicates whether the additional contact informations can be managed by the authenticated user   # noqa: E501

        :param can_manage: The can_manage of this UserContactInfosListData.  # noqa: E501
        :type: bool
        """

        self._can_manage = can_manage

    @property
    def can_create(self):
        """Gets the can_create of this UserContactInfosListData.  # noqa: E501

        Indicates whether new additional contact informations can be created by the authenticated user   # noqa: E501

        :return: The can_create of this UserContactInfosListData.  # noqa: E501
        :rtype: bool
        """
        return self._can_create

    @can_create.setter
    def can_create(self, can_create):
        """Sets the can_create of this UserContactInfosListData.

        Indicates whether new additional contact informations can be created by the authenticated user   # noqa: E501

        :param can_create: The can_create of this UserContactInfosListData.  # noqa: E501
        :type: bool
        """

        self._can_create = can_create

    @property
    def max_contact_infos(self):
        """Gets the max_contact_infos of this UserContactInfosListData.  # noqa: E501

        Indicates the maximum number of additional contact informations the user can have   # noqa: E501

        :return: The max_contact_infos of this UserContactInfosListData.  # noqa: E501
        :rtype: int
        """
        return self._max_contact_infos

    @max_contact_infos.setter
    def max_contact_infos(self, max_contact_infos):
        """Sets the max_contact_infos of this UserContactInfosListData.

        Indicates the maximum number of additional contact informations the user can have   # noqa: E501

        :param max_contact_infos: The max_contact_infos of this UserContactInfosListData.  # noqa: E501
        :type: int
        """

        self._max_contact_infos = max_contact_infos

    @property
    def availability(self):
        """Gets the availability of this UserContactInfosListData.  # noqa: E501

        The availability for additional contacts Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required   # noqa: E501

        :return: The availability of this UserContactInfosListData.  # noqa: E501
        :rtype: AvailabilityEnum
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this UserContactInfosListData.

        The availability for additional contacts Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required   # noqa: E501

        :param availability: The availability of this UserContactInfosListData.  # noqa: E501
        :type: AvailabilityEnum
        """

        self._availability = availability

    @property
    def custom_fields(self):
        """Gets the custom_fields of this UserContactInfosListData.  # noqa: E501

        The list of additional contact informations custom fields  # noqa: E501

        :return: The custom_fields of this UserContactInfosListData.  # noqa: E501
        :rtype: list[CustomFieldDetailed]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this UserContactInfosListData.

        The list of additional contact informations custom fields  # noqa: E501

        :param custom_fields: The custom_fields of this UserContactInfosListData.  # noqa: E501
        :type: list[CustomFieldDetailed]
        """

        self._custom_fields = custom_fields

    @property
    def contact_infos(self):
        """Gets the contact_infos of this UserContactInfosListData.  # noqa: E501

        The additional contact information list  # noqa: E501

        :return: The contact_infos of this UserContactInfosListData.  # noqa: E501
        :rtype: list[ContactInfoResult]
        """
        return self._contact_infos

    @contact_infos.setter
    def contact_infos(self, contact_infos):
        """Sets the contact_infos of this UserContactInfosListData.

        The additional contact information list  # noqa: E501

        :param contact_infos: The contact_infos of this UserContactInfosListData.  # noqa: E501
        :type: list[ContactInfoResult]
        """

        self._contact_infos = contact_infos

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
        if issubclass(UserContactInfosListData, dict):
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
        if not isinstance(other, UserContactInfosListData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserContactInfosListData):
            return True

        return self.to_dict() != other.to_dict()