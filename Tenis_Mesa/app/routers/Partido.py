from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import Partido as crud_partido

"""
Módulo de rutas (router) para Partido

Administra los encuentros o partidos del torneo, permitiendo registrar, consultar, actualizar y eliminar partidos. Cada partido está vinculado a una mesa, categoría y torneo, así como a los participantes correspondientes. Opera siempre usando sesiones de base de datos controladas por FastAPI.
"""

router = APIRouter(
    prefix="/partidos",
    tags=["partidos"]
)

@router.post("/")
def crear_partido(
    tipo: str,
    fecha_hora: str,
    mesa_id: int,
    torneo_id: int,
    grupo_id: int = None,
    ronda: int = None,
    db: Session = Depends(get_db)
):
    return crud_partido.crear_partido(db, tipo, fecha_hora, mesa_id, torneo_id, grupo_id, ronda)

@router.get("/")
def listar_partidos(db: Session = Depends(get_db)):
    return crud_partido.listar_partidos(db)

@router.get("/{partido_id}")
def obtener_partido(partido_id: int, db: Session = Depends(get_db)):
    partido = crud_partido.obtener_partido(db, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return partido

@router.put("/{partido_id}")
def actualizar_partido(
    partido_id: int,
    tipo: str = None,
    fecha_hora: str = None,
    mesa_id: int = None,
    torneo_id: int = None,
    grupo_id: int = None,
    ronda: int = None,
    db: Session = Depends(get_db)
):
    partido = crud_partido.actualizar_partido(
        db, partido_id, tipo, fecha_hora, mesa_id, torneo_id, grupo_id, ronda
    )
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return partido

@router.delete("/{partido_id}")
def eliminar_partido(partido_id: int, db: Session = Depends(get_db)):
    eliminado = crud_partido.eliminar_partido(db, partido_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return {"detail": "Partido eliminado correctamente"}