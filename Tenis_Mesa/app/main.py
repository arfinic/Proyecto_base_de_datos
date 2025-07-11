from fastapi import FastAPI
from app.routers import jugador, asociacion, equipodoble, categoria, torneo, grupo

app = FastAPI()

app.include_router(jugador.router)
app.include_router(asociacion.router)
app.include_router(equipodoble.router)
app.include_router(categoria.router)
app.include_router(torneo.router)
app.include_router(grupo.router)

if __name__ == "__main__":
    from app.database import engine, Base
    Base.metadata.create_all(bind=engine)