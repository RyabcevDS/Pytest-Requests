import requests
import json

host = "https://reqres.in/api/"


def test_create_user():  # Проверка создания пользователя
    body = {"name": "Dmitriy", "job": "Quality Assurance"}
    response = requests.post(f"{host}users", json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 201
    assert "name" in response.json()
    assert "job" in response.json()
    assert "id" in response.json()


def test_succesfull_registration():  # Проверка успешной регистрации
    body = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(f"{host}register", json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 200
    assert "id" in response.json()  # При регистрации присваивается id
    assert "token" in response.json()  # В ответ должен придти токен


def test_registration_with_another_email():  # Регистрация с помощью недоступной почты
    body = {"email": "ryabcev@mail.ru", "password": "pistol"}
    response = requests.post(f"{host}register", json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 400
    assert (
        response.json()["error"] == "Note: Only defined users succeed registration"
    )  # Регистрация только с определённой почтой


def test_unsuccesful_registration():  # Проверка неуспешной регистрации без указания пароля
    body = {
        "email": "ryabcev@mail.ru",
    }
    response = requests.post(f"{host}register", json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"


def test_unsuccesful_registration_without_email():  # Проверка неуспешной регистрации без указания почты
    body = {
        "password": "Proverka_parol",
    }
    response = requests.post(f"{host}register", json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 400
    assert response.json()["error"] == "Missing email or username"


def test_succesful_login():  # Проверка успешной авторизации
    body = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{host}login", json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 200
    assert "token" in response.json()  # В ответ должен придти токен


def test_login_with_another_email():  # Проверка авторизации с несуществующей почтой
    body = {"email": "ryabcev@mail.ru", "password": "cityslicka"}
    response = requests.post(f"{host}login", json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 400
    assert response.json()["error"] == "user not found"


def test_unsuccesful_login():  # Проверка авторизации без отправки пароля
    body = {
        "email": "eve.holt@reqres.in",
    }
    response = requests.post(f"{host}login", json=body)
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"
