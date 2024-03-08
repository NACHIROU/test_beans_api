import pytest
import requests
import os
from dotenv import load_dotenv
from samples import beans_tokens
from requests.auth import HTTPBasicAuth

load_dotenv()


def test_list_rule(base_url):
    url = base_url + "liana/rule/"
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.get(url=url, auth=auth)
    j = response.json()
    assert response.status_code == 200


def test_create_rule(base_url):
    url = base_url + "liana/rule/"
    rule_data = beans_tokens["rule_data"]
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.post(url, auth=auth, data=rule_data)
    j = response.json()
    breakpoint()
    assert response.status_code == 201


def test_retrieve_rule(base_url):
    id = os.getenv("RULE_ID")
    url = base_url + "liana/rule/" + str(id)
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.get(url=url, auth=auth)
    json = response.json()
    breakpoint()
    assert response.status_code == 200


def test_update_rule(base_url):
    id = os.getenv("RULE_ID")
    url = base_url + "liana/rule/" + str(id)
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    new_rule_data = beans_tokens["new_rule_data"]
    response = requests.put(url, auth=auth, json=new_rule_data)
    json = response.json()
    breakpoint()
    assert response.status_code == 202


def test_delete_rule(base_url):
    id = os.getenv("RULE_ID")
    url = base_url + "liana/rule/" + str(id)
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.delete(url, auth=auth)
    assert response.status_code == 204
