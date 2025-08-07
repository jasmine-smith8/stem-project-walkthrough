from flask import Flask, render_template, request
from ...usecases.generate_fact import RandomFactService

def create_app():
    app = Flask(__name__, template_folder='../../../templates')
    random_service = RandomFactService()

    @app.route("/generate", methods=["GET"])
    def generate():
        fact_entity = random_service.generate()
        return render_template("generate.html", random_fact=fact_entity.fact)

    return app