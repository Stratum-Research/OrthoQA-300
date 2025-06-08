import json
import os


def save_json(data, filepath):
    dirname = os.path.dirname(filepath)
    if dirname:  # Only create directory if there is one
        os.makedirs(dirname, exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
