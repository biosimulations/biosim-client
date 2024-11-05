from biosim_client.simdataclient import SimdataClient


def test_foo() -> None:
    assert SimdataClient().get_health() == "{'status': <Status.OK: 'ok'>}"
