import requests
import pytest
import yaml
from faker import Faker

def generate():
    fake = Faker()
    return fake

def data(*keys):
    with open('resources/endpoints.yaml', 'r') as file:
        getData = yaml.load(file, Loader=yaml.FullLoader)

    for key in keys:
        getData = getData[key]
    
    return getData