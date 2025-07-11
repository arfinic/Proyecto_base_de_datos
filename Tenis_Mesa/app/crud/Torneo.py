from app.model.models import Torneo

def crear_torneo(db, nombre, fecha_inscripcion_i, fecha_inscripcion_f, fecha_competencia_i, fecha_competencia_f, mesas_disponibles):
    torneo = Torneo(
        nombre=nombre,
        fecha_inscripcion_i=fecha_inscripcion_i,
        fecha_inscripcion_f=fecha_inscripcion_f,
        fecha_competencia_i=fecha_competencia_i,
        fecha_competencia_f=fecha_competencia_f,
        mesas_disponibles=mesas_disponibles
    )
    db.add(torneo)
    db.commit()
    db.refresh(torneo)
    return torneo

def listar_torneos(db):
    return db.query(Torneo).all()

def obtener_torneo(db, torneo_id):
    return db.query(Torneo).filter(Torneo.id == torneo_id).first()

def actualizar_torneo(db, torneo_id, **kwargs):
    torneo = obtener_torneo(db, torneo_id)
    if not torneo:
        return None
    for key, value in kwargs.items():
        setattr(torneo, key, value)
    db.commit()
    db.refresh(torneo)
    return torneo

def eliminar_torneo(db, torneo_id):
    torneo = obtener_torneo(db, torneo_id)
    if torneo:
        db.delete(torneo)
        db.commit()
        return True
    return False