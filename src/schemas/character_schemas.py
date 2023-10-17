from pydantic import BaseModel

# Schema for endpoints for characters methods http
class CharacterSchema(BaseModel):
    id: int
    name: str
    height: float
    mass: float
    hair_color: str
    skin_color: str
    eye_color: str
