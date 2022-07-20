# Logic

This repository contains a simple project focusing on providing a framework of automatic formal deduction. The formality is based on **propositional logic** and it's main goal is to set the means of automatic logic formulas resolver.

---

## Project Structure

This project is structured as seen on the list below:

- `/.github` contains workflows for **GitHub Actions**. Currently, there is defined only one workflow starting unit tests (see [Testing](#testing-chap "Testing"))
- `/scripts` contains the actual project code
    - `/scripts/src` - the whole framework with all "*production*" code
    - `/scripts/testing` - unit tests definition


## Testing <a name="testing-chap" />

The automatic unit test definitions are groupped in a package `/scripts/tests`. To run these tests, just locate the terminal in the root of the repository and run

`python -m unittest`

These tests are also triggered by pushes and pull requests to `master` branch (supported by GitHub Actions).

---

## Terms

`Terms` or `Formulas` are the most general elements in propositional logic. These are meant to be virtually any structure the logical expression is built from.

## Atoms

## Logical Operators


## Axiomatic Transformations


## Environment


## String parsers

***Not supported yet***
