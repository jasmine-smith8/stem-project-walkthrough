from flask import render_template, jsonify
from ..postgres.generate_fact import PostgresFactRepository
from ...usecases.generate_fact import RandomFactService

repository = PostgresFactRepository()
random_service = RandomFactService(repository)

# TASK
def generate_route():
    fact_entity = random_service.generate()
    return render_template("generate.html", random_fact=fact_entity.fact)

def generate_fact_api():
    """API endpoint to get a new random fact as JSON"""
    fact_entity = random_service.generate()
    return jsonify({"fact": fact_entity.fact})
