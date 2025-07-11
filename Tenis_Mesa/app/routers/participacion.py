from fastapi import APIRouter, Depends, HTTPException
from app.crud import participacion as crud_participacion
from sqlalchemy.orm import Session
from app.database import get_db

"""
Módulo de rutas (router) para Participación

Gestiona las inscripciones de jugadores y equipos en los torneos, vinculando adecuadamente con categoría, torneo y grupo. Permite realizar operaciones CRUD sobre las participaciones, asegurando el correcto registro de los participantes en cada evento.
"""


router = APIRouter(
    prefix="/Participaciones",
    tags=["Participaciones"]
    )


@router.post("/")
def crear_participacion(jugador_id: int, torneo_id: int, categoria_id: int, grupo_id: int = None, equipo_id: int = None, db=Depends(get_db)):
    return crud_participacion.crear_participacion(db, jugador_id, torneo_id, categoria_id, grupo_id, equipo_id)

@router.get("/")
def listar_participaciones(db=Depends(get_db)):
    return crud_participacion.listar_participaciones(db)

@router.get("/{participacion_id}")
def obtener_participacion(participacion_id: int, db=Depends(get_db)):
    participacion = crud_participacion.obtener_participacion(db, participacion_id)
    if not participacion:
        raise HTTPException(status_code=404, detail="Participación no encontrada")
    return participacion

@router.put("/{participacion_id}")
def actualizar_participacion(
    participacion_id: int,
    jugador_id: int = None,
    torneo_id: int = None,
    categoria_id: int = None,
    grupo_id: int = None,
    equipo_id: int = None,
    db=Depends(get_db)
):
    participacion = crud_participacion.actualizar_participacion(
        db, participacion_id, jugador_id, torneo_id, categoria_id, grupo_id, equipo_id
    )
    if not participacion:
        raise HTTPException(status_code=404, detail="Participación no encontrada")
    return participacion

@router.delete("/{participacion_id}")
def eliminar_participacion(participacion_id: int, db=Depends(get_db)):
    eliminado = crud_participacion.eliminar_participacion(db, participacion_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Participación no encontrada")
    return {"detail": "Participación eliminada correctamente"}
