from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import ResultadoSet as crud_resultadoset
from app.database import get_db

router = APIRouter(prefix="/resultados_sets", tags=["resultados_sets"])

@router.post("/")
def crear_resultado_set(numero_set: int, puntos: int, participante_partido_id: int, partido_id: int, db: Session = Depends(get_db)):
    return crud_resultadoset.crear_resultado_set(db, numero_set, puntos, participante_partido_id, partido_id)

@router.get("/")
def listar_resultados_set(db: Session = Depends(get_db)):
    return crud_resultadoset.listar_resultados_set(db)

@router.get("/{resultado_id}")
def obtener_resultado_set(resultado_id: int, db: Session = Depends(get_db)):
    resultado = crud_resultadoset.obtener_resultado_set(db, resultado_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="ResultadoSet no encontrado")
    return resultado

@router.put("/{resultado_id}")
def actualizar_resultado_set(
    resultado_id: int,
    numero_set: int = None,
    puntos: int = None,
    participante_partido_id: int = None,
    partido_id: int = None,
    db: Session = Depends(get_db)
):
    resultado = crud_resultadoset.actualizar_resultado_set(
        db, resultado_id, numero_set, puntos, participante_partido_id, partido_id
    )
    if not resultado:
        raise HTTPException(status_code=404, detail="ResultadoSet no encontrado")
    return resultado

@router.delete("/{resultado_id}")
def eliminar_resultado_set(resultado_id: int, db: Session = Depends(get_db)):
    resultado = crud_resultadoset.eliminar_resultado_set(db, resultado_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="ResultadoSet no encontrado")
    return {"ok": True}
