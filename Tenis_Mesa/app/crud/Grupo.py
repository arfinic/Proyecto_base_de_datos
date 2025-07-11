from app.model.models import Grupo

def crear_grupo(db, nombre, torneo_id):
    grupo = Grupo(nombre=nombre, torneo_id=torneo_id)
    db.add(grupo)
    db.commit()
    db.refresh(grupo)
    return grupo

def listar_grupos(db):
    return db.query(Grupo).all()

def obtener_grupo(db, grupo_id):
    return db.query(Grupo).filter(Grupo.id == grupo_id).first()

def eliminar_grupo(db, grupo_id):
    grupo = db.query(Grupo).filter(Grupo.id == grupo_id).first()
    if grupo:
        db.delete(grupo)
        db.commit()
        return True
    return False
