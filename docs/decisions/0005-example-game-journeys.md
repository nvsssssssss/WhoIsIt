# 0005 — Example Game Journeys

## Status
Accepted

## Purpose

These examples validate the interaction between the WhoIsIt V1 game
rules, answer semantics, early-guess policy, question limit, and
wrong-guess recovery.

These are illustrative journeys, not fixed question sequences. The
actual questions will be selected adaptively by the reasoning engine.

---

# Journey 1 — Early Correct Guess

### Target
Harry Potter

### Questions

1. Is your character fictional?
   - Yes

2. Is your character male?
   - Yes

3. Is your character human?
   - Yes

4. Is your character associated with magic?
   - Yes

5. Is your character from a book series?
   - Yes

At this point the engine has enough evidence and identifies
Harry Potter as the dominant candidate.

### Engine state

- Questions answered: 5
- Top candidate: Harry Potter
- Probability: 88%
- Second candidate: Ron Weasley
- Probability: 12%
- Lead: 76 percentage points

### Result

Early-guess conditions are satisfied.

> "My guess is Harry Potter."

User: Yes.

### Outcome

SUCCESS.

---

# Journey 2 — Early Guess Not Yet Justified

### Target
Batman

### Questions

1. Is your character male?
   - Yes

2. Is your character human?
   - Yes

3. Is your character a hero?
   - Yes

4. Does your character fight crime?
   - Yes

5. Is your character from DC?
   - Yes

### Engine state

- Questions answered: 5
- Batman: 72%
- Superman: 15%
- Green Arrow: 13%

### Result

The engine does NOT guess.

Reason:

72% < 85%.

It asks another question.

6. Does your character primarily operate at night?
   - Yes

7. Does your character use advanced technology?
   - Yes

### Engine state

- Batman: 91%
- Green Arrow: 6%
- Other: 3%

The engine now makes an early guess.

> "My guess is Batman."

User: Yes.

### Outcome

SUCCESS.

---

# Journey 3 — "Probably" Answers

### Target
Spider-Man

### Questions

1. Is your character male?
   - Yes

2. Is your character human?
   - Yes

3. Does your character have superhuman abilities?
   - Yes

4. Is your character associated with Marvel?
   - Probably

5. Is your character a superhero?
   - Yes

6. Does your character use a mask?
   - Yes

7. Is your character associated with New York?
   - Probably

The probability engine incorporates uncertain answers without treating
them as equivalent to definite Yes answers.

### Engine state

- Spider-Man: 87%
- Daredevil: 7%
- Other: 6%

The early-guess conditions are satisfied.

### Result

> "My guess is Spider-Man."

User: Yes.

### Outcome

SUCCESS.

---

# Journey 4 — "Don't Know" Answers

### Target
Pikachu

### Questions

1. Is your character male?
   - Don't know

2. Is your character human?
   - No

3. Is your character an animal-like creature?
   - Yes

4. Is your character from a video game?
   - Probably

5. Is your character yellow?
   - Yes

6. Is your character associated with Pokémon?
   - Yes

7. Can your character use electricity?
   - Yes

The "Don't know" answer does not act as either Yes or No.

The engine relies on the remaining evidence.

### Engine state

- Pikachu: 90%
- Raichu: 5%
- Other: 5%

### Result

> "My guess is Pikachu."

User: Yes.

### Outcome

SUCCESS.

---

# Journey 5 — "Probably Not" Answers

### Target
Sherlock Holmes

### Questions

1. Is your character male?
   - Yes

2. Is your character human?
   - Yes

3. Is your character a superhero?
   - Probably not

4. Is your character highly intelligent?
   - Yes

5. Is your character a detective?
   - Yes

6. Is your character primarily associated with modern superhero
   stories?
   - Probably not

7. Is your character from literature?
   - Yes

The engine uses the negative-but-uncertain answers as evidence against
superhero candidates.

### Engine state

- Sherlock Holmes: 89%
- Hercule Poirot: 7%
- Other: 4%

### Result

> "My guess is Sherlock Holmes."

User: Yes.

