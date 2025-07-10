from sqlalchemy.orm import Session
from app.model import Jugador

def crear_jugador(db: Session, nombre: str, fecha_nac: str, genero: str, ciudad: str, pais: str, asociacion_id: int = None):
    jugador = Jugador(
        nombre=nombre,
        fecha_nac=fecha_nac,
        genero=genero,
        ciudad=ciudad,
        pais=pais,
        asociacion_id=asociacion_id
    )
    db.add(jugador)
    db.commit()
    db.refresh(jugador)
    return jugador

def listar_jugadores(db: Session):
    return db.query(Jugador).all()

def obtener_jugador(db: Session, jugador_id: int):
    return db.query(Jugador).filter(Jugador.id == jugador_id).first()

def actualizar_jugador(db: Session, jugador_id: int, nombre=None, fecha_nac=None, genero=None, ciudad=None, pais=None, asociacion_id=None):
    jugador = db.query(Jugador).filter(Jugador.id == jugador_id).first()
    if not jugador:
        return None
    if nombre is not None:
        jugador.nombre = nombre
    if fecha_nac is not None:
        jugador.fecha_nac = fecha_nac
    if genero is not None:
        jugador.genero = genero
    if ciudad is not None:
        jugador.ciudad = ciudad
    if pais is not None:
        jugador.pais = pais
    if asociacion_id is not None:
        jugador.asociacion_id = asociacion_id
    db.commit()
    db.refresh(jugador)
    return jugador

def eliminar_jugador(db: Session, jugador_id: int):
    jugador = db.query(Jugador).filter(Jugador.id == jugador_id).first()
    if not jugador:
        return False
    db.delete(jugador)
    db.commit()
    return True

