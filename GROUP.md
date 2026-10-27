# Group 3 — Catch-up Group C3

## Project Information

- **Project:** The Hostel Games Evening
- **Repository:** https://github.com/aheebwaabraham78/ucu-oop-class-examples
- **Group:** Catch-up Group C3
- **Foundation work:** Eight assigned foundation tasks
- **Selected advanced extensions:** A2, A3 and A4
- **Default branch:** `main`

## 1. Group Members and Foundation Responsibilities

| No. | Full Name | Registration Number | University Access Number | Foundation Task |
|---:|---|---|---|---|
| 1 | Aheebwa Abraham | S24B13/042 | B30127 | `RacingGame` subclass |
| 2 | Okello Mark | S24B13/050 | B30259 | `GameCredits.add_more(amount)` |
| 3 | Mugabi Ernest | S25B13/062 | B34215 | `TriviaFromMemory` |
| 4 | Ntare Ernest Karuhinda | S25B13/053 | B34835 | `affordable(choices, limit)` |
| 5 | Namakula Zaina | S25B13/013 | B34603 | `GamesEvening.summary()` |
| 6 | Obitre Warren Joshua | S25B13/041 | B34732 | `QuickPractice` subclass |
| 7 | Nankwanga Fridah | M25B13/033 | B33240 | `GamesEvening.cancel_last()` |
| 8 | Murwani Samuel | S26B13/145 | B41005 | `GamesEvening.complete_bundle(choices)` |

Each member was assigned a foundation task. The assignment requires each member to provide a runnable demonstration, test their contribution, and submit a foundation pull request. The corresponding demonstration, testing and review evidence should be recorded when verified.

## 2. Foundation Work and Integration

The group worked on the eight assigned foundation tasks for *The Hostel Games Evening*. These tasks extend the existing game-session implementation with additional game choices, resource management, session summaries, affordability checks, cancellation, and bundled game completion.

The contributions were brought together in `stories/09_games_evening/story.py`. The combined file is present on the group's `main` branch, and the group has confirmed that the story runs.

The original `main()` entry point and expected story behaviour should be preserved while extensions are integrated. Individual demonstrations and automated tests should also remain available as required by the assignment.

## 3. Selected Advanced Extensions

The group selected exactly three advanced extensions from `stories/09_games_evening/ADVANCED_EXTENSIONS.md`:

1. **A2 — Custom exceptions and strict game requests**
2. **A3 — Save and load a games evening using JSON**
3. **A4 — Choice factory and separation of responsibilities**

Selection of these extensions establishes the group's intended advanced work. Their individual implementation and verification must be supported by the actual code, demonstrations, tests and pull-request evidence.

Every member must contribute code or meaningful automated tests to at least one selected advanced extension through a later-topic pull request. Documentation or review comments alone do not satisfy this requirement.

### 3.1 A2 — Custom Exceptions and Strict Game Requests

**Objective**

Provide clear error handling for invalid choices, invalid requests and insufficient game credits, without changing credits or successful-game history when a request is refused.

**Required implementation**

- `GamesChoiceError` for a missing or invalid choice, such as `None`.
- `GamesRequestError` for an invalid request, including a negative calculated credit requirement.
- `GamesResourceError` when a valid choice costs more than the available credits.
- A `StrictGamesEvening` subclass or service that provides a `safe_play(choice)` method.
- Appropriate exceptions raised before an unsuccessful request changes credits or history.
- Delegation to the existing play functionality for valid, affordable choices.
- Support for valid zero-cost choices.

**Demonstration and verification**

The demonstration should handle each custom exception using specific `except` clauses and include a `finally` message. Automated tests should exercise all three exception types, confirm that refused requests leave credits and history unchanged, and verify that a valid request succeeds.

### 3.2 A3 — Save and Load Using JSON

**Objective**

Support saving and restoring a games evening while preserving the important state of the session.

**Required implementation**

