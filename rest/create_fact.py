# TASKS P1.2, P4.3

from flask import render_template, request
from database import create_fact

def create_route():
    if request.method == "GET":
        # TODO: (Task P1.2) Render the create.html template

    if request.method == "POST":
        # TODO: (Task P1.2) Get the fact_text from the form

        # TODO: (Task P4.3) Get the category from the form

        # TODO: Check that fact text is provided, if not return an error
        
        # TODO: Call the create_fact function from the database folder

        return render_template() # TODO: Pass the HTML template, fact and category (Task P4.3) parameters
