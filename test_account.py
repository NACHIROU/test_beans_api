from requests.auth import HTTPBasicAuth
import pytest
import requests
import json
import os
from dotenv import load_dotenv
from samples import beans_tokens

load_dotenv()

def test_retrieve_account(base_url):
    beans_first_name = os.getenv("BEANS_FIRSTNAME")
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    id = os.getenv("BEANS_ID")
    url = base_url + "liana/account/" + str(id)
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.get(url=url, auth=auth)
    account_data = response.json()
    breakpoint()
    assert response.status_code == 200
    assert account_data["id"]== id


def test_list_account(base_url):
    beans_first_name = os.getenv("BEANS_FIRSTNAME")
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    url = base_url + "liana/account/"
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.get(url=url, auth=auth)
    account_data = response.json()
    assert response.status_code == 200

def test_create_account(base_url):
    beans_first_name = os.getenv("BEANS_FIRSTNAME")
    beans_last_name = os.getenv("BEANS_LASTNAME")

    account_data = beans_tokens["account_data"]

    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")

    url = base_url + "liana/account/"
    response = requests.post(url, json=account_data, auth=auth)
    new_data = response.json()
    assert response.status_code == 201
    # assert beans_first_name == new_data["first_name"]
    # assert beans_last_name == new_data["last_name"]


def test_update_account(base_url):
    id = os.getenv("BEANS_ID")
    url = base_url + f"liana/account/{id}/"

    new_account_data = beans_tokens["new_account_data"]
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")

    response = requests.put(url, auth=auth, data=new_account_data)

    assert response.status_code == 202