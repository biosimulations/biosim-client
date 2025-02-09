"""
biosim-server

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import unittest

from biosim_client.api.biosim.models.biosimulator_version import BiosimulatorVersion


class TestBiosimulatorVersion(unittest.TestCase):
    """BiosimulatorVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BiosimulatorVersion:
        """Test BiosimulatorVersion
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `BiosimulatorVersion`
        """
        model = BiosimulatorVersion()
        if include_optional:
            return BiosimulatorVersion(
                id = '',
                name = '',
                version = '',
                image_url = '',
                image_digest = '',
                created = '',
                updated = ''
            )
        else:
            return BiosimulatorVersion(
                id = '',
                name = '',
                version = '',
                image_url = '',
                image_digest = '',
                created = '',
                updated = '',
        )
        """

    def testBiosimulatorVersion(self):
        """Test BiosimulatorVersion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
