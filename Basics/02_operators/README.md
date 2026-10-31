# 02 — Operators

Arithmetic, comparison, logic, membership, identity and bitwise operators — with the handful of places where they quietly surprise you.

## Notebooks

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_operators.ipynb`](./01_operators.ipynb) | `/` vs `//` vs `%`, the negative-number trap, float-money bug and paise, `==` vs `is`, short-circuiting, membership, assignment operators, permission flags with bitwise operators, precedence; capstone: an integer-paise fee calculator |
| 2 | [`02_practice.ipynb`](./02_practice.ipynb) | 9 self-checking exercises (divmod, leap year, gate pass, peak hours, flags, rupees→paise, capped fine) |
| 3 | [`03_solutions.ipynb`](./03_solutions.ipynb) | Reference answers that pass the same checks |

## Why this order

Operators come right after types because **an operator's behaviour depends on the type** of what it's applied to. With the name-tag model from the previous notebook you can now see *why* `+=` on a list differs from `+`, and why `is` and `==` are different questions. It also sets up conditionals: every `if` condition is built from the operators in this folder.

## The running example

Everything in Python Basics builds one small system: **Iron Gym** - a front desk, a fee list, a gate and an attendance sheet. This folder's capstone: **a fee calculator in whole paise with GST, discount, grace days and a capped late fine**.

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

- Predict `-7 // 2`, `-7 % 3` and `int(-7 / 2)` and explain why they differ.
- Explain why `19.99 * 100` is not `1999` and name two ways to avoid the bug.
- Say when to use `==` and when to use `is` — and why `is 5` is a bug.
- Use `or` for defaults and explain short-circuit evaluation.
- Grant, check, revoke and toggle flags with `|`, `&`, `& ~` and `^`.

## Next

[`03_conditionals/`](../03_conditionals) — turning these yes/no answers into decisions.
