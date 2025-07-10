from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import jugador as crud_jugador

router = APIRouter(
    prefix="/jugadores",
    tags=["jugadores"]
)

@router.post("/")
def crear_jugador(
    nombre: str, 
    fecha_nac: str, 
    genero: str, 
    ciudad: str, 
    pais: str, 
    asociacion_id: int = None, 
    db: Session = Depends(get_db)
):
    return crud_jugador.crear_jugador(db, nombre, fecha_nac, genero, ciudad, pais, asociacion_id)

@router.get("/")
def listar_jugadores(db: Session = Depends(get_db)):
    return crud_jugador.listar_jugadores(db)

@router.get("/{jugador_id}")
def obtener_jugador(jugador_id: int, db: Session = Depends(get_db)):
    jugador = crud_jugador.obtener_jugador(db, jugador_id)
    if jugador is None:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return jugador

@router.put("/{jugador_id}")
def actualizar_jugador(
    jugador_id: int, 
    nombre: str = None, 
    fecha_nac: str = None, 
    genero: str = None, 
    ciudad: str = None, 
    pais: str = None, 
    asociacion_id: int = None,
    db: Session = Depends(get_db)
):
    jugador = crud_jugador.actualizar_jugador(db, jugador_id, nombre, fecha_nac, genero, ciudad, pais, asociacion_id)
    if jugador is None:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return jugador

@router.delete("/{jugador_id}")
def eliminar_jugador(jugador_id: int, db: Session = Depends(get_db)):
    eliminado = crud_jugador.eliminar_jugador(db, jugador_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return {"ok": True, "mensaje": "Jugador eliminado"}
