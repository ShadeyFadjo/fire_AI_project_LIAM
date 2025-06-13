import json

file_name="01_exploration.ipynb"
with open(file_name, "r", encoding='latin1') as f:
    data = json.load(f)

if "widgets" in data.get("metadata", {}):
    del data["metadata"]["widgets"]

with open(file_name, "w") as f:
    json.dump(data, f, indent=4)

print("Done 🚀")
