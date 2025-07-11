from fastapi import APIRouter, Depends, HTTPException
from app.crud import Torneo as crud_torneo
from app.database import SessionLocal

router = APIRouter(
        prefix="/Torneos",
        tags=["Torneos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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