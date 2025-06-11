import json

# Charger le notebook
with open("01_exploration.ipynb", "r", encoding='latin1') as f:
    data = json.load(f)

# Supprimer les widgets
if "widgets" in data.get("metadata", {}):
    del data["metadata"]["widgets"]

# Sauvegarder le fichier nettoyé
with open("01_exploration.ipynb", "w") as f:
    json.dump(data, f, indent=4)

print("Nettoyage terminé 🚀")
