# API CRUD de Productos

API REST desarrollada con FastAPI para gestionar productos mediante operaciones CRUD.

Utiliza PostgreSQL como base de datos y SQLAlchemy como ORM.

## Tecnologías

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- Psycopg
- Git

## Funcionalidades

- Crear productos
- Obtener todos los productos
- Buscar un producto por nombre
- Actualizar la cantidad de un producto
- Eliminar productos

## Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Mensaje de inicio |
| GET | `/productos` | Obtener todos los productos |
| GET | `/productos/{nombre}` | Obtener un producto |
| POST | `/productos` | Crear un producto |
| PUT | `/productos/{nombre}` | Actualizar la cantidad de un producto |
| DELETE | `/productos/{nombre}` | Eliminar un producto |

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd MAIN.PY
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual en Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```bash
pip install fastapi uvicorn sqlalchemy psycopg python-dotenv
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=postgresql+psycopg://usuario:contraseña@localhost:5432/productos_db
```

## Ejecución

```bash
uvicorn main:app --reload
```