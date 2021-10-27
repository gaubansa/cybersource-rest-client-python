# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.chargeback_details_api import ChargebackDetailsApi


class TestChargebackDetailsApi(unittest.TestCase):
    """ ChargebackDetailsApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.chargeback_details_api.ChargebackDetailsApi()

    def tearDown(self):
        pass

    def test_get_chargeback_details(self):
        """
        Test case for get_chargeback_details

        Get Chargeback Details
        """
        pass


if __name__ == '__main__':
    unittest.main()