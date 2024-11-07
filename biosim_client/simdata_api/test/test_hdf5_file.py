# coding: utf-8

"""
    simdata-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from biosim_client.simdata_api.models.hdf5_file import HDF5File

class TestHDF5File(unittest.TestCase):
    """HDF5File unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HDF5File:
        """Test HDF5File
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HDF5File`
        """
        model = HDF5File()
        if include_optional:
            return HDF5File(
                filename = '',
                id = '',
                uri = '',
                groups = [
                    biosim_client.simdata_api.models.hdf5_group.HDF5Group(
                        name = '', 
                        attributes = [
                            biosim_client.simdata_api.models.hdf5_attribute.HDF5Attribute(
                                key = '', 
                                value = null, )
                            ], 
                        datasets = [
                            biosim_client.simdata_api.models.hdf5_dataset.HDF5Dataset(
                                name = '', 
                                shape = [
                                    56
                                    ], 
                                attributes = [
                                    biosim_client.simdata_api.models.hdf5_attribute.HDF5Attribute(
                                        key = '', 
                                        value = null, )
                                    ], )
                            ], )
                    ]
            )
        else:
            return HDF5File(
                filename = '',
                id = '',
                uri = '',
                groups = [
                    biosim_client.simdata_api.models.hdf5_group.HDF5Group(
                        name = '', 
                        attributes = [
                            biosim_client.simdata_api.models.hdf5_attribute.HDF5Attribute(
                                key = '', 
                                value = null, )
                            ], 
                        datasets = [
                            biosim_client.simdata_api.models.hdf5_dataset.HDF5Dataset(
                                name = '', 
                                shape = [
                                    56
                                    ], 
                                attributes = [
                                    biosim_client.simdata_api.models.hdf5_attribute.HDF5Attribute(
                                        key = '', 
                                        value = null, )
                                    ], )
                            ], )
                    ],
        )
        """

    def testHDF5File(self):
        """Test HDF5File"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
