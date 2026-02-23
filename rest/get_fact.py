# Task P0.2, P4.3

from flask import render_template, jsonify, request
from database import get_fact

def get_route():
    # TODO: (Task P0.2) Call database function to get a random fact

    # Check if the client wants JSON response based on query parameters
    wants_json = request.args.get("json") in ("1", "true", "True")

    if wants_json:
        return jsonify({
            "id": getattr(fact, "id", None),
            "fact": fact.fact,
            "likes": getattr(fact, "likes", 0),
            "dislikes": getattr(fact, "dislikes", 0) 
            # TODO: (Task P4.3) Add category
        })
    
    return render_template("generate.html") # Render the HTML template and pass the fact data to it
    # TODO: (Task P4.3) Add category data
