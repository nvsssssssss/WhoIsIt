from data_pipeline.ingestion.deduplicator import deduplicate_entities


def test_deduplicate_entities():
    entities = [
        {"name": "Batman", "id": "Q42"},
        {"name": "Batman", "id": "Q42"},
        {"name": "Superman", "id": "Q43"},
    ]

    result = deduplicate_entities(entities)

    assert result == [
        {"name": "Batman", "id": "Q42"},
        {"name": "Superman", "id": "Q43"},
    ]
