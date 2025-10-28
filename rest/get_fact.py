from flask import render_template, jsonify, request
from database import get_fact

def get_route():
    fact = get_fact()
    wants_json = request.args.get("json") in ("1", "true", "True")
    if wants_json:
        return jsonify({
            "id": getattr(fact, "id", None),
            "fact": fact.fact,
            "category": getattr(fact, "category", None),
            "likes": getattr(fact, "likes", 0),
            "dislikes": getattr(fact, "dislikes", 0) 
        })
    return render_template("generate.html",
                         random_fact=fact.fact,
                         category=fact.category,
                         random_fact_id=fact.id,
                         random_fact_likes=getattr(fact, "likes", 0),
                         random_fact_dislikes=getattr(fact, "dislikes", 0))