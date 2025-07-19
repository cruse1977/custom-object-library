import os
import argparse
import yaml
import json

GIT_ROOT = "https://github.com/cruse1977/custom-object-library/blob/main/"

catalog = {
    "data": []
}
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=True)
    args = parser.parse_args()

    path = args.path
    print(f"Processing path: {path}")

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".yaml"):
                print(f"Processing file: {file}")
                with open(os.path.join(root, file), "r") as f:
                    data = yaml.safe_load(f)
                    if "catalog" in data.keys():
                        add_to_catalog(data)
    save_catalog()

def save_catalog() -> None:
    with open("../catalog/catalog.json", "w") as f:
        json.dump(catalog, f, indent=4)

def add_to_catalog(data: dict) -> None:
    ''' create a new entry in the catalog '''
    new_entry = {
        "id": data["catalog"]["id"],
        "name": data["name"],
        "version": data["catalog"]["latest_version"],
        "tags": data["catalog"]["tags"].copy(),
        "url": f"{GIT_ROOT}{data['catalog']['id'].replace('.', '/')}.yaml",
    }
    catalog["data"].append(new_entry)
    print(f"Added {data['catalog']['id']} to catalog")

if __name__ == "__main__":
    main()