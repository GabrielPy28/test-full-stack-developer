# Prueba de Desarrollador Full-Stack

## Ejercicio Uno
La empresa internacional de desarrollo de software quiere crear un servicio de calendario al que puedan acceder los usuarios desde diferentes plataformas y dispositivos. El calendario estará disponible en una página web donde los usuarios podrán iniciar sesión con una clave de usuario y contraseña. También habrá diferentes aplicaciones móviles que podrán generar varias visualizaciones de calendario.

Los calendarios cifrados se almacenan debido a que contienen información confidencial, por lo que los usuarios primero deben autenticarse y, si tienen los permisos necesarios, descifrar el calendario para las operaciones requeridas. Los usuarios pueden configurar alertas para eventos específicos que se reflejarán en las diferentes aplicaciones.

### Architecture
1. [Diagrama con el Punto de Vista de Componentes y Conectores.pdf](Exercise_One/Components%20_and_%20Connectors.pdf)

2. [Diagrama con el Punto de Vista de Deployment.pdf](Exercise_One/Deployment.pdf)

### Restrictions
Las restricciones se encuentran listadas en el archivo [restrictions_about_solution.md](Exercise_One/requirements.txt).

## Ejercicio Dos
El objetivo es crear una aplicación web que obtenga datos de usuarios, publicaciones y fotografías de una API externa (https://jsonplaceholder.typicode.com/) y los presente en un diseño responsivo. El backend consultará la API externa y registrará cada solicitud, mientras que el frontend mostrará la lista de usuarios y brindará opciones para ver las publicaciones, fotos y registros del usuario.

### Backend
- Obtener datos de la API externa
- Registre cada solicitud
- Exponer una API para que la interfaz acceda a datos de usuarios, publicaciones y fotografías.

### Frontend
- Mostrar una lista de usuarios receptiva
- Proporcionar opciones para ver publicaciones, fotos y registros de usuarios.