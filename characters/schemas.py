from typing import Optional

from pydantic import BaseModel


class CharacterModel(BaseModel):
    id: Optional[int]
    name: str
    alter_ego: str
    power: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "SpiderMan",
                "alter_ego": "Peter Parker",
                "power": "Throw spider web",
            }
        }
