from flask import render_template, jsonify, request
from ..postgres.vote_fact import PostgresFactRepository
from ...usecases.vote_fact import VoteFactUseCase

repository = PostgresFactRepository()
usecase = VoteFactUseCase(repository)

def vote_route():
    data = request.json
    fact_id = data.get("fact_id")
    vote_type = data.get("vote_type")

    try:
        updated_fact = usecase.vote_fact(fact_id, vote_type)
        
        new_count = updated_fact.likes if vote_type == 'like' else updated_fact.dislikes
        
        response = {
            "fact_id": updated_fact.id,
            "new_count": new_count,
            "likes": updated_fact.likes,
            "dislikes": updated_fact.dislikes
        }
        return jsonify(response), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400