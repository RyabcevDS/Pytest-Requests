import requests
import json

host = "https://reqres.in/api/"

def test_list_users():
    total_pages=(requests.get(f"{host}users")).json()["total_pages"]
    for i in range(1,total_pages+1):
        response = requests.get(f"{host}users?page={i}") 
        print(json.dumps(response.json(), indent=3))
        assert response.status_code == 200
        assert "data" in response.json()


def test_user():
    user_id=(requests.get(f"{host}users")).json()["total"] 
    response = requests.get(f"{host}users/{user_id}") 
    print(json.dumps(response.json(), indent=3))
    assert response.status_code == 200
    assert "data" in response.json()


def test_user_not_found():
    user_id=(requests.get(f"{host}users")).json()["total"] 
    response = requests.get(f"{host}users/{user_id+1}") 
    assert response.status_code == 404
