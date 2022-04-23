import pytest

from src.artis import utils


@pytest.fixture
def get_string():
    return "Hello"


def test_cart_to_polar():

    cart = (1, 0)

    want = (1, 0)
    have = utils.cart_to_polar(cart)

    assert want == have


@pytest.mark.great
def test_dummy():
    assert True


def test_string(get_string):
    assert get_string == "Hello"


def test_string_conf(get_string_conf):
    assert get_string_conf == "Bye"


@pytest.mark.parametrize("cart, output", [((1, 0), (1, 0))])
def test_multiplication_11(cart, output):

    assert utils.cart_to_polar(cart) == output


@pytest.mark.skip
def test_skipping_this():
    assert False


@pytest.mark.xfail
def test_running_but_not_break():
    assert False


def test_empty_dir(tmp_path):

    CONTENT = "Hello"

    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
