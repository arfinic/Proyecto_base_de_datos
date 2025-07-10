from fastapi import FastAPI
from app.routers import jugador

app = FastAPI()

app.include_router(jugador.router)

if __name__ == "__main__":
    from app.database import engine, Base
    Base.metadata.create_all(bind=engine)