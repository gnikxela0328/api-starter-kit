import requests
import json

headers = {
    "Content-Type": "application/json"
}

def test_signup():
    data = {
        "email": "alex@alex.com",
        "password": "alexpassword"
    }

    response = requests.post(url="http://0.0.0.0:8080/api/signup/", json=data, headers=headers)
    res = json.loads(response.content)

    assert response.status_code == 201
    assert res["message"] == "New user created!"
    
    pass

def test_successful_authenticate():
    data = {
        "email": "alex@alex.com",
        "password": "alexpassword"
    }

    response = requests.post(url="http://0.0.0.0:8080/api/auth/", json=data, headers=headers)
    res = json.loads(response.content)

    assert response.status_code == 201
    assert any(res["access_token"])

    pass

def test_failed_authenticate():
    data = {
        "email": "notalex@alex.com",
        "password": "alexpassword"
    }

    response = requests.post(url="http://0.0.0.0:8080/api/auth/", json=data, headers=headers)
    res = json.loads(response.content)

    assert response.status_code == 401
    assert res["message"] == "Bad username or password"

    pass

def test_update_credentials():

    # First, get refreshed token
    data = {
        "email": "alex@alex.com",
        "password": "alexpassword"
    }

    response = requests.post(url="http://0.0.0.0:8080/api/auth/", json=data, headers=headers)
    res = json.loads(response.content)

    # Add token to headers, update password
    headers["Authorization"] = res["access_token"]
    data = {
        "email": "alex@alex.com",
        "password": "alexnewpassword"
    }

    response = requests.put(url="http://0.0.0.0:8080/api/auth/", json=data, headers=headers)
    res = json.loads(response.content)

    assert response.status_code == 201
    assert any(res["access_token"])

    # Reset password for further testing
    headers["Authorization"] = res["access_token"]
    data = {
        "email": "alex@alex.com",
        "password": "alexpassword"
    }

    response = requests.put(url="http://0.0.0.0:8080/api/auth/", json=data, headers=headers)
    res = json.loads(response.content)

    pass
