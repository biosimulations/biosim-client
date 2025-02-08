from pathlib import Path

import numpy as np
import pytest

from biosim_client.api.biosim.models.verify_workflow_output import VerifyWorkflowOutput
from biosim_client.api.biosim.models.verify_workflow_status import VerifyWorkflowStatus
from biosim_client.verify.biosim_client import BiosimClient
from biosim_client.verify.models import DatasetComparison, NDArray3D, VerifyResults


def test_api_version() -> None:
    assert BiosimClient().get_api_version() == "0.2.0"


def test_verify_runs_not_found() -> None:
    run_1_name = "run1"
    run_2_name = "run2"
    # expect the following statement to raise a ValueError with a message that the run was not found
    with pytest.raises(ValueError) as e:
        _run: VerifyResults = BiosimClient().compare_runs(run_ids=[run_1_name, run_2_name])
        assert str(e.value) in [
            f"Simulation run with id {run_1_name} not found.",
            f"Simulation run with id {run_2_name} not found.",
        ]


def test_verify_omex(
    omex_path: Path, omex_verify_workflow_output: VerifyWorkflowOutput, omex_verify_workflow_output_path: Path
) -> None:
    run: VerifyResults = BiosimClient().compare_omex(
        omex_path=omex_path, simulators=["copasi:4.45.296", "tellurium:2.2.10"]
    )

    # write out run to a json file - to refresh the fixture - set refresh_fixture to True
    refresh_fixture = False
    if refresh_fixture:
        with open(omex_verify_workflow_output_path, "w") as f:
            f.write(run.run_verify_results.model_dump_json(indent=2))

    assert run.run_verify_results.workflow_status == VerifyWorkflowStatus.COMPLETED
    assert run.run_verify_results.workflow_error is None
    assert run.run_verify_results.workflow_results is not None
    assert run.run_verify_results.workflow_results.sims_run_info is not None

    assert run.simulator_version_names == ["copasi:4.45.296", "tellurium:2.2.10"]

    expected_results = VerifyResults(run_verify_results=omex_verify_workflow_output)
    compare_verify_results(expected_results=expected_results, observed_results=run, abs_tol=1e-3, rel_tol=1e-3)


def test_verify_runs(runs_verify_workflow_output: VerifyWorkflowOutput, runs_verify_workflow_output_path: Path) -> None:
    run_ids = ["67817a2e1f52f47f628af971", "67817a2eba5a3f02b9f2938d"]
    run: VerifyResults = BiosimClient().compare_runs(run_ids=run_ids)

    # write out run to a json file - to refresh the fixture - set refresh_fixture to True
    refresh_fixture = False
    if refresh_fixture:
        with open(runs_verify_workflow_output_path, "w") as f:
            f.write(run.run_verify_results.model_dump_json(indent=2))

    assert run.run_verify_results.workflow_status == VerifyWorkflowStatus.COMPLETED
    assert run.run_verify_results.workflow_error is None
    assert run.run_verify_results.workflow_results is not None
    assert run.run_verify_results.workflow_results.sims_run_info is not None

    assert run.simulator_version_names == ["vcell:7.7.0.13", "copasi:4.45.296"]

    expected_results = VerifyResults(run_verify_results=runs_verify_workflow_output)
    compare_verify_results(expected_results=expected_results, observed_results=run, abs_tol=1e-8, rel_tol=1e-8)


