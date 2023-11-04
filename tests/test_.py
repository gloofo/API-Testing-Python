from src.main import *

def test_GET_All_Products():
	All_Products()

def test_POST_All_Products():
	POST_All_Products()

def test_GET_All_Brands():
	All_Brands()

def test_PUT_All_Brands():
	PUT_All_Brands()

def test_Search_Product():
	Search_Product()

def test_Search_Product_No_Parameter():
	Search_Without_Parameter()

def test_CREATE_User():
	CREATE_User()

def test_VALID_Login():
	VALID_Login()

def test_Login_No_Pass():
	No_Pass_Login()

def test_Delete_Logi():
	DELETE_Verify_login()

def test_Invalid_Login():
	INVALID_Login()

def test_DELETE_User():
	DELETE_Account()

def test_UPDATE_Account():
	UPDATE_User()

def test_show_user_details():
	GET_User_details()
