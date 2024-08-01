# to  run in terminal use pytest
# to  show output in terminal use Pytest -rA
# to generate xml report use  pytest -rA --junit-xml="junitXMLReport.xml" in terminal
import pytest


@pytest.mark.smoke
#to skip add this @pytest.mark.skip
def test_method_one():
    print("Madhu")

def test_method_two():
    print("Be yourself")

def test_method_three():
    print("Be Confident")
