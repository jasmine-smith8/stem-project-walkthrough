# Tasks P0.3, P3.3

from flask import Flask
from .home import home_route
# TODO: Import the get_route function from the get_fact module
from .create_fact import create_route
# TODO: Import the vote_fact function from the vote_fact module

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')

    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    # TODO: Add a URL rule for the generate route
    app.add_url_rule("/create", view_func=create_route, methods=["GET","POST"]) # TASK
    # TODO: Add a URL rule for the vote route

    return app