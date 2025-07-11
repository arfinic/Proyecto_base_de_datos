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
- sqlalchemy 
- [Opcional] Git

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
