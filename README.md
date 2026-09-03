# WhoIsIt

WhoIsIt is an adaptive fictional-character identification system inspired by Akinator-style games.

The system tries to identify the fictional character a user has in mind by asking questions, learning from the user's answers, and progressively narrowing down the possible characters.

## Project Goal

The goal of WhoIsIt is to build a question-based identification system that can intelligently determine which fictional character the user is thinking of.

Unlike a simple fixed decision tree, WhoIsIt is designed around adaptive and probabilistic reasoning so that the next question can depend on the answers given so far and the remaining candidate characters.

## Key Goals

- Identify fictional characters through interactive questioning
- Select questions adaptively based on the current candidate set
- Use probabilistic reasoning to maintain character likelihoods
- Handle uncertain, unknown, and contradictory user responses
- Make efficient guesses when sufficient evidence is available
- Scale the character knowledge base from a small prototype to 500+ entities
- Evaluate the system using curated benchmark games
- Provide a clean and intuitive user experience

## Project Structure

~~~text
WhoIsIt/
├── backend/
├── frontend/
├── data-pipeline/
├── docs/
└── tests/
~~~

### Backend

Contains the server-side application, game logic, APIs, reasoning engine, and related backend components.

### Frontend

Contains the user interface through which players interact with the WhoIsIt game.

### Data Pipeline

Contains tools and processes for collecting, cleaning, validating, transforming, and preparing character and question data.

### Docs

Contains project documentation, architecture information, technical decisions, experiments, and other supporting material.

### Tests

Contains unit tests, integration tests, evaluation tests, and benchmark-related testing code.

## Tech Stack

- Backend: Python / FastAPI
- Frontend: TBD
- Machine Learning / Reasoning: TBD
- Database: TBD
- Testing: TBD
- Deployment: TBD

Technology choices that are currently marked as TBD will be finalized as the corresponding part of the system is designed.

Major technical decisions will be documented in the `docs/` directory.

## Core System Concept

At a high level, the system will operate through the following process:

~~~text
User thinks of a character
          ↓
Initial candidate characters
          ↓
Ask an informative question
          ↓
Receive user answer
          ↓
Update candidate probabilities
          ↓
Select the next best question
          ↓
Repeat
          ↓
Make a character guess
          ↓
Evaluate result
~~~

The central reasoning system will determine which question should be asked next based on the information available at that point in the game.

## Development Status

🚧 Foundation and engineering setup phase.

The project is currently being established with a structured repository, development standards, documentation, testing strategy, and architecture.

## Evaluation Goals

The system will eventually be evaluated using curated benchmark games.

Important evaluation metrics will include:

- Guess accuracy
- Average number of questions per successful game
- Question-selection latency
- Performance across different character categories
- Performance when users provide uncertain or unknown answers
- Performance as the character knowledge base grows

Target values for these metrics will be defined during the foundation and evaluation planning stages.

## Initial Scale

The project will be developed incrementally.

~~~text
Prototype
   ↓
~50 characters
   ↓
Stage 1
   ↓
500+ characters
~~~

The initial prototype will allow the reasoning system and game mechanics to be tested on a manageable dataset before scaling the knowledge base.

## Roadmap

1. Foundation & Engineering Setup
2. Character Knowledge Base
3. Question & Answer Representation
4. Probabilistic Reasoning Engine
5. Adaptive Question Selection
6. Guessing System
7. Backend API
8. Frontend
9. Testing & Evaluation
10. Scaling
11. Deployment

## Engineering Principles

WhoIsIt will be developed with the following principles:

- Keep the reasoning system modular
- Separate data from application logic
- Prefer measurable evaluation over assumptions
- Record important architectural decisions
- Keep experiments reproducible
- Design for gradual scaling
- Write tests for important system behavior
- Avoid unnecessary complexity until it is justified

## Documentation

Important technical decisions will be recorded in:

~~~text
docs/decisions/
~~~

Experiments, architecture documentation, dataset documentation, and other project notes will also be maintained under `docs/`.

## Contributing

During the early development stages, the project will follow the defined repository structure, coding standards, branch strategy, and testing practices.

Changes should be developed on feature branches and merged into `main` after validation.

## License

License: TBD