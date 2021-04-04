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
from swagger_client.api.pos_api import POSApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPOSApi(unittest.TestCase):
    """POSApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.pos_api.POSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_calculate_receive_payment_installments(self):
        """Test case for calculate_receive_payment_installments

        Calculates the default installments for a scheduled payment  # noqa: E501
        """
        pass

    def test_data_for_receive_payment(self):
        """Test case for data_for_receive_payment

        Returns configuration data for receiving a payment (POS)  # noqa: E501
        """
        pass

    def test_preview_receive_payment(self):
        """Test case for preview_receive_payment

        Previews a POS payment before receiving it  # noqa: E501
        """
        pass

    def test_receive_payment(self):
        """Test case for receive_payment

        Receives a payment (POS)  # noqa: E501
        """
        pass

    def test_receive_payment_otp(self):
        """Test case for receive_payment_otp

        Generates a new One-Time-Password (OTP) for a pos payment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()