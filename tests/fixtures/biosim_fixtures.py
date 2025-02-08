from pathlib import Path

import pytest

from biosim_client.api.biosim.models.verify_workflow_output import VerifyWorkflowOutput

ROOT_DIR = Path(__file__).parent.parent.parent
FIXTURE_DATA_DIR = ROOT_DIR / "tests" / "fixtures" / "data"


@pytest.fixture
def omex_path() -> Path:
    return FIXTURE_DATA_DIR / "BIOMD0000000010_tellurium_Negative_feedback_and_ultrasen.omex"


@pytest.fixture
def runs_verify_workflow_output_path() -> Path:
    return FIXTURE_DATA_DIR / "RunsVerifyWorkflowOutput_expected.json"


@pytest.fixture
def runs_verify_workflow_output(runs_verify_workflow_output_path: Path) -> VerifyWorkflowOutput:
    with open(runs_verify_workflow_output_path) as f:
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
