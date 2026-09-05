## Domain/Category Hierarchy for Future Expansion

**Decision: INCLUDE ✅**

WhoIsIt should use a flexible, extensible domain/category hierarchy so new types of fictional content can be added without redesigning the core Character schema.

### Design

Do **NOT** hardcode domains/categories as attributes in the `Character` table.

Instead, use separate entities/tables:

- `domains`
  - `domain_id`
  - `name`
  - `description`

- `categories`
  - `category_id`
  - `domain_id`
  - `name`
  - `description`

### Example

Domain
├── Anime & Manga
├── Movies & TV
├── Video Games
├── Comics
└── Literature

### Benefits

- Keeps the `Character` schema domain-independent.
- Allows new domains/categories to be added easily.
- Avoids redesigning the database as WhoIsIt expands.
- Supports future classification and filtering.
- Keeps the knowledge base scalable and maintainable.

### Final Rule

> **Domains and categories should be data-driven, separate from the Character schema, and designed for future expansion.**

**Final decision: ☑️ INCLUDE**