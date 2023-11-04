from src.modules import *

def make_REQUEST(method, endpoint, param=None, headers=None, getData=None, json=None):
    response = requests.request(
        method,
        data('base') + 
        endpoint,
        params=param,
        headers=headers,
        data=getData,
        json=json)
    
    return response

def verify_Message(text, response):
    assert text in response.json()['message']

def details(email, password):
    return {
		'name': generate().name(),
		'email': email,
		'password': password,
		'title': generate().prefix(),
		'birth_date': generate().day_of_month(),
		'birth_month': generate().month(),
		'birth_year': generate().year(),
		'firstname': generate().first_name(),
		'lastname': generate().last_name(),
		'company': generate().company(),
		'address1': generate().address(),
		'address2': generate().address(),
		'country': generate().country(),
		'zipcode': generate().zipcode(),
		'state': generate().state(),
		'city': generate().city(),
		'mobile_number': generate().phone_number()
	}