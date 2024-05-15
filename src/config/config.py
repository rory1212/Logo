import os
import yaml
from src.config.config_types import Config


CONFIG_FILE_PATH = os.path.join("..", "config.yaml")


def load_config(config_file: str) -> Config:
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)


config = load_config(CONFIG_FILE_PATH)
