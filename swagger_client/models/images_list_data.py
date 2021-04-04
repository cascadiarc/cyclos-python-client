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


class ImagesListData(object):
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
        'max_images': 'int',
        'availability': 'AvailabilityEnum',
        'images': 'list[Image]'
    }

    attribute_map = {
        'can_manage': 'canManage',
        'can_create': 'canCreate',
        'max_images': 'maxImages',
        'availability': 'availability',
        'images': 'images'
    }

    def __init__(self, can_manage=None, can_create=None, max_images=None, availability=None, images=None, _configuration=None):  # noqa: E501
        """ImagesListData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._can_manage = None
        self._can_create = None
        self._max_images = None
        self._availability = None
        self._images = None
        self.discriminator = None

        if can_manage is not None:
            self.can_manage = can_manage
        if can_create is not None:
            self.can_create = can_create
        if max_images is not None:
            self.max_images = max_images
        if availability is not None:
            self.availability = availability
        if images is not None:
            self.images = images

    @property
    def can_manage(self):
        """Gets the can_manage of this ImagesListData.  # noqa: E501

        Does the authenticated user has permission to manage these images?   # noqa: E501

        :return: The can_manage of this ImagesListData.  # noqa: E501
        :rtype: bool
        """
        return self._can_manage

    @can_manage.setter
    def can_manage(self, can_manage):
        """Sets the can_manage of this ImagesListData.

        Does the authenticated user has permission to manage these images?   # noqa: E501

        :param can_manage: The can_manage of this ImagesListData.  # noqa: E501
        :type: bool
        """

        self._can_manage = can_manage

    @property
    def can_create(self):
        """Gets the can_create of this ImagesListData.  # noqa: E501

        Does the authenticated user has permission to create a new image?   # noqa: E501

        :return: The can_create of this ImagesListData.  # noqa: E501
        :rtype: bool
        """
        return self._can_create

    @can_create.setter
    def can_create(self, can_create):
        """Sets the can_create of this ImagesListData.

        Does the authenticated user has permission to create a new image?   # noqa: E501

        :param can_create: The can_create of this ImagesListData.  # noqa: E501
        :type: bool
        """

        self._can_create = can_create

    @property
    def max_images(self):
        """Gets the max_images of this ImagesListData.  # noqa: E501

        The maximum number of images allowed  # noqa: E501

        :return: The max_images of this ImagesListData.  # noqa: E501
        :rtype: int
        """
        return self._max_images

    @max_images.setter
    def max_images(self, max_images):
        """Sets the max_images of this ImagesListData.

        The maximum number of images allowed  # noqa: E501

        :param max_images: The max_images of this ImagesListData.  # noqa: E501
        :type: int
        """

        self._max_images = max_images

    @property
    def availability(self):
        """Gets the availability of this ImagesListData.  # noqa: E501

        The availability for images Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required   # noqa: E501

        :return: The availability of this ImagesListData.  # noqa: E501
        :rtype: AvailabilityEnum
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this ImagesListData.

        The availability for images Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required   # noqa: E501

        :param availability: The availability of this ImagesListData.  # noqa: E501
        :type: AvailabilityEnum
        """

        self._availability = availability

    @property
    def images(self):
        """Gets the images of this ImagesListData.  # noqa: E501

        The list of images  # noqa: E501

        :return: The images of this ImagesListData.  # noqa: E501
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ImagesListData.

        The list of images  # noqa: E501

        :param images: The images of this ImagesListData.  # noqa: E501
        :type: list[Image]
        """

        self._images = images

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
        if issubclass(ImagesListData, dict):
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
        if not isinstance(other, ImagesListData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImagesListData):
            return True

        return self.to_dict() != other.to_dict()
