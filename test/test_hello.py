from v2_hello_function import hello


def test_argument():
    assert hello("David") == "Hello, David"


def test_default():
    assert hello() == "Hello, world"

