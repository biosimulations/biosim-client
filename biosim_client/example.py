from pprint import pprint

from biosim_client.simdataclient import SimdataClient

client = SimdataClient()
run_id = "61fea4a08c1e3dc95a79802e"  # "649b11e033437e21669d5733"

simdata = client.get_simdata(run_id)
for dataset_name in simdata.dataset_names():
    dataset = simdata.get_dataset(dataset_name)
    nparray = dataset.to_numpy()
    dataframe = dataset.to_pandas()

    print("==================================================================")
    print()
    print(f"          dataset = {dataset_name}")
    print()
    print("==================================================================")
    pprint(dataset.attributes)
    print()
    print(nparray)
    print()
    print(dataframe)
    print()
