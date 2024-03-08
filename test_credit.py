import pytest
import requests
import os
from requests.auth import HTTPBasicAuth
from samples import beans_tokens

# Ca renvoie un 409 parce que le credit qu'on  essaie de creer existe deja... trouver un moyen de contourner ceci
def test_create_credit(base_url):
    url = base_url + "liana/credit/"
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    credit_data = beans_tokens["credit_data"]
    auth = HTTPBasicAuth(beans_access_token, "")
    response = requests.post(url, auth=auth, data=credit_data)
    new_data = response.json()
    assert response.status_code == 201



def test_cancel_credit(base_url):
    id = os.getenv("CREDIT_ID")
    url = base_url + "liana/credit/" + str(id) + "/cancel/"
    beans_access_token = os.getenv("BEANS_ACCESS_TOKEN")
    auth = HTTPBasicAuth(beans_access_token, "")
    credit_canceled_data = beans_tokens["credit_canceled_data"]
    response = requests.post(url, auth=auth, data=credit_canceled_data)
    assert response.status_code == 202
