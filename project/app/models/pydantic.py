from pydantic import BaseModel


# class SummaryPayloadSchema(BaseModel):
#     url: str


# class SummaryResponseSchema(SummaryPayloadSchema):
#     id: int

# class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
#     summary: str


class CountryPayloadSchema(BaseModel):
    name: str


class CountryResponseSchema(CountryPayloadSchema):
    id: int

class CountryUpdatePayloadSchema(CountryPayloadSchema):
    region: str
    name: str
