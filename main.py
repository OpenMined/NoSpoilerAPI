from syftbox_sdk.datasets import load_dataset
from syftbox.lib import Client
import json

if __name__ == "__main__":
    client = Client.load()

    ionesio_datasite_path = client.datasites / "ionesio@openmined.org" / "api_data" / "dont_spoiler" / (client.email + ".json")
    dataset = load_dataset("Netflix Data")
    
    result = "No"
    if "The Intern" in dataset['Title']:
       result = "Yes"

    with open(str(ionesio_datasite_path), 'w') as json_file:
        json.dump({"watched": result},json_file, indent=4)

