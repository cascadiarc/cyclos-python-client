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
from swagger_client.api.validation_api import ValidationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestValidationApi(unittest.TestCase):
    """ValidationApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.validation_api.ValidationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_validate_email_change(self):
        """Test case for validate_email_change

        Validate a pending e-mail change.  # noqa: E501
        """
        pass

    def test_validate_user_registration(self):
        """Test case for validate_user_registration

        Validate a pending user registration.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
