#def setup_function(function): for function
def setup_module(module):
    print("launch browser")

#def teardown(function): for function
def teardown_module(module):
    print("Close browser")

def test_one():
    print("one")

def test_two():
    print("two")

def test_three():
    print("three")