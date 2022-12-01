import pytest
import json
from server.app import app

def test_signup():

    data = {
        "email": "test@user.com",
        "password": "testpassword"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = app.test_client().post("/api/signup/", data=json.dumps(data), headers=headers)

    assert response.status_code == 201
    res_data = json.loads(response.data)
    assert "jwt_token" in res_data
    print(res_data["jwt_token"])