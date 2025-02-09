"""
simdata-api

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import unittest

from biosim_client.api.simdata.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_get_health(self) -> None:
        """Test case for get_health

        Health
        """
        pass

    def test_get_metadata(self) -> None:
        """Test case for get_metadata

        Hdf5 File Metadata
        """
        pass

    def test_get_modified(self) -> None:
        """Test case for get_modified

        Modified Datetime
        """
        pass

    def test_read_dataset(self) -> None:
        """Test case for read_dataset

        Read Dataset
        """
        pass

    def test_root_get(self) -> None:
        """Test case for root_get

        Root
        """
        pass


if __name__ == "__main__":
    unittest.main()
