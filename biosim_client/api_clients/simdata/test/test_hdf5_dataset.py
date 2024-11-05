# coding: utf-8

"""
    simdata-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from biosim_client.api_clients.simdata.openapi_client.models.hdf5_dataset import HDF5Dataset

class TestHDF5Dataset(unittest.TestCase):
    """HDF5Dataset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HDF5Dataset:
        """Test HDF5Dataset
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HDF5Dataset`
        """
        model = HDF5Dataset()
        if include_optional:
            return HDF5Dataset(
                name = '',
                shape = [
                    56
                    ],
                attributes = [
                    openapi_client.models.hdf5_attribute.HDF5Attribute(
                        key = '', 
                        value = null, )
                    ]
            )
        else:
            return HDF5Dataset(
                name = '',
                shape = [
                    56
                    ],
                attributes = [
                    openapi_client.models.hdf5_attribute.HDF5Attribute(
                        key = '', 
                        value = null, )
                    ],
        )
        """

    def testHDF5Dataset(self):
        """Test HDF5Dataset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()