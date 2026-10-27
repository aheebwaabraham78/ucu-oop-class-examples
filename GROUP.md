# Group 3 — Catch-up Group C3

## Project Information

- **Project:** The Hostel Games Evening
- **Repository:** https://github.com/aheebwaabraham78/ucu-oop-class-examples
- **Group:** Catch-up Group C3
- **Foundation work:** All eight foundation tasks
- **Selected advanced extensions:** A2, A3 and A4
- **Default branch:** `main`

## 1. Group Members and Foundation Responsibilities

| No. | Full Name | Registration Number | University Access Number| Foundation Task |
|---:|---|---|---|---|---|
| 1 | Aheebwa Abraham | S24B13/042 | B30127| RacingGame subclass |
| 2 | Okello Mark | S24B13/050 | B30259| GameCredits.add_more(amount) |
| 3 | Mugabi Ernest | S25B13/062 | B34215| TriviaFromMemory |
| 4 | Ntare Ernest Karuhinda | S25B13/053 B34835| To be completed | affordable(choices, limit) |
| 5 | Namakula Zaina | S25B13/013 | B34603| GamesEvening.summary() |
| 6 | Obitre Warren Joshua | S25B13/041 | B34732| QuickPractice subclass |
| 7 | Nankwanga Fridah | M25B13/033 | B33240| GamesEvening.cancel_last() |
| 8 | Murwani Samuel | S26B13/145 | B41005| GamesEvening.complete_bundle(choices) |

Each member is responsible for implementing their assigned foundation task, providing a personal runnable demonstration, testing their contribution, and submitting their own foundation pull request.

## 2. Foundation Contribution Records

The following table records the evidence required for each member's foundation contribution. Links must point to the actual branches, commits and merged pull requests.

| Member | Branch Name | Commit Link | Merged Foundation PR | Demo and Verification |
|---|---|---|---|---|
| Aheebwa Abraham | To be added | To be added | To be added | To be verified |
| Okello Mark | To be added | To be added | To be added | To be verified |
| Mugabi Ernest | To be added | To be added | To be added | To be verified |
| Ntare Ernest Karuhinda | To be added | To be added | To be added | To be verified |
| Namakula Zaina | To be added | To be added | To be added | To be verified |
| Obitre Warren Joshua | To be added | To be added | To be added | To be verified |
| Nankwanga Fridah | To be added | To be added | To be added | To be verified |
| Murwani Samuel | To be added | To be added | To be added | To be verified |

## 3. Selected Advanced Extensions

The group has selected exactly three different advanced extensions from `stories/09_games_evening/ADVANCED_EXTENSIONS.md`.

1. **A2 — Custom exceptions and strict game requests**
2. **A3 — Save and load a games evening using JSON**
3. **A4 — Choice factory and separation of responsibilities**

These options extend the foundation implementation while retaining the original story, its `main()` entry point, and compatibility with existing foundation demonstrations.

Every member must contribute code or meaningful automated tests to at least one selected advanced option through their own later-topic pull request. Documentation or review comments alone do not satisfy this requirement.

### 3.1 A2 — Custom Exceptions and Strict Game Requests

**Objective**

Introduce specific exceptions for invalid game choices, invalid game requests and insufficient resources. Provide a strict game-session interface that rejects invalid or unaffordable requests before changing the resource balance or successful-game history.

**Required implementation**

- `GamesChoiceError` for a missing or invalid choice, such as `None`.
- `GamesRequestError` for an invalid request, including a negative calculated resource requirement.
- `GamesResourceError` for a valid choice that costs more than the available credits.
- A `StrictGamesEvening` subclass or service wrapping `GamesEvening`.
- A `safe_play(choice)` method that raises the appropriate exception before any unsuccessful request changes credits or history.
- Valid affordable requests delegate to the existing play functionality. Zero-cost choices remain valid.

**Demonstration and verification**

The demonstration must use specific `except` clauses for the custom exceptions and a `finally` message. Automated checks must trigger all three exception types, verify that refused attempts leave resources and successful history unchanged, and verify that a valid request succeeds.

**Responsible members:** To be recorded.

**Merged PR links:** To be added.

**Demo filename and command:** To be recorded after implementation.

**Test filename and command:** To be recorded after implementation.

### 3.2 A3 — Save and Load Using JSON

**Objective**

Allow a games evening to be saved to and restored from a JSON file, preserving the session's important state.

**Required implementation**

- Save the student details, remaining credits, successful-game history and relevant state introduced by the foundation features.
- Preserve recorded choices and their original saved costs in history entries.
- Use ordinary JSON-compatible data and explicit allowed type labels.
- Restore a new `GamesEvening` with a fresh resource object and compatible successful history.
- Support continued foundation behaviour after loading, including refunds based on the saved historical cost.
- Validate loaded data before making the restored session available.
- Do not use `eval` or execute arbitrary class names from the saved file.

**Demonstration and verification**

Use temporary files for automated checks. Verify a successful round trip, preservation of resources and history, and an additional action after loading. Also test a missing file, malformed JSON, and structurally invalid data such as a negative resource balance or unknown choice type. Loading failures must be clear and must not damage an existing running session.

