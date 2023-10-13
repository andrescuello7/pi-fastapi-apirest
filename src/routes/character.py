from fastapi import APIRouter

from config.database import conn
from enums.routes_enum import RoutesEnum
from sqlalchemy import insert, delete
from src.models.character import character
from src.schemas.character_schema import Character

router = APIRouter()
path = RoutesEnum()

@router.post(path.post_character)
def createCharacter(character_data: Character):
    try:
        result = conn.execute(insert(character).values(dict(character_data)))
        return {'message': f'Character created successfully {conn.execute(character.select().where(character.c.id == result.lastrowid)).first()}'}
    except Exception as e:
        return {'error': str(e)}

@router.get(path.get_all_characters)
def find_all_characters():
    try:
        response = conn.execute(character.select()).fetchall()
        return {'message': response}
    except Exception as e:
        return {'error': str(e)}
    
@router.get(path.get_character_by_id)
def find_character_by_id(id: int):
    try:
        characters = conn.execute(character.select().where(character.c.id == id))
        response = [dict(item) for item in characters]
        if response:
            return {'message': response[0]}
        else:
            return {'message': 'Character not found'}
    except Exception as e:
        return {'error': str(e)}

@router.delete(path.get_character_by_id)
def delete_character(id: int):
    try:
        delete_character = delete(character).where(character.c.id == id)
        response = conn.execute(delete_character)
        if response.rowcount > 0:
            return {'message': f'Character deleted'}
        else:
            return {'message': 'Character not deleted'}
    except Exception as e:
        return {'error': str(e)}
