import requests

def test_get_post():
    """Проверка GET запроса"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_create_post():
    """Проверка POST запроса"""
    payload = {"title": "QA", "body": "Test", "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "QA"