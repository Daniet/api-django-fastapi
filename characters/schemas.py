from typing import Optional
from pydantic import BaseModel

class CharacterBase(BaseModel):
    name: str
    alter_ego: str
    power: str

class CharacterCreate(CharacterBase):
    pass

class CharacterModel(CharacterBase):
    id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "examples": {
                "name": "SpiderMan",
                "alter_ego": "Peter Parker"
                "power": "Throw spider web"
            }
        } 

