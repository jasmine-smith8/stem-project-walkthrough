from flask import Flask
from .home import home_route
from .generate_fact import generate_route, generate_fact_api, create_route, vote_route # TASK

def create_app():
    app = Flask(__name__,
                template_folder='../../../templates',
                static_folder='../../../static')
    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    app.add_url_rule("/generate", view_func=generate_route, methods=["GET"]) # TASK
    app.add_url_rule("/api/generate-fact", view_func=generate_fact_api, methods=["GET"])
    app.add_url_rule("/create", view_func=create_route, methods=["GET","POST"]) # TASK
    app.add_url_rule("/api/vote", view_func=vote_route, methods=["POST"]) # TASK

    # Print all registered routes
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> {rule.methods}")
    return app