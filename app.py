from fastapi import FastAPI
from config.database import engine
from src.routes.character_router import router
from src.models.character_models import Base
import uvicorn

#Server running from FastAPI
app = FastAPI()

# Include Routes for methods HTTP
app.include_router(router)

# Create Models in Database
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8080, reload=True, workers=2)