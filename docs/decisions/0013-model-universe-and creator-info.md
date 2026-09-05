## Universe & Creator Modeling Decision

### Decision
**INCLUDE — model Universe and Creator as separate entities/tables.**

### Schema Design

- `Character` → separate entity/table
- `Universe` → separate entity/table
- `Creator` → separate entity/table
- Do **NOT** store Universe or Creator as simple attributes in `Character`.

### Relationships

Use relationship/junction tables to support many-to-many relationships:

- `character_universes`
  - Connects Characters ↔ Universes
- `character_creators`
  - Connects Characters ↔ Creators

### Structure

Character
- character_id
- name
- ...

Universe
- universe_id
- name
- description
- ...

Creator
- creator_id
- name
- type
- ...

Relationships:

Creator ↔ Character ↔ Universe

### Reason

A character may:
- Have multiple creators
- Belong to multiple universes/continuities
- Need additional relationship information in the future

Therefore, Universe and Creator should **not** be simple Character attributes.

### Final Rule

> **Universe = separate entity**
>
> **Creator = separate entity**
>
> **Character ↔ Universe = relationship/junction table**
>
> **Character ↔ Creator = relationship/junction table**

Both must be represented in the final **WhoIsIt ER diagram**.