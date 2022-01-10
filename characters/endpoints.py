from django.shortcuts import get_object_or_404

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.encoders import jsonable_encoder

from asgiref.sync import sync_to_async

from typing import List

from .models import Character
from .schemas import CharacterModel

no_exist_character = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="This character does not exist"
)

routes_characters = APIRouter(tags=["characters"])

@sync_to_async
@routes_characters.post(
    "",
    response_model=CharacterModel,
    status_code=status.HTTP_201_CREATED
)
def create_character(character: CharacterModel):
    new_character = Character.objects.create(
        name=character.name,
        alter_ego=character.alter_ego,
        power=character.power
    )
    new_character.save()

    return new_character

@sync_to_async
@routes_characters.get(
    "",
    response_model=List[CharacterModel],
    status_code=status.HTTP_200_OK
)
def read_characters():
    characters = list(Character.objects.all())
    
    return characters

@sync_to_async
@routes_characters.put(
    "/{character_id}",
    response_model=CharacterModel,
    status_code=status.HTTP_200_OK
)
def update_character(character_id: int, character: CharacterModel):
    try:
        edit_character = get_object_or_404(Character, pk=character_id)

        edit_character.name=character.name
        edit_character.alter_ego=character.alter_ego
        edit_character.power=character.power

        edit_character.save()

        return edit_character

    except:
        raise no_exist_character
    
        
@sync_to_async
@routes_characters.delete(
    "/{character_id}",
    response_model=CharacterModel,
    status_code=status.HTTP_200_OK
)
def delete_character(character_id: int):
    try:
        delete_character = get_object_or_404(Character, pk=character_id)
        delete_character.delete()

        return delete_character

    except:
        raise no_exist_character
    