def test_verify_results(runs_verify_workflow_output: VerifyWorkflowOutput) -> None:
    # the test fixture reads this from a json file
    run_verify_results = VerifyResults(run_verify_results=runs_verify_workflow_output)
    assert run_verify_results.run_ids == ["67817a2e1f52f47f628af971", "67817a2eba5a3f02b9f2938d"]
    assert run_verify_results.dataset_names == [
        "BIOMD0000000010_url.sedml/autogen_report_for_task_fig2a",
        "BIOMD0000000010_url.sedml/plot_0",
        "BIOMD0000000010_url.sedml/plot_1",
        "BIOMD0000000010_url.sedml/report_2",
        "BIOMD0000000010_url.sedml/report_3",
    ]

    ds1_score: NDArray3D = np.array(
        dtype=np.float64,
        object=[
            [[0.0, 0.0], [0.0, 0.0]],
            [[0.0, 0.21125174], [0.21124728, 0.0]],
            [[0.0, 0.61685992], [0.61689798, 0.0]],
            [[0.0, 0.08086148], [0.08086213, 0.0]],
            [[0.0, 0.13417488], [0.13417308, 0.0]],
            [[0.0, 0.08458215], [0.08458287, 0.0]],
            [[0.0, 0.32113636], [0.32114668, 0.0]],
            [[0.0, 0.21478327], [0.21478788, 0.0]],
            [[0.0, 0.9624532], [0.96254584, 0.0]],
            [[0.0, 0.0], [0.0, 0.0]],
            [[0.0, 0.00641189], [0.00641189, 0.0]],
            [[0.0, 0.00125752], [0.00125752, 0.0]],
            [[0.0, 0.01260924], [0.01260922, 0.0]],
            [[0.0, 0.01310387], [0.01310386, 0.0]],
            [[0.0, 0.01134159], [0.0113416, 0.0]],
            [[0.0, 0.00968109], [0.0096811, 0.0]],
            [[0.0, 0.09644475], [0.09644568, 0.0]],
            [[0.0, 0.09908284], [0.09908382, 0.0]],
            [[0.0, 0.00204604], [0.00204604, 0.0]],
            [[0.0, 0.01975421], [0.01975424, 0.0]],
        ],
    ).reshape(20, 2, 2)
    ds2_score: NDArray3D = np.array(
        dtype=np.float64,
        object=[[[0.0, np.inf], [np.inf, 0.0]], [[0.0, np.inf], [np.inf, 0.0]], [[0.0, np.inf], [np.inf, 0.0]]],
    ).reshape(3, 2, 2)
    ds3_score: NDArray3D = np.array(
        dtype=np.float64,
        object=[[[0.0, np.inf], [np.inf, 0.0]], [[0.0, np.inf], [np.inf, 0.0]], [[0.0, np.inf], [np.inf, 0.0]]],
    ).reshape(3, 2, 2)
    ds4_score: NDArray3D = np.array(
        dtype=np.float64,
        object=[
            [[0.00000000e00, 1.20533119e-12], [1.20533119e-12, 0.00000000e00]],
            [[0.00000000e00, 2.11251741e-01], [2.11247279e-01, 0.00000000e00]],
            [[0.00000000e00, 6.16859922e-01], [6.16897976e-01, 0.00000000e00]],
        ],
    ).reshape(3, 2, 2)
    ds5_score: NDArray3D = np.array(
        dtype=np.float64,
        object=[
            [[0.00000000e00, 1.15160897e-12], [1.15160897e-12, 0.00000000e00]],
            [[0.00000000e00, 1.44912293e-01], [1.44910193e-01, 0.00000000e00]],
            [[0.00000000e00, 1.57961864e-01], [1.57964360e-01, 0.00000000e00]],
        ],
    ).reshape(3, 2, 2)

    dataset_results: list[tuple[str, list[str], NDArray3D]] = [  # (dataset_name, var_names, dataset_score)
        (
            "BIOMD0000000010_url.sedml/autogen_report_for_task_fig2a",
            [
                "Time",
                "MAPK_PP",
                "MAPK",
                "MKKK",
                "MKKK_P",
                "MKK",
                "MKK_P",
                "MKK_PP",
                "MAPK_P",
                "uVol",
                "J0",
                "J1",
                "J2",
                "J3",
                "J4",
                "J5",
                "J6",
                "J7",
                "J8",
                "J9",
            ],
            ds1_score,
        ),
        ("BIOMD0000000010_url.sedml/plot_0", ["plot_0_0_0", "plot_0_0_1", "plot_0_1_1"], ds2_score),
        ("BIOMD0000000010_url.sedml/plot_1", ["plot_1_0_0", "plot_1_0_1", "plot_1_1_1"], ds3_score),
        (
            "BIOMD0000000010_url.sedml/report_2",
            ["task_fig2a.time/60", "task_fig2a.MAPK_PP", "task_fig2a.MAPK"],
            ds4_score,
        ),
        (
            "BIOMD0000000010_url.sedml/report_3",
            ["task_fig2b.time/60", "task_fig2b.MAPK_PP", "task_fig2b.MAPK"],
            ds5_score,
        ),
    ]

    for dataset_name, var_names, dataset_score in dataset_results:
        print(dataset_score)
        print()
        assert run_verify_results.get_var_names(dataset_name) == var_names
        dataset_comparison = run_verify_results.get_dataset_comparison(dataset_name)
        assert dataset_comparison is not None
        # assert str(dataset_comparison.dataset_score) == str(dataset_score)
        assert dataset_comparison.dataset_score.shape == dataset_score.shape
        assert dataset_comparison.dataset_score.dtype == dataset_score.dtype
        assert str(dataset_comparison.dataset_score.reshape(-1)) == str(dataset_score.reshape(-1))
        assert np.isclose(
            a=dataset_comparison.dataset_score, b=dataset_score, atol=1e-8, rtol=1e-8, equal_nan=True
        ).all()

    compare_verify_results(
        expected_results=run_verify_results, observed_results=run_verify_results, abs_tol=1e-8, rel_tol=1e-8
    )


def compare_verify_results(
    expected_results: VerifyResults, observed_results: VerifyResults, abs_tol: float, rel_tol: float
) -> None:
    expected: VerifyWorkflowOutput = expected_results.run_verify_results
    observed: VerifyWorkflowOutput = observed_results.run_verify_results
    assert expected.workflow_status == observed.workflow_status
    assert expected.workflow_error == observed.workflow_error
    assert expected.workflow_results is not None and observed.workflow_results is not None
    assert expected.compare_settings == observed.compare_settings

    # in addition - loop over datasets and compare the processed score values to ensure they are the same
    for dataset_name in expected_results.dataset_names:
        expected_ds_comp: DatasetComparison | None = expected_results.get_dataset_comparison(dataset_name)
        observed_ds_comp: DatasetComparison | None = observed_results.get_dataset_comparison(dataset_name)
        assert expected_ds_comp is not None and observed_ds_comp is not None
        assert str(expected_ds_comp.dataset_score) == str(observed_ds_comp.dataset_score)
        assert np.isclose(
            a=expected_ds_comp.dataset_score,
            b=observed_ds_comp.dataset_score,
            atol=abs_tol,
            rtol=rel_tol,
            equal_nan=True,
        ).all()
