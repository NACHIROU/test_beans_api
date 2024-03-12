from dotenv import load_dotenv
import pytest
from requests.auth import HTTPBasicAuth
import requests
from samples import beans_tokens
import os

load_dotenv()


def test_list_rule_type(base_url):
    url = base_url + "liana/rule_type/"
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.get(url, auth=auth)
    j = response.json()
    assert response.status_code == 200


def test_create_rule_type(base_url):
    url = base_url + "liana/rule_type/"
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    rule_type_data = beans_tokens["rule_type_data"]
    response = requests.post(url, auth=auth, data=rule_type_data)
    j = response.json()
    assert response.status_code == 201


def test_retrieve_rule_type(base_url):
    id = os.getenv("RULE_TYPE_ID")
    url = base_url + "liana/rule_type/" + str(id)
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.get(url, auth=auth)
    j = response.json()
    assert response.status_code == 200


def test_update_rule_type(base_url):
    id = os.getenv("RULE_TYPE_ID")
    url = base_url + "liana/rule_type/" + str(id)
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    data = beans_tokens["new_rule_type_data"]
    response = requests.put(url, auth=auth, data=data)
    j = response.json()
    assert response.status_code == 200
