# 0004 — Wrong-Guess Recovery

## Status
Accepted

## Decision

WhoIsIt V1 supports recovery after an incorrect guess.

### Rules

1. A rejected guess is permanently excluded from the current game.
2. Existing answers and accumulated evidence are retained.
3. The engine re-ranks the remaining candidates.
4. A game permits a maximum of 3 total guesses.
5. The 25-question limit is not reset during recovery.
6. If all 3 guesses are rejected, the game ends as unsuccessful.
7. The user may optionally reveal the correct character.
8. Revealed answers may be stored as feedback/training data.
9. A single user report must not automatically modify the production
   knowledge base.

## Rationale

Recovery allows WhoIsIt to make use of the evidence already collected
instead of restarting the game after an incorrect guess, while limiting
the number of guesses to prevent an unnecessarily long game.