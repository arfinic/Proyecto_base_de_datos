from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import Torneo as crud_torneo

router = APIRouter(prefix="/torneos", tags=["torneos"])

@router.post("/")
def crear_torneo(
    nombre: str,
    fecha_inscripcion_i: str,
    fecha_inscripcion_f: str,
    fecha_competencia_i: str,
    fecha_competencia_f: str,
    mesas_disponibles: int,
    db: Session = Depends(get_db)
):
    return crud_torneo.crear_torneo(
        db,
        nombre,
        fecha_inscripcion_i,
        fecha_inscripcion_f,
        fecha_competencia_i,
        fecha_competencia_f,
        mesas_disponibles
    )

@router.get("/")
def listar_torneos(db: Session = Depends(get_db)):
    return crud_torneo.listar_torneos(db)

@router.get("/{torneo_id}")
def obtener_torneo(torneo_id: int, db: Session = Depends(get_db)):
    torneo = crud_torneo.obtener_torneo(db, torneo_id)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return torneo

@router.put("/{torneo_id}")
def actualizar_torneo(
    torneo_id: int,
    nombre: str = None,
    fecha_inscripcion_i: str = None,
    fecha_inscripcion_f: str = None,
    fecha_competencia_i: str = None,
    fecha_competencia_f: str = None,
    mesas_disponibles: int = None,
    db: Session = Depends(get_db)
):
    update_data = {k: v for k, v in {
        "nombre": nombre,
        "fecha_inscripcion_i": fecha_inscripcion_i,
        "fecha_inscripcion_f": fecha_inscripcion_f,
        "fecha_competencia_i": fecha_competencia_i,
        "fecha_competencia_f": fecha_competencia_f,
        "mesas_disponibles": mesas_disponibles
    }.items() if v is not None}
    torneo = crud_torneo.actualizar_torneo(db, torneo_id, **update_data)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return torneo

@router.delete("/{torneo_id}")
def eliminar_torneo(torneo_id: int, db: Session = Depends(get_db)):
    if not crud_torneo.eliminar_torneo(db, torneo_id):
        raise HTTPException(status_code=404, detail="Torneo no encontrado")
    return {"detail": "Torneo eliminado"}
