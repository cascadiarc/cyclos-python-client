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
from swagger_client.api.recurring_payments_api import RecurringPaymentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRecurringPaymentsApi(unittest.TestCase):
    """RecurringPaymentsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.recurring_payments_api.RecurringPaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_recurring_payment(self):
        """Test case for cancel_recurring_payment

        Cancels a recurring payment.  # noqa: E501
        """
        pass

    def test_process_failed_recurring_payment_occurrence(self):
        """Test case for process_failed_recurring_payment_occurrence

        Processes a failed recurring payment occurrence.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
