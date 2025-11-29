import json
import os

def load_config(env):
    path = os.path.join("config", f"{env}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Environment file not found: {path}")

    with open(path, "r") as f:
        return json.load(f)
