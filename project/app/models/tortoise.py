from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Country(models.Model):
    name = fields.TextField()
    capital = fields.TextField()
    region = fields.TextField()
    population = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


CountrySchema = pydantic_model_creator(Country)