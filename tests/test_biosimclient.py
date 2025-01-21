from biosim_client.api.biosim.models.runs_verify_workflow_status import RunsVerifyWorkflowStatus
from biosim_client.biosimclient import BiosimClient, VerifyResults


def test_foo() -> None:
    assert BiosimClient().get_root() == "{'docs': 'https://biosim.biosimulations.org/docs'}"


def test_verify_runs_not_found() -> None:
    run_1_name = "run1"
    run_2_name = "run2"
    run: VerifyResults = BiosimClient().compare_runs(run_ids=[run_1_name, run_2_name])
    run.wait_for_done()
    assert run.is_done()
    assert run.run_verify_results.workflow_status == RunsVerifyWorkflowStatus.RUN_ID_NOT_FOUND
    assert run.run_verify_results.workflow_error in [
        f"Simulation run with id {run_1_name} not found.",
        f"Simulation run with id {run_2_name} not found.",
    ]


def test_verify_runs() -> None:
    run_ids = ["67817a2e1f52f47f628af971", "67817a2eba5a3f02b9f2938d"]
    run: VerifyResults = BiosimClient().compare_runs(run_ids=run_ids)
    run.wait_for_done()
    assert run.is_done()
    assert run.run_verify_results.workflow_status == RunsVerifyWorkflowStatus.COMPLETED
    assert run.run_verify_results.workflow_error is None
    assert run.run_verify_results.workflow_results is not None
    assert run.run_verify_results.workflow_results.comparison_statistics is not None
