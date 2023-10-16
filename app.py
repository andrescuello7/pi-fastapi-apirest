from fastapi import FastAPI
from src.routes.character import router
from config.database import engine
from src.models.character import Base

app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)