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


class AddressNew(object):
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
        'name': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'street': 'str',
        'building_number': 'str',
        'complement': 'str',
        'zip': 'str',
        'po_box': 'str',
        'neighborhood': 'str',
        'city': 'str',
        'region': 'str',
        'country': 'str',
        'location': 'GeographicalCoordinate',
        'default_address': 'bool',
        'hidden': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'street': 'street',
        'building_number': 'buildingNumber',
        'complement': 'complement',
        'zip': 'zip',
        'po_box': 'poBox',
        'neighborhood': 'neighborhood',
        'city': 'city',
        'region': 'region',
        'country': 'country',
        'location': 'location',
        'default_address': 'defaultAddress',
        'hidden': 'hidden'
    }

    def __init__(self, name=None, address_line1=None, address_line2=None, street=None, building_number=None, complement=None, zip=None, po_box=None, neighborhood=None, city=None, region=None, country=None, location=None, default_address=None, hidden=None, _configuration=None):  # noqa: E501
        """AddressNew - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._address_line1 = None
        self._address_line2 = None
        self._street = None
        self._building_number = None
        self._complement = None
        self._zip = None
        self._po_box = None
        self._neighborhood = None
        self._city = None
        self._region = None
        self._country = None
        self._location = None
        self._default_address = None
        self._hidden = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if street is not None:
            self.street = street
        if building_number is not None:
            self.building_number = building_number
        if complement is not None:
            self.complement = complement
        if zip is not None:
            self.zip = zip
        if po_box is not None:
            self.po_box = po_box
        if neighborhood is not None:
            self.neighborhood = neighborhood
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if country is not None:
            self.country = country
        if location is not None:
            self.location = location
        if default_address is not None:
            self.default_address = default_address
        if hidden is not None:
            self.hidden = hidden

    @property
    def name(self):
        """Gets the name of this AddressNew.  # noqa: E501

        The address name  # noqa: E501

        :return: The name of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddressNew.

        The address name  # noqa: E501

        :param name: The name of this AddressNew.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address_line1(self):
        """Gets the address_line1 of this AddressNew.  # noqa: E501

        The first line of the descriptive address   # noqa: E501

        :return: The address_line1 of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this AddressNew.

        The first line of the descriptive address   # noqa: E501

        :param address_line1: The address_line1 of this AddressNew.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this AddressNew.  # noqa: E501

        The second line of the descriptive address   # noqa: E501

        :return: The address_line2 of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this AddressNew.

        The second line of the descriptive address   # noqa: E501

        :param address_line2: The address_line2 of this AddressNew.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def street(self):
        """Gets the street of this AddressNew.  # noqa: E501

        The street name   # noqa: E501

        :return: The street of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this AddressNew.

        The street name   # noqa: E501

        :param street: The street of this AddressNew.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def building_number(self):
        """Gets the building_number of this AddressNew.  # noqa: E501

        The numeric identifier for a land parcel, house, building or other   # noqa: E501

        :return: The building_number of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._building_number

    @building_number.setter
    def building_number(self, building_number):
        """Sets the building_number of this AddressNew.

        The numeric identifier for a land parcel, house, building or other   # noqa: E501

        :param building_number: The building_number of this AddressNew.  # noqa: E501
        :type: str
        """

        self._building_number = building_number

    @property
    def complement(self):
        """Gets the complement of this AddressNew.  # noqa: E501

        The complement (like apartment number)     # noqa: E501

        :return: The complement of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._complement

    @complement.setter
    def complement(self, complement):
        """Sets the complement of this AddressNew.

        The complement (like apartment number)     # noqa: E501

        :param complement: The complement of this AddressNew.  # noqa: E501
        :type: str
        """

        self._complement = complement

    @property
    def zip(self):
        """Gets the zip of this AddressNew.  # noqa: E501

        A zip code that identifies a specific geographic (postal) delivery area   # noqa: E501

        :return: The zip of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this AddressNew.

        A zip code that identifies a specific geographic (postal) delivery area   # noqa: E501

        :param zip: The zip of this AddressNew.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def po_box(self):
        """Gets the po_box of this AddressNew.  # noqa: E501

        The post-office box, is an uniquely addressable box   # noqa: E501

        :return: The po_box of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._po_box

    @po_box.setter
    def po_box(self, po_box):
        """Sets the po_box of this AddressNew.

        The post-office box, is an uniquely addressable box   # noqa: E501

        :param po_box: The po_box of this AddressNew.  # noqa: E501
        :type: str
        """

        self._po_box = po_box

    @property
    def neighborhood(self):
        """Gets the neighborhood of this AddressNew.  # noqa: E501

        The neighborhood name    # noqa: E501

        :return: The neighborhood of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood):
        """Sets the neighborhood of this AddressNew.

        The neighborhood name    # noqa: E501

        :param neighborhood: The neighborhood of this AddressNew.  # noqa: E501
        :type: str
        """

        self._neighborhood = neighborhood

    @property
    def city(self):
        """Gets the city of this AddressNew.  # noqa: E501

        The city name   # noqa: E501

        :return: The city of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AddressNew.

        The city name   # noqa: E501

        :param city: The city of this AddressNew.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def region(self):
        """Gets the region of this AddressNew.  # noqa: E501

        The region or state   # noqa: E501

        :return: The region of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AddressNew.

        The region or state   # noqa: E501

        :param region: The region of this AddressNew.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def country(self):
        """Gets the country of this AddressNew.  # noqa: E501

        The country, represented as 2-letter, uppercase, ISO 3166-1 code   # noqa: E501

        :return: The country of this AddressNew.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddressNew.

        The country, represented as 2-letter, uppercase, ISO 3166-1 code   # noqa: E501

        :param country: The country of this AddressNew.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def location(self):
        """Gets the location of this AddressNew.  # noqa: E501

        The geolocation of the current address  # noqa: E501

        :return: The location of this AddressNew.  # noqa: E501
        :rtype: GeographicalCoordinate
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AddressNew.

        The geolocation of the current address  # noqa: E501

        :param location: The location of this AddressNew.  # noqa: E501
        :type: GeographicalCoordinate
        """

        self._location = location

    @property
    def default_address(self):
        """Gets the default_address of this AddressNew.  # noqa: E501

        Indicates whether this is the default address for the user  # noqa: E501

        :return: The default_address of this AddressNew.  # noqa: E501
        :rtype: bool
        """
        return self._default_address

    @default_address.setter
    def default_address(self, default_address):
        """Sets the default_address of this AddressNew.

        Indicates whether this is the default address for the user  # noqa: E501

        :param default_address: The default_address of this AddressNew.  # noqa: E501
        :type: bool
        """

        self._default_address = default_address

    @property
    def hidden(self):
        """Gets the hidden of this AddressNew.  # noqa: E501

        Whether this address should be hidden for other users  # noqa: E501

        :return: The hidden of this AddressNew.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this AddressNew.

        Whether this address should be hidden for other users  # noqa: E501

        :param hidden: The hidden of this AddressNew.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

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
        if issubclass(AddressNew, dict):
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
        if not isinstance(other, AddressNew):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressNew):
            return True

        return self.to_dict() != other.to_dict()
