# Proyecto_base_de_datos
Proyecto de Base de Datos en donde se guardará todo lo relacionado al proyecto

Felipe Delgado
Bastián Sanhueza
Samuel Delgado

Generic single-database configuration.
# Proyecto Torneo de Tenis de Mesa

## Requisitos previos

- Python 3.11+
- PostgreSQL
- [Opcional] Git
- ﻿alembic==1.15.2
-annotated-types==0.7.0
-anyio==4.9.0
-click==8.2.1
-colorama==0.4.6
-fastapi==0.116.0
-greenlet==3.2.3
-h11==0.16.0
-idna==3.10
-psycopg2-binary==2.9.10
-python-dotenv==1.1.1
-sniffio==1.3.1
-SQLAlchemy==2.0.41
-starlette==0.46.2
-typing-inspection==0.4.1
-typing_extensions==4.14.1
-uvicorn==0.35.0

## Instalación del entorno

1. Clona el repositorio:
    ```bash
    git clone <URL-del-repo>
    cd <carpeta-del-proyecto>
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv env
    # En Windows:
    env\Scripts\activate
    # En Linux/macOS:
    source env/bin/activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configura tu base de datos:
    - Crea la base de datos en PostgreSQL.
    - Edita `.env` o los archivos de configuración para que la app apunte a tu base de datos.

5. Realiza las migraciones (si usas Alembic):
    ```bash
    alembic upgrade head
    ```

## Ejecución del servidor

1. En la raíz del proyecto, ejecuta:
    ```bash
    uvicorn app.main:app --reload
    ```
2. Accede a la API en:  
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Notas

- El entorno virtual **`env`** se usa para aislar las dependencias.
- FastAPI es el framework utilizado para exponer la API REST.
- La estructura del proyecto sigue el patrón: `app/models.py`, `app/crud/`, `app/routers/`, etc.
