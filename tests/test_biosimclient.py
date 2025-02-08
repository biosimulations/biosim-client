from pathlib import Path

import pytest

from biosim_client.api.biosim.models.verify_workflow_output import VerifyWorkflowOutput
from biosim_client.api.biosim.models.verify_workflow_status import VerifyWorkflowStatus
from biosim_client.verify.biosim_client import BiosimClient
from biosim_client.verify.models import VerifyResults
from tests.test_reports import compare_verify_results


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
    compare_verify_results(expected_results=expected_results, observed_results=run, abs_tol=1e-2, rel_tol=1e-2)


def test_verify_runs_2(
    runs_verify_workflow_output_2: VerifyWorkflowOutput, runs_verify_workflow_output_2_path: Path
) -> None:
    run_ids = ["67817a2e1f52f47f628af971", "67817a2eba5a3f02b9f2938d"]
    run: VerifyResults = BiosimClient().compare_runs(run_ids=run_ids)

    # write out run to a json file - to refresh the fixture - set refresh_fixture to True
    refresh_fixture = False
    if refresh_fixture:
        with open(runs_verify_workflow_output_2_path, "w") as f:
            f.write(run.run_verify_results.model_dump_json(indent=2))

    assert run.run_verify_results.workflow_status == VerifyWorkflowStatus.COMPLETED
    assert run.run_verify_results.workflow_error is None
    assert run.run_verify_results.workflow_results is not None
    assert run.run_verify_results.workflow_results.sims_run_info is not None

    assert run.simulator_version_names == ["vcell:7.7.0.13", "copasi:4.45.296"]

    expected_results = VerifyResults(run_verify_results=runs_verify_workflow_output_2)
    compare_verify_results(expected_results=expected_results, observed_results=run, abs_tol=1e-8, rel_tol=1e-8)


def test_verify_runs_4(
    runs_verify_workflow_output_4: VerifyWorkflowOutput, runs_verify_workflow_output_4_path: Path
) -> None:
    run_ids = [
        "674e9088dc98815570335845",
        "674e597df6b91e483a90c248",
        "674e509df643f14403cb4716",
        "674eae0eca37d49ba02087e6",
    ]
    run: VerifyResults = BiosimClient().compare_runs(run_ids=run_ids)

    # write out run to a json file - to refresh the fixture - set refresh_fixture to True
    refresh_fixture = False
    if refresh_fixture:
        with open(runs_verify_workflow_output_4_path, "w") as f:
            f.write(run.run_verify_results.model_dump_json(indent=2))

    assert run.run_verify_results.workflow_status == VerifyWorkflowStatus.COMPLETED
    assert run.run_verify_results.workflow_error is None
    assert run.run_verify_results.workflow_results is not None
    assert run.run_verify_results.workflow_results.sims_run_info is not None

    assert run.simulator_version_names == ["amici:0.18.1", "copasi:4.45.296", "tellurium:2.2.10", "vcell:7.7.0.10"]

    expected_results = VerifyResults(run_verify_results=runs_verify_workflow_output_4)
    compare_verify_results(expected_results=expected_results, observed_results=run, abs_tol=1e-8, rel_tol=1e-8)
