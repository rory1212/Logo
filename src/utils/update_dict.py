from typing import Any, Dict


def update_dict(original_dict: Dict[str, Any], new_dict: Dict[str, Any]) -> Dict[str, Any]:
    for key, value in new_dict.items():
        if isinstance(value, dict) and key in original_dict and isinstance(original_dict[key], dict):
            original_dict[key] = update_dict(original_dict[key], value)
        elif key in original_dict and original_dict[key] != value:
            original_dict[key] = value
    return original_dict
