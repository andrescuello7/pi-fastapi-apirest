from fastapi import FastAPI
from config.database import engine
from src.routes.character_router import router
from src.models.character_models import Base

#Server running from FastAPI
app = FastAPI()

# Include Routes for methods HTTP
app.include_router(router)

# Create Models in Database
Base.metadata.create_all(bind=engine)