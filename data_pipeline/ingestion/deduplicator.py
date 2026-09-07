def deduplicate_entities(entities: list[dict]) -> list[dict]:
    """Remove duplicate entities using their normalized identifier."""

    seen_ids = set()
    unique_entities = []

    for entity in entities:
        identifier = entity["id"]

        if identifier not in seen_ids:
            seen_ids.add(identifier)
            unique_entities.append(entity)

    return unique_entities
