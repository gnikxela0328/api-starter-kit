import requests
import json
import random
import pytest

headers = {
    "Content-Type": "application/json"
}

@pytest.fixture(scope="session", autouse=True)
def create_testuser():
    data = {
        "email": "test@alex.com",
        "password": "testpassword"
    }

    requests.post(url="http://0.0.0.0:8080/api/signup/", json=data, headers=headers)
    

@pytest.fixture
def authenticate():
    data = {
        "email": "test@alex.com",
        "password": "testpassword"
    }

    response = requests.post(url="http://0.0.0.0:8080/api/auth/", json=data, headers=headers)
    res = json.loads(response.content)

    return res["access_token"]

@pytest.fixture
def create_contact_uuid(authenticate):
    data = {
        "first_name": str(random.randrange(5)),
        "last_name": "to be deleted",
        "email": "test@delete.com",
        "discord_username": "test#1234",        
        "github_username": "test1234",
        "twitter_username": "@test1234"        
    }
    headers["Authorization"] = authenticate

    response = requests.post(url="http://0.0.0.0:8080/api/contacts/", json=data, headers=headers)
    res = json.loads(response.content)

    return res["uuid"]



def test_create_contact(authenticate):
    data = {
        "first_name": "test",
        "last_name": "contact",
        "email": "test@contact.com",
        "discord_username": "test#1234",        
        "github_username": "test1234",
        "twitter_username": "@test1234"        
    }
    headers["Authorization"] = authenticate

    response = requests.post(url="http://0.0.0.0:8080/api/contacts/", json=data, headers=headers)
    res = json.loads(response.content)

    assert res["message"] == "Contact created"
    assert any(res["uuid"])
    assert response.status_code == 201

def test_get_contacts(authenticate):
    headers["Authorization"] = authenticate

    response = requests.get(url="http://0.0.0.0:8080/api/contacts/", headers=headers)
    res = json.loads(response.content)

    assert any(res["contacts"])
    assert response.status_code == 200

def test_update_contact(authenticate, create_contact_uuid):
    data = {
        "first_name": "tetetete",
        "uuid": create_contact_uuid,
        "email": "newtest@contact.com",
        "discord_username": "test#12asdasd34",        
        "github_username": "test1234",
        "twitter_username": "@testdas1234"        
    }
    headers["Authorization"] = authenticate

    response = requests.put(url="http://0.0.0.0:8080/api/contacts/", json=data, headers=headers)
    res = json.loads(response.content)

    assert res["message"] == "Contact successfully updated"
    assert response.status_code == 201

def test_delete_contact(authenticate, create_contact_uuid):
    headers["Authorization"] = authenticate

    response = requests.delete(url="http://0.0.0.0:8080/api/contacts/?user=" + create_contact_uuid, headers=headers)
    res = json.loads(response.content)

    assert res["message"] == "Contact successfully deleted"
    assert response.status_code == 201