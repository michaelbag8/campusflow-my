# CampusFlow — AI-Native Engineering Sprint

**A Python Command-Line Helpdesk Ticket Management System**

> A six-hour, two-person engineering challenge focused on building a working product, learning with AI, testing carefully, and collaborating professionally through GitHub.

## 1. Project Overview

### The Problem

Learn2Earn campus staff receive technical support requests involving Wi-Fi outages, faulty laptops, broken development environments, and inaccessible platforms. When these problems are reported informally, requests can be lost, priorities can become unclear, and responsibility may not be assigned.

### Our Solution

**CampusFlow** is a Python command-line application that helps campus staff record technical problems, calculate their priorities, assign responsibility, track progress, and monitor unresolved issues.

The application uses ordinary Python business logic to calculate ticket priorities and JSON files to preserve ticket data between sessions.

### Project Goals

* Record and validate support tickets.
* Automatically generate unique ticket IDs.
* Calculate ticket priority using specified rules.
* Assign tickets to responsible staff members.
* Track ticket status from open to resolved.
* Display an ordered queue of unresolved tickets.
* Generate reports showing ticket totals and breakdowns.
* Save and reload tickets using JSON.
* Verify functionality with automated tests.
* Demonstrate responsible AI-assisted learning and professional GitHub collaboration.

## 2. Team Members and Responsibilities

Update the placeholders below with the actual names and GitHub usernames of both fellows.

