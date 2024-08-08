import pytest

from Common_files import Excel_reader

excel_file_path = "C:Users\\Madhu Kumar PSI-3442\\Desktop\\Practice.xlsx"
sheet1 = "Sheet1"
@pytest.mark.parametrize("username,password", Excel_reader.Extract_Excel_data(excel_file_path, sheet1))
def test_login(username,password):
    print("logged in username is "+username+" logged in user password is "+password)
