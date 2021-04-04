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


class ImageConfigurationForUserProfile(object):
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
        'manage': 'bool',
        'availability': 'AvailabilityEnum',
        'max_images': 'int'
    }

    attribute_map = {
        'manage': 'manage',
        'availability': 'availability',
        'max_images': 'maxImages'
    }

    def __init__(self, manage=None, availability=None, max_images=None, _configuration=None):  # noqa: E501
        """ImageConfigurationForUserProfile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._manage = None
        self._availability = None
        self._max_images = None
        self.discriminator = None

        if manage is not None:
            self.manage = manage
        if availability is not None:
            self.availability = availability
        if max_images is not None:
            self.max_images = max_images

    @property
    def manage(self):
        """Gets the manage of this ImageConfigurationForUserProfile.  # noqa: E501

        Can the authenticated user has permission to manage images?   # noqa: E501

        :return: The manage of this ImageConfigurationForUserProfile.  # noqa: E501
        :rtype: bool
        """
        return self._manage

    @manage.setter
    def manage(self, manage):
        """Sets the manage of this ImageConfigurationForUserProfile.

        Can the authenticated user has permission to manage images?   # noqa: E501

        :param manage: The manage of this ImageConfigurationForUserProfile.  # noqa: E501
        :type: bool
        """

        self._manage = manage

    @property
    def availability(self):
        """Gets the availability of this ImageConfigurationForUserProfile.  # noqa: E501

        The availability for images Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required   # noqa: E501

        :return: The availability of this ImageConfigurationForUserProfile.  # noqa: E501
        :rtype: AvailabilityEnum
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this ImageConfigurationForUserProfile.

        The availability for images Possible values are: * disabled: The data is disabled * optional: The data is enabled and optional * required: The data is enabled and required   # noqa: E501

        :param availability: The availability of this ImageConfigurationForUserProfile.  # noqa: E501
        :type: AvailabilityEnum
        """

        self._availability = availability

    @property
    def max_images(self):
        """Gets the max_images of this ImageConfigurationForUserProfile.  # noqa: E501

        The maximum allowed number of profile images  # noqa: E501

        :return: The max_images of this ImageConfigurationForUserProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_images

    @max_images.setter
    def max_images(self, max_images):
        """Sets the max_images of this ImageConfigurationForUserProfile.

        The maximum allowed number of profile images  # noqa: E501

        :param max_images: The max_images of this ImageConfigurationForUserProfile.  # noqa: E501
        :type: int
        """

        self._max_images = max_images

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
        if issubclass(ImageConfigurationForUserProfile, dict):
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
        if not isinstance(other, ImageConfigurationForUserProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageConfigurationForUserProfile):
            return True

        return self.to_dict() != other.to_dict()
