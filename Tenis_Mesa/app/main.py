from fastapi import FastAPI
from app.routers import jugador, asociacion, equipodoble, categoria, torneo, grupo, mesa, Partido, ParticipantesPartido
from app.routers import Resultadosset, participacion

app = FastAPI()

app.include_router(jugador.router)
app.include_router(asociacion.router)
app.include_router(equipodoble.router)
app.include_router(categoria.router)
app.include_router(torneo.router)
app.include_router(mesa.router)
app.include_router(Partido.router)
app.include_router(participacion.router)
app.include_router(ParticipantesPartido.router)
app.include_router(Resultadosset.router)
app.include_router(grupo.router)

if __name__ == "__main__":
    from app.database import engine, Base
    Base.metadata.create_all(bind=engine)