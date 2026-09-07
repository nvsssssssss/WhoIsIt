import json
from pathlib import Path


def save_raw_json(data: dict, file_path: str) -> None:
    """Save raw JSON data to a file."""

    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
