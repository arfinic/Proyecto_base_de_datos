from app.model.models import Participacion

def crear_participacion(db, jugador_id, torneo_id, categoria_id, grupo_id=None, equipo_id=None):
    participacion = Participacion(
        jugador_id=jugador_id,
        torneo_id=torneo_id,
        categoria_id=categoria_id,
        grupo_id=grupo_id,
        equipo_id=equipo_id
    )
    db.add(participacion)
    db.commit()
    db.refresh(participacion)
    return participacion

def listar_participaciones(db):
    return db.query(Participacion).all()

def obtener_participacion(db, participacion_id):
    return db.query(Participacion).filter(Participacion.id == participacion_id).first()

def actualizar_participacion(db, participacion_id, jugador_id=None, torneo_id=None, categoria_id=None, grupo_id=None, equipo_id=None):
    participacion = db.query(Participacion).filter(Participacion.id == participacion_id).first()
    if not participacion:
        return None
    if jugador_id is not None:
        participacion.jugador_id = jugador_id
    if torneo_id is not None:
        participacion.torneo_id = torneo_id
    if categoria_id is not None:
        participacion.categoria_id = categoria_id
    if grupo_id is not None:
        participacion.grupo_id = grupo_id
    if equipo_id is not None:
        participacion.equipo_id = equipo_id
    db.commit()
    db.refresh(participacion)
    return participacion

def eliminar_participacion(db, participacion_id):
    participacion = db.query(Participacion).filter(Participacion.id == participacion_id).first()
    if participacion:
        db.delete(participacion)
        db.commit()
        return True
    return False