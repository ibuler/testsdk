# coding: utf-8

"""
    Jumpserver API Docs

    Jumpserver Restful api docs  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@fit2cloud.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.ops_celery_api import OpsCeleryApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOpsCeleryApi(unittest.TestCase):
    """OpsCeleryApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.ops_celery_api.OpsCeleryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ops_v1_celery_task_log_read(self):
        """Test case for ops_v1_celery_task_log_read

        """
        pass

    def test_ops_v1_celery_task_result_read(self):
        """Test case for ops_v1_celery_task_result_read

        """
        pass


if __name__ == '__main__':
    unittest.main()