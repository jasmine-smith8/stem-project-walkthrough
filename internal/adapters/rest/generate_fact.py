from flask import render_template, jsonify, request
from ..postgres.generate_fact import PostgresFactRepository
from ...usecases.generate_fact import RandomFactService

repository = PostgresFactRepository()
random_service = RandomFactService(repository)

# TASK
def generate_route():
    fact_entity = random_service.generate()
    return render_template(
        "generate.html",
        random_fact=fact_entity.fact,
        random_fact_id=fact_entity.id,
        random_fact_likes=fact_entity.likes,
        random_fact_dislikes=fact_entity.dislikes
    )

def generate_fact_api():
    """API endpoint to get a new random fact as JSON"""
    fact_entity = random_service.generate()
    return jsonify({
        "fact": fact_entity.fact,
        "id": fact_entity.id,
        "likes": fact_entity.likes,
        "dislikes": fact_entity.dislikes
    })

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

# TASK
def vote_route():
    if request.method == "POST":
        try:
            # Check if we have any data at all
            if not request.data:
                return jsonify({"error": "No data received in request body"}), 400
            
            # Try to parse JSON
            try:
                data = request.get_json(force=True)
                print(f"Parsed JSON data: {data}")
            except Exception as json_error:
                print(f"JSON parsing error: {json_error}")
                return jsonify({"error": "Invalid JSON format", "details": str(json_error)}), 400
            
            if not data:
                return jsonify({"error": "Empty JSON data"}), 400
            
            fact_id = data.get("fact_id")
            vote_type = data.get("vote_type")
            
            print(f"Extracted - fact_id: {fact_id}, vote_type: {vote_type}")

            if not fact_id:
                return jsonify({"error": "Missing fact_id"}), 400
            
            if vote_type not in ["like", "dislike"]:
                return jsonify({"error": "Invalid vote_type, must be 'like' or 'dislike'"}), 400

            # Convert fact_id to int
            try:
                fact_id_int = int(fact_id)
            except (ValueError, TypeError) as convert_error:
                return jsonify({"error": "fact_id must be a valid integer", "details": str(convert_error)}), 400

            # Perform the vote operation
            if vote_type == "like":
                repository.increment_likes(fact_id_int)
                new_count = repository.get_likes_count(fact_id_int)
            else:
                repository.increment_dislikes(fact_id_int)
                new_count = repository.get_dislikes_count(fact_id_int)

            return jsonify({"new_count": new_count}), 200

        except Exception as e:
            print(f"Unexpected error in vote_route: {e}")
            import traceback
            traceback.print_exc()
            return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

    return jsonify({"error": "Method not allowed"}), 405
