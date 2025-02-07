from pathlib import Path

import pytest

from biosim_client.biosimclient import VerifyResults

ROOT_DIR = Path(__file__).parent.parent.parent
FIXTURE_DATA_DIR = ROOT_DIR / "tests" / "fixtures" / "data"


@pytest.fixture
def verify_results_path() -> Path:
    return FIXTURE_DATA_DIR / "verify_results.json"


@pytest.fixture
def verify_results(verify_results_path: Path) -> VerifyResults:
    with open(verify_results_path) as f:
        data = f.read()
        return VerifyResults.model_validate_json(data)
