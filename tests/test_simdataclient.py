from biosim_client.sim_data import SimData
from biosim_client.simdataclient import SimdataClient


def test_foo() -> None:
    assert SimdataClient().get_health() == "{'status': <Status.OK: 'ok'>}"


def test_get_metadata() -> None:
    run_id = "67817a2e1f52f47f628af971"
    simdata: SimData = SimdataClient().get_simdata(run_id)
    assert simdata.run_id == run_id
    assert simdata.hdf5_file is not None
    assert len(simdata.dataset_names()) > 0
    assert simdata.datasets is not None
    expected_names = [
        "BIOMD0000000010_url.sedml/autogen_report_for_task_fig2a",
        "BIOMD0000000010_url.sedml/plot_0",
        "BIOMD0000000010_url.sedml/plot_1",
        "BIOMD0000000010_url.sedml/report_2",
        "BIOMD0000000010_url.sedml/report_3",
    ]
    assert simdata.dataset_names() == expected_names
    assert simdata.get_dataset(expected_names[0]).to_numpy().shape == (20, 1001)
    assert simdata.get_dataset(expected_names[1]).to_numpy().shape == (3, 1001)
