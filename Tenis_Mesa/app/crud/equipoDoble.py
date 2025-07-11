from sqlalchemy.orm import Session
from app.model import EquipoDoble, Jugador

def crear_equipo_doble(db: Session, jugador1_id: int, jugador2_id: int, nombre: str = None):
    """
    Crea un nuevo equipo doble.

    Parámetros:
        db (Session): Sesión de base de datos.
        nombre (str): Nombre del equipo doble.
        jugador1_id (int): ID del primer jugador.
        jugador2_id (int): ID del segundo jugador.

    Retorna:
        EquipoDoble: El equipo doble creado.
    """
    jugador1 = db.query(Jugador).filter(Jugador.id == jugador1_id).first()
    jugador2 = db.query(Jugador).filter(Jugador.id == jugador2_id).first()
    if not jugador1 or not jugador2:
        return None 
    equipo = EquipoDoble(jugador1_id=jugador1_id, jugador2_id=jugador2_id, nombre=nombre)
    db.add(equipo)
    db.commit()
    db.refresh(equipo)
    return equipo

def listar_equipos_dobles(db: Session):
    """
    Lista todos los equipos dobles.

    Parámetros:
        db (Session): Sesión de base de datos.

    Retorna:
        List[EquipoDoble]: Lista de equipos dobles.
    """
    return db.query(EquipoDoble).all()

def obtener_equipo_doble(db: Session, equipo_id: int):
    """
    Busca un equipo doble por ID.

    Parámetros:
        db (Session): Sesión de base de datos.
        equipo_id (int): ID del equipo doble.

    Retorna:
        EquipoDoble o None.
    """
    
    return db.query(EquipoDoble).filter(EquipoDoble.id == equipo_id).first()

def eliminar_equipo_doble(db: Session, equipo_id: int):
    """
    Elimina un equipo doble.

    Parámetros:
        db (Session): Sesión de base de datos.
        equipo_id (int): ID del equipo doble.

    Retorna:
        bool: True si eliminado, False si no.
    """
    equipo = db.query(EquipoDoble).filter(EquipoDoble.id == equipo_id).first()
    if not equipo:
        return False
    db.delete(equipo)
    db.commit()
    return True