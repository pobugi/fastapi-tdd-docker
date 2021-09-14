from typing import List
from attr import s

from fastapi import APIRouter, HTTPException
# from pydantic.types import PaymentCardBrand

from app.api import crud
from app.models.pydantic import (
    CountryPayloadSchema, 
    CountryResponseSchema, 
    CountryUpdatePayloadSchema
)
from app.models.tortoise import CountrySchema

# from pydantic import BaseModel
# from app.config import get_settings, Settings
# from app.api.countries_parser.countries import CountryData


router = APIRouter()

@router.post("/", response_model=CountryResponseSchema, status_code=201)
async def create_country(payload: CountryPayloadSchema) -> CountryResponseSchema:
    country_id = await crud.post(payload)

    response_object = {
        "id": country_id,
        "name": payload.name
    }
    return response_object


@router.get("/", response_model=List[CountrySchema])
async def read_all_countries() -> List[CountrySchema]:
    return await crud.get_all()


@router.get("/{id}/", response_model=CountrySchema)
async def read_country(id: int) -> CountrySchema:
    country = await crud.get(id)
    if not country:
        raise HTTPException(
            status_code=404, 
            detail="Country not found"
        )
    return country


@router.delete("/{id}/", response_model=CountryResponseSchema)
async def delete_country(id: int) -> CountryResponseSchema:
    country = await crud.get(id)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    await crud.delete(id)

    return country

@router.put("/{id}/", response_model=CountrySchema)
async def update_country(id: int, payload: CountryUpdatePayloadSchema) -> CountrySchema:
    country = await crud.put(id, payload)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country

