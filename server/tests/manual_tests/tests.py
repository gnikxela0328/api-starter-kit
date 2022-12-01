import requests
import json

from test_util import TestUtil

headers = {
    "Content-Type": "application/json"
}


class Tests():
    def test_signup():
        data = {
            "email": "alex@alex.com",
            "password": "alexpassword"
        }

        response = requests.post(url="http://0.0.0.0:8080/api/signup/", json=data, headers=headers)
        res = json.loads(response.content)

        TestUtil.check_status(actual=response.status_code, expected=201)
        TestUtil.check_message(actual=res["message"], expected="New user created!")
        
        print("Signup: Finished")

    def test_successful_authenticate():
        data = {
            "email": "alex@alex.com",
            "password": "alexpassword"
        }

        response = requests.post(url="http://0.0.0.0:8080/api/auth/", json=data, headers=headers)
        res = json.loads(response.content)

        TestUtil.check_status(actual=response.status_code, expected=201)
        TestUtil.check_any(actual=res["access_token"], key="JWT Access Token")

        print("Authenticate: Finished")
    
    def test_failed_authenticate():
        data = {
            "email": "notalex@alex.com",
            "password": "alexpassword"
        }

        response = requests.post(url="http://0.0.0.0:8080/api/auth/", json=data, headers=headers)
        res = json.loads(response.content)

        TestUtil.check_status(actual=response.status_code, expected=401)
        TestUtil.check_message(actual=res["message"], expected="Bad username or password")

        print("Failed Authenticate: Finished")

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

        TestUtil.check_status(actual=response.status_code, expected=201)
        TestUtil.check_any(actual=res["access_token"], key="JWT Access Token")

        # Reset password for further testing
        headers["Authorization"] = res["access_token"]
        data = {
            "email": "alex@alex.com",
            "password": "alexpassword"
        }

        response = requests.put(url="http://0.0.0.0:8080/api/auth/", json=data, headers=headers)
        res = json.loads(response.content)

        print("Update Credentials: Finished")

