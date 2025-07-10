from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import asociacion as crud_asociacion

router = APIRouter(
    prefix="/asociaciones",
    tags=["asociaciones"]
)

@router.post("/")
def crear_asociacion(nombre: str, ciudad: str, pais: str, db: Session = Depends(get_db)):
    return crud_asociacion.crear_asociacion(db, nombre, ciudad, pais)

@router.get("/")
def listar_asociaciones(db: Session = Depends(get_db)):
    return crud_asociacion.listar_asociaciones(db)

@router.get("/{asociacion_id}")
def obtener_asociacion(asociacion_id: int, db: Session = Depends(get_db)):
    asociacion = crud_asociacion.obtener_asociacion(db, asociacion_id)
    if asociacion is None:
        raise HTTPException(status_code=404, detail="Asociación no encontrada")
    return asociacion

@router.put("/{asociacion_id}")
def actualizar_asociacion(
    asociacion_id: int,
    nombre: str = None,
    ciudad: str = None,
    pais: str = None,
    db: Session = Depends(get_db)
):
    asociacion = crud_asociacion.actualizar_asociacion(db, asociacion_id, nombre, ciudad, pais)
    if asociacion is None:
        raise HTTPException(status_code=404, detail="Asociación no encontrada")
    return asociacion

@router.delete("/{asociacion_id}")
def eliminar_asociacion(asociacion_id: int, db: Session = Depends(get_db)):
    eliminado = crud_asociacion.eliminar_asociacion(db, asociacion_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Asociación no encontrada")
    return {"bien": True, "mensaje": "Asociación ejecutada"}