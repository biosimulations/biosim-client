from biosim_client.client import Client
from pprint import pprint

client = Client()
represillator_run_id = "61fea4a08c1e3dc95a79802e"  # "649b11e033437e21669d5733"

sim_results = client.get_sim_results(represillator_run_id)
for dataset_name in sim_results.dataset_names():
    dataset = sim_results.get_dataset(dataset_name)
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

