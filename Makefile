## docker-compose: Start the Docker container for the database.
.PHONY: docker-compose
docker-compose:
	docker compose -f docker-compose.yaml up -d db


## db-shell: Enter the facts database.
.PHONY: db-shell
db-shell:
	psql -h localhost -U postgres -d factsdb
