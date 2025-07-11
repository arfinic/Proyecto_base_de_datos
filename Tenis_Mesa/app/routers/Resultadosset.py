from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import ResultadoSet as crud_resultadoset

"""
Módulo de rutas (router) para ResultadoSet

Administra los resultados individuales de cada set dentro de un partido. Permite registrar, consultar, actualizar y eliminar los puntajes obtenidos por los participantes en cada set, vinculando correctamente con los partidos y los participantes de cada set.
"""

router = APIRouter(
    prefix="/resultadosets",
    tags=["resultadosets"]
)

@router.post("/")
def crear_resultado_set(
    partido_id: int,
    participante_partido_id: int,
    numero_set: int,
    puntos: int,
    db: Session = Depends(get_db)
):
    return crud_resultadoset.crear_resultado_set(
        db, partido_id, participante_partido_id, numero_set, puntos
    )

@router.get("/")
def listar_resultados_sets(db: Session = Depends(get_db)):
    return crud_resultadoset.listar_resultados_sets(db)

@router.get("/{resultado_set_id}")
def obtener_resultado_set(resultado_set_id: int, db: Session = Depends(get_db)):
    resultado = crud_resultadoset.obtener_resultado_set(db, resultado_set_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="ResultadoSet no encontrado")
    return resultado

@router.put("/{resultado_set_id}")
def actualizar_resultado_set(
    resultado_set_id: int,
    partido_id: int = None,
    participante_partido_id: int = None,
    numero_set: int = None,
    puntos: int = None,
    db: Session = Depends(get_db)
):
    resultado = crud_resultadoset.actualizar_resultado_set(
        db, resultado_set_id, partido_id, participante_partido_id, numero_set, puntos
    )
    if not resultado:
        raise HTTPException(status_code=404, detail="ResultadoSet no encontrado")
    return resultado

@router.delete("/{resultado_set_id}")
def eliminar_resultado_set(resultado_set_id: int, db: Session = Depends(get_db)):
    eliminado = crud_resultadoset.eliminar_resultado_set(db, resultado_set_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="ResultadoSet no encontrado")
    return {"detail": "ResultadoSet eliminado correctamente"}
