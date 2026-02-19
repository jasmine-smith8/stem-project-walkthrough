# Tasks P0.3, P1.3, P3.3

from flask import Flask
from .home import home_route
# TODO: Import the get_route function from the get_fact module
# TODO: (Task P1.3) Import the create_route function from the create_fact module
# TODO: Import the vote_fact function from the vote_fact module

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')

    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    # TODO: Add a URL rule for the generate route
    # TODO: Add a URL rule for the create route
    # TODO: Add a URL rule for the vote route

    return app