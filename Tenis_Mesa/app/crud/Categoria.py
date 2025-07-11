from app.model.models import Categoria

def crear_categoria(db, nombre, edad_minima, edad_maxima, genero, sets_por_partido, puntos_por_set):
    categoria = Categoria(
        nombre=nombre,
        edad_minima=edad_minima,
        edad_maxima=edad_maxima,
        genero=genero,
        sets_por_partido=sets_por_partido,
        puntos_por_set=puntos_por_set
    )
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

def listar_categorias(db):
    return db.query(Categoria).all()

def obtener_categoria(db, categoria_id):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def eliminar_categoria(db, categoria_id):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria:
        db.delete(categoria)
        db.commit()
        return True
    return False
