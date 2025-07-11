from app.model.models import Torneo

def crear_torneo(db, nombre, fecha_inscripcion, fecha_competencia, mesas_disponibles):
    """
    Crea un nuevo torneo en la base de datos.

    Parámetros:
        db (Session): Sesión de base de datos.
        nombre (str): Nombre del torneo.
        fecha_inscripcion_i (date): Fecha de inicio de inscripciones.
        fecha_inscripcion_f (date): Fecha de cierre de inscripciones.
        fecha_competencia_i (date): Fecha de inicio de competencia.
        fecha_competencia_f (date): Fecha de término de competencia.
        mesas_disponibles (int): Número de mesas disponibles para el torneo.

    Retorna:
        Torneo: El torneo creado.
    """
    torneo = Torneo(
        nombre=nombre,
        fecha_inscripcion=fecha_inscripcion,
        fecha_competencia=fecha_competencia,
        mesas_disponibles=mesas_disponibles
    )
    db.add(torneo)
    db.commit()
    db.refresh(torneo)
    return torneo

def listar_torneos(db):
    """
    Lista todos los torneos registrados en la base de datos.

    Parámetros:
        db (Session): Sesión de base de datos.

    Retorna:
        List[Torneo]: Lista de torneos registrados.
    """
    return db.query(Torneo).all()

def obtener_torneo(db, torneo_id):
    """
    Busca y retorna un torneo específico por su ID.

    Parámetros:
        db (Session): Sesión de base de datos.
        torneo_id (int): ID del torneo a buscar.

    Retorna:
        Torneo o None: El torneo encontrado, o None si no existe.
    """
    return db.query(Torneo).filter(Torneo.id == torneo_id).first()

def eliminar_torneo(db, torneo_id):
    """
    Elimina un torneo de la base de datos por su ID.

    Parámetros:
        db (Session): Sesión de base de datos.
        torneo_id (int): ID del torneo a eliminar.

    Retorna:
        bool: True si fue eliminado, False si no existía.
    """
    torneo = db.query(Torneo).filter(Torneo.id == torneo_id).first()
    if torneo:
        db.delete(torneo)
        db.commit()
        return True
    return False