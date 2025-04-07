import requests

def test_login_success():
    payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post("https://fakestoreapi.com/auth/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()
