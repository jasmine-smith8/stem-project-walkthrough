## docker-compose: Start the Docker container for the database.
.PHONY: docker-compose
docker-compose:
	docker compose -f docker-compose.yaml up -d db

## setup-db: Set up the database.
.PHONY: setup-db
setup-db:
	python internal/adapters/postgres/migrations/migrate.py 

## db-shell: Enter the facts database.
.PHONY: db-shell
db-shell:
	psql -h localhost -U postgres -d factsdb
