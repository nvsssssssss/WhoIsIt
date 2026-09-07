from data_pipeline.ingestion.fetcher import fetch_json


def test_fetch_json():
    data = fetch_json("https://httpbin.org/json")

    assert isinstance(data, dict)
    assert "slideshow" in data
