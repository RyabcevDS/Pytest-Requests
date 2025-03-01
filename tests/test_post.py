import requests
import json

host = "https://reqres.in/api/"

def test_create_user():
    body = {
    "name": "Dmitriy",
    "job": "Quality Assurance"
}
    response=requests.post(f'{host}users', json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 201
    assert "name" in response.json()
    assert "job" in response.json()
    assert "id" in response.json()

def test_succesfull_registration():
    body = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
    response=requests.post(f'{host}register', json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 200
    assert "id" in response.json()
    assert "token" in response.json()


def test_registration_with_another_email():
    body = {
    "email": "ryabcev@mail.ru",
    "password": "pistol"
}
    response=requests.post(f'{host}register', json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 400
    assert response.json()["error"] == "Note: Only defined users succeed registration"


def test_unsuccesful_registration():
    body = {
    "email": "ryabcev@mail.ru",
}
    response=requests.post(f'{host}register', json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"
    
def test_succesful_login():
    body = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
    response=requests.post(f'{host}login', json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_with_another_email():
    body = {
    "email": "ryabcev@mail.ru",
    "password": "cityslicka"
}
    response=requests.post(f'{host}login', json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 400
    assert response.json()["error"] == "user not found"

def test_unsuccesful_login():
    body = {
    "email": "eve.holt@reqres.in",
}
    response=requests.post(f'{host}login', json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"
    