from dotenv import load_dotenv
import pytest
from requests.auth import HTTPBasicAuth
import requests
from samples import beans_tokens
import os

load_dotenv()

def test_list_rule_type(base_url):
    url = base_url+"liana/rule_type/"
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.get(url, auth=auth)
    j = response.json()
    breakpoint()
    assert response.status_code == 200

def test_create_rule_type(base_url):
    url = base_url+"liana/rule_type/"
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    rule_type_data = beans_tokens["rule_type_data"]
    response = requests.post(url, auth=auth, data=rule_type_data)
    j = response.json()
    breakpoint()
    assert response.status_code == 201
    
