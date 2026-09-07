from data_pipeline.ingestion.filter import filter_fictional_entities


def test_filter_fictional_entities():
    entities = [
        {"name": "Batman", "id": "Q1", "fictional": True},
        {"name": "Albert Einstein", "id": "Q2", "fictional": False},
        {"name": "Unknown", "id": "Q3"},
    ]

    accepted, rejected = filter_fictional_entities(entities)

    assert accepted == [
        {"name": "Batman", "id": "Q1", "fictional": True},
    ]

    assert rejected == [
        {
            "entity": {
                "name": "Albert Einstein",
                "id": "Q2",
                "fictional": False,
            },
            "reason": "not_fictional",
        },
        {
            "entity": {
                "name": "Unknown",
                "id": "Q3",
            },
            "reason": "fictional_status_missing",
        },
    ]
