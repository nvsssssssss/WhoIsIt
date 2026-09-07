def normalize_name(name: str) -> str:
    """Normalize a character name."""

    return " ".join(name.strip().split())


def normalize_identifier(identifier: str) -> str:
    """Normalize an external identifier."""

    return identifier.strip()
