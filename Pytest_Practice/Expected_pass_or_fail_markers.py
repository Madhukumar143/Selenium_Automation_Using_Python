import pytest


@pytest.mark.smoke
#to skip add this @pytest.mark.skip
def test_method_one():
    print("Madhu")

@pytest.mark.xfail
def test_method_two():
    print("Be yourself")
    assert  False

@pytest.mark.xfail
def test_method_three():
    print("Be Confident")
