from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import Categoria as crud_categoria

"""
Módulo de rutas (router) para Categoría

Administra las diferentes categorías de competencia, definidas por rangos de edad, género y condiciones de juego (sets, puntos). Permite realizar operaciones CRUD para organizar mejor los participantes según sus características y nivel. Utiliza sesiones de base de datos de FastAPI para las transacciones.
"""

router = APIRouter(
        prefix="/categorias",
        tags=["categorias"]
                )

@router.post("/")
def crear_categoria(nombre: str, edad_minima: int, edad_maxima: int, genero: str, sets_por_partido: int, puntos_por_set: int, db: Session = Depends(get_db)):
    return crud_categoria.crear_categoria(db, nombre, edad_minima, edad_maxima, genero, sets_por_partido, puntos_por_set)

@router.get("/")
def listar_categorias(db: Session = Depends(get_db)):
    return crud_categoria.listar_categorias(db)

@router.get("/{categoria_id}")
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud_categoria.obtener_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@router.delete("/{categoria_id}")
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    eliminado = crud_categoria.eliminar_categoria(db, categoria_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return {"ok": True}