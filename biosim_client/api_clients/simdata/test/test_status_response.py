# coding: utf-8

"""
    simdata-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from biosim_client.api_clients.simdata.openapi_client.models.status_response import StatusResponse

class TestStatusResponse(unittest.TestCase):
    """StatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatusResponse:
        """Test StatusResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatusResponse`
        """
        model = StatusResponse()
        if include_optional:
            return StatusResponse(
                status = 'ok'
            )
        else:
            return StatusResponse(
                status = 'ok',
        )
        """

    def testStatusResponse(self):
        """Test StatusResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()