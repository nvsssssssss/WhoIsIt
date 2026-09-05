# Source / Provenance Schema

## Purpose

The Source/Provenance schema defines how WhoIsIt stores information about its data sources and records which source a stored fact came from.

## 1. Source

A **Source** is where WhoIsIt obtains information from.

Example structure:

    sources
    --------------------------------
    id
    name
    type
    url
    description
    status
    created_at
    updated_at

This answers:

> **What source do we use?**

## 2. Provenance

Suppose WhoIsIt stores:

    Character: Superman
    Attribute: can_fly
    Value: true

We need to record which source provided this fact:

    Superman → can_fly → true
                           ↓
                        source_id = 1
                           ↓
                        Wikipedia

Provenance records the relationship:

> **This particular piece of knowledge came from this particular source.**

Therefore:

- `Wikipedia` → **Source**
- `can_fly = true` → **Knowledge / Fact**
- `can_fly = true → Wikipedia` → **Provenance**

## 3. Why Provenance Is Needed

A single source can provide many facts:

    Wikipedia
       │
       ├── Superman → can_fly = true
       ├── Superman → is_human = false
       ├── Batman → is_human = true
       └── Batman → uses_magic = false

Different facts can also come from different sources:

    Superman → can_fly = true    → Wikipedia
    Superman → is_human = false  → DC source
    Batman   → is_human = true   → Wikipedia

Therefore, WhoIsIt needs a way to associate each stored fact with its source.

## 4. Possible Database Designs

### Option A — Source Directly on the Fact

    character_attributes
    ------------------------------------------------
    character_id | attribute_id | value | source_id

Here, `source_id` directly points to the source that provided the fact.

### Option B — Separate Provenance Table

    character_attributes
    -----------------------------
    id | character_id | attribute_id | value

    provenance
    -----------------------------
    id | fact_id | source_id

This represents provenance as a separate relationship between a fact and a source.

Option B is more flexible if one fact can have multiple sources.

    Superman → can_fly = true
           ↙              ↘
      Wikipedia        DC Database

## 5. Scope

This decision covers:

1. The structure of the `sources` table.
2. How stored knowledge/facts reference their sources.
3. How provenance is represented between a fact and a source.

### Not Covered Yet

The exact supporting passage, snippet, section, page, or reference from a source is **not** part of this decision.

That will be designed separately under:

> **Evidence Snippet / Reference Model**

## 6. Core Concept

Keep these three concepts separate:

    SOURCE
    "What source did we get data from?"

            ↓

    PROVENANCE
    "Which stored fact came from which source?"

            ↓

    EVIDENCE
    "What exact part of that source supports the fact?"

The Source/Provenance schema establishes the link between **WhoIsIt knowledge** and its **origin**.