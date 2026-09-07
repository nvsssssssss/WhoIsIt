# Question System

## Status

Accepted

## Decision

WhoIsIt will use **one centralized `questions` table** as the question bank.

Each question will be stored as one row in the table.

The `questions` table represents **what WhoIsIt can ask** about the attributes defined in the knowledge model.

### Questions Table

| Column | Purpose |
|---|---|
| `id` | Unique identifier for the question |
| `text` | Question wording shown to the user |
| `attribute_key` | Stable internal concept represented by the question |
| `answer_type` | Type of answer expected |
| `status` | Whether the question is active or inactive |
| `created_at` | When the question was created |
| `updated_at` | When the question was last updated |

## Stable Internal Attribute Keys

Each question will reference a stable internal `attribute_key`.

The `attribute_key` represents the underlying attribute concept, while `text` represents the user-facing wording.

For example:

```text
Question:
"Can this character fly?"

attribute_key:
can_fly