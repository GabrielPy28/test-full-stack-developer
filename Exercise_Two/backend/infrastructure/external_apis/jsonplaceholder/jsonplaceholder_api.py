import requests

def get_users() -> list:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return response.json()

def get_user_by_id(user_id: int) -> list:
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return response.json()

def get_posts_by_user_id(user_id: int) -> list:
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    return response.json()

def get_photos_by_user_id(user_id: int) -> list:
    response = requests.get(f"https://jsonplaceholder.typicode.com/photos?albumId={user_id}")
    return response.json()