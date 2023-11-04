### What does this thing do?

-- Automates the following API:
- **GET** All Products List
- **POST** To All Products List
- **GET** All Brands List
- **PUT** To All Brands List
- **POST** To Search Product
- **POST** To Search Product without search_product parameter
- **POST** To Verify Login with valid details
- **POST** To Verify Login without email parameter
- **DELETE** To Verify Login
- **POST** To Create/Register User Account
- **DELETE** To Delete User Account
- **PUT** To Update User Account
- **GET** user account detail by email


-- Please refer to API TESTING url:
https://automationexercise.com/api_list


### Project Dependencies
---------------------

- *`requests`*
- *`pyyaml`*
- *`pytest`*
- *`Faker`*


### Installation
---------------------
**Clone repository**
> git clone https://github.com/gloofo/API-Testing-Python

**Install dependencies:**
> pip install -r requirements.txt

Run:
> pytest -v -rA
