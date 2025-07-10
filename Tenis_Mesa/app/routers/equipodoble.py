from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import equipoDoble as crud_equipodoble

router = APIRouter(
    prefix="/equiposdobles",
    tags=["equiposdobles"]
)

@router.post("/")
def crear_equipo_doble(jugador1_id: int, jugador2_id: int, nombre: str = None, db: Session = Depends(get_db)):
    equipo = crud_equipodoble.crear_equipo_doble(db, jugador1_id, jugador2_id, nombre)
    if equipo is None:
        raise HTTPException(status_code=400, detail="Uno o ambos jugadores no existen")
    return equipo

@router.get("/")
def listar_equipos_dobles(db: Session = Depends(get_db)):
    return crud_equipodoble.listar_equipos_dobles(db)

@router.get("/{equipo_id}")
def obtener_equipo_doble(equipo_id: int, db: Session = Depends(get_db)):
    equipo = crud_equipodoble.obtener_equipo_doble(db, equipo_id)
    if equipo is None:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo

@router.delete("/{equipo_id}")
def eliminar_equipo_doble(equipo_id: int, db: Session = Depends(get_db)):
    eliminado = crud_equipodoble.eliminar_equipo_doble(db, equipo_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return {"ok": True, "mensaje": "Equipo eliminado"}