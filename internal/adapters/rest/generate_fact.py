from flask import render_template, jsonify, request
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

# TASK
def create_route():
    if request.method == "GET":
        # Render the form for creating a new fact
        return render_template("create.html")
    if request.method == "POST":
        fact_text = request.form.get("fact_text")
        if not fact_text:
            return "Fact text is required", 400
        fact_create_entity = random_service.create(fact_text)
        return render_template("create.html", random_fact=fact_create_entity.fact)
