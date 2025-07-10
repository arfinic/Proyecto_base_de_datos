from sqlalchemy.orm import Session
from app.model import Asociacion

def crear_asociacion(db: Session, nombre: str, ciudad: str, pais: str):
    asociacion = Asociacion(
        nombre=nombre,
        ciudad=ciudad,
        pais=pais
    )
    db.add(asociacion)
    db.commit()
    db.refresh(asociacion)
    return asociacion

def listar_asociaciones(db: Session):
    return db.query(Asociacion).all()

def obtener_asociacion(db: Session, asociacion_id: int):
    return db.query(Asociacion).filter(Asociacion.id == asociacion_id).first()

def actualizar_asociacion(db: Session, asociacion_id: int, nombre: str = None, ciudad: str = None, pais: str = None):
    asociacion = db.query(Asociacion).filter(Asociacion.id == asociacion_id).first()
    if not asociacion:
        return None
    if nombre is not None:
        asociacion.nombre = nombre
    if ciudad is not None:
        asociacion.ciudad = ciudad
    if pais is not None:
        asociacion.pais = pais
    db.commit()
    db.refresh(asociacion)
    return asociacion

def eliminar_asociacion(db: Session, asociacion_id: int):
    asociacion = db.query(Asociacion).filter(Asociacion.id == asociacion_id).first()
    if not asociacion:
        return False
    db.delete(asociacion)
    db.commit()
    return True