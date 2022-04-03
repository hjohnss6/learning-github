# Pre-commit

Scripts that aim to run some traditional git server side checks
and formatting on client side instead. The usecase is to check
formatting, tests, etc. before even pushing to remote. This
speeds up the work for developers, but even more for reviewers.

Pre-commit hooks can be simple checks, but can also actively change
the code.

## How to setup

- install the pre-commit lib by `pip install pre-commit`
- setup in already existing git repo by `pre-commit install`.
This creates a `hooks` dir in the `.git` dir.
- create a `.pre-commit-config` file with the settings. (what to run)

## How to use

Can be triggered via:

- `pre-commit run`: This will run all actions
- `git commit`: will run actions on all staged

if the hooks do not go through the commit will not be done.

## configure


## Refs

- [pre-commit home page](https://pre-commit.com/)
