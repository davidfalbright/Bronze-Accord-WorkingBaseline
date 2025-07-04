import yaml
import os

CHARTER_PATH = os.getenv("CHARTER_YAML_PATH", "charter_v2_2.yaml")

def load_charter_yaml(path: str = None):
    """
    Load the YAML charter file into a Python dictionary.

    Parameters:
        - path (optional): override the default path with a custom file location

    Returns:
        dict containing top-level keys: convictions, safeguards, principles, articles
    """
    yaml_path = path if path else CHARTER_PATH

    if not os.path.exists(yaml_path):
        raise FileNotFoundError(f"Charter YAML not found at: {yaml_path}")

    with open(yaml_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # Normalize structure: ensure each section is a list of items with 'id' and 'text'
    for section in ["convictions", "safeguards", "principles", "articles"]:
        items = data.get(section, [])
        for i, item in enumerate(items):
            if "id" not in item:
                item["id"] = f"{section[0].upper()}{i+1}"
            if "text" not in item and "statement" in item:
                item["text"] = item.pop("statement")
        data[section] = items

    return data