from flask import render_template, request
from ..postgres.create_fact import PostgresFactRepository
from ...usecases.create_fact import CreateFactUseCase

repository = PostgresFactRepository()
usecase = CreateFactUseCase(repository)

# TASK
def create_route():
    if request.method == "GET":
        # Render the form for creating a new fact
        return render_template("create.html")
    if request.method == "POST":
        fact_text = request.form.get("fact_text")
        category = request.form.get("category") 
        if not fact_text:
            return "Fact text is required", 400
        fact_create_entity = usecase.create_fact(fact_text, category)
        return render_template("create.html", random_fact=fact_create_entity.fact, category=fact_create_entity.category)
