from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import Participantespartido as crud_participantepartido

"""
Módulo de rutas (router) para ParticipantePartido

Gestiona la relación de participación específica en un partido, ya sea de jugadores individuales o equipos dobles. Permite crear, consultar, actualizar y eliminar estas relaciones, que conectan participaciones con partidos y roles (ej. titular, suplente).
"""

router = APIRouter(
    prefix="/participantespartido",
    tags=["participantespartido"]
)

@router.post("/")
def crear_participante_partido(
    partido_id: int,
    participacion_id: int,
    equipo_doble_id: int = None,
    es_ganador: bool = False,
    db: Session = Depends(get_db)
):
    return crud_participantepartido.crear_participante_partido(
        db, partido_id, participacion_id, equipo_doble_id, es_ganador
    )

@router.get("/")
def listar_participantes_partido(db: Session = Depends(get_db)):
    return crud_participantepartido.listar_participantes_partido(db)

@router.get("/{pp_id}")
def obtener_participante_partido(pp_id: int, db: Session = Depends(get_db)):
    pp = crud_participantepartido.obtener_participante_partido(db, pp_id)
    if not pp:
        raise HTTPException(status_code=404, detail="ParticipantePartido no encontrado")
    return pp

@router.put("/{pp_id}")
def actualizar_participante_partido(
    pp_id: int,
    partido_id: int = None,
    participacion_id: int = None,
    equipo_doble_id: int = None,
    es_ganador: bool = None,
    db: Session = Depends(get_db)
):
    pp = crud_participantepartido.actualizar_participante_partido(
        db, pp_id, partido_id, participacion_id, equipo_doble_id, es_ganador
    )
    if not pp:
        raise HTTPException(status_code=404, detail="ParticipantePartido no encontrado")
    return pp

@router.delete("/{pp_id}")
def eliminar_participante_partido(pp_id: int, db: Session = Depends(get_db)):
    eliminado = crud_participantepartido.eliminar_participante_partido(db, pp_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="ParticipantePartido no encontrado")
    return {"detail": "ParticipantePartido eliminado correctamente"}