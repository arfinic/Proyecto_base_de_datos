from app.model.models import Torneo

def crear_torneo(db, nombre, fecha_inscripcion, fecha_competencia, mesas_disponibles):
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
    return db.query(Torneo).all()

def obtener_torneo(db, torneo_id):
    return db.query(Torneo).filter(Torneo.id == torneo_id).first()

def eliminar_torneo(db, torneo_id):
    torneo = db.query(Torneo).filter(Torneo.id == torneo_id).first()
    if torneo:
        db.delete(torneo)
        db.commit()
        return True
    return False