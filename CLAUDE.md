# CLAUDE.md — Network Automation Repository

## Overview

Despite the repository name (`network_automation`), this is a **Python learning repository** that tracks progress through *Python Crash Course* (by Eric Matthes). It contains standalone exercise scripts organized by book chapter, with no network automation code present yet.

**Current progress:** Chapters 1–10 (Files and Exceptions — in progress)

---

## Repository Structure

```
network_automation/
├── scripts/
│   ├── main.py                              # PyCharm default entry point (boilerplate)
│   ├── Chapter 1 - Getting Started/
│   ├── Chapter 2 - Variables and Simple Data Types/
│   ├── Chapter 3 - Lists/
│   ├── Chapter 4 - Working with Lists/
│   ├── Chapter 5 - if Statements/
│   ├── Chapter 6 - Dictionaries/
│   ├── Chapter 7 - User Input and While Loops/
│   ├── Chapter 8 - Functions/
│   ├── Chapter 9 - Classes/
│   └── Chapter 10 - Files and Exceptions/
└── .idea/                                   # PyCharm project config (not relevant to code)
```

Each chapter directory contains:
- Worked examples from the book (e.g. `car.py`, `restaurant.py`, `pizza.py`)
- Exercise files named by exercise number (e.g. `9-3 - users.py`, `8-1 - message.py`)
- `try_it_yourself.py` files for scratch exploration

---

## Code Conventions

- **Python 3** throughout — no Python 2 compatibility
- **f-strings** are the standard string formatting style (not `.format()` or `%`)
- **snake_case** for variables and function names
- **PascalCase** for class names
- No external dependencies — standard library only (`random`, `string`, `pathlib`, etc.)
- No `requirements.txt`, virtual environment, or package management in use
- No test suite (exercises are run directly and verified by visual output)
- Docstrings present on many class methods; single-line `# comments` used for inline notes

### File naming

Files follow two patterns:
- Descriptive names: `car.py`, `restaurant.py`, `printing_models.py`
- Exercise numbers: `9-3 - users.py`, `8-10 - sending messages.py`

Some filenames contain spaces (e.g. `"electric car.py"`, `"pizza toppings.py"`) — preserve this where it exists; prefer underscores in new files.

---

## Key Concepts by Chapter

| Chapter | Topics | Notable Files |
|---------|--------|---------------|
| 1 | Hello World | `hello_world.py` |
| 2 | Variables, strings, numbers | `full_name.py`, `numbers.py`, `strip.py` |
| 3 | Lists, indexing, sorting | `lists.py`, `cars.py`, `guest_list.py` |
| 4 | Loops, slices, tuples | `magicians.py`, `numbers.py`, `tuples.py` |
| 5 | if/elif/else, conditionals | `age.py`, `cars.py`, `toppings.py` |
| 6 | Dictionaries, nesting | `aliens.py`, `favorite_languages.py`, `user.py` |
| 7 | input(), while loops | `parrot.py`, `mountain_poll.py`, `greeter.py` |
| 8 | Functions, \*args, \*\*kwargs, modules | `printing_models.py`, `user_profile.py`, `pizza.py` |
| 9 | Classes, inheritance, modules | `car.py` (Car/Battery/ElectricCar), `restaurant.py`, `privileges.py` |
| 10 | File I/O with `pathlib.Path` | `file_reader.py`, `pi_digits.txt` |

### Chapter 9 class hierarchy (most complex code in the repo)

```
Car
├── ElectricCar(Car)   — adds Battery composition
└── (other subclasses in exercises)

Restaurant
└── (subclassed in exercises like IceCreamStand)
```

`car.py` is imported by `my_car.py` and `my_electric_car.py` as a module import example.
`restaurant.py` is imported by `e_restaurant.py` and `9-10 - imported restaurant.py`.

---

## Development Environment

- **IDE:** PyCharm (`.idea/` config present; run configs in `.idea/runConfigurations/`)
- **Python:** 3.x (no version pin file present)
- **No build system, linter, formatter, or CI/CD pipeline**

### Running scripts

Each script is standalone and run directly:

```bash
python "scripts/Chapter 9 - Classes/car.py"
python scripts/main.py
```

Note: many example files have their `main` execution code commented out (e.g. `car.py` lines 76–83). Un-comment to run.

---

## Git Workflow

- **Main branch:** `main` (remote), `master` (local tracking)
- **Commit style:** Short, chapter-based messages — e.g. `Chapter 9 - Progress`, `Chapter 10 - Progress`
- All commits go directly to the main/master branch; no PRs or feature branches in normal workflow

---

## What Does Not Exist (yet)

The following are absent from the current codebase:
- No actual network automation code (Netmiko, NAPALM, Nornir, Paramiko, etc.)
- No tests (`unittest`, `pytest`)
- No `requirements.txt` or `pyproject.toml`
- No `.env` or configuration files
- No CI/CD (GitHub Actions, etc.)
- No `__init__.py` files (scripts are not packaged as modules)

---

## Guidance for AI Assistants

1. **Scope:** Keep changes aligned with the chapter being worked on. Don't introduce external libraries or abstractions beyond what the textbook covers at that point.
2. **Style:** Match the existing minimal, educational style — short scripts, descriptive variable names, f-strings, inline comments where logic is non-obvious.
3. **File placement:** New exercise files belong in the appropriate `scripts/Chapter N - Name/` directory.
4. **No over-engineering:** These are learning exercises. Avoid adding error handling, type hints, or abstractions not called for by the exercise.
5. **Filenames:** Follow existing naming conventions (exercise number prefix for exercises, descriptive names for standalone examples).
6. **Module imports:** Chapter 9 introduces importing classes across files — preserve the existing import structure (`from car import Car`, `from restaurant import Restaurant`).
7. **Commented-out code:** The repo uses comments to disable example runs. This is intentional; don't remove commented code unless explicitly asked.
