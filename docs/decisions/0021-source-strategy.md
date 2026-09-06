## Source Priority & Conflict Resolution

WhoIsIt may collect information about the same character from multiple sources. Since different sources can provide different or conflicting information, we need clear rules for deciding which information to trust.

### 1. Source Priority

Sources will generally be ranked according to their reliability:

1. **Official / Canonical Sources**
   - Official franchise websites
   - Official publishers, developers, studios, etc.
   - Canonical material
   - Highest priority when directly available

2. **Trusted Structured Sources**
   - Wikidata
   - TMDB
   - AniList
   - Other well-maintained structured datasets
   - Useful for structured facts, relationships, works, and metadata

3. **Reliable Reference Sources**
   - Wikipedia
   - Other established reference databases
   - Useful for descriptions, background information, and contextual facts

4. **Community / Fan Sources**
   - Fandom wikis
   - Fan-maintained databases
   - Useful for detailed information but treated with lower default confidence

> Source priority is not necessarily universal. A source may be more reliable for one type of fact than another.

### 2. Fact-Specific Source Priority

We should not blindly use one global ranking for every fact.

For example:

- **Character → Movie/TV appearance**
  - TMDB or an official source may be preferred.

- **Character → Universe**
  - Wikidata or an official source may be preferred.

- **Detailed character description**
  - Wikipedia, an official source, or a well-maintained franchise wiki may be more useful.

Therefore, source priority can depend on the **type of information being collected**.

### 3. Preserve Conflicting Information

When two sources disagree, WhoIsIt should **not silently overwrite one value with another**.

Example:

    Wikidata → species = Human
    Fandom   → species = Metahuman

Instead, we retain both claims along with their sources:

    Fact: species = Human
    Source: Wikidata

    Fact: species = Metahuman
    Source: Fandom

This is possible because WhoIsIt maintains **provenance information** for its knowledge.

### 4. Prefer Higher-Priority Evidence

If a single value is required by the system and sources conflict, the higher-priority source should normally be preferred.

Example:

    Official source → Human
    Wikipedia       → Metahuman
    Fandom          → Metahuman

The system would prefer:

    species = Human

because the official source has higher priority.

### 5. Agreement Between Sources

If multiple independent sources provide the same information, their agreement can increase our confidence in that fact.

Example:

    Wikidata  → Human
    Wikipedia → Human
    Fandom    → Human

This provides stronger evidence than:

    Fandom → Human

The exact confidence calculation will be defined later when we design the knowledge/confidence system.

### 6. Unresolved Conflicts

Sometimes there may be no clear correct answer.

Example:

    Source A → Human
    Source B → Alien
    Source C → Unknown

If the conflict cannot be reliably resolved, WhoIsIt should **not invent an answer**.

Instead:

    Status: Conflicting

    Claims:
      - Human
      - Alien

    Sources:
      - Source A
      - Source B

The conflict can then be reviewed or handled later by the knowledge-quality system.

### 7. Provenance Must Be Preserved

Every important fact entering the WhoIsIt knowledge base should be traceable back to its source.

    Character
        ↓
      Fact
        ↓
    Provenance
        ↓
      Source

This allows us to answer:

- Where did this fact come from?
- Which source provided it?
- Are multiple sources saying the same thing?
- Which source was preferred?
- Why was a particular value selected?
- Is there an unresolved conflict?

### Overall Rule

> **WhoIsIt will prefer the most reliable source for each type of fact, preserve the provenance of all collected claims, use agreement between sources as supporting evidence, and retain unresolved conflicts rather than silently discarding information.**