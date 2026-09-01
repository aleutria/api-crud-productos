# API CRUD de Productos

API REST desarrollada con **FastAPI** para gestionar productos mediante operaciones CRUD.

El proyecto utiliza **PostgreSQL** como base de datos, **SQLAlchemy** como ORM y **Docker Compose** para ejecutar la API y la base de datos de forma sencilla.

## Tecnologías

* Python 3.12
* FastAPI
* Pydantic
* SQLAlchemy
* PostgreSQL
* Psycopg
* Docker
* Docker Compose
* Git / GitHub

## Funcionalidades

* Crear productos
* Obtener todos los productos
* Buscar un producto por nombre
* Actualizar la cantidad de un producto
* Eliminar productos
* Validación de datos mediante Pydantic
* Manejo de errores HTTP
* Creación automática de tablas al iniciar la aplicación

## Endpoints

| Método | Endpoint              | Descripción                           |
| ------ | --------------------- | ------------------------------------- |
| GET    | `/`                   | Mensaje de inicio                     |
| GET    | `/productos/`         | Obtener todos los productos           |
| GET    | `/productos/{nombre}` | Obtener un producto por nombre        |
| POST   | `/productos/`         | Crear un producto                     |
| PUT    | `/productos/{nombre}` | Actualizar la cantidad de un producto |
| DELETE | `/productos/{nombre}` | Eliminar un producto                  |

## Estructura del proyecto

```text
API-REST-CRUD-PRODUCTOS/
│
├── routers/
│   └── productos.py
│
├── .dockerignore
├── .env
├── .gitignore
├── crear_tablas.py
├── crud.py
├── database.py
├── docker-compose.yml
├── Dockerfile
├── main.py
├── models.py
├── requirements.txt
└── schemas.py
```

## Instalación y ejecución

### Opción recomendada: Docker Compose

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd API-REST-CRUD-PRODUCTOS
```

Crear un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@db:5432/productos_db
```

Levantar los contenedores:

```bash
docker compose up --build
```

Docker Compose levantará:

* Un contenedor con PostgreSQL.
* Un contenedor con la API FastAPI.
* La API esperará a que PostgreSQL esté preparado antes de iniciarse.
* Las tablas se crearán automáticamente antes de arrancar Uvicorn.

La API estará disponible en:

```text
http://localhost:8000
```

## Documentación

FastAPI genera automáticamente la documentación interactiva.

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

## Detener la aplicación

Para detener los contenedores:

```bash
docker compose down
```

## Notas

El archivo `.env` contiene información de configuración y **no debe subirse a GitHub**.

La aplicación utiliza un volumen de Docker para conservar los datos de PostgreSQL entre reinicios de los contenedores.
