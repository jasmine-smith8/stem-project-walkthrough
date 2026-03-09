# Tasks P0.2, P4.4

from flask import render_template, jsonify, request
from database import get_fact

def get_route():
    fact = None # TODO: (Task P0.2) Call database function to get a random fact
    fact = get_fact()


    # Check if the client wants JSON response based on query parameters
    wants_json = request.args.get("json") in ("1", "true", "True")

    if wants_json:
        return jsonify({
            "id": getattr(fact, "id", None),
            "fact": fact.fact,
            # TODO: (Task P4.3) Add category
            "likes": getattr(fact, "likes", 0),
            "dislikes": getattr(fact, "dislikes", 0) 
        })
    # Render the HTML template and pass the fact data to it
    # TODO: (Task P4.4) Add category data
    return render_template(
        "generate.html",
        None, # TODO: (Task P0.2) Update here to pass the fact data to the template
        None,
        None,
        None
    )
