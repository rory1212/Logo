import os
import yaml
from typing import Any, Dict

CONFIG_FILE_PATH = os.path.join("..", "config.yaml")


def load_config(config_file: str) -> Dict[str, Any]:
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)


config = load_config(CONFIG_FILE_PATH)
