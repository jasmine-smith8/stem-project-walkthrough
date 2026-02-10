# Task P3.2

# TODO: Import necessary modules

def vote_route():
    data = request.json
    # TODO: Extract fact_id from the JSON data
    # TODO: Extract vote_type from the JSON data

    try:
        # TODO: Call the vote_fact function to get the updated fact details after voting

        # TODO: Determine the new count based on the vote type

        # TODO: Create the response JSON with fact_id, new_count, likes, and dislikes
        response = {}
        return jsonify(response), 200 # Return the JSON response with status code 200 for successful vote
    except ValueError as e: # Catch the ValueError raised by vote_fact for invalid vote types
        return jsonify({"error": str(e)}), 400