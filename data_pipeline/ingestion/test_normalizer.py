from data_pipeline.ingestion.normalizer import (
    normalize_identifier,
    normalize_name,
)


def test_normalize_name():
    assert normalize_name("  Batman   ") == "Batman"
    assert normalize_name("  Bruce    Wayne  ") == "Bruce Wayne"


def test_normalize_identifier():
    assert normalize_identifier("  Q42  ") == "Q42"
