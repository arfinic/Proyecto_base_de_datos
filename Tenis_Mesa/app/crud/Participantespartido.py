from app.model.models import ParticipantePartido
from sqlalchemy.orm import Session

def crear_participante_partido(db: Session, partido_id: int, participacion_id: int, equipo_doble_id: int = None, es_ganador: bool = False):
    """
    Crea un nuevo registro de participante en partido.

    Parámetros:
        db (Session): Sesión de base de datos.
        rol (str): Rol en el partido (por ejemplo, "titular", "suplente").
        participacion_id (int): ID de la participación.
        partido_id (int): ID del partido.
        equipo_doble_id (int, opcional): ID del equipo doble si corresponde.

    Retorna:
        ParticipantePartido: El registro creado.
    """
    pp = ParticipantePartido(
        partido_id=partido_id,
        participacion_id=participacion_id,
        equipo_doble_id=equipo_doble_id,
        es_ganador=es_ganador
    )
    db.add(pp)
    db.commit()
    db.refresh(pp)
    return pp

def listar_participantes_partido(db: Session):
    """
    Lista todos los registros de participantes en partido.

    Parámetros:
        db (Session): Sesión de base de datos.

    Retorna:
        List[ParticipantePartido].
    """
    return db.query(ParticipantePartido).all()

def obtener_participante_partido(db: Session, pp_id: int):
    """
    Busca un registro de participante en partido por ID.

    Parámetros:
        db (Session): Sesión de base de datos.
        participante_id (int): ID del registro.

    Retorna:
        ParticipantePartido o None.
    """ 
    return db.query(ParticipantePartido).filter_by(id=pp_id).first()

def actualizar_participante_partido(db: Session, pp_id: int, partido_id=None, participacion_id=None, equipo_doble_id=None, es_ganador=None):
    """
    Actualiza los datos de un registro de participante en partido.

    Parámetros:
        db (Session): Sesión de base de datos.
        participante_id (int).
        rol (str, opcional).
        participacion_id (int, opcional).
        partido_id (int, opcional).
        equipo_doble_id (int, opcional).

    Retorna:
        ParticipantePartido actualizado o None.
    """
    pp = db.query(ParticipantePartido).filter_by(id=pp_id).first()
    if not pp:
        return None
    if partido_id is not None:
        pp.partido_id = partido_id
    if participacion_id is not None:
        pp.participacion_id = participacion_id
    if equipo_doble_id is not None:
        pp.equipo_doble_id = equipo_doble_id
    if es_ganador is not None:
        pp.es_ganador = es_ganador
    db.commit()
    db.refresh(pp)
    return pp

def eliminar_participante_partido(db: Session, pp_id: int):
    """
    Elimina un registro de participante en partido.

    Parámetros:
        db (Session): Sesión de base de datos.
        participante_id (int).

    Retorna:
        bool: True si eliminado, False si no.
    """
    pp = db.query(ParticipantePartido).filter_by(id=pp_id).first()
    if not pp:
        return False
    db.delete(pp)
    db.commit()
    return True
