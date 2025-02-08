from biosim_client.verify.biosim_client import BiosimClient
from biosim_client.verify.models import VerifyResults

run_ids = [
    "674e9088dc98815570335845",
    "674e597df6b91e483a90c248",
    "674e509df643f14403cb4716",
    "674eae0eca37d49ba02087e6",
]
run: VerifyResults = BiosimClient().compare_runs(run_ids=run_ids)
print(run.simulator_version_names)
