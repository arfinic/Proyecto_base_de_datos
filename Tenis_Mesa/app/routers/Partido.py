from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import Partido
from app.crud.Partido import crear_partido  
from datetime import datetime

router = APIRouter(
    prefix="/partidos",
    tags=["partidos"]
)

@router.post("/")
def crear_partido_router(
    tipo_partido: str,
    horario_inicio: str,
    fase: str = None,
    ronda_eliminacion: str = None,
    ganador_id: int = None,
    perdedor_id: int = None,
    is_bye: bool = False,
    torneo_id: int = None,
    categoria_id: int = None,
    mesa_id: int = None,
    db: Session = Depends(get_db)
):
    try:
        horario_dt = datetime.fromisoformat(horario_inicio)
    except Exception:
        raise HTTPException(status_code=400, detail="El formato de la fecha debe ser YYYY-MM-DDTHH:MM:SS")
    partido = crear_partido(
        db, tipo_partido, horario_dt, fase, ronda_eliminacion, ganador_id, perdedor_id,
        is_bye, torneo_id, categoria_id, mesa_id
    )
    return partido

@router.get("/")
def listar_partidos(db: Session = Depends(get_db)):
    return db.query(Partido).all()

@router.get("/{partido_id}")
def obtener_partido(partido_id: int, db: Session = Depends(get_db)):
    partido = db.query(Partido).get(partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return partido

@router.put("/{partido_id}")
def actualizar_partido(
    partido_id: int,
    tipo_partido: str = None,
    horario_inicio: str = None,
    fase: str = None,
    ronda_eliminacion: str = None,
    ganador_id: int = None,
    perdedor_id: int = None,
    is_bye: bool = None,
    torneo_id: int = None,
    categoria_id: int = None,
    mesa_id: int = None,
    db: Session = Depends(get_db)
):
    partido = db.query(Partido).get(partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    if tipo_partido is not None:
        partido.tipo_partido = tipo_partido
    if horario_inicio is not None:
        partido.horario_inicio = datetime.fromisoformat(horario_inicio)
    if fase is not None:
        partido.fase = fase
    if ronda_eliminacion is not None:
        partido.ronda_eliminacion = ronda_eliminacion
    if ganador_id is not None:
        partido.ganador_id = ganador_id
    if perdedor_id is not None:
        partido.perdedor_id = perdedor_id
    if is_bye is not None:
        partido.is_bye = is_bye
    if torneo_id is not None:
        partido.torneo_id = torneo_id
    if categoria_id is not None:
        partido.categoria_id = categoria_id
    if mesa_id is not None:
        partido.mesa_id = mesa_id
    db.commit()
    db.refresh(partido)
    return partido

@router.delete("/{partido_id}")
def eliminar_partido(partido_id: int, db: Session = Depends(get_db)):
    partido = db.query(Partido).get(partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    db.delete(partido)
    db.commit()
    return {"message": "Partido eliminado"}
