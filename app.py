from fastapi import FastAPI
from src.routes.character import router
from config.database import engine
from src.models.character import Base

#Server running from FastAPI
app = FastAPI()

# Include Routes for methods HTTP
app.include_router(router)

# Create Models in Database
Base.metadata.create_all(bind=engine)