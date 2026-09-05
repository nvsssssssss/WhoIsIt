# WHOISIT V1 ANSWER SET

## Answer Options

### YES

The user believes the proposition is definitely or strongly true.

### PROBABLY

The user believes the proposition is more likely true than false, but lacks sufficient certainty for **Yes**.

### DON'T KNOW

The user cannot determine whether the proposition is true or false.

This represents **missing information**, not a negative answer.

### PROBABLY NOT

The user believes the proposition is more likely false than true, but lacks sufficient certainty for **No**.

### NO

The user believes the proposition is definitely or strongly false.

---

## Skip Policy

WhoIsIt V1 does **not** allow users to skip questions.

Every presented question must be answered using exactly one of:

- Yes
- Probably
- Don't know
- Probably not
- No

**Don't know** represents insufficient knowledge about the question.

There is **no separate Skip state** in V1.

---

## Maximum Questions

**Maximum Questions: 25**

WhoIsIt may ask at most **25 questions** in a single game.

After the 25th answered question, the engine must:

1. Stop question selection.
2. Make a guess using the **highest-ranked remaining candidate**.

The **25-question limit is a hard upper bound**.

Reaching the limit does **not** imply that the engine is confident in its guess.

---

## Early Guess Policy

WhoIsIt may make an **early guess** only when **all three** conditions are satisfied:

1. At least **5 questions** have been answered.
2. The highest-ranked candidate has a probability of at least **85%**.
3. The highest-ranked candidate leads the second-ranked candidate by at least **20 percentage points**.

All three conditions must be satisfied.

If **any condition is not satisfied**, the engine continues asking questions until either:

- The early-guess conditions are met, or
- The **25-question maximum** is reached.

If the 25-question limit is reached, the engine makes a **forced guess regardless of confidence**.