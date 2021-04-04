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


class FullProfileEditResult(object):
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
        'created_land_line_phones': 'list[str]',
        'created_mobile_phones': 'list[str]',
        'created_addresses': 'list[str]',
        'created_contact_infos': 'list[str]',
        'created_images': 'list[str]'
    }

    attribute_map = {
        'created_land_line_phones': 'createdLandLinePhones',
        'created_mobile_phones': 'createdMobilePhones',
        'created_addresses': 'createdAddresses',
        'created_contact_infos': 'createdContactInfos',
        'created_images': 'createdImages'
    }

    def __init__(self, created_land_line_phones=None, created_mobile_phones=None, created_addresses=None, created_contact_infos=None, created_images=None, _configuration=None):  # noqa: E501
        """FullProfileEditResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_land_line_phones = None
        self._created_mobile_phones = None
        self._created_addresses = None
        self._created_contact_infos = None
        self._created_images = None
        self.discriminator = None

        if created_land_line_phones is not None:
            self.created_land_line_phones = created_land_line_phones
        if created_mobile_phones is not None:
            self.created_mobile_phones = created_mobile_phones
        if created_addresses is not None:
            self.created_addresses = created_addresses
        if created_contact_infos is not None:
            self.created_contact_infos = created_contact_infos
        if created_images is not None:
            self.created_images = created_images

    @property
    def created_land_line_phones(self):
        """Gets the created_land_line_phones of this FullProfileEditResult.  # noqa: E501

        Identifiers of created land-line phones  # noqa: E501

        :return: The created_land_line_phones of this FullProfileEditResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._created_land_line_phones

    @created_land_line_phones.setter
    def created_land_line_phones(self, created_land_line_phones):
        """Sets the created_land_line_phones of this FullProfileEditResult.

        Identifiers of created land-line phones  # noqa: E501

        :param created_land_line_phones: The created_land_line_phones of this FullProfileEditResult.  # noqa: E501
        :type: list[str]
        """

        self._created_land_line_phones = created_land_line_phones

    @property
    def created_mobile_phones(self):
        """Gets the created_mobile_phones of this FullProfileEditResult.  # noqa: E501

        Identifiers of created mobile phones  # noqa: E501

        :return: The created_mobile_phones of this FullProfileEditResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._created_mobile_phones

    @created_mobile_phones.setter
    def created_mobile_phones(self, created_mobile_phones):
        """Sets the created_mobile_phones of this FullProfileEditResult.

        Identifiers of created mobile phones  # noqa: E501

        :param created_mobile_phones: The created_mobile_phones of this FullProfileEditResult.  # noqa: E501
        :type: list[str]
        """

        self._created_mobile_phones = created_mobile_phones

    @property
    def created_addresses(self):
        """Gets the created_addresses of this FullProfileEditResult.  # noqa: E501

        Identifiers of created addresses  # noqa: E501

        :return: The created_addresses of this FullProfileEditResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._created_addresses

    @created_addresses.setter
    def created_addresses(self, created_addresses):
        """Sets the created_addresses of this FullProfileEditResult.

        Identifiers of created addresses  # noqa: E501

        :param created_addresses: The created_addresses of this FullProfileEditResult.  # noqa: E501
        :type: list[str]
        """

        self._created_addresses = created_addresses

    @property
    def created_contact_infos(self):
        """Gets the created_contact_infos of this FullProfileEditResult.  # noqa: E501

        Identifiers of created additional contacts  # noqa: E501

        :return: The created_contact_infos of this FullProfileEditResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._created_contact_infos

    @created_contact_infos.setter
    def created_contact_infos(self, created_contact_infos):
        """Sets the created_contact_infos of this FullProfileEditResult.

        Identifiers of created additional contacts  # noqa: E501

        :param created_contact_infos: The created_contact_infos of this FullProfileEditResult.  # noqa: E501
        :type: list[str]
        """

        self._created_contact_infos = created_contact_infos

    @property
    def created_images(self):
        """Gets the created_images of this FullProfileEditResult.  # noqa: E501

        Identifiers of created profile images  # noqa: E501

        :return: The created_images of this FullProfileEditResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._created_images

    @created_images.setter
    def created_images(self, created_images):
        """Sets the created_images of this FullProfileEditResult.

        Identifiers of created profile images  # noqa: E501

        :param created_images: The created_images of this FullProfileEditResult.  # noqa: E501
        :type: list[str]
        """

        self._created_images = created_images

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
        if issubclass(FullProfileEditResult, dict):
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
        if not isinstance(other, FullProfileEditResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullProfileEditResult):
            return True

        return self.to_dict() != other.to_dict()
