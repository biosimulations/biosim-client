"""
biosim-server

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import unittest

from biosim_client.api.biosim.models.hdf5_attribute import HDF5Attribute


class TestHDF5Attribute(unittest.TestCase):
    """HDF5Attribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HDF5Attribute:
        """Test HDF5Attribute
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `HDF5Attribute`
        """
        model = HDF5Attribute()
        if include_optional:
            return HDF5Attribute(
                key = '',
                value = None
            )
        else:
            return HDF5Attribute(
                key = '',
                value = None,
        )
        """

    def testHDF5Attribute(self):
        """Test HDF5Attribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
