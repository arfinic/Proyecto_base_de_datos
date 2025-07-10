from fastapi import FastAPI
from app.routers import jugador, asociacion

app = FastAPI()

app.include_router(jugador.router)
app.include_router(asociacion.router)

if __name__ == "__main__":
    from app.database import engine, Base
    Base.metadata.create_all(bind=engine)