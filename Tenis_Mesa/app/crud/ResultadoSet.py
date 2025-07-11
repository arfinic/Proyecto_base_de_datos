from app.model.models import ResultadoSet
from sqlalchemy.orm import Session

def crear_resultado_set(db: Session, partido_id: int, participante_partido_id: int, numero_set: int, puntos: int):
    resultado = ResultadoSet(
        partido_id=partido_id,
        participante_partido_id=participante_partido_id,
        numero_set=numero_set,
        puntos=puntos
    )
    db.add(resultado)
    db.commit()
    db.refresh(resultado)
    return resultado

def listar_resultados_sets(db: Session):
    return db.query(ResultadoSet).all()

def obtener_resultado_set(db: Session, resultado_set_id: int):
    return db.query(ResultadoSet).filter_by(id=resultado_set_id).first()

def actualizar_resultado_set(db: Session, resultado_set_id: int, partido_id=None, participante_partido_id=None, numero_set=None, puntos=None):
    resultado = db.query(ResultadoSet).filter_by(id=resultado_set_id).first()
    if not resultado:
        return None
    if partido_id is not None:
        resultado.partido_id = partido_id
    if participante_partido_id is not None:
        resultado.participante_partido_id = participante_partido_id
    if numero_set is not None:
        resultado.numero_set = numero_set
    if puntos is not None:
        resultado.puntos = puntos
    db.commit()
    db.refresh(resultado)
    return resultado

def eliminar_resultado_set(db: Session, resultado_set_id: int):
    resultado = db.query(ResultadoSet).filter_by(id=resultado_set_id).first()
    if not resultado:
        return False
    db.delete(resultado)
    db.commit()
    return True
