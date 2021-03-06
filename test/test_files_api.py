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
from swagger_client.api.files_api import FilesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFilesApi(unittest.TestCase):
    """FilesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.files_api.FilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_raw_file(self):
        """Test case for delete_raw_file

        Removes a file by id  # noqa: E501
        """
        pass

    def test_get_raw_file_content(self):
        """Test case for get_raw_file_content

        Returns the content of a raw file (temp or custom field value)  # noqa: E501
        """
        pass

    def test_list_temp_files(self):
        """Test case for list_temp_files

        Lists temporary files related to the currently authenticated user or guest   # noqa: E501
        """
        pass

    def test_upload_temp_file(self):
        """Test case for upload_temp_file

        Adds a new temporary file for the currently authenticated user or guest.   # noqa: E501
        """
        pass

    def test_view_raw_file(self):
        """Test case for view_raw_file

        Returns a file details by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
