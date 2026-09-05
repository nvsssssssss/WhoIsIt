# Media Types and Franchises

## Purpose

Define how WhoIsIt stores the media types and franchises associated with characters.

## Media Types

A **media type** describes the kind of media/work in which a character appears.

Examples:

- Movie
- TV Show
- Anime
- Manga
- Comic
- Video Game
- Book

Store media types separately:

    media_types
    ----------------
    id
    name
    description
    status

## Franchises

A **franchise** is the larger fictional property or universe a character belongs to.

Examples:

- Marvel
- DC
- Harry Potter
- Super Mario

Store franchises separately:

    franchises
    ----------------
    id
    name
    description
    status

## Relationships

A character can appear in multiple media types, and each media type can contain many characters.

Therefore:

    characters
         ↕
    character_media_types
         ↕
    media_types

Similarly, characters can be associated with franchises:

    characters
         ↕
    character_franchises
         ↕
    franchises

These middle tables are **relationship/junction tables** used to represent many-to-many relationships.

## Note

> `media_types`, `franchises`, `character_media_types`, and `character_franchises` are all separate database tables.

## Core Decision

> Store `media_types` and `franchises` as separate entities, and use relationship tables to connect characters to them.