from flask import Flask
from .home import home_route
from .generate_fact import generate_route

def create_app():
    app = Flask(__name__,
                template_folder='../../../templates',
                static_folder='../../../static')
    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    app.add_url_rule("/generate", view_func=generate_route, methods=["GET"]) # TASK
    return app