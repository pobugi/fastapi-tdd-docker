import requests
# from app.api import summaries, countries
from typing import List, Union

from app.models.pydantic import (
    CountryPayloadSchema,
    CountryUpdatePayloadSchema,
    CountryResponseSchema
) #CountryResponseSchema, SummaryPayloadSchema, , 
from app.models.tortoise import Country#, TextSummary

# from app.api.countries_parser.countries import CountryData

def get_country_data(country_name):
    api_url = "http://restcountries.eu/rest/v2/name/{}"
    resp = requests.get(api_url.format(country_name))
    try: 
        data = resp.json()[0]
        result = {
            "name": data["name"],
            "capital": data["capital"],
            "region": data["region"],
            "population": data["population"]
        }
    except:
        result = {
            "name": country_name,
            "capital": 'n/a',
            "region": 'n/a',
            "population": 'n/a'
        }
    return result


async def post(payload: CountryPayloadSchema) -> int:
    country_data = get_country_data(payload.name)
    country = Country(
        name=country_data['name'],
        capital=country_data['capital'],
        region=country_data['region'],
        population=country_data['population']
    )
    await country.save()
    return country.id


async def get(id: int) -> Union[dict, None]:
    country = await Country.filter(id=id).first().values()
    if country:
        return country[0]
    return None


async def get_all() -> List:
    countries = await Country.all().values()
    return countries


async def delete(id: int) -> int:
    country = await Country.filter(id=id).first().delete()
    return country

async def put(id: int, payload: CountryPayloadSchema) -> Union[dict, None]:
    country = await Country.filter(id=id).update(name=payload.name, region=payload.region)
    if country: 
        updated_country = await Country.filter(id=id).first().values()
        return updated_country[0]
    return None
