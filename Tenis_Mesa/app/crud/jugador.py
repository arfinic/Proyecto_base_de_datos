from sqlalchemy.orm import Session
from app.model import Jugador

def crear_jugador(db: Session, nombre: str, fecha_nac: str, genero: str, ciudad: str, pais: str, asociacion_id: int = None):
    """
    Crea y guarda un nuevo jugador en la base de datos.

    Parámetros:
        db: Sesión de base de datos.
        nombre (str): Nombre del jugador.
        fecha_nac (date): Fecha de nacimiento.
        genero (str): Género del jugador.
        ciudad (str): Ciudad de residencia.
        pais (str): País de residencia.
        asociacion_id (int, opcional): ID de la asociación.

    Retorna:
        Jugador creado (objeto Jugador).
    """
    jugador = Jugador(
        nombre=nombre,
        fecha_nac=fecha_nac,
        genero=genero,
        ciudad=ciudad,
        pais=pais,
        asociacion_id=asociacion_id
    )
    db.add(jugador)
    db.commit()
    db.refresh(jugador)
    return jugador

def listar_jugadores(db: Session):
    """
    Obtiene la lista de todos los jugadores almacenados en la base de datos.

    Parámetros:
        db (Session): Sesión de base de datos.

    Retorna:
        List[Jugador]: Lista de todos los jugadores registrados.
    """
    return db.query(Jugador).all()

def obtener_jugador(db: Session, jugador_id: int):
    """
    Busca y retorna un jugador específico por su ID.

    Parámetros:
        db (Session): Sesión de base de datos.
        jugador_id (int): ID del jugador a buscar.

    Retorna:
        Jugador o None: El jugador encontrado, o None si no existe.
    """
    return db.query(Jugador).filter(Jugador.id == jugador_id).first()

def actualizar_jugador(db: Session, jugador_id: int, nombre=None, fecha_nac=None, genero=None, ciudad=None, pais=None, asociacion_id=None):
    """
    Actualiza los datos de un jugador existente. Solo los campos no nulos serán modificados.

    Parámetros:
        db (Session): Sesión de base de datos.
        jugador_id (int): ID del jugador a actualizar.
        nombre (str, opcional): Nuevo nombre.
        fecha_nac (date, opcional): Nueva fecha de nacimiento.
        genero (str, opcional): Nuevo género.
        ciudad (str, opcional): Nueva ciudad.
        pais (str, opcional): Nuevo país.
        asociacion_id (int, opcional): Nueva asociación.

    Retorna:
        Jugador actualizado o None si no se encontró el jugador.
    """
    jugador = db.query(Jugador).filter(Jugador.id == jugador_id).first()
    if not jugador:
        return None
    if nombre is not None:
        jugador.nombre = nombre
    if fecha_nac is not None:
        jugador.fecha_nac = fecha_nac
    if genero is not None:
        jugador.genero = genero
    if ciudad is not None:
        jugador.ciudad = ciudad
    if pais is not None:
        jugador.pais = pais
    if asociacion_id is not None:
        jugador.asociacion_id = asociacion_id
    db.commit()
    db.refresh(jugador)
    return jugador

def eliminar_jugador(db: Session, jugador_id: int):
    """
    Elimina un jugador de la base de datos según su ID.

    Parámetros:
        db (Session): Sesión de base de datos.
        jugador_id (int): ID del jugador a eliminar.

    Retorna:
        bool: True si la eliminación fue exitosa, False si no se encontró el jugador.
    """
    jugador = db.query(Jugador).filter(Jugador.id == jugador_id).first()
    if not jugador:
        return False
    db.delete(jugador)
    db.commit()
    return True

