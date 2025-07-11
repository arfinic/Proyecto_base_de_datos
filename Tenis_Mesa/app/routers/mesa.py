from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import mesa as crud_mesa

router = APIRouter(prefix="/mesas", tags=["mesas"])

@router.post("/")
def crear_mesa(numero: int, torneo_id: int, db: Session = Depends(get_db)):
    return crud_mesa.crear_mesa(db, numero, torneo_id)

@router.get("/")
def listar_mesas(db: Session = Depends(get_db)):
    return crud_mesa.listar_mesas(db)

@router.get("/{mesa_id}")
def obtener_mesa(mesa_id: int, db: Session = Depends(get_db)):
    mesa = crud_mesa.obtener_mesa(db, mesa_id)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return mesa

@router.put("/{mesa_id}")
def actualizar_mesa(mesa_id: int, numero: int = None, torneo_id: int = None, db: Session = Depends(get_db)):
    mesa = crud_mesa.actualizar_mesa(db, mesa_id, numero, torneo_id)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return mesa

@router.delete("/{mesa_id}")
def eliminar_mesa(mesa_id: int, db: Session = Depends(get_db)):
    mesa = crud_mesa.eliminar_mesa(db, mesa_id)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return {"buena": True, "mensaje": "mesa inexistente"}

