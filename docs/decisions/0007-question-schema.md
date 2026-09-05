# Question System

## Status

Accepted

## Decision

WhoIsIt will use **one centralized `questions` table** as the question bank.

Each question will be stored as one row in the table.

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

### Example

| id | text | attribute_key | answer_type |
|---|---|---|---|
| 1 | Can this character fly? | `can_fly` | `boolean` |
| 2 | Is this character masked? | `is_masked` | `boolean` |
| 3 | Is this character a hero? | `is_hero` | `boolean` |
| 4 | Is this character human? | `is_human` | `boolean` |
| 5 | Does this character use magic? | `uses_magic` | `boolean` |

## Important Principle

The `questions` table stores **what WhoIsIt can ask**, not the answers for individual characters.

Character-specific answers will be stored separately in the `character_answers` table.

```text
questions
    │
    │ defines questions
    ↓
character_answers
    │
    │ stores character-specific knowledge
    ↓
characters