# ADR 0006: Character / Entity Schema

## Status

Accepted

## Context

WhoIsIt needs a consistent way to represent fictional characters in its knowledge base.

A character record should contain basic identity information, while detailed knowledge about the character should be modeled separately through attributes, relationships, question answers, and provenance.

## Decision

For V1, the core Character/Entity schema will contain:

- `id` — unique identifier for the character
- `canonical_name` — primary name used to represent the character
- `aliases` — alternative names referring to the same character
- `description` — short general description
- `status` — current validity/availability of the record
- `created_at` — timestamp when the record was created
- `updated_at` — timestamp when the record was last updated

Detailed character knowledge will NOT be embedded directly into the core Character entity.

The following will be modeled separately:

- Attributes — gender, species, role, abilities, etc.
- Relationships — franchise, universe, media, creators, other characters, etc.
- Question Answers — answers to questions, including probability and confidence
- Provenance — sources and supporting evidence

## Rationale

Keeping the Character entity focused on identity and basic metadata prevents it from becoming a large, rigid object containing every possible piece of character knowledge.

Separating detailed knowledge makes the system easier to extend, query, validate, and use with the probabilistic reasoning engine.

## Consequences

### Positive

- Clear separation of identity and knowledge
- Easier to extend the knowledge model
- Supports many-to-many relationships
- Better suited for probabilistic reasoning
- Easier to maintain and validate

### Negative

- The data model becomes more complex
- Retrieving complete character information may require multiple related records

## Related Decisions

- Relationships & Taxonomy
- Question Bank Design
- Answer Probability and Confidence
- Provenance & Evidence
- Schema Validation



Character
    │
    ├── Identity
    │     ├── id
    │     ├── canonical_name
    │     └── description
    │
    ├── Aliases
    │
    ├── Attributes
    │     ├── gender
    │     ├── age
    │     ├── species
    │     ├── role
    │     └── ...
    │
    ├── Relationships
    │     ├── franchise
    │     ├── universe
    │     ├── media
    │     └── other characters
    │
    └── Question Answers
          ├── question
          ├── answer
          ├── probability
          └── confidence