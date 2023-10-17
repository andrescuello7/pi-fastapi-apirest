from typing import List
from fastapi import APIRouter
from fastapi.params import Depends, Depends
from starlette.responses import RedirectResponse

from config.database import Session, get_db
from enums.routes_enum import RoutesEnum
from enums.request_status_enum import HttpStatus

from interfaces.i_request import RequestResponse
from src.models.character_models import CharacterModel
from src.schemas.character_schemas import CharacterSchema

router = APIRouter()
path = RoutesEnum()
requestResponse = RequestResponse()


# Route '/' redirect for swagger
@router.get("/")
def main():
    return RedirectResponse(url="/docs/")


# Get for all characters of DB
@router.get(path.get_all_characters, response_model=List[CharacterSchema])
def find_all_characters(db: Session = Depends(get_db)):
    response = db.query(CharacterModel).all()
    if response:
        return response
    return requestResponse.error("Error in show characters", HttpStatus.BAD_REQUEST)


# Get Element for ID of url parameter
@router.get(path.get_character_by_id)
def find_character_by_id(id: int, db: Session = Depends(get_db)):
    response = db.query(CharacterModel).filter_by(id=id).first()
    if response:
        return response
    return requestResponse.error("Error get characters for ID", HttpStatus.BAD_REQUEST)


# Create Character with model of schema
@router.post(path.post_character)
def create_character(req: CharacterSchema, db: Session = Depends(get_db)):
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
    if response:
        return requestResponse.response("Character created!", HttpStatus.CREATED)
    return requestResponse.error("Character not saved", HttpStatus.CONFLICT)


# Delete Character for ID of url parameter
@router.delete(path.delete_character)
def delete_character(id: int, db: Session = Depends(get_db)):
    response = db.query(CharacterModel).filter_by(id=id).first()
    db.delete(response)
    db.commit()
    if response:
        return requestResponse.response("Character deleted!", HttpStatus.OK)
    return requestResponse.error("Error delete characters", HttpStatus.CONFLICT)
