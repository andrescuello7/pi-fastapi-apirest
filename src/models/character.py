from sqlalchemy import Column, Integer, String
from config.database import Base


class CharacterModel(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(255))
    skin_color = Column(String(255))
    eye_color = Column(String(255))
