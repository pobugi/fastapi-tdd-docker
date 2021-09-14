import json
import pytest
from tortoise.fields import data


def test_create_country(test_app_with_db):
  response = test_app_with_db.post(
    '/countries/', 
    data=json.dumps({
      "name": "Russia",
      "region": "Europe"
    })
    )

  assert response.status_code == 201
  assert response.json()["name"] == "Russia"

def test_read_all_countries(test_app_with_db):
  response = test_app_with_db.post("/countries/", data=json.dumps({"name": "Zimbabwe"}))
  country_id = response.json()["id"]

  response = test_app_with_db.get("/countries/")
  assert response.status_code == 200

  response_list = response.json()
  assert len(list(filter(lambda x: x["id"] == country_id, response_list))) == 1