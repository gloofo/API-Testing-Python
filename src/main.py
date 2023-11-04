from src.modules import * 
from src.helpers import *

#get all the product lists
def All_Products():
	response = make_REQUEST('GET', '/productsList')
	status = response.json()['responseCode']
	assert response.status_code == status

#POST should not work but status should be 200 --
def POST_All_Products():
	response = make_REQUEST('POST', '/productsList')
	status = response.json()['responseCode']
	assert response.status_code == 200
	assert status == 405
	verify_Message('not supported', response)

#gets all the brands lists
def All_Brands():
	response = make_REQUEST('GET', '/brandsList')
	status = response.json()['responseCode']
	assert response.status_code == status

def PUT_All_Brands():
	response = make_REQUEST('PUT', '/brandsList')
	status = response.json()['responseCode']
	assert response.status_code == 200
	assert status == 405
	verify_Message('not supported', response)

#search a product eg: 'tshirt', 'tops', 'dress'
def Search_Product():
	param = {'search_product': 'tshirt'}
	response = make_REQUEST('POST', '/searchProduct', getData=param)
	status = response.json()['responseCode']
	assert response.status_code == status

#search a product without a parameter
def Search_Without_Parameter():
	response = make_REQUEST('POST', '/searchProduct')
	status = response.json()['responseCode']
	assert response.status_code == 200
	assert status == 400
	verify_Message('Bad request', response)

#creates or register a new user
def CREATE_User():
	password = generate().password()
	email = generate().email()
	params = details(email, password)
	response = make_REQUEST('POST', '/createAccount', getData=params)
	status = response.json()['responseCode']
	assert response.status_code == 200
	assert status == 201
	verify_Message('created', response)
	return email, password

#pre-requisite: need to create user in order to veriry login or login.
def VALID_Login(valid=True):
	creds = CREATE_User()
	params = {'email': creds[0], 'password': creds[1]}
	response = make_REQUEST('POST', '/verifyLogin', getData=params)
	status = response.json()['responseCode']
	assert response.status_code == status
	verify_Message('exists!', response)

#login without a password
def No_Pass_Login():
	creds = CREATE_User()
	params = {'password': creds[1]}
	response = make_REQUEST('POST', '/verifyLogin', getData=params)
	status = response.json()['responseCode']
	assert response.status_code == 200
	assert status == 400
	verify_Message('Bad request', response)

#request should not work but status should be 200
def DELETE_Verify_login():
	response = make_REQUEST('DELETE', '/verifyLogin' )
	status = response.json()['responseCode']
	assert response.status_code == 200
	assert status == 405
	verify_Message('not supported', response)

#login with non existent credentials
def INVALID_Login():
	params = {'email': generate().email(), 'password': generate().password()}
	response = make_REQUEST('POST', '/verifyLogin', getData=params)
	status = response.json()['responseCode']
	assert status == 404
	verify_Message('not found!', response)

#delete an existing user/account
def DELETE_Account():
	creds = CREATE_User()
	params = {'email': creds[0], 'password': creds[1]}
	response = make_REQUEST('DELETE', '/deleteAccount',  getData=params)
	status = response.json()['responseCode']
	assert response.status_code == status
	verify_Message('deleted!', response)

#updates/edit a user
def UPDATE_User():
	creds = CREATE_User()
	password = creds[1]
	email = creds[0]
	params = details(email, password)
	response = make_REQUEST('PUT', '/updateAccount', getData=params)
	status = response.json()['responseCode']
	assert response.status_code == status
	verify_Message('updated!', response)
	return email

#shows the user account details
def GET_User_details():
	email = UPDATE_User()
	print(email)
	param = {'email': email}
	response = make_REQUEST('GET', '/getUserDetailByEmail', param=param)
	status = response.json()['responseCode']
	assert response.status_code == status
	assert email == response.json()['user']['email']
