from flask import render_template, jsonify, request
from ..postgres.get_fact import PostgresFactRepository
from ...usecases.get_fact import GetFactUseCase

repository = PostgresFactRepository()
usecase = GetFactUseCase(repository)

# TASK
def get_route():
    fact_entity = usecase.get_fact()
    wants_json = request.args.get("json") in ("1", "true", "True")
    if wants_json:
        return jsonify({
            "id": getattr(fact_entity, "id", None),
            "fact": fact_entity.fact,
            "category": getattr(fact_entity, "category", None)
        })
    return render_template("generate.html", random_fact=fact_entity.fact)
