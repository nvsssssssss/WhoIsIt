# ADR 0006: Character / Entity Schema

## Status

Accepted

## Context

WhoIsIt needs a consistent way to represent fictional characters in its knowledge base.

The database should distinguish between:

1. The identity of a character.
2. Information about that character.
3. Relationships between the character and other entities.
4. Answers associated with questions about the character.

The core `characters` table should therefore contain only information that identifies and describes the character itself. Detailed knowledge should be stored in separate tables and connected using relationships and foreign keys.

## Decision

For V1, the core `characters` table will contain:

- `id` — unique identifier for the character and primary key.
- `canonical_name` — primary name used to represent the character.
- `description` — short general description of the character.
- `status` — indicates whether the character record is currently active/valid.
- `created_at` — timestamp indicating when the character record was created.
- `updated_at` — timestamp indicating when the character record was last updated.

Aliases will be modeled separately rather than being treated as part of the character's core identity fields.

Detailed character knowledge will NOT be stored directly as columns in the `characters` table.

Instead, it will be modeled through separate tables for:

- **Aliases** — alternative names associated with a character.
- **Attributes** — properties such as gender, species, role, age, abilities, appearance, etc.
- **Character–Attribute Knowledge** — the state of each attribute for each character.
- **Relationships** — connections between characters and other entities such as franchises, universes, media, creators, and other characters.
- **Question Answers** — the knowledge used by WhoIsIt to determine how a character relates to a question, including answer probability and confidence where applicable.
- **Provenance & Evidence** — sources and supporting evidence for stored knowledge.

These tables will be connected to the `characters` table through appropriate primary-key and foreign-key relationships.

### Character–Attribute Relationship

For V1, WhoIsIt will store **every possible Character × Attribute pair**.

For example, if there are:

- 100 characters
- 50 attributes

the Character–Attribute relationship will contain:

`100 × 50 = 5,000` pairs.

Each pair will have an explicit state rather than relying on the absence of a row to represent missing information.

The possible states are:

- `true` — the attribute is known to be true for the character.
- `false` — the attribute is known to be false for the character.
- `unknown` — the system does not currently know whether the attribute applies.
- `not_applicable` — the attribute does not apply to the character.

Therefore:

```text
Character   Attribute       State
------------------------------------------
Superman    can_fly         true
Superman    uses_magic      false
Superman    is_masked       unknown
Superman    some_attribute  not_applicable