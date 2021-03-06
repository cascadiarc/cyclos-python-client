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


class FullProfileEdit(object):
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
        'user': 'UserEdit',
        'create_land_line_phones': 'list[PhoneNew]',
        'create_mobile_phones': 'list[PhoneNew]',
        'modify_land_line_phones': 'list[PhoneEditWithId]',
        'modify_mobile_phones': 'list[PhoneEditWithId]',
        'remove_phones': 'list[str]',
        'create_addresses': 'list[AddressNew]',
        'modify_addresses': 'list[AddressEditWithId]',
        'remove_addresses': 'list[str]',
        'create_contact_infos': 'list[ContactInfoNew]',
        'modify_contact_infos': 'list[ContactInfoEditWithId]',
        'remove_contact_infos': 'list[str]',
        'add_images': 'list[str]',
        'remove_images': 'list[str]',
        'reorder_images': 'list[str]'
    }

    attribute_map = {
        'user': 'user',
        'create_land_line_phones': 'createLandLinePhones',
        'create_mobile_phones': 'createMobilePhones',
        'modify_land_line_phones': 'modifyLandLinePhones',
        'modify_mobile_phones': 'modifyMobilePhones',
        'remove_phones': 'removePhones',
        'create_addresses': 'createAddresses',
        'modify_addresses': 'modifyAddresses',
        'remove_addresses': 'removeAddresses',
        'create_contact_infos': 'createContactInfos',
        'modify_contact_infos': 'modifyContactInfos',
        'remove_contact_infos': 'removeContactInfos',
        'add_images': 'addImages',
        'remove_images': 'removeImages',
        'reorder_images': 'reorderImages'
    }

    def __init__(self, user=None, create_land_line_phones=None, create_mobile_phones=None, modify_land_line_phones=None, modify_mobile_phones=None, remove_phones=None, create_addresses=None, modify_addresses=None, remove_addresses=None, create_contact_infos=None, modify_contact_infos=None, remove_contact_infos=None, add_images=None, remove_images=None, reorder_images=None, _configuration=None):  # noqa: E501
        """FullProfileEdit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user = None
        self._create_land_line_phones = None
        self._create_mobile_phones = None
        self._modify_land_line_phones = None
        self._modify_mobile_phones = None
        self._remove_phones = None
        self._create_addresses = None
        self._modify_addresses = None
        self._remove_addresses = None
        self._create_contact_infos = None
        self._modify_contact_infos = None
        self._remove_contact_infos = None
        self._add_images = None
        self._remove_images = None
        self._reorder_images = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if create_land_line_phones is not None:
            self.create_land_line_phones = create_land_line_phones
        if create_mobile_phones is not None:
            self.create_mobile_phones = create_mobile_phones
        if modify_land_line_phones is not None:
            self.modify_land_line_phones = modify_land_line_phones
        if modify_mobile_phones is not None:
            self.modify_mobile_phones = modify_mobile_phones
        if remove_phones is not None:
            self.remove_phones = remove_phones
        if create_addresses is not None:
            self.create_addresses = create_addresses
        if modify_addresses is not None:
            self.modify_addresses = modify_addresses
        if remove_addresses is not None:
            self.remove_addresses = remove_addresses
        if create_contact_infos is not None:
            self.create_contact_infos = create_contact_infos
        if modify_contact_infos is not None:
            self.modify_contact_infos = modify_contact_infos
        if remove_contact_infos is not None:
            self.remove_contact_infos = remove_contact_infos
        if add_images is not None:
            self.add_images = add_images
        if remove_images is not None:
            self.remove_images = remove_images
        if reorder_images is not None:
            self.reorder_images = reorder_images

    @property
    def user(self):
        """Gets the user of this FullProfileEdit.  # noqa: E501

        The basic fields. If null, the fields are not modified  # noqa: E501

        :return: The user of this FullProfileEdit.  # noqa: E501
        :rtype: UserEdit
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this FullProfileEdit.

        The basic fields. If null, the fields are not modified  # noqa: E501

        :param user: The user of this FullProfileEdit.  # noqa: E501
        :type: UserEdit
        """

        self._user = user

    @property
    def create_land_line_phones(self):
        """Gets the create_land_line_phones of this FullProfileEdit.  # noqa: E501

        Land-line phones to be created. If not sent / empty, no land-line phones are created.   # noqa: E501

        :return: The create_land_line_phones of this FullProfileEdit.  # noqa: E501
        :rtype: list[PhoneNew]
        """
        return self._create_land_line_phones

    @create_land_line_phones.setter
    def create_land_line_phones(self, create_land_line_phones):
        """Sets the create_land_line_phones of this FullProfileEdit.

        Land-line phones to be created. If not sent / empty, no land-line phones are created.   # noqa: E501

        :param create_land_line_phones: The create_land_line_phones of this FullProfileEdit.  # noqa: E501
        :type: list[PhoneNew]
        """

        self._create_land_line_phones = create_land_line_phones

    @property
    def create_mobile_phones(self):
        """Gets the create_mobile_phones of this FullProfileEdit.  # noqa: E501

        Mobile phones to be created. If not sent / empty, no mobile phones are created.   # noqa: E501

        :return: The create_mobile_phones of this FullProfileEdit.  # noqa: E501
        :rtype: list[PhoneNew]
        """
        return self._create_mobile_phones

    @create_mobile_phones.setter
    def create_mobile_phones(self, create_mobile_phones):
        """Sets the create_mobile_phones of this FullProfileEdit.

        Mobile phones to be created. If not sent / empty, no mobile phones are created.   # noqa: E501

        :param create_mobile_phones: The create_mobile_phones of this FullProfileEdit.  # noqa: E501
        :type: list[PhoneNew]
        """

        self._create_mobile_phones = create_mobile_phones

    @property
    def modify_land_line_phones(self):
        """Gets the modify_land_line_phones of this FullProfileEdit.  # noqa: E501

        Land-line phones to be modified. If not sent / empty, no land-line phones are modified   # noqa: E501

        :return: The modify_land_line_phones of this FullProfileEdit.  # noqa: E501
        :rtype: list[PhoneEditWithId]
        """
        return self._modify_land_line_phones

    @modify_land_line_phones.setter
    def modify_land_line_phones(self, modify_land_line_phones):
        """Sets the modify_land_line_phones of this FullProfileEdit.

        Land-line phones to be modified. If not sent / empty, no land-line phones are modified   # noqa: E501

        :param modify_land_line_phones: The modify_land_line_phones of this FullProfileEdit.  # noqa: E501
        :type: list[PhoneEditWithId]
        """

        self._modify_land_line_phones = modify_land_line_phones

    @property
    def modify_mobile_phones(self):
        """Gets the modify_mobile_phones of this FullProfileEdit.  # noqa: E501

        Mobile phones to be modified. If not sent / empty, no mobile phones are modified.   # noqa: E501

        :return: The modify_mobile_phones of this FullProfileEdit.  # noqa: E501
        :rtype: list[PhoneEditWithId]
        """
        return self._modify_mobile_phones

    @modify_mobile_phones.setter
    def modify_mobile_phones(self, modify_mobile_phones):
        """Sets the modify_mobile_phones of this FullProfileEdit.

        Mobile phones to be modified. If not sent / empty, no mobile phones are modified.   # noqa: E501

        :param modify_mobile_phones: The modify_mobile_phones of this FullProfileEdit.  # noqa: E501
        :type: list[PhoneEditWithId]
        """

        self._modify_mobile_phones = modify_mobile_phones

    @property
    def remove_phones(self):
        """Gets the remove_phones of this FullProfileEdit.  # noqa: E501

        Phones (both land-line and mobile) to be removed. If not sent / empty, no phones are removed.   # noqa: E501

        :return: The remove_phones of this FullProfileEdit.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_phones

    @remove_phones.setter
    def remove_phones(self, remove_phones):
        """Sets the remove_phones of this FullProfileEdit.

        Phones (both land-line and mobile) to be removed. If not sent / empty, no phones are removed.   # noqa: E501

        :param remove_phones: The remove_phones of this FullProfileEdit.  # noqa: E501
        :type: list[str]
        """

        self._remove_phones = remove_phones

    @property
    def create_addresses(self):
        """Gets the create_addresses of this FullProfileEdit.  # noqa: E501

        Addresses to be created. If not sent / empty, no  addresses are created.   # noqa: E501

        :return: The create_addresses of this FullProfileEdit.  # noqa: E501
        :rtype: list[AddressNew]
        """
        return self._create_addresses

    @create_addresses.setter
    def create_addresses(self, create_addresses):
        """Sets the create_addresses of this FullProfileEdit.

        Addresses to be created. If not sent / empty, no  addresses are created.   # noqa: E501

        :param create_addresses: The create_addresses of this FullProfileEdit.  # noqa: E501
        :type: list[AddressNew]
        """

        self._create_addresses = create_addresses

    @property
    def modify_addresses(self):
        """Gets the modify_addresses of this FullProfileEdit.  # noqa: E501

        Addresses to be modified. If not sent / empty, no  addresses are modified.   # noqa: E501

        :return: The modify_addresses of this FullProfileEdit.  # noqa: E501
        :rtype: list[AddressEditWithId]
        """
        return self._modify_addresses

    @modify_addresses.setter
    def modify_addresses(self, modify_addresses):
        """Sets the modify_addresses of this FullProfileEdit.

        Addresses to be modified. If not sent / empty, no  addresses are modified.   # noqa: E501

        :param modify_addresses: The modify_addresses of this FullProfileEdit.  # noqa: E501
        :type: list[AddressEditWithId]
        """

        self._modify_addresses = modify_addresses

    @property
    def remove_addresses(self):
        """Gets the remove_addresses of this FullProfileEdit.  # noqa: E501

        Addresses to be removed. If not sent / empty, no addresses are removed.   # noqa: E501

        :return: The remove_addresses of this FullProfileEdit.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_addresses

    @remove_addresses.setter
    def remove_addresses(self, remove_addresses):
        """Sets the remove_addresses of this FullProfileEdit.

        Addresses to be removed. If not sent / empty, no addresses are removed.   # noqa: E501

        :param remove_addresses: The remove_addresses of this FullProfileEdit.  # noqa: E501
        :type: list[str]
        """

        self._remove_addresses = remove_addresses

    @property
    def create_contact_infos(self):
        """Gets the create_contact_infos of this FullProfileEdit.  # noqa: E501

        Additional contacts to be created. If not sent / empty, no additional contacts are created.   # noqa: E501

        :return: The create_contact_infos of this FullProfileEdit.  # noqa: E501
        :rtype: list[ContactInfoNew]
        """
        return self._create_contact_infos

    @create_contact_infos.setter
    def create_contact_infos(self, create_contact_infos):
        """Sets the create_contact_infos of this FullProfileEdit.

        Additional contacts to be created. If not sent / empty, no additional contacts are created.   # noqa: E501

        :param create_contact_infos: The create_contact_infos of this FullProfileEdit.  # noqa: E501
        :type: list[ContactInfoNew]
        """

        self._create_contact_infos = create_contact_infos

    @property
    def modify_contact_infos(self):
        """Gets the modify_contact_infos of this FullProfileEdit.  # noqa: E501

        Additional contacts to be modified. If not sent / empty, no  additional contacts are modified.   # noqa: E501

        :return: The modify_contact_infos of this FullProfileEdit.  # noqa: E501
        :rtype: list[ContactInfoEditWithId]
        """
        return self._modify_contact_infos

    @modify_contact_infos.setter
    def modify_contact_infos(self, modify_contact_infos):
        """Sets the modify_contact_infos of this FullProfileEdit.

        Additional contacts to be modified. If not sent / empty, no  additional contacts are modified.   # noqa: E501

        :param modify_contact_infos: The modify_contact_infos of this FullProfileEdit.  # noqa: E501
        :type: list[ContactInfoEditWithId]
        """

        self._modify_contact_infos = modify_contact_infos

    @property
    def remove_contact_infos(self):
        """Gets the remove_contact_infos of this FullProfileEdit.  # noqa: E501

        Additional contacts to be removed. If not sent / empty, no additional contacts are removed.   # noqa: E501

        :return: The remove_contact_infos of this FullProfileEdit.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_contact_infos

    @remove_contact_infos.setter
    def remove_contact_infos(self, remove_contact_infos):
        """Sets the remove_contact_infos of this FullProfileEdit.

        Additional contacts to be removed. If not sent / empty, no additional contacts are removed.   # noqa: E501

        :param remove_contact_infos: The remove_contact_infos of this FullProfileEdit.  # noqa: E501
        :type: list[str]
        """

        self._remove_contact_infos = remove_contact_infos

    @property
    def add_images(self):
        """Gets the add_images of this FullProfileEdit.  # noqa: E501

        Identifiers of previously uploaded temporary images to be added as profile images. If not sent / empty, no images are added.   # noqa: E501

        :return: The add_images of this FullProfileEdit.  # noqa: E501
        :rtype: list[str]
        """
        return self._add_images

    @add_images.setter
    def add_images(self, add_images):
        """Sets the add_images of this FullProfileEdit.

        Identifiers of previously uploaded temporary images to be added as profile images. If not sent / empty, no images are added.   # noqa: E501

        :param add_images: The add_images of this FullProfileEdit.  # noqa: E501
        :type: list[str]
        """

        self._add_images = add_images

    @property
    def remove_images(self):
        """Gets the remove_images of this FullProfileEdit.  # noqa: E501

        Identifiers of existing profile images to be removed. If not sent / empty, no images are removed.   # noqa: E501

        :return: The remove_images of this FullProfileEdit.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_images

    @remove_images.setter
    def remove_images(self, remove_images):
        """Sets the remove_images of this FullProfileEdit.

        Identifiers of existing profile images to be removed. If not sent / empty, no images are removed.   # noqa: E501

        :param remove_images: The remove_images of this FullProfileEdit.  # noqa: E501
        :type: list[str]
        """

        self._remove_images = remove_images

    @property
    def reorder_images(self):
        """Gets the reorder_images of this FullProfileEdit.  # noqa: E501

        Identifiers of either existing or added profile images in the order they should be listed.   # noqa: E501

        :return: The reorder_images of this FullProfileEdit.  # noqa: E501
        :rtype: list[str]
        """
        return self._reorder_images

    @reorder_images.setter
    def reorder_images(self, reorder_images):
        """Sets the reorder_images of this FullProfileEdit.

        Identifiers of either existing or added profile images in the order they should be listed.   # noqa: E501

        :param reorder_images: The reorder_images of this FullProfileEdit.  # noqa: E501
        :type: list[str]
        """

        self._reorder_images = reorder_images

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
        if issubclass(FullProfileEdit, dict):
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
        if not isinstance(other, FullProfileEdit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullProfileEdit):
            return True

        return self.to_dict() != other.to_dict()
