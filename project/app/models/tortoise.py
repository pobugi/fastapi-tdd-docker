from tortoise import fields, models


class Country(models.Model):
    name = fields.TextField()
    region = fields.TextField()

    def __str__(self) -> str:
        return self.name

class TextSummary(models.Model):
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url