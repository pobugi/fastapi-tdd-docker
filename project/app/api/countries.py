from os import name
from fastapi import APIRouter, Depends
from pydantic import BaseModel


from app.config import get_settings, Settings
from app.api.countries_parser.countries import CountryData


router = APIRouter()

# class Country(Model):
#     id = fields.IntField(pk=True)
#     name = fields.CharField(100, unique=True)
#     region = fields.CharField(100)



class Country(BaseModel):
    name: str
    region: str

countries_obj = CountryData()
DB = countries_obj.get_all_countries()

@router.get('/countries')
async def get_countries(settings: Settings = Depends(get_settings)):
    return {
        "countries": DB,
        "environment": settings.environment,
        "testing": settings.testing
    }

@router.get('/countries/{country_id}')
async def get_country(country_id: int, settings: Settings = Depends(get_settings)):
    return {
        "country {}".format(country_id): DB[country_id-1],
        "environment": settings.environment,
        "testing": settings.testing
    }

@router.post('/countries')
async def create_country(country: Country, settings: Settings = Depends(get_settings)):
    DB.append(country.dict())
    return {
        "countries": DB,
        "environment": settings.environment,
        "testing": settings.testing
    }

@router.delete('/countries/{city_id}')
async def delete_country(country_id: int, settings: Settings = Depends(get_settings)):
    DB.pop(country_id-1)
    return {
        "countries": DB,
        "environment": settings.environment,
        "testing": settings.testing
    }
