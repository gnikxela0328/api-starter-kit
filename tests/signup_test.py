import pytest
import json
from app import app

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
    print(response.data.decode('utf-8'))