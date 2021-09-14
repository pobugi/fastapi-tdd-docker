import json
from app.api import countries
# import pytest
# from tortoise.fields import data


def test_create_country(test_app_with_db):
		response = test_app_with_db.post(
			'/countries/',
			data=json.dumps({
				"name": "Russia",
			})
			)
		assert response.status_code == 201
		assert response.json()["name"] == "Russia"


def test_create_country_invalid_json(test_app):
		response = test_app.post("/countries/", data=json.dumps({}))
		assert response.status_code == 422


def test_read_country(test_app_with_db):
		response = test_app_with_db.post(
			"/countries/",
			data=json.dumps({"name": "Spain"})
		)
		country_id = response.json()["id"]

		response = test_app_with_db.get("/countries/{}".format(country_id))
		response_dict = response.json()

		assert response_dict["created_at"][:4] == '2021'
		assert response_dict["region"] == "Europe"
		assert response_dict["capital"] != "Barcelona"


def test_read_country_incorrect_id(test_app_with_db, country_id=9999999):
		response = test_app_with_db.get("/countries/{}".format(country_id))
		assert response.status_code == 404
		assert response.json()['detail'] == 'Country not found'


def test_read_all_countries(test_app_with_db):
		response = test_app_with_db.post("/countries/", data=json.dumps({"name": "Zimbabwe"}))
		country_id = response.json()["id"]

		response = test_app_with_db.get("/countries/")
		assert response.status_code == 200

		response_list = response.json()
		assert len(list(filter(lambda x: x["id"] == country_id, response_list))) == 1


def test_remove_country(test_app_with_db):
		response = test_app_with_db.post(
			'/countries/',
			data=json.dumps({
				"name": "Germany",
			})
			)
		print(response.json())
		country_id = response.json()["id"]

		response = test_app_with_db.delete("/summaries/{}/".format(country_id))
		assert response.status_code == 404
		assert 'not found' in response.json()["detail"].lower()


def test_remove_country_incorrect_id(test_app_with_db):
		response = test_app_with_db.delete("/countries/9435399/")
		assert response.status_code == 404
		assert 'not found' in response.json()["detail"].lower()
