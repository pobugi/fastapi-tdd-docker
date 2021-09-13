# fastapi-tdd-docker

Commands:

Build the image:
    docker-compose build

Run the container in detached mode:
    docker-compose up -d

Check the logs of the web service:
    docker-compose logs web

Build the new image and spin up the two containers:
    chmod +x project/entrypoint.sh
    docker-compose up -d --build

Access DB:
    docker-compose exec web-db psql -U postgres

Aerich init (migrations):
    docker-compose exec web aerich init -t app.db.TORTOISE_ORM

Create migration:
    docker-compose exec web aerich init-db

Apply migration:
    docker-compose exec web aerich upgrade

Run the tests:
    docker-compose exec web python -m pytest

Generate schema via Tortoise:
    docker-compose exec web python app/db.py

Test (curl):
    http --json POST http://localhost:8004/summaries/ url=http://testdriven.io