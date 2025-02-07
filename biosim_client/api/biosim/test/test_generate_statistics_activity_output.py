"""
biosim-server

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import unittest

from biosim_client.api.biosim.models.generate_statistics_activity_output import GenerateStatisticsActivityOutput


class TestGenerateStatisticsActivityOutput(unittest.TestCase):
    """GenerateStatisticsActivityOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenerateStatisticsActivityOutput:
        """Test GenerateStatisticsActivityOutput
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GenerateStatisticsActivityOutput`
        """
        model = GenerateStatisticsActivityOutput()
        if include_optional:
            return GenerateStatisticsActivityOutput(
                sims_run_info = [
                    biosim_client.api.biosim.models.simulation_run_info.SimulationRunInfo(
                        biosim_sim_run = biosim_client.api.biosim.models.biosim_simulation_run.BiosimSimulationRun(
                            id = '',
                            name = '',
                            simulator_version = biosim_client.api.biosim.models.biosimulator_version.BiosimulatorVersion(
                                id = '',
                                name = '',
                                version = '',
                                image_url = '',
                                image_digest = '',
                                created = '',
                                updated = '', ),
                            status = 'CREATED',
                            error_message = '', ),
                        hdf5_file = biosim_client.api.biosim.models.hdf5_file.HDF5File(
                            filename = '',
                            id = '',
                            uri = '',
                            groups = [
                                biosim_client.api.biosim.models.hdf5_group.HDF5Group(
                                    name = '',
                                    attributes = [
                                        biosim_client.api.biosim.models.hdf5_attribute.HDF5Attribute(
                                            key = '',
                                            value = null, )
                                        ],
                                    datasets = [
                                        biosim_client.api.biosim.models.hdf5_dataset.HDF5Dataset(
                                            name = '',
                                            shape = [
                                                56
                                                ],
                                            attributes = [
                                                biosim_client.api.biosim.models.hdf5_attribute.HDF5Attribute(
                                                    key = '',
                                                    value = null, )
                                                ], )
                                        ], )
                                ], ), )
                    ],
                comparison_statistics = {
                    'key' : [
                        [
                            biosim_client.api.biosim.models.comparison_statistics.ComparisonStatistics(
                                dataset_name = '',
                                simulator_version_i = '',
                                simulator_version_j = '',
                                var_names = [
                                    ''
                                    ],
                                score = [
                                    1.337
                                    ],
                                is_close = [
                                    True
                                    ],
                                error_message = '', )
                            ]
                        ]
                    },
                sim_run_data = [
                    biosim_client.api.biosim.models.run_data.RunData(
                        run_id = '',
                        dataset_name = '',
                        var_names = [
                            ''
                            ],
                        data = biosim_client.api.biosim.models.hdf5_data_values.Hdf5DataValues(
                            shape = [
                                56
                                ],
                            values = [
                                1.337
                                ], ), )
                    ]
            )
        else:
            return GenerateStatisticsActivityOutput(
                sims_run_info = [
                    biosim_client.api.biosim.models.simulation_run_info.SimulationRunInfo(
                        biosim_sim_run = biosim_client.api.biosim.models.biosim_simulation_run.BiosimSimulationRun(
                            id = '',
                            name = '',
                            simulator_version = biosim_client.api.biosim.models.biosimulator_version.BiosimulatorVersion(
                                id = '',
                                name = '',
                                version = '',
                                image_url = '',
                                image_digest = '',
                                created = '',
                                updated = '', ),
                            status = 'CREATED',
                            error_message = '', ),
                        hdf5_file = biosim_client.api.biosim.models.hdf5_file.HDF5File(
                            filename = '',
                            id = '',
                            uri = '',
                            groups = [
                                biosim_client.api.biosim.models.hdf5_group.HDF5Group(
                                    name = '',
                                    attributes = [
                                        biosim_client.api.biosim.models.hdf5_attribute.HDF5Attribute(
                                            key = '',
                                            value = null, )
                                        ],
                                    datasets = [
                                        biosim_client.api.biosim.models.hdf5_dataset.HDF5Dataset(
                                            name = '',
                                            shape = [
                                                56
                                                ],
                                            attributes = [
                                                biosim_client.api.biosim.models.hdf5_attribute.HDF5Attribute(
                                                    key = '',
                                                    value = null, )
                                                ], )
                                        ], )
                                ], ), )
                    ],
                comparison_statistics = {
                    'key' : [
                        [
                            biosim_client.api.biosim.models.comparison_statistics.ComparisonStatistics(
                                dataset_name = '',
                                simulator_version_i = '',
                                simulator_version_j = '',
                                var_names = [
                                    ''
                                    ],
                                score = [
                                    1.337
                                    ],
                                is_close = [
                                    True
                                    ],
                                error_message = '', )
                            ]
                        ]
                    },
        )
        """

    def testGenerateStatisticsActivityOutput(self):
        """Test GenerateStatisticsActivityOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
