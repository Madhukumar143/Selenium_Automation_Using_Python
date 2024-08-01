# to  run in terminal use pytest
# to  show output in terminal use Pytest -rA
# to run specific method use pytest -k "one" -> it will run methods with one text
# to run specific method use pytest -k "one or two" -> it will run methods with one and two text
import pytest


def test_method_one():
    a = 5
    b = 4
    assert a>b, "This will not be printed as a is greater than b"
    print("Madhu")

@pytest.mark.xfail
def test_method_two():
    a = 5
    b = 4
    assert a < b, "This will  be printed as a is greater than b"
    print("Be yourself")

#@pytest.mark.xfail
def test_method_three():
    a = 5
    b = 5
    assert a.__eq__(b), "This will not be printed as a is equal to b"
    print("Be Confident")
