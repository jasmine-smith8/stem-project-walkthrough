from flask import render_template
from ..postgres.generate_fact import PostgresFactRepository
from ...usecases.generate_fact import RandomFactService

repository = PostgresFactRepository()
random_service = RandomFactService(repository)

# TASK
def generate_route():
    fact_entity = random_service.generate()
    return render_template("generate.html", random_fact=fact_entity.fact)
