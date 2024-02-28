from requests.auth import HTTPBasicAuth
import pytest
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def test_retrieve_account(base_url):
    beans_first_name = "NACHIROU"
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    url = base_url + "liana/account/"
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.get(url=url, auth=auth)
    account_data = response.json()
    assert response.status_code == 200
    assert beans_first_name == account_data["data"][0]["first_name"]
