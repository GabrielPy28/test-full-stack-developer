# Backend
Esta es una aplicación FastAPI simple que proporciona una interfaz para acceder a álbumes, publicaciones y fotos de los usuarios desde la API JSONPlaceholder. La aplicación también registra cada solicitud de API con fines de auditoría y depuración.

## Prerequisites
- Python 3.8 or higher
- FastAPI
- Uvicorn
- MongoDB

## Installation
1. Create a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate
```

2. Install the required packages:
```
pip install -r requirements.txt
```

3. Run the application:
```
uvicorn main:app --reload
```

## Documentación de la API
The API documentation is available at 
- http://localhost:8000/docs#/
- http://localhost:8000/redoc

## Endpoints
- `GET /users`: Returns a list of users.
    - Curl:
        ```
        curl -X 'GET' \
            'http://localhost:8000/users' \
            -H 'accept: application/json'
        ```
    - Request URL: `http://localhost:8000/users`

- `GET /users/{user_id}`: Returns a specific user.
    - Curl:
        ```
        curl -X 'GET' \
            'http://localhost:8000/users/3' \
            -H 'accept: application/json'
        ```
    - Request URL: `http://localhost:8000/users/3`

- `GET /posts/{user_id}`: Returns a list of posts by a user with the given ID.
    - Curl:
        ```
        curl -X 'GET' \
            'http://localhost:8000/post/5' \
            -H 'accept: application/json'
        ```
    - Request URL: `http://localhost:8000/post/5`

- `GET /photos/{user_id}`: Returns a list of photos by a user with the given ID.
    - Curl:
        ```
        curl -X 'GET' \
            'http://localhost:8000/photos/6' \
            -H 'accept: application/json'
        ```
    - Request URL: `http://localhost:8000/photos/6`

- `GET /logs`: Returns a list of logs.
    - Curl:
        ```
        curl -X 'GET' \
            'http://localhost:8000/logs' \
            -H 'accept: application/json'
        ```
    - Request URL: `http://localhost:8000/logs`

> [!NOTE]
> La aplicación registra cada solicitud de API con fines de auditoría y depuración. Los registros se almacenan en una base de datos MongoDB.