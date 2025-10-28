from flask import Flask
from .home import home_route
from .get_fact import get_route
from .create_fact import create_route
from .vote_fact import vote_route

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    app.add_url_rule("/generate", view_func=get_route, methods=["GET"]) # TASK
    app.add_url_rule("/create", view_func=create_route, methods=["GET","POST"]) # TASK
    app.add_url_rule("/api/vote", view_func=vote_route, methods=["POST"]) # TASK

    # Print all registered routes
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> {rule.methods}")
    return app