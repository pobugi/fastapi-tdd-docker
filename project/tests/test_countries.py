from app.api import countries

TEST_DB = [
    {
      "Timor-Leste": "Asia"
    },
    {
      "Togo": "Africa"
    },
    {
      "Tokelau": "Oceania"
    },
    {
      "Tonga": "Oceania"
    },
    {
      "Trinidad and Tobago": "Americas"
    },
    {
      "Tunisia": "Africa"
    },
    {
      "Turkey": "Asia"
    },
    {
      "Turkmenistan": "Asia"
    },
    {
      "Turks and Caicos Islands": "Americas"
    },
    {
      "Tuvalu": "Oceania"
    },
    {
      "Uganda": "Africa"
    },
    {
      "Ukraine": "Europe"
    },
    {
      "United Arab Emirates": "Asia"
    },
    {
      "United Kingdom of Great Britain and Northern Ireland": "Europe"
    },
    {
      "United States of America": "Americas"
    },
    {
      "Uruguay": "Americas"
    },
    {
      "Uzbekistan": "Asia"
    },
    {
      "Vanuatu": "Oceania"
    },
    {
      "Venezuela (Bolivarian Republic of)": "Americas"
    },
    {
      "Viet Nam": "Asia"
    },
    {
      "Wallis and Futuna": "Oceania"
    },
    {
      "Western Sahara": "Africa"
    },
    {
      "Yemen": "Asia"
    },
    {
      "Zambia": "Africa"
    },
    {
      "Zimbabwe": "Africa"
    }
  ]

def test_create_country(test_app):
    initial_db_size = len(TEST_DB)
    country_obj = {
        "name": "France",
        "region": "Europe"
    }
    create_country = test_app.post("/countries", json=country_obj)
    assert create_country.status_code == 200
    # assert len(TEST_DB) == initial_db_size + 1

def test_delete_country(test_app):
    initial_db_size = len(TEST_DB)

    delete_country = test_app.delete("/countries/3")
    assert delete_country.status_code == 200
    # assert len(TEST_DB) == initial_db_size - 1