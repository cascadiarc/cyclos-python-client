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


class AdCategoryWithChildren(object):
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
        'image': 'Image',
        'children': 'list[AdCategoryWithChildren]'
    }

    attribute_map = {
        'image': 'image',
        'children': 'children'
    }

    def __init__(self, image=None, children=None, _configuration=None):  # noqa: E501
        """AdCategoryWithChildren - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._image = None
        self._children = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if children is not None:
            self.children = children

    @property
    def image(self):
        """Gets the image of this AdCategoryWithChildren.  # noqa: E501

        The category image.  # noqa: E501

        :return: The image of this AdCategoryWithChildren.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AdCategoryWithChildren.

        The category image.  # noqa: E501

        :param image: The image of this AdCategoryWithChildren.  # noqa: E501
        :type: Image
        """

        self._image = image

    @property
    def children(self):
        """Gets the children of this AdCategoryWithChildren.  # noqa: E501

        The child categories  # noqa: E501

        :return: The children of this AdCategoryWithChildren.  # noqa: E501
        :rtype: list[AdCategoryWithChildren]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this AdCategoryWithChildren.

        The child categories  # noqa: E501

        :param children: The children of this AdCategoryWithChildren.  # noqa: E501
        :type: list[AdCategoryWithChildren]
        """

        self._children = children

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
        if issubclass(AdCategoryWithChildren, dict):
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
        if not isinstance(other, AdCategoryWithChildren):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdCategoryWithChildren):
            return True

        return self.to_dict() != other.to_dict()
