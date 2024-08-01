import pytest
@pytest.mark.parametrize("username,password",[("Madhu","Test@1234"),("Manoj","Test@1235"),("Manogna","Test@1236"),("Kalyan","Test@1236"),])
#to skip add this @pytest.mark.skip
def test_method_one(username,password):
    print(username," -> ",password)

