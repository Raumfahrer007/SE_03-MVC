from flask import Blueprint, render_template, session, request, redirect
from flask import current_app as app
from app.blueprints.hello_world.model import Name

blueprint = Blueprint("hello_world", __name__)

@blueprint.get("/")
def index():
    if "name_object" in session:
        name = Name(session["name_object"]["name"])
        return render_template("/output.html", name=name)
    
    return render_template("/input.html")

@blueprint.post("/new")
def new_name():
    input = request.form.get("name_input")

    name = Name(input)
    session['name_object'] = name.__dict__
    app.logger.info("Name added to Session")
    return redirect("/")

@blueprint.get("/delete")
def delete_name():
    session.pop("name_object")
    app.logger.info("Name deleted from Session")
    return redirect("/")