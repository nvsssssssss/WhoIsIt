def filter_fictional_entities(
    entities: list[dict],
) -> tuple[list[dict], list[dict]]:
    """Keep fictional entities and record rejected entities with reasons."""

    accepted = []
    rejected = []

    for entity in entities:
        if entity.get("fictional") is True:
            accepted.append(entity)
        else:
            reason = (
                "not_fictional"
                if entity.get("fictional") is False
                else "fictional_status_missing"
            )

            rejected.append(
                {
                    "entity": entity,
                    "reason": reason,
                }
            )

    return accepted, rejected
