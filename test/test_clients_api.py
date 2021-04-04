# coding: utf-8

"""
    Cyclos 4.11.5 API

    The REST API for Cyclos 4.11.5  # noqa: E501

    OpenAPI spec version: 4.11.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.clients_api import ClientsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestClientsApi(unittest.TestCase):
    """ClientsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.clients_api.ClientsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_client(self):
        """Test case for activate_client

        Activates an access client  # noqa: E501
        """
        pass

    def test_list_client_types_for_user(self):
        """Test case for list_client_types_for_user

        Returns the list of access clients types for a user  # noqa: E501
        """
        pass

    def test_unassign_client(self):
        """Test case for unassign_client

        Unassign (disconnects) an access client  # noqa: E501
        """
        pass

    def test_view_client(self):
        """Test case for view_client

        Returns details of an access client  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()