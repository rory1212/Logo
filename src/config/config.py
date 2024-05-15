import os
import yaml
from src.config.config_types import Config


script_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(script_dir, "..", "..", "config.yaml")


def load_config(config_file: str) -> Config:
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)


config = load_config(config_file_path)
