# Testing

This documents some things around testing for python.
Uses pytest specifically.

```
Pytest is a python based testing framework, which is used
to write and execute test codes. In the present days of REST
services, pytest is mainly used for API testing even though
we can use pytest to write simple to complex tests, i.e.,
we can write codes to test API, database, UI, etc.
```

## Setup pytest in repo

Just add `pytest` to the requirements.

## Run

Running:

```
pytest
```

Will check current dir and sub dirs for files with names like `*_test.pt`
and `test_*.py`. Inside these files, functions with name like `test*` will
be executed as tests.

This setup is `pytest` default and is difficult to change.

To get the verbose version:

`pytest -v`

A single file can be tested by `pytest <file path>`.

## Example test

```
def test_function_x():
    assert True

```

This test would pass since the assertion works.

## Test part of test suite

There a a few ways to test a part of the test suite.

### By path

```
pytest <path to dir>
```

Will run tests for files in dir and subdir of
the specified directory.

### by substring in test name

```
pytest -k <substring>
```

Will run all tests where function name
has substring specified.

### using markers

Pytest supports markers to annotate test functions. This
is done via decorators:

```
@pytest.mark.<name of marker>
def test_nameoftest():
    assert True

```

If running `pytest -m <name of marker>` only the functions with the
relevant marker will be executed.

## Fixtures

A fixture is sort of a helper function that can be used in the tests.
Most often used when need to repeat code for many tests.

It replaces the standard `setup` and `teardown` patern.

The fixture is a decorated python function:

```
@pytest.fixture
def an_example_fixture():
    return "a value"

```

This can then be added as an input in test function:

```
def test_with_fixture(an_example_fixture):
    assert an_example_fixture == "a value"

```

Fixtures can be used to help out with data and database connections.

Mark that the fixture is not executed as a normal py function.
Instead, this is called just like a variable. This is called
dependency injection.

## scopes of fixtures

Default, the fixture will be executed in every function it is used
in. This is called a `function` scope. This might be inefficient.
The available scopes are:

- function (default)
- class
- module
- package
- session: run function 1 time per `pytest` execution

A session scoped fixture is probably more suited to be in `conftest.py`

## Conftest

The fixtures are file scoped. If we would like to have *fixtures* on
a wider scope, we should use `conftest`.

A fixture can be placed in `conftest.py` and will be automatically
found by pytest. A fixture in the actual test file will take prio
over a conftest specified one.

In the actual test file, test function can ref a fixture from a
conftest just like a normal fixture.

## Parametrization

Sometimes we want to test the same function with multiple different
inputs and outputs. This can be specified in code, but it is easier to user `pytest.mark.parametrize`.

```
@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output
```

## skipping tests

Pytest has built in markers for omitting tests functions.

by adding the decorator:

```
@pytest.mark.skip
```

The test will not be executed.

By adding the decorator:

```
@pytest.mark.xfail
```

will run test but does not take the result into account.

## tmpdir

Sometimes we want to create some filesystem objects as part of
test. This can be done in a temporary dir, using a fixture in
pytest called `tmpdir`.

## Refs

- [Tutorialspoint](https://www.tutorialspoint.com/pytest)
- [Pytest](https://docs.pytest.org/en/7.1.x/)
- [Scopes on pytest fixture scopes](https://betterprogramming.pub/understand-5-scopes-of-pytest-fixtures-1b607b5c19ed)
- [tmpdir](https://docs.pytest.org/en/6.2.x/tmpdir.html)
