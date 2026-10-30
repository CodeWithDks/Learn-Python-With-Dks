# 01 — Variables & Data Types

Every program starts here: what a variable really is, what kinds of values exist, and how to convert between them without crashing.

## Notebooks

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_variables_and_datatypes.ipynb`](./01_variables_and_datatypes.ipynb) | Names vs boxes, mutable vs immutable, the five everyday types, conversion at the edge, truthy/falsy, f-string formatting, naming rules; capstone: an Iron Gym membership receipt |
| 2 | [`02_practice.ipynb`](./02_practice.ipynb) | 8 self-checking exercises (type conversion, swap, GST, formatting, truthiness, aliasing, a member card) |
| 3 | [`03_solutions.ipynb`](./03_solutions.ipynb) | Reference answers that pass the same checks |

## Why this order

Variables and types come first because **every later bug is a type bug in disguise**: a string where you wanted a number, a list changed through a second name, a `None` where you expected text. Operators and conditionals only make sense once you know what kind of thing they're operating on.

## The running example

Everything in Python Basics builds one small system: **Iron Gym** - a front desk, a fee list, a gate and an attendance sheet. This folder's capstone: **a membership receipt built from messy text inputs**.

## Prerequisites

Python 3.10 or newer (`match`/`case` appears in the Conditionals notebook). No installs, no API keys.

```bash
python --version
jupyter notebook
```

## Running

Open `01_*.ipynb` and run cells top to bottom - each notebook is self-contained. Then do `02_practice.ipynb` (self-checking), and only then peek at `03_solutions.ipynb`.

> Your earlier `theory.py` and `practice/` files in this folder are untouched - the notebooks are the upgraded, practice-first version of the same topic.

## What you should be able to do after this folder

- Explain the "name tag" model and predict what `b = a` does for both an `int` and a `list`.
- Convert raw text to the right type once, at the edge, and explain why `int("25.5")` fails but `int(25.9)` doesn't.
- Say which of `0`, `"0"`, `[]`, `[0]`, `None` are falsy — without running them.
- Format any value with width, alignment, thousands separators and decimals using an f-string.
- Make a real copy of a list and prove it's independent.

## Next

[`02_operators/`](../02_operators) — arithmetic, comparison and logic, and the float-money trap.
