# Frontend
Esta aplicación React está construida con TypeScript y usa Bootstrap para los estilos. La aplicación consta de cuatro componentes principales: usuarios, publicaciones, fotos y registros.

## Tecnologías
- React
- React Router
- TypeScript
- Bootstrap
- Axios

## Estructura de la aplicación
Hay cuatro componentes principales en la aplicación:
1. **Users**: El componente Usuarios muestra los datos de todos los usuarios que existen en la API

2. **Posts**: El componente Publicaciones muestra las publicaciones para un usuario específico.

3. **Photos**: El componente Fotos muestra una lista de fotos para un usuario específico.

4. **Logs**: El componente Registros muestra una tabla con una lista de registros del servidor, actualizada cada vez que el usuario navega a la ruta de registros.

## Cómo ejecutar la aplicación

1. **Instalar dependencias**
```
npm install
```

2. **Iniciar el servidor de desarrollo**
```
npm start
```
> [!NOTE]
> La aplicación estará disponible en `http://localhost:3000.`

## Endpoints
Los siguientes puntos finales están disponibles:

- http://localhost:3000/: muestra los datos de todos los usuarios que existen en la API
- http://localhost:3000/users/1: muestra las publicaciones para un usuario específico.
- http://localhost:3000/users/1/photos: muestra una lista de fotos para un usuario específico.
- http://localhost:3000/logs: muestra una tabla con una lista de registros del servidor, actualizada cada vez que el usuario navega a la ruta de registros.

