from pydantic import BaseModel


class CountryPayloadSchema(BaseModel):
    name: str


class CountryResponseSchema(CountryPayloadSchema):
    id: int


class CountryUpdatePayloadSchema(CountryPayloadSchema):
    region: str
    name: str
