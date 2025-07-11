from app.model.models import ResultadoSet

def crear_resultado_set(db, numero_set, puntos, participante_partido_id, partido_id):
    resultado = ResultadoSet(
        numero_set=numero_set,
        puntos=puntos,
        participante_partido_id=participante_partido_id,
        partido_id=partido_id
    )
    db.add(resultado)
    db.commit()
    db.refresh(resultado)
    return resultado

def listar_resultados_set(db):
    return db.query(ResultadoSet).all()

def obtener_resultado_set(db, resultado_id):
    return db.query(ResultadoSet).filter(ResultadoSet.id == resultado_id).first()

def actualizar_resultado_set(db, resultado_id, numero_set=None, puntos=None, participante_partido_id=None, partido_id=None):
    resultado = db.query(ResultadoSet).filter(ResultadoSet.id == resultado_id).first()
    if resultado:
        if numero_set is not None:
            resultado.numero_set = numero_set
        if puntos is not None:
            resultado.puntos = puntos
        if participante_partido_id is not None:
            resultado.participante_partido_id = participante_partido_id
        if partido_id is not None:
            resultado.partido_id = partido_id
        db.commit()
        db.refresh(resultado)
    return resultado

def eliminar_resultado_set(db, resultado_id):
    resultado = db.query(ResultadoSet).filter(ResultadoSet.id == resultado_id).first()
    if resultado:
        db.delete(resultado)
        db.commit()
    return resultado

