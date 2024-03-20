# Backend
Esta es una aplicación FastAPI simple que proporciona una interfaz para acceder a álbumes, publicaciones y fotos de los usuarios desde la API JSONPlaceholder. La aplicación también registra cada solicitud de API con fines de auditoría y depuración.

## Pre-requisitos
- Python 3.8 or higher
- FastAPI
- Uvicorn
- MongoDB

## Instalación
1. Crea un entorno virtual y actívalo:
```
python3 -m venv venv
source venv/bin/activate
```

2. Instalar los paquetes requeridos:
```
pip install -r requirements.txt
```

3. Ejecutar la aplicación:
```
uvicorn main:app --reload
```

## Documentación de la API
The API documentation is available at 
- http://localhost:8000/docs#/
- http://localhost:8000/redoc

## Endpoints
- `GET /users`: Devuelve una lista de usuarios.
    - Curl:
        ```
        curl -X 'GET' \
            'http://localhost:8000/users' \
            -H 'accept: application/json'
        ```
    - Request URL: `http://localhost:8000/users`

- `GET /users/{user_id}`: Devuelve una usuario específico.
    - Curl:
        ```
        curl -X 'GET' \
            'http://localhost:8000/users/3' \
            -H 'accept: application/json'
        ```
    - Request URL: `http://localhost:8000/users/3`

- `GET /posts/{user_id}`: Devuelve una lista de publicaciones de un usuario con el ID dado.
    - Curl:
        ```
        curl -X 'GET' \
            'http://localhost:8000/post/5' \
            -H 'accept: application/json'
        ```
    - Request URL: `http://localhost:8000/post/5`

- `GET /photos/{user_id}`: Devuelve una lista de fotos de un usuario con la identificación proporcionada.
    - Curl:
        ```
        curl -X 'GET' \
            'http://localhost:8000/photos/6' \
            -H 'accept: application/json'
        ```
    - Request URL: `http://localhost:8000/photos/6`

- `GET /logs`: Devuelve una lista de los Logs registrados en la base de datos.
    - Curl:
        ```
        curl -X 'GET' \
            'http://localhost:8000/logs' \
            -H 'accept: application/json'
        ```
    - Request URL: `http://localhost:8000/logs`

> [!NOTE]
> La aplicación registra cada solicitud de API con fines de auditoría y depuración. Los registros se almacenan en una base de datos MongoDB.
