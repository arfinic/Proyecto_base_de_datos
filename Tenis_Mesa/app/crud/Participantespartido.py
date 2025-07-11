from app.model.models import ParticipantePartido

def crear_participante_partido(db, rol, participacion_id, partido_id, equipo_doble_id=None):
    participante = ParticipantePartido(
        rol=rol,
        participacion_id=participacion_id,
        partido_id=partido_id,
        equipo_doble_id=equipo_doble_id 
    )
    db.add(participante)
    db.commit()
    db.refresh(participante)
    return participante

def listar_participantes_partido(db):
    return db.query(ParticipantePartido).all()

def obtener_participante_partido(db, participante_id):
    return db.query(ParticipantePartido).filter(ParticipantePartido.id == participante_id).first()

def actualizar_participante_partido(db, participante_id, rol=None, participacion_id=None, partido_id=None, equipo_doble_id=None):
    participante = db.query(ParticipantePartido).filter(ParticipantePartido.id == participante_id).first()
    if participante:
        if rol is not None:
            participante.rol = rol
        if participacion_id is not None:
            participante.participacion_id = participacion_id
        if partido_id is not None:
            participante.partido_id = partido_id
        participante.equipo_doble_id = equipo_doble_id  
        db.commit()
        db.refresh(participante)
    return participante

def eliminar_participante_partido(db, participante_id):
    participante = db.query(ParticipantePartido).filter(ParticipantePartido.id == participante_id).first()
    if participante:
        db.delete(participante)
        db.commit()
        return True
    return False
