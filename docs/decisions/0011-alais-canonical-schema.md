# Aliases and Canonical Names

## Purpose

Define how WhoIsIt stores the primary name of a character and alternative names that refer to the same character.

## Canonical Name

The **canonical name** is the primary/standard name stored for a character.

Stored in:

    characters
    ----------------------------
    id
    canonical_name
    description
    status
    created_at
    updated_at

## Alias

An **alias** is an alternative name that refers to the same character.

Stored separately:

    aliases
    ----------------------------
    id
    character_id
    alias
    created_at
    updated_at

## Relationship

One character can have many aliases.

    characters
        │
        │ 1
        ↓
      aliases
        │
        │ many

Example:

    Superman
       │
       ├── Clark Kent
       ├── Kal-El
       └── Man of Steel

All aliases point to the same `character_id`.

## Core Decision

> Store one canonical name for each character in `characters`, and store alternative names in a separate `aliases` table linked to the character through `character_id`.

This also supports entity matching and deduplication during data ingestion.