from app.model import Partido
from datetime import datetime

def crear_partido(db, tipo_partido, horario_inicio, fase, ronda_eliminacion, ganador_id, perdedor_id, is_bye, torneo_id, categoria_id, mesa_id):
    
    if isinstance(horario_inicio, str):
        horario_inicio = datetime.fromisoformat(horario_inicio)
    partido = Partido(
        tipo_partido=tipo_partido,
        horario_inicio=horario_inicio,
        fase=fase,
        ronda_eliminacion=ronda_eliminacion,
        ganador_id=ganador_id,
        perdedor_id=perdedor_id,
        is_bye=is_bye,
        torneo_id=torneo_id,
        categoria_id=categoria_id,
        mesa_id=mesa_id
    )
    db.add(partido)
    db.commit()
    db.refresh(partido)
    return partido

def listar_partidos(db):
    return db.query(Partido).all()

def obtener_partido(db, partido_id):
    return db.query(Partido).filter(Partido.id == partido_id).first()

def actualizar_partido(db, partido_id, torneo_id=None, categoria_id=None, tipo=None, fecha_hora=None, mesa_id=None):
    partido = db.query(Partido).filter(Partido.id == partido_id).first()
    if not partido:
        return None
    if torneo_id is not None:
        partido.torneo_id = torneo_id
    if categoria_id is not None:
        partido.categoria_id = categoria_id
    if tipo is not None:
        partido.tipo = tipo
    if fecha_hora is not None:
        partido.fecha_hora = fecha_hora
    if mesa_id is not None:
        partido.mesa_id = mesa_id
    db.commit()
    db.refresh(partido)
    return partido

def eliminar_partido(db, partido_id):
    partido = db.query(Partido).filter(Partido.id == partido_id).first()
    if partido:
        db.delete(partido)
        db.commit()
        return True
    return False