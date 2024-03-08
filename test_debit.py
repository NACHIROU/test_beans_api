import pytest
import requests
import os
from samples import beans_tokens
from requests.auth import HTTPBasicAuth

# 409 a cause de repetition du meme type de donnes
def test_create_debit(base_url):
    url = base_url + "liana/debit/"
    debit_data = beans_tokens["debit_data"]
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.post(url, auth=auth, data=debit_data)
    j = response.json()
    breakpoint()
    assert response.status_code == 201


def test_cancel_debit(base_url):
    id = os.getenv("DEBIT_ID")
    url = base_url + "liana/debit/" + str(id) + "/cancel/"
    debit_canceled_data = beans_tokens["debit_canceled_data"]
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.post(url, auth=auth, data=debit_canceled_data)
    j = response.json()
    breakpoint()
    assert response.status_code == 202
