import requests
import json

host = "https://reqres.in/api/"

def test_list_users(): # Проверка что на всех страницах есть поле "data"
    total_pages=(requests.get(f"{host}users")).json()["total_pages"] # Узнаём сколько всего странци с помощью поля "total_page"
    for i in range(1,total_pages+1):
        response = requests.get(f"{host}users?page={i}") 
        print(json.dumps(response.json(), indent=3))
        assert response.status_code == 200
        assert "data" in response.json()


def test_user(): # Проверка конкретного пользователя, что в ответе есть поле "data"
    user_id=(requests.get(f"{host}users")).json()["total"] 
    response = requests.get(f"{host}users/{user_id}") 
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 200
    assert "data" in response.json()


def test_user_not_found(): # Проверка поведения при поиске несуществующего пользователя
    user_id=(requests.get(f"{host}users")).json()["total"] 
    response = requests.get(f"{host}users/{user_id+1}") # Находим айди последнего пользователя и добавляем единицу, чтобы найти несуществующего
    assert response.status_code == 404
