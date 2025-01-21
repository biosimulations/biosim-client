from biosim_client.biosimclient import BiosimClient, VerifyResults
from biosim_client.sim_data import SimData


def test_foo() -> None:
    assert BiosimClient().get_root() == "{'docs': 'https://biosim.biosimulations.org/docs'}"


def test_verify_runs() -> None:
    run: VerifyResults = BiosimClient().compare_runs(["run1", "run2"])
    run.wait_for_done()
    assert run.is_done()
    sim_data_list: list[SimData] = run.get_simdata()
    for sim_data in sim_data_list:
        assert sim_data.run_id in ["run1", "run2"]
        assert sim_data.hdf5_file is not None
        assert sim_data.datasets is not None
        assert sim_data.dataset_names() is not None
        assert sim_data.dataset_uris() is not None
        assert sim_data.get_dataset("dataset1") is not None
        assert str(sim_data) is not None
