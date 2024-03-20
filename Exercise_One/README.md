# Calendar and Alert App
Este repositorio contiene el código para la solución al examen practico 1. La aplicación está construida utilizando Flask, un marco web ligero para Python. La aplicación incluye funciones de gestión de usuarios, creación de calendarios y gestión de alertas.

## Primeros Pasos

### Pre-requisitos:
- Python 3.x
- Virtualenv

### Instalación

2. Crea un entorno virtual y actívalo:
```
cd calendar_alert_app
python3 -m venv venv
source venv/bin/activate
```

3. Instalar las bibliotecas y dependencias necesarias:
```
pip install -r requirements.txt
```

4. Crear el archivo `.env` en el directorio raiz del proyecto con las siguientes variables:
```
USER_NAME = 'YOUR_USER_NAME'
PASSWORD = 'YOUR_PASSWORD'
DATABASE_NAME = 'YOUR_DATABASE_NAME'
SECRET_KEY = 'YOUR_SECRET_KEY'
JWT_SECRET_KEY = 'YOUR_JWT_SECRET_KEY'
```

5. Inicializar la base de datos:
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. Run the application:
```
flask run
```

## Testing:

### Users:
- Create a user: `POST /users`
```
{
    "username":"username",
    "password":"1234567"
}
```

- Update a user: `PUT /users/<user_id>`
```
{
    "username":"nickname",
    "password":"p455w0rd"
}
```

- Delete a user: `DELETE /users/<user_id>`
```
http://127.0.0.1:5000/users/1
```

### Authentication
- Login: `POST /auth/login`
```
{
    "username":"username",
    "password":"1234567"
}
```

- Logout: `POST /auth/logout`
```
> Autorization > Type = 'Bearer Token': 'user_token' 
```

### Calendars:
- Create a calendar: `POST /calendars`
```
{
    "user_id":2,
    "name":"Calendar Test-07",
    "description":"Inspeccionando ejecución de la Creación",
    "data":"BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VEVENT\nDTSTART:20240318T100000\nDTEND:20240319T110000\nSUMMARY:Creación de Prueba N°02 creando mi calendario para eliminar\nEND:VEVENT\nEND:VCALENDAR"
}
```

- Delete a calendar: `DELETE /calendars/<calendar_id>`
```
http://127.0.0.1:5000/calendars/1
```

### Alerts:
- Create an alert: `POST /alerts`
```
{
    "calendar_id":1,
    "title":"Alert Test-01",
    "description":"Creando una Alerta",
    "start_time":"18/03/2024 18:10:47",
    "end_time":"19/03/2024 18:10:50"
}
```

## Diagramas
- [Diagrama con el Punto de Vista de Componentes y Conectores.pdf](/Components%20_and_%20Connectors.pdf)
- [Diagrama con el Punto de Vista de Deployment.pdf](/Deployment.pdf)

## Restricciones sobre la solución
Para obtener más información sobre las restricciones de la solución, consulte el archivo [restrictions_about_solution.md](/restrictions_about_solution.md).