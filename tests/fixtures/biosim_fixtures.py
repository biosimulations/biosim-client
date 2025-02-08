from pathlib import Path

import pytest

from biosim_client.api.biosim.models.verify_workflow_output import VerifyWorkflowOutput

ROOT_DIR = Path(__file__).parent.parent.parent
FIXTURE_DATA_DIR = ROOT_DIR / "tests" / "fixtures" / "data"


@pytest.fixture
def omex_path() -> Path:
    return FIXTURE_DATA_DIR / "BIOMD0000000010_tellurium_Negative_feedback_and_ultrasen.omex"


@pytest.fixture
def runs_verify_workflow_output_2_path() -> Path:
    return FIXTURE_DATA_DIR / "RunsVerifyWorkflowOutput_2_expected.json"


@pytest.fixture
def runs_verify_workflow_output_2(runs_verify_workflow_output_2_path: Path) -> VerifyWorkflowOutput:
    with open(runs_verify_workflow_output_2_path) as f:
        data = f.read()
        return VerifyWorkflowOutput.model_validate_json(data)


@pytest.fixture
def runs_verify_workflow_output_4_path() -> Path:
    return FIXTURE_DATA_DIR / "RunsVerifyWorkflowOutput_4_expected.json"


@pytest.fixture
def runs_verify_workflow_output_4(runs_verify_workflow_output_4_path: Path) -> VerifyWorkflowOutput:
    with open(runs_verify_workflow_output_4_path) as f:
        data = f.read()
        return VerifyWorkflowOutput.model_validate_json(data)


@pytest.fixture
def omex_verify_workflow_output_path() -> Path:
    return FIXTURE_DATA_DIR / "OmexVerifyWorkflowOutput_expected.json"


@pytest.fixture
def omex_verify_workflow_output(omex_verify_workflow_output_path: Path) -> VerifyWorkflowOutput:
    with open(omex_verify_workflow_output_path) as f:
        data = f.read()
        return VerifyWorkflowOutput.model_validate_json(data)


@pytest.fixture
def expected_omex_report() -> str:
    return (
        "- Group [[copasi:4.45.296](https://biosimulations.org/runs/67a7863d259fb524843108f5), "
        "[tellurium:2.2.10](https://biosimulations.org/runs/67a7863d259fb524843108f6)] "
        "matched (max score 0.5072752543311626)\n"
    )


@pytest.fixture
def expected_run_report_2() -> str:
    return (
        "- no match for "
        "[vcell:7.7.0.13](https://biosimulations.org/runs/67817a2e1f52f47f628af971) "
        "(closest score inf)\n"
        "- no match for "
        "[copasi:4.45.296](https://biosimulations.org/runs/67817a2eba5a3f02b9f2938d) "
        "(closest score inf)\n"
    )


@pytest.fixture
def expected_run_report_4() -> str:
    return (
        "- Group "
        "[[amici:0.18.1](https://biosimulations.org/runs/674e9088dc98815570335845), "
        "[copasi:4.45.296](https://biosimulations.org/runs/674e597df6b91e483a90c248), "
        "[tellurium:2.2.10](https://biosimulations.org/runs/674e509df643f14403cb4716)] "
        "matched (max score 1.8806043209090398e-08)\n"
        "- no match for "
        "[vcell:7.7.0.10](https://biosimulations.org/runs/674eae0eca37d49ba02087e6) "
        "(closest score inf)\n"
    )
