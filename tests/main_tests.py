from typing import List
from fastapi.testclient import TestClient

from main import app
from enums.routes_enum import RoutesEnum
from enums.request_status_enum import HttpStatus
from src.schemas.character_schemas import CharacterSchema

client = TestClient(app)
routes = RoutesEnum()


# Test for getAll characters
# Route -> /api/character/getAll
def test_find_all_characters():
    try:
        response = client.get(
            routes.get_all_characters, headers={"accept": "application/json"}
        )
        assert response.status_code == HttpStatus.OK
        # assert response.json() == List[CharacterSchema]
    except:
        print(f"Error in getAll characters, StatusCode {response.status_code}")


# Test for create character
# Route -> /api/character/add
def create_character():
    try:
        response = client.post(
            routes.post_character,
            headers={"accept": "application/json"},
            json={
                "id": 0,
                "name": "John Skywalker",
                "height": 172,
                "mass": 77,
                "hair_color": "blond",
                "skin_color": "fair",
                "eye_color": "blue",
            },
        )
        assert response.status_code == HttpStatus.CREATED
        assert response.json() == {"detail": "Character created!"}
    except:
        print(f"Character not saved, StatusCode {response.status_code}")


# Test for get by ID characters
# Route -> /api/character/get/{id}
def find_character_by_id(id: int):
    try:
        response = client.get(
            f"/api/character/get/{id}", headers={"accept": "application/json"}
        )
        assert response.status_code == HttpStatus.OK
        # assert response.json() == CharacterSchema
    except:
        print(f"Error get characters for ID, StatusCode {response.status_code}")


# Test for delete character
# Route -> /api/character/delete/{id}
def delete_character(id: int):
    try:
        response = client.delete(
            f"/api/character/delete/{id}", headers={"accept": "application/json"}
        )
        assert response.status_code == HttpStatus.OK
        assert response.json() == {"detail": "Character deleted!"}
    except:
        print(f"Error delete characters for ID, StatusCode {response.status_code}")


test_find_all_characters()
create_character()
find_character_by_id(3)
delete_character(3)