| Team member       | Role                              | Main responsibilities                                                                                                                                       |
| ----------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Fellow A's Name] | Engineer A                        | Ticket creation, input validation, priority calculation, and related automated tests.                                                                       |
| [Fellow B's Name] | Engineer B                        | Ticket assignment, status workflow, work queue, reporting, and related automated tests.                                                                     |
| Both fellows      | Integration and quality assurance | Agree on function contracts, integrate JSON persistence, review each other's pull requests, maintain AI learning logs, and prepare the final demonstration. |

Both fellows must contribute real application code and tests on their own Git branches. Neither fellow should be responsible only for documentation or observation.

## 3. Technology Stack

* **Language:** Python 3
* **Interface:** Command-line interface (CLI)
* **Data storage:** JSON
* **Automated testing:** Python's built-in `unittest` module
* **Version control:** Git
* **Collaboration and code review:** GitHub
* **AI-assisted learning:** AI tools used for explanations, experimentation, debugging, and critical evaluation

The project uses Python's standard library. No web framework, database server, AI SDK, or API key is required.

## 4. Project Features

CampusFlow must provide the following seven features through a menu that continues running until the user chooses Exit.

### F1 — Create Tickets

Users can create a support ticket by providing:

* `title`: Description of the reported problem.
* `category`: Type of technical issue.
* `urgency`: Reported urgency level.
* `affected_users`: Number of users affected.

The application validates the input, calculates priority, generates a unique ID, and stores the new ticket.

### F2 — List and View Tickets

Users can display all tickets or inspect an individual ticket by its ID.

### F3 — Assign Tickets

Users can assign a ticket to a named staff member. Blank staff names and unknown ticket IDs must be rejected.

### F4 — Manage Ticket Status

Tickets use three main statuses:

* `open`: The issue has been reported.
* `in_progress`: An assigned staff member is working on the issue.
* `resolved`: The issue has been fixed.

An unassigned ticket cannot move into `in_progress`. A resolved ticket must be explicitly reopened, setting its status to `open`, before it can be modified again.

### F5 — Display the Work Queue

The queue displays unresolved tickets in this priority order:

1. Critical
2. High
3. Medium
4. Low

Tickets with the same priority are ordered by their numeric ticket IDs, from earliest to latest. Resolved tickets are excluded.

### F6 — Generate Reports

Reports display:

* Total number of tickets.
* Ticket counts grouped by status.
* Ticket counts grouped by priority.

Reports must work correctly when there are no tickets.

### F7 — JSON Persistence

Tickets are saved to JSON and reloaded when the application starts.

* A missing data file allows a fresh start.
* Malformed JSON produces a clear error rather than silently erasing data.
* Existing ticket IDs must be preserved.
* New tickets must receive unique IDs after a restart.

## 5. Ticket Data Structure

Each ticket contains the following eight required fields:

| Field            | Description              | Example                  |
| ---------------- | ------------------------ | ------------------------ |
| `id`             | Unique ticket identifier | `"T001"`                 |
| `title`          | Problem description      | `"Campus Wi-Fi is down"` |
| `category`       | Type of issue            | `"Network"`              |
| `urgency`        | Reported urgency         | `"high"`                 |
| `affected_users` | Number of affected users | `15`                     |
| `priority`       | Calculated priority      | `"critical"`             |
| `status`         | Current workflow status  | `"open"`                 |
| `assigned_to`    | Responsible staff member | `None`                   |

Example ticket:

```python
{
    "id": "T001",
    "title": "Campus Wi-Fi is down",
    "category": "Network",
    "urgency": "high",
    "affected_users": 15,
    "priority": "critical",
    "status": "open",
    "assigned_to": None,
}
```

### Validation Rules

* Ticket IDs must be unique and automatically generated.
* Allowed categories are `Network`, `Hardware`, `Software`, and `Other`.
* Allowed urgency levels are `low`, `medium`, and `high`.
* Titles must not be blank.
* `affected_users` must be a positive integer; zero, negative numbers, decimals, and text are invalid.
* Valid case variations must be normalized consistently.
* Invalid inputs must produce useful errors without corrupting stored tickets.

## 6. Priority Calculation Rules

Ticket priority is calculated using ordinary Python business logic. AI is not used to determine ticket priority at runtime.

The rules must be evaluated in the following order, applying the first matching rule.

| Rule | Condition                                   | Result     |
| ---- | ------------------------------------------- | ---------- |
| 1    | High urgency AND at least 10 affected users | `critical` |
| 2    | High urgency OR at least 10 affected users  | `high`     |
| 3    | Medium urgency OR at least 3 affected users | `medium`   |
| 4    | All remaining valid tickets                 | `low`      |

Examples:

| Urgency | Affected users | Expected priority |
| ------- | -------------: | ----------------- |
| High    |             12 | Critical          |
| High    |              2 | High              |
| Low     |             10 | High              |
| Low     |              4 | Medium            |
| Medium  |              1 | Medium            |
| Low     |              1 | Low               |

**Important:** The priority engine must check the rules in the specified order. Automated tests must verify the examples and boundary conditions.

## 7. Project Structure

The planned repository structure is:

```text
campusflow/
├── README.md
├── .gitignore
├── main.py
├── campusflow/
│   ├── __init__.py
│   ├── tickets.py
│   ├── workflow.py
│   ├── storage.py
│   └── reports.py
├── tests/
│   ├── test_tickets.py
│   ├── test_workflow.py
│   └── test_storage.py
└── docs/
    ├── ai-learning-log.md
    └── design-decisions.md
```

Additional test files, such as `tests/test_reports.py`, may be added when useful.

### Module Responsibilities

| File                       | Responsibility                                                                                                                |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `main.py`                  | Displays the menu, collects user input, calls application functions, handles user-facing errors, and coordinates persistence. |
| `campusflow/tickets.py`    | Validates ticket fields, calculates priority, and creates ticket records.                                                     |
| `campusflow/workflow.py`   | Assigns tickets, manages status transitions, retrieves tickets, and builds the work queue.                                    |
| `campusflow/storage.py`    | Generates unique IDs and loads and saves JSON data.                                                                           |
| `campusflow/reports.py`    | Calculates totals and breakdowns by status and priority.                                                                      |
| `tests/test_tickets.py`    | Tests ticket creation, input validation, and priority rules.                                                                  |
| `tests/test_workflow.py`   | Tests assignment, lifecycle rules, ticket retrieval, and queue ordering.                                                      |
| `tests/test_storage.py`    | Tests JSON persistence, missing files, malformed JSON, and ID uniqueness after reload.                                        |
| `docs/design-decisions.md` | Records agreed function contracts, data structures, and design decisions.                                                     |
| `docs/ai-learning-log.md`  | Records each fellow's verified AI learning interactions.                                                                      |

Runtime data, including `data/tickets.json`, must not be committed to Git.

## 8. Installation and Setup

### Prerequisites

Install Python 3 and Git. Python 3.10 or later is a suitable baseline for this project structure.

Verify the installations:

```bash
python --version
git --version
```

Depending on your operating system, you may need to use `python3` instead of `python`.

### Clone the Repository

Replace the URL with your team's actual GitHub repository URL.

```bash
git clone <repository-url>
cd <repository-folder>
```

### Optional: Create a Virtual Environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

CampusFlow uses the Python standard library, so installing external packages should not be necessary.

## 9. Running CampusFlow

From the project root, run:

```bash
python main.py
```

The CLI should present a menu containing the following options:

1. Create a ticket.
2. List all tickets.
3. View a ticket by ID.
4. Assign a ticket.
5. Change ticket status.
6. Reopen a resolved ticket.
7. Display the work queue.
8. Generate a report.
9. Exit.

The menu must remain available until the user chooses Exit.

**Implementation status:** The menu describes the required interface. Confirm that each option is implemented and working before treating the application as complete.

## 10. Running Automated Tests

CampusFlow uses Python's built-in `unittest` framework.

Run the complete test suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

The test suite should cover:

* Successful ticket creation.
* Priority calculation and rule boundaries.
* Invalid input rejection.
* Assignment and unknown ticket IDs.
* Status transitions and assignment requirements.
* Reopening resolved tickets.
* Work queue priority ordering and numeric ID tie-breaking.
* Correct reports, including an empty ticket list.
* JSON save-and-load behavior.
* Unique ticket IDs after reloading existing tickets.

At least eight meaningful automated tests must pass on the integrated `main` branch.

**Test results:** Record the actual command output and number of passing tests after running the suite. Do not report tests as passing unless they have been executed successfully.

## 11. Data Persistence and Resetting

CampusFlow stores tickets in a JSON file, planned as:

```text
data/tickets.json
```

The storage module is responsible for loading and saving ticket records. The CLI coordinates saving after successful changes.

### Expected Behavior

* When the data file exists and contains valid JSON, load the saved tickets.
* When the data file is missing, start with an empty ticket collection.
* When the data file is malformed, display a clear error and preserve the original file.
* When a ticket is created after reloading, generate an ID that does not duplicate an existing ID.
* When the application saves and restarts, ticket assignments and statuses must be preserved.

### Starting Fresh

To start a new local dataset, first stop the application and back up any data you want to keep. Then remove the local runtime file:

```text
data/tickets.json
```

The next startup should begin with an empty ticket collection, provided the application implements the missing-file behavior described above.

Do not delete the data file merely to work around a malformed JSON error; investigate the error and preserve the data first.

## 12. Git and GitHub Collaboration

Both fellows must contribute through their own feature branches and pull requests.

### Branch Naming

Use descriptive branch names tied to actual GitHub Issues.

Examples:

```text
feat/1-ticket-creation
feat/2-status-workflow
fix/7-invalid-status-transition
test/8-ticket-validation
docs/9-readme-setup
```

Replace the example issue numbers with real issue numbers from your repository.

### Recommended Workflow

1. Create or select a GitHub Issue with clear acceptance criteria.
2. Update the local `main` branch.
3. Create a feature branch.
4. Implement a small feature and its tests.
5. Inspect changes with `git status` and `git diff`.
6. Commit meaningful changes.
7. Push the branch to GitHub.
8. Open a pull request against `main`.
9. Request review from the other fellow.
10. Address blocking review feedback and obtain approval.
11. Merge only after the required review and tests.
12. Update the other feature branch from the latest `main` and rerun tests when necessary.

Useful commands:

```bash
git switch main
git pull origin main
git switch -c feat/1-ticket-creation

git status
git diff
git add campusflow/tickets.py tests/test_tickets.py
git commit -m "feat: implement ticket creation"
git push -u origin feat/1-ticket-creation
```

Do not commit directly to `main`, expose secrets, fabricate review evidence, or merge unreviewed changes.

### Pull Request Requirements

Each fellow must:

* Author at least one feature pull request.
* Review the other fellow's pull request.
* Inspect the actual implementation and tests.
* Leave at least two substantive review observations.
* Request changes when blocking problems exist.
* Approve only after the final changes have been reviewed.
* Ensure the integrated application and tests work after merging.

### Pull Request Links

Add the actual links when the pull requests exist.

* Engineer A's pull request: [Add PR link]
* Engineer B's pull request: [Add PR link]
* Repository: [Add GitHub repository URL]

## 13. AI-Assisted Learning and Verification

AI is a learning partner, not a replacement for engineering understanding.

Each fellow must record at least three meaningful AI learning interactions in `docs/ai-learning-log.md`. At least one interaction must document an AI suggestion that was independently corrected, improved, or rejected after verification.

### Required Learning Cycle

1. Identify a concept or problem you do not fully understand.
2. Record your initial understanding and the specific question.
3. Ask AI for an explanation or a small, unrelated example.
4. Predict the result of an experiment before running it.
5. Run the experiment or test independently.
6. Verify the result using observed output, automated tests, or reliable documentation.
7. Explain what you learned in your own words.
8. Record whether you accepted, improved, or rejected the AI guidance.

### Suggested Learning Topics

* Python exceptions and input validation.
* JSON serialization and deserialization.
* Unit testing with `unittest`.
* Sorting and stable ordering.
* Git branches and merge conflicts.
* Code review and test design.

### Evidence Requirements

Each fellow's log should include the actual prompt, useful guidance, independent experiment, verification result, decision, and a related file, commit, test, or pull request where applicable.

Do not invent experiments or claim verification that did not happen. Each fellow must be able to explain their learning without simply repeating AI-generated text.

## 14. Design Decisions

The team should document its shared technical agreements in `docs/design-decisions.md`.

At minimum, record:

* The ticket dictionary structure.
* How the ticket collection is shared between functions.
* Function return values and error-handling conventions.
* Which module owns JSON loading and saving.
* How unique ticket IDs are generated.
* Which module owns each feature.
* How the application can be tested without interactive input.
* How the team resolves integration issues and reviews changes.

Keeping these agreements explicit helps both fellows implement compatible features on separate branches.

## 15. Acceptance Criteria and Definition of Done

CampusFlow is complete only when the team can demonstrate all of the following.

### Functionality

* [ ] All seven features are available through the CLI menu.
* [ ] Valid tickets are created with all required fields.
* [ ] Ticket IDs are unique and automatically generated.
* [ ] Priority calculation follows the exact specified rule order.
* [ ] Invalid ticket data is rejected with useful errors.
* [ ] Assignment rejects blank staff names and unknown IDs.
* [ ] An unassigned ticket cannot move into `in_progress`.
* [ ] Tickets follow the required lifecycle and explicit reopen rule.
* [ ] The work queue excludes resolved tickets and sorts correctly.
* [ ] Reports contain correct totals and breakdowns, including for zero tickets.
* [ ] JSON data survives a restart.
* [ ] Malformed JSON is handled without silently erasing saved data.
* [ ] IDs remain unique after reloading existing tickets.

### Testing and Reliability

* [ ] At least eight meaningful automated tests pass.
* [ ] Tests include normal cases, invalid inputs, and boundary conditions.
* [ ] The full test suite passes on the integrated `main` branch.
* [ ] The team has tested JSON round-trip persistence and ID uniqueness after reload.
* [ ] Invalid operations do not corrupt ticket data.

### Collaboration and Learning

* [ ] Both fellows contributed application code and tests.
* [ ] Each fellow authored a pull request.
* [ ] Each fellow reviewed the partner's pull request.
* [ ] Both pull requests have genuine review, approval, and merge evidence.
* [ ] Each fellow has at least three verified AI learning log entries.
* [ ] Each fellow documented one AI suggestion that was corrected, improved, or rejected.
* [ ] `docs/design-decisions.md` and `docs/ai-learning-log.md` are committed.

### Final Demonstration

The team should demonstrate the following sequence:

1. Create several tickets with different priorities.
2. Show the calculated priorities.
3. Attempt an invalid input and explain the error.
4. Assign a ticket to a staff member.
5. Progress the ticket through its lifecycle.
6. Demonstrate rejection of an invalid status transition.
7. Display the ordered work queue and reports.
8. Save tickets, restart the application, and verify the data reloads correctly.
9. Run the full automated test suite.
10. Show both pull requests, partner reviews, and AI learning evidence.

Both fellows must explain their own implementation decisions and relevant tests.

## 16. Known Limitations and Future Improvements

This is a time-limited educational prototype, not a production helpdesk platform.

Potential future improvements include:

* Staff accounts and authentication.
* Ticket search and filtering.
* Audit logs for assignment and status changes.
* More detailed ticket descriptions and timestamps.
* Configurable staff teams and assignment rules.
* Exportable reports.
* A graphical or web interface.
* More comprehensive integration testing.

These are possible extensions, not requirements for the six-hour sprint. The priority is to implement and verify the required CLI features first.

**Current implementation status:** Confirm the actual state of the code, tests, and integrations before listing any feature as completed. Document remaining gaps honestly.

## 17. Final Submission Information

Complete this section before submitting the project.

| Submission item           | Evidence                                     |
| ------------------------- | -------------------------------------------- |
| GitHub repository         | [Add repository URL]                         |
| Engineer A's pull request | [Add PR URL]                                 |
| Engineer B's pull request | [Add PR URL]                                 |
| Full test-suite result    | [Record actual command output or result]     |
| AI learning log           | `docs/ai-learning-log.md`                    |
| Design decisions          | `docs/design-decisions.md`                   |
| Final demonstration       | [Add recording or evidence link if required] |

### Individual Reflection

Each fellow should independently answer:

1. Which feature did I personally implement, and how do I know it works?
2. What did AI teach me that I did not understand at the beginning?
3. Which AI suggestion did I verify, improve, or reject, and why?
4. What did I learn from reviewing my partner's pull request?
5. What would I improve if I had another hour?

---

## Final Principle

**AI is your learning partner, Git is your collaboration tool, and a pull request is an invitation to review—not automatic approval.**

CampusFlow succeeds when both fellows understand what they have built, verify their work with tests, collaborate professionally, and demonstrate the application with genuine evidence.

*Adapted from the Fellows' Engineering Guide — AI-Native Engineering Sprint, CampusFlow.*
