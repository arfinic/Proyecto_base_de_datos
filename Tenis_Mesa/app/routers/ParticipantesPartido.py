from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import Participantespartido as crud_participante
from app.database import get_db

router = APIRouter(prefix="/participantes_partido", tags=["participantes_partido"])

@router.post("/")
def crear_participante_partido(
    rol: str,
    participacion_id: int,
    partido_id: int,
    equipo_doble_id: int = None,
    db: Session = Depends(get_db)
):
    return crud_participante.crear_participante_partido(
        db, rol, participacion_id, partido_id, equipo_doble_id
    )

@router.get("/")
def listar_participantes_partido(db: Session = Depends(get_db)):
    return crud_participante.listar_participantes_partido(db)

@router.get("/{participante_id}")
def obtener_participante_partido(participante_id: int, db: Session = Depends(get_db)):
    participante = crud_participante.obtener_participante_partido(db, participante_id)
    if not participante:
        raise HTTPException(status_code=404, detail="No encontrado")
    return participante

@router.put("/{participante_id}")
def actualizar_participante_partido(
    participante_id: int,
    rol: str = None,
    participacion_id: int = None,
    partido_id: int = None,
    equipo_doble_id: int = None,  
    db: Session = Depends(get_db)
):
    participante = crud_participante.actualizar_participante_partido(
        db, participante_id, rol, participacion_id, partido_id, equipo_doble_id
    )
    if not participante:
        raise HTTPException(status_code=404, detail="No encontrado")
    return participante

@router.delete("/{participante_id}")
def eliminar_participante_partido(participante_id: int, db: Session = Depends(get_db)):
    ok = crud_participante.eliminar_participante_partido(db, participante_id)
    if not ok:
        raise HTTPException(status_code=404, detail="No encontrado")
    return {"ok": True}
