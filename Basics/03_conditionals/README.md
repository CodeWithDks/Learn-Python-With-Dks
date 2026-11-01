# 03 — Conditionals

Turning yes/no answers into decisions — if/elif/else, guard clauses, truthiness, the ternary and `match`/`case` — with the focus on the one thing that causes real bugs: order.

## Notebooks

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_conditionals.ipynb`](./01_conditionals.ipynb) | First-match-wins and the ordering bug, guard clauses vs nesting, truthiness and the `0` trap, ternary, `match`/`case` with guards, independent `if`s; capstone: the Iron Gym gate with priority-ordered rules |
| 2 | [`02_practice.ipynb`](./02_practice.ipynb) | 9 self-checking exercises (status, plans, gate priority, ticket price, `or` defaults, None vs 0, `match`, BMI, triangles) |
| 3 | [`03_solutions.ipynb`](./03_solutions.ipynb) | Reference answers that pass the same checks |

## Why this order

Conditionals come after operators because every condition is built *from* operators — comparisons joined by `and`/`or`/`not`. They come before loops because a loop without a condition (`break`, `continue`, `while cond`) can't do anything useful.

## The running example

Everything in Python Basics builds one small system: **Iron Gym** - a front desk, a fee list, a gate and an attendance sheet. This folder's capstone: **the gate: one function, six rules, where the order of the checks is the priority**.

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

- Explain "first match wins" and fix a mis-ordered `elif` chain.
- Flatten a nested `if` pyramid into guard clauses.
- Choose between `if x:` and `if x is None:` — and say why `0` makes it matter.
- Write a ternary, and know when *not* to nest it.
- Write a `match` statement with literal, sequence and guard patterns.

## Next

[`04_loops/`](../04_loops) — repeating decisions over every member, every day.
