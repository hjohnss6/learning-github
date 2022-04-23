import pytest


@pytest.fixture(scope="module")
def get_string_conf():
    return "Bye"
