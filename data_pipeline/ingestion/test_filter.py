from data_pipeline.ingestion.filter import filter_fictional_entities


def test_filter_fictional_entities():
    entities = [
        {"name": "Batman", "id": "Q1", "fictional": True},
        {"name": "Albert Einstein", "id": "Q2", "fictional": False},
        {"name": "Unknown", "id": "Q3"},
    ]

    result = filter_fictional_entities(entities)

    assert result == [
        {"name": "Batman", "id": "Q1", "fictional": True},
    ]
