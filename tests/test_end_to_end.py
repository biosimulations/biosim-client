from pathlib import Path

from biosim_client.verify.biosim_client import BiosimClient
from biosim_client.verify.models import VerifyResults


def test_simulators_with_and_without_colons(omex_path: Path) -> None:
    simulators = ["amici", "copasi", "tellurium", "vcell"]
    run: VerifyResults = BiosimClient().compare_omex(omex_path=omex_path, simulators=simulators)
    run.show_saved_plots()


def test_simulators_with_versions(omex_path: Path) -> None:
    simulators = ["amici:0.18.1", "copasi:4.45.296", "tellurium:2.2.10", "vcell:7.7.0.13"]
    run: VerifyResults = BiosimClient().compare_omex(omex_path=omex_path, simulators=simulators)
    run.show_saved_plots()