**Responsible members:** To be recorded.

**Merged PR links:** To be added.

**Demo filename and command:** To be recorded after implementation.

**Test filename and command:** To be recorded after implementation.

### 3.3 A4 — Choice Factory and Separation of Responsibilities

**Objective**

Provide a common factory for creating supported game choices and improve the separation of responsibilities in the implementation.

**Required implementation**

- Implement `create_choice(key, **settings)`.
- Support at least `FootballGame`, `LudoRound` and `CheeringContest`.
- Document the settings required for each choice.
- Report unknown factory keys with a clear error.
- Keep callers working through the common choice interface rather than adding class-specific branches to the coordinator.
- Establish clear responsibilities for object creation, rule checking and display.
- Refactor at least one area to improve the Single Responsibility Principle and explain the improvement.

**Demonstration and verification**

Provide a runnable demonstration and at least six meaningful automated `unittest` checks. Tests must cover factory-created choices through a real caller, a refused request that leaves state unchanged, an unknown factory key and separate state between instances. Tests must assert results and state, not only printed output or object types.

**Responsible members:** To be recorded.

**Merged PR links:** To be added.

**Demo filename and command:** To be recorded after implementation.

**Test command:**

On Linux or macOS:

```bash
python3 -m unittest discover -s stories/09_games_evening -p "test_*.py"
```

On Windows:

```powershell
py -3 -m unittest discover -s stories/09_games_evening -p "test_*.py"
```

Confirm that the test runner discovers and executes the intended tests rather than reporting zero tests.


## 5. Pull Request Review Evidence

Every pull request must receive at least one useful review comment from every other member of the eight-person group before merging. This means seven teammate reviews per PR.

Reviews should identify a method, rule, test case or behaviour that was checked and explain what worked or what needs improvement. General comments such as "good" or "done" are insufficient.

Record actual review-comment links below.

| PR Author | Teammate Reviewer | Review Comment Link |
|---|---|---|
| To be recorded for each PR | To be recorded | To be added |

Repeat the entries as necessary so that all required teammate reviews for every PR are evidenced.

## 6. Verification and Run Commands

The exact demo and test commands must match the filenames and test files that actually exist in the repository.

### Original story

From the repository root, the expected command is:

```bash
python3 stories/09_games_evening/story.py
```

On Windows, if `python3` is unavailable, use:

```powershell
py -3 stories/09_games_evening/story.py
```

Verify that the original story runs and its output matches the supplied `expected_output.txt`. Do not change the original `main()` or expected output merely to accommodate an extension.

### Foundation demonstrations

Record the exact command for each member's actual demonstration file:

| Member | Demo File | Command | Result |
|---|---|---|---|
| Aheebwa Abraham | To be confirmed | To be confirmed | To be verified |
| Okello Mark | To be confirmed | To be confirmed | To be verified |
| Mugabi Ernest | To be confirmed | To be confirmed | To be verified |
| Ntare Ernest Karuhinda | To be confirmed | To be confirmed | To be verified |
| Namakula Zaina | To be confirmed | To be confirmed | To be verified |
| Obitre Warren Joshua | To be confirmed | To be confirmed | To be verified |
| Nankwanga Fridah | To be confirmed | To be confirmed | To be verified |
| Murwani Samuel | To be confirmed | To be confirmed | To be verified |

### Advanced demonstrations and automated checks

Record the actual runnable demo and test commands for A2, A3 and A4 after their files are available. Run all required demonstrations and automated checks on the combined `main` branch before submission.

## 7. Group Evaluation

To be completed after the group has verified the final implementation.

The evaluation must be no more than 250 words and describe:

- What the group built.
- The object-oriented programming concepts used.
- What worked successfully.
- The main difficulty and how the group handled it.
- Any remaining limitation.

The evaluation must describe the actual final work and test results rather than claim unverified features or tests are complete.

## 8. Final Submission Checklist

- [ ] All eight foundation tasks have been implemented and demonstrated.
- [ ] Every member's foundation contribution is evidenced by their own branch and PR.
- [ ] Exactly three advanced options, A2, A3 and A4, are recorded.
- [ ] Every member has made a meaningful code or automated-testing contribution to at least one selected advanced option.
- [ ] Every member has authored a later-topic PR containing their contribution.
- [ ] Every PR has useful comments from all seven of its author's teammates before merging.
- [ ] Required changes have been merged into the group's `main` branch.
- [ ] Every member's full name, access number, registration number and GitHub username are recorded.
- [ ] Branch, commit, merged PR and review-comment links are complete.
- [ ] The original story still runs and matches its expected output.
- [ ] All foundation and advanced demonstrations and automated checks work together on the final `main` branch.
- [ ] No unresolved merge-conflict markers remain.
- [ ] The group evaluation is complete and no more than 250 words.
- [ ] The final submission link points to the group's fork.

**Group repository:** https://github.com/aheebwaabraham78/ucu-oop-class-examples
