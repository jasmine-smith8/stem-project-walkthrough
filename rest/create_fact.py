# TASK P1.2

from flask import render_template, request
from database import create_fact

def create_route():
    if request.method == "GET":
        # TODO: Render the create.html template

    if request.method == "POST":
        # TODO: Get the fact_text from the form

        # TODO: (Task P4.3) Get the category from the form

        # TODO: Check that fact text is provided, if not return an error
        
        # TODO: Call the create_fact function from the database folder

        return render_template() # TODO: Pass the HTML template, fact and category (Task P4.3) parameters
