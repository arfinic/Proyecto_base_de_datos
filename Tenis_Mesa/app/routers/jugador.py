from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import jugador as crud_jugador
"""
Módulo de Rutas (Router) para Jugador

Este archivo define los endpoints relacionados con la entidad Jugador. Permite gestionar la creación, consulta, actualización y eliminación de jugadores dentro del sistema de gestión de torneos de tenis de mesa.

Las rutas implementadas permiten:

- Crear un nuevo jugador con sus datos personales y, opcionalmente, su asociación.
- Listar todos los jugadores registrados.
- Obtener información detallada de un jugador por su identificador único.
- Actualizar los datos de un jugador existente (por ejemplo, para corregir errores o cambiar de asociación).
- Eliminar un jugador del sistema.

Todos los endpoints utilizan una sesión de base de datos gestionada por FastAPI mediante la dependencia `get_db`, lo que asegura el manejo adecuado de conexiones y transacciones.
"""

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
    return {"buena": True, "mensaje": "Jugador exterminado"}
