from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from starlette.responses import RedirectResponse

from config.database import Session, get_db
from enums.routes_enum import RoutesEnum
from src.models.character import CharacterModel
from src.schemas.character_schema import CharacterSchema

router = APIRouter()
path = RoutesEnum()


# Route '/' redirect for swagger
@router.get("/")
def main():
    return RedirectResponse(url="/docs/")


# Get for all characters of DB
@router.get(path.get_all_characters, response_model=List[CharacterSchema])
def find_all_characters(db: Session = Depends(get_db)):
    try:
        response = db.query(CharacterModel).all()
        return response
    except Exception as e:
        return {"error": str(e)}


# Get Element for ID of url parameter
@router.get(path.get_character_by_id)
def find_character_by_id(id: int, db: Session = Depends(get_db)):
    try:
        response = db.query(CharacterModel).filter_by(id=id).first()
        return response
    except Exception as e:
        return {"error": str(e)}


# Create Character with model of schema
@router.post(path.post_character, response_model=CharacterSchema)
def createCharacter(req: CharacterSchema, db: Session = Depends(get_db)):
    try:
        response = CharacterModel(
            name=req.name,
            height=req.height,
            mass=req.mass,
            hair_color=req.hair_color,
            skin_color=req.skin_color,
            eye_color=req.eye_color,
        )
        db.add(response)
        db.commit()
        db.refresh(response)
        return response
    except Exception as e:
        return {"error": str(e)}


# Delete Character for ID of url parameter
@router.delete(path.get_character_by_id, response_model=CharacterSchema)
def delete_character(id: int, db: Session = Depends(get_db)):
    try:
        response = db.query(CharacterModel).filter_by(id=id).first()
        db.delete(response)
        db.commit()
        return response
    except Exception as e:
        return {"error": str(e)}