- Save student details, remaining credits, successful-game history and relevant state from the foundation features.
- Preserve each recorded choice and its original saved cost.
- Use ordinary JSON-compatible data and explicit allowed type labels.
- Restore a new `GamesEvening` with a fresh resource object and compatible history.
- Preserve foundation behaviour after loading, including cancellation refunds based on recorded historical costs.
- Validate loaded data before making the restored session available.
- Avoid `eval` and do not execute arbitrary class names from saved files.

**Demonstration and verification**

Tests should cover a save/load round trip, continued actions after loading, a missing file, malformed JSON and structurally invalid data. Failed loads should produce clear errors without mutating the running session.

### 3.3 A4 — Choice Factory and Separation of Responsibilities

**Objective**

Provide a common factory for supported game choices and improve the separation of responsibilities within the implementation.

**Required implementation**

- Implement `create_choice(key, **settings)`.
- Support `FootballGame`, `LudoRound` and `CheeringContest`.
- Document the settings required for each choice.
- Report unknown factory keys with a clear error.
- Keep callers working through the common choice interface rather than introducing class-specific branches into the coordinator.
- Establish clear responsibilities for object creation, rule checking and display.
- Refactor at least one area to improve the Single Responsibility Principle and explain the improvement.

**Demonstration and verification**

Automated tests should exercise factory-created objects through the real caller, check that refused requests do not change state, verify that unknown keys are rejected, and confirm that separate instances maintain independent state.

## 4. Advanced Extension Test Commands

The assignment specifies the following test-discovery commands.

**Linux or macOS**

```bash
python3 -m unittest discover -s stories/09_games_evening -p "test_*.py"
```

**Windows**

```powershell
py -3 -m unittest discover -s stories/09_games_evening -p "test_*.py"
```

These commands must be run against the final repository state. Record the actual test results and confirm that the runner discovers and executes the intended tests rather than reporting zero tests.

## 5. Pull Request Review Evidence

The assignment requires every pull request to receive a useful review comment from every other member of the eight-person group before merging. This means seven teammate review comments per pull request.

Useful reviews should identify the method, rule, test case or behaviour examined and explain what worked or what needs improvement. General comments such as “good” or “done” are insufficient.

Record actual review evidence here as it becomes available:

- **Foundation pull requests:** Add the relevant PR links and review-comment links.
- **Later-topic pull requests:** Add the relevant PR links and review-comment links.
- **Member contributions:** Identify each member's later-topic contribution and link to the supporting PR.

Do not record a review, contribution or link as complete unless it can be verified.

## 6. Verification and Run Commands

Run the original story from the repository root.

**Linux or macOS**

```bash
python3 stories/09_games_evening/story.py
```

**Windows**

```powershell
py -3 stories/09_games_evening/story.py
```

Compare the output with the supplied `expected_output.txt`. The original `main()` and expected behaviour should remain intact.

Record the actual commands and results for the personal demonstrations and automated tests once their filenames and successful execution have been confirmed. Do not assume a demonstration or test has run successfully merely because its code is present.

## 7. Group Evaluation

Our group worked on *The Hostel Games Evening*, an object-oriented Python project that models a student games session. We combined the group's foundation contributions in `story.py` and confirmed that the combined story runs on the `main` branch.

The foundation tasks address game-choice inheritance, resource management, affordability checking, session-history reporting, cancellation and bundled game completion. These features provide practical experience with classes, objects, inheritance, method overriding, encapsulation and collaboration when integrating code.

We selected three advanced extensions: A2, custom exceptions and strict game requests; A3, JSON-based saving and loading; and A4, a choice factory and separation of responsibilities. These extensions are intended to improve error handling, persistence, extensibility and maintainability while preserving the existing story interface.

One important challenge was bringing several members' contributions together in the same project. We addressed integration by combining the code into the shared `story.py` file and merging work into the group's `main` branch. The group confirmed that the resulting story runs.

Further evidence is still needed in this document for individual demonstrations, automated test results, later-topic contributions and the required teammate review comments. These should be verified and recorded before the final submission so that the evaluation accurately reflects the completed work.

## 8. Group Repository

https://github.com/aheebwaabraham78/ucu-oop-class-examples
