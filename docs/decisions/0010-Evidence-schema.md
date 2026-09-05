# Evidence Snippet / Reference Model

## Purpose

The purpose of the Evidence Snippet / Reference Model is to decide how WhoIsIt will store the specific piece of source material that supports a fact.

We already have:

    Fact
      ↓
    Provenance
      ↓
    Source

Evidence adds the supporting material:

    Fact
      ↓
    Provenance
      ↓
    Source
      ↓
    Evidence

More precisely, evidence belongs to the fact/source relationship because it explains why that source supports that particular fact.

## Example

Suppose we have:

    Superman → can_fly = true

The provenance says:

    This fact came from Wikipedia.

The evidence says:

    "The character possesses the ability to fly."

So:

    FACT
    Superman → can_fly = true
            │
            ↓
    PROVENANCE
    Source → Wikipedia
            │
            ↓
    EVIDENCE
    Snippet → "The character possesses the ability to fly."

## Possible Evidence Record

A possible design is:

    evidence
    --------------------------------
    id
    provenance_id
    snippet
    reference
    created_at

Where:

- `id` → evidence identifier
- `provenance_id` → which fact/source relationship this evidence supports
- `snippet` → relevant text extracted from the source
- `reference` → where in the source the evidence came from
- `created_at` → when the evidence record was created

The `reference` could point to things such as a page, section, paragraph, URL fragment, or other location depending on the source type.

## Important Distinction

### Source

    Wikipedia

### Provenance

    Superman's `can_fly = true` fact came from Wikipedia.

### Evidence

    The specific text/section from Wikipedia supporting `can_fly = true`.

## Current Data Model

The data model would roughly look like:

    characters
        ↓
    character_attributes
        ↓
    provenance
        ↓
    sources
        ↓
    evidence

## Design Consideration

The exact columns should not be finalized until we decide what kinds of sources WhoIsIt will ingest, such as APIs, datasets, web pages, books, etc.

The best `reference` structure may depend on the source type.

## Core Design Question

> **What information do we need to store so that we can later locate and inspect the exact evidence supporting a WhoIsIt fact?**