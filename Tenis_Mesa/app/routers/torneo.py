from fastapi import APIRouter, Depends, HTTPException
from app.crud import Torneo as crud_torneo
from sqlalchemy.orm import Session
from app.database import get_db
"""
Módulo de Rutas (Router) para Torneo

Este archivo implementa los endpoints para la gestión de torneos. Permite la administración completa del ciclo de vida de un torneo de tenis de mesa desde la creación, consulta, modificación y eliminación.

Las funcionalidades disponibles incluyen:

- Registrar un nuevo torneo con sus fechas y cantidad de mesas disponibles.
- Listar todos los torneos existentes en el sistema.
- Obtener los detalles de un torneo específico usando su identificador.
- Actualizar información relevante de un torneo, como fechas o cantidad de mesas.
- Eliminar un torneo en caso de cancelación o finalización.

Todos los endpoints aseguran el acceso a la base de datos usando la sesión proporcionada por FastAPI.
"""

router = APIRouter(
        prefix="/Torneos",
        tags=["Torneos"])

@router.post("/")
def crear_torneo(nombre: str, fecha_inscripcion: str, fecha_competencia: str, mesas_disponibles: int, db=Depends(get_db)):
    return crud_torneo.crear_torneo(db, nombre, fecha_inscripcion, fecha_competencia, mesas_disponibles)

@router.get("/")
def listar_torneos(db=Depends(get_db)):
    return crud_torneo.listar_torneos(db)

@router.get("/{torneo_id}")
def obtener_torneo(torneo_id: int, db=Depends(get_db)):
    torneo = crud_torneo.obtener_torneo(db, torneo_id)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return torneo

@router.delete("/{torneo_id}")
def eliminar_torneo(torneo_id: int, db=Depends(get_db)):
    eliminado = crud_torneo.eliminar_torneo(db, torneo_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return {"detail": "Torneo eliminado correctamente"}