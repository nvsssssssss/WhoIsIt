import json

from data_pipeline.ingestion.cache import save_raw_json


def test_save_raw_json(tmp_path):
    data = {
        "name": "Batman",
        "publisher": "DC",
    }

    file_path = tmp_path / "raw" / "batman.json"

    save_raw_json(data, str(file_path))

    assert file_path.exists()

    with file_path.open("r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == data
