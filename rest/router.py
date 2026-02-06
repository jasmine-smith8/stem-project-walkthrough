# Task P0.3

from flask import Flask
from .home import home_route
# Import the get_route function from the get_fact module
from .create_fact import create_route
from .vote_fact import vote_route

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    
    app.add_url_rule("/", view_func=home_route, methods=["GET"])
   # Add URL rules for the generate route

    app.add_url_rule("/create", view_func=create_route, methods=["GET","POST"]) # TASK
    app.add_url_rule("/api/vote", view_func=vote_route, methods=["POST"]) # TASK

    return app