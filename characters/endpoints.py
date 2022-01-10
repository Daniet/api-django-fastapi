from fastapi import APIRouter, Depends, status, HTTPException

from typing import List

from .models import Character
from .schemas import CharacterCreate, CharacterModel

routes_characters = APIRouter(
    prefix="/characters",
    tags=["characters"]
)

@routes_characters.post(
    "/",
    response_model=CharacterModel,
    status_code=status.HTTP_201_CREATED
)
async def create_character(character: CharacterCreate):
    new_character = Character.objects.create(
        name=character.name,
        alter_ego=character.alter_ego,
        power=character.power
    )
    new_character.save()

    return new_character

@routes_characters.get(
    "/",
    response_model=List[CharacterModel],
    status_code=status.HTTP_200_OK
)
async def read_characters():
    characters = Character.objects.all()

    return characters

@routes_characters.put(
    "/{character_id}",
    response_model=CharacterModel,
    status_code=status.HTTP_200_OK
)
async def update_character(character_id: int, character: CharacterModel):
    try:
        edit_character = Character.objects.get(character_id)

        edit_character.name=character.name
        edit_character.alter_ego=character.alter_ego
        edit_character.power=character.power

        edit_character.save()

        return edit_character

    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This character does not exist"
        )
        
@routes_characters.delete(
    "/{character_id}",
    response_model=CharacterModel,
    status_code=status.HTTP_200_OK
)
async def delete_character(character_id: int):
    try:
        delete_character = Character.objects.get(character_id)
        delete_character.delete()

        return delete_character

    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This character does not exist"
        )