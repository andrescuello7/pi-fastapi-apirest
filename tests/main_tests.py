from fastapi.testclient import TestClient
from typing import List

from main import app
from enums.routes_enum import RoutesEnum
from enums.request_status_enum import HttpStatus
from src.schemas.character_schemas import CharacterSchema


client = TestClient(app)
routes = RoutesEnum()

# Test for getting all characters
# Route -> /api/character/getAll
def test_find_all_characters():
    # Send a GET request to retrieve all characters
    response = client.get(
        routes.get_all_characters, headers={"accept": "application/json"}
    )
    characters: List(CharacterSchema) = response.json()
    assert response.status_code == HttpStatus.OK
    assert len(characters) != 0


# Test for creating a character
# Route -> /api/character/add
def create_character():
    global characterId
    # Send a POST request to create a character
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
    character: CharacterSchema = response.json()
    characterId = character["id"]
    assert response.status_code == HttpStatus.OK
    assert character != None


# Test for getting a character by ID
# Route -> /api/character/get/{id}
def find_character_by_id():
    # Send a GET request to retrieve a character by ID
    response = client.get(
        f"/api/character/get/{characterId}", headers={"accept": "application/json"}
    )
    character: CharacterSchema = response.json()
    assert response.status_code == HttpStatus.OK
    assert character != None


# Test for deleting a character
# Route -> /api/character/delete/{id}
def delete_character():
    global characterId
    # Send a DELETE request to delete a character by ID
    response = client.delete(
        f"/api/character/delete/{characterId}", headers={"accept": "application/json"}
    )
    assert response.status_code == HttpStatus.OK
    assert response.json() == {"detail": "Character deleted!"}


# Run the test cases
test_find_all_characters()
create_character()
find_character_by_id()
delete_character()
