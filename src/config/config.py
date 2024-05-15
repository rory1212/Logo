import os
import yaml

from src.config.config_types import Config
from src.utils.update_dict import update_dict


def get_file_path(filename: str) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "..", "..", filename)


def load_file(config_file: str) -> Config:
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)


def load_config() -> Config:
    base_config = load_file(get_file_path("config.yaml"))
    if "ENV" in os.environ:
        curr_env = os.environ['ENV']
        try:
            curr_config = load_file(get_file_path(f"config.{curr_env.lower()}.yaml"))
            update_dict(base_config, curr_config)
        except IOError:
            print(f"Env {curr_env} is not exists")

    return base_config


config = load_config()
