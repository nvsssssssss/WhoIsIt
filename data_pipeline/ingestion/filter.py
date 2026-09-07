def filter_fictional_entities(entities: list[dict]) -> list[dict]:
    """Keep only entities identified as fictional."""

    return [entity for entity in entities if entity.get("fictional") is True]
