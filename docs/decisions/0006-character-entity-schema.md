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
- **Relationships** — connections between characters and other entities such as franchises, universes, media, creators, and other characters.
- **Question Answers** — the knowledge used by WhoIsIt to determine how a character relates to a question, including answer probability and confidence where applicable.
- **Provenance & Evidence** — sources and supporting evidence for stored knowledge.

These tables will be connected to the `characters` table through appropriate primary-key and foreign-key relationships.

## Rationale

The `characters` table represents the **identity of the character**, not every piece of knowledge about that character.

Keeping the core table small prevents it from becoming a large and rigid table containing hundreds of possible attributes.

Separating character knowledge into related tables allows the system to:

- Add new types of information without constantly changing the core character table.
- Represent one-to-many and many-to-many relationships properly.
- Handle complex character knowledge more cleanly.
- Support uncertain or probabilistic information.
- Maintain provenance and evidence independently.
- Keep the database easier to maintain and validate.
- Provide a better foundation for the probabilistic reasoning engine.

## Database Structure

The high-level structure is:

Character
│
├── Core Identity
│   ├── id
│   ├── canonical_name
│   ├── description
│   ├── status
│   ├── created_at
│   └── updated_at
│
├── Aliases
│
├── Attributes
│   ├── gender
│   ├── age
│   ├── species
│   ├── role
│   ├── abilities
│   └── appearance
│
├── Relationships
│   ├── franchise
│   ├── universe
│   ├── media
│   ├── creators
│   └── other characters
│
├── Question Answers
│   ├── question
│   ├── answer
│   ├── probability
│   └── confidence
│
└── Provenance & Evidence
    ├── source
    └── evidence

The `characters.id` primary key will be referenced by foreign keys in related tables where appropriate.

## Example SQL-Level Concept

The core table represents the character:

    characters
    ├── id (PK)
    ├── canonical_name
    ├── description
    ├── status
    ├── created_at
    └── updated_at

Other tables will reference `characters.id`:

    characters
         │
         │  primary key
         ↓
    related tables
         │
         └── character_id (FK)

The exact structure of these related tables will be decided in subsequent ADRs.

## Consequences

### Positive

- Clear separation between character identity and character knowledge.
- Easier to extend the knowledge model.
- Supports one-to-many and many-to-many relationships.
- Better suited for probabilistic reasoning.
- Easier to maintain and validate.
- Allows related data to be independently managed.

### Negative

- The database contains more tables and relationships.
- Retrieving complete information about a character may require joins across multiple tables.
- The overall data model is more complex than a single wide character table.

## Related Decisions

- Relationships & Taxonomy
- Question Schema & Stable Internal Attribute Keys
- Answer Probability & Confidence
- Provenance & Evidence
- Schema Validation