import requests

headers = {
    "Content-Type": "application/json"
}


class Tests():
    def test_signup():
        data = {
            "email": "alex@alex.com",
            "password": "alexpassword"
        }

        res = requests.post("0.0.0.0:8080/api/signup/", json=data, headers=headers)

        assert res.status_code == 201
        assert res["message"] == "New user created!"

    def test_successful_authenticate():
        data = {
            "email": "alex@alex.com",
            "password": "alexpassword"
        }

        res = requests.post("0.0.0.0:8080/api/auth/", json=data, headers=headers)

        assert res.status_code == 201
        assert any(res["access_token"])
    
    def test_failed_authenticate():
        data = {
            "email": "notalex@alex.com",
            "password": "alexpassword"
        }

        res = requests.post("0.0.0.0:8080/api/auth/", json=data, headers=headers)

        assert res.status_code == 401
        assert res["message"] == "Bad username or password"

    def test_update_credentials():

        # First, get refreshed token
        data = {
            "email": "alex@alex.com",
            "password": "alexpassword"
        }
        res = requests.post("0.0.0.0:8080/api/signup/", json=data, headers=headers)

        # Add token to headers, update password
        headers["Authorization"] = res["access_token"]
        data = {
            "email": "alex@alex.com",
            "password": "alexnewpassword"
        }

        res = requests.put("0.0.0.0:8080/api/auth/", json=data, headers=headers)

        assert res.status_code == 201
        assert any(res["access_token"])

        # Reset password for further testing
        headers["Authorization"] = res["access_token"]
        data = {
            "email": "alex@alex.com",
            "password": "alexpassword"
        }

        res = requests.put("0.0.0.0:8080/api/auth/", json=data, headers=headers)

