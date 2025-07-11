from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import Grupo as crud_grupo

"""
Módulo de rutas (router) para Grupo

Administra los grupos de jugadores o equipos dentro de una categoría específica de un torneo. Permite crear, consultar, modificar y eliminar grupos, así como gestionar la relación con sus categorías y participaciones asociadas. Utiliza sesiones de base de datos para integridad de la información.
"""

router = APIRouter(
        prefix="/Grupos",
        tags=["Grupos"])

@router.post("/")
def crear_grupo(nombre: str, torneo_id: int, db=Depends(get_db)):
    return crud_grupo.crear_grupo(db, nombre, torneo_id)

@router.get("/")
def listar_grupos(db=Depends(get_db)):
    return crud_grupo.listar_grupos(db)

@router.get("/{grupo_id}")
def obtener_grupo(grupo_id: int, db=Depends(get_db)):
    grupo = crud_grupo.obtener_grupo(db, grupo_id)
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo no encontrado")
    return grupo

@router.delete("/{grupo_id}")
def eliminar_grupo(grupo_id: int, db=Depends(get_db)):
    eliminado = crud_grupo.eliminar_grupo(db, grupo_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Grupo no encontrado")
    return {"detail": "Grupo eliminado correctamente"}
