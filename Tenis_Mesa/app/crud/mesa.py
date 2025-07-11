from sqlalchemy.orm import Session
from app.model.models import Mesa

def crear_mesa(db: Session, numero: int, torneo_id: int):
    mesa = Mesa(numero=numero, torneo_id=torneo_id)
    db.add(mesa)
    db.commit()
    db.refresh(mesa)
    return mesa

def listar_mesas(db: Session):
    return db.query(Mesa).all()

def obtener_mesa(db: Session, mesa_id: int):
    return db.query(Mesa).filter(Mesa.id == mesa_id).first()

def actualizar_mesa(db: Session, mesa_id: int, numero: int = None, torneo_id: int = None):
    mesa = db.query(Mesa).filter(Mesa.id == mesa_id).first()
    if mesa:
        if numero is not None:
            mesa.numero = numero
        if torneo_id is not None:
            mesa.torneo_id = torneo_id
        db.commit()
        db.refresh(mesa)
    return mesa

def eliminar_mesa(db: Session, mesa_id: int):
    mesa = db.query(Mesa).filter(Mesa.id == mesa_id).first()
    if mesa:
        db.delete(mesa)
        db.commit()
    return mesa