### Outcome

SUCCESS.

---

# Journey 6 — Maximum Questions Reached

### Target
An obscure fictional character

The character is difficult to distinguish from several similar
characters.

The user answers all questions, including several "Don't know"
responses.

After Question 24:

- Candidate A: 34%
- Candidate B: 27%
- Candidate C: 18%
- Remaining candidates: 21%

The engine asks Question 25.

### Question 25

> Is your character associated with a fictional kingdom?

User: Probably.

### Final engine state

- Candidate A: 38%
- Candidate B: 31%
- Candidate C: 16%
- Others: 15%

No early-guess threshold is satisfied.

However, the maximum question limit has been reached.

### Result

The engine MUST guess.

> "My guess is Candidate A."

### Outcome

This is a FORCED GUESS.

The low confidence does not prevent the guess.

---

# Journey 7 — First Guess Wrong, Second Guess Correct

### Target
Geralt of Rivia

The engine reaches an early-guess state.

### First guess

> "My guess is Aragorn."

User: No.

### Recovery

Aragorn is permanently excluded from the current game.

Previously collected answers are retained.

The engine re-ranks the remaining candidates.

### Second guess

> "Let me try again. Is your character Geralt of Rivia?"

User: Yes.

### Outcome

SUCCESS.

### Important behavior

The engine did NOT:

- restart the game,
- discard previous answers,
- reset the question counter,
- reconsider Aragorn.

---

# Journey 8 — Two Wrong Guesses, Third Correct

### Target
A difficult character

### First guess

> "My guess is Character A."

User: No.

Character A is removed.

### Second guess

> "My guess is Character B."

User: No.

Character B is removed.

### Third guess

The engine re-ranks the remaining candidates.

> "My guess is Character C."

User: Yes.

### Outcome

SUCCESS.

The game ends after the third guess.

No fourth guess is permitted.

---

# Journey 9 — Three Wrong Guesses

### Target
A character absent or poorly represented in the knowledge base

### First guess

> Character A

User: No.

### Second guess

> Character B

User: No.

### Third guess

> Character C

User: No.

### Result

The engine stops.

It does NOT:

- make a fourth guess,
- restart the questions,
- reset the probability model.

It displays:

> "I couldn't identify your character."

It then optionally asks:

> "Would you like to tell me who it was?"

User:

> "Yes — it was Character D."

### Outcome

The result is recorded as feedback/training data.

The production knowledge base is NOT automatically modified.

---

# Journey 10 — Correct Guess at Question 25

### Target
A difficult but supported character

The engine asks questions throughout the game because no early-guess
condition is satisfied.

After Question 24:

- Candidate A: 61%
- Candidate B: 24%
- Candidate C: 8%
- Others: 7%

The engine asks Question 25.

### User answer

> Yes

### Updated state

- Candidate A: 88%
- Candidate B: 7%
- Candidate C: 3%
- Others: 2%

The question limit has now been reached.

### Result

The engine makes its mandatory final guess:

> "My guess is Candidate A."

User: Yes.

### Outcome

SUCCESS.

This is still considered a final/forced guess because the maximum
question limit was reached, even though the final probability is high.

---

# Summary of Valid Game Endings

WhoIsIt V1 supports the following endings:

1. Early successful guess
2. Guess after additional questions
3. Forced guess after Question 25
4. Wrong first guess → recovery → correct guess
5. Wrong second guess → recovery → correct third guess
6. Three wrong guesses → unsuccessful game
7. Three wrong guesses → user reveals correct character → feedback recorded

## Global Rules Demonstrated

- Every question receives exactly one of five answers.
- Questions cannot be skipped.
- "Don't know" is not treated as "No".
- "Probably" and "Probably not" represent uncertain evidence.
- Early guessing requires all early-guess conditions.
- Maximum questions per game: 25.
- Maximum guesses per game: 3.
- Rejected guesses are removed from the current candidate set.
- Recovery does not reset accumulated evidence.
- Recovery does not reset the question counter.
- A user-revealed character is feedback and does not automatically
  modify the production knowledge base.