from fastapi import FastAPI
from src.routes.character import router

app = FastAPI()
app.include_router(router)