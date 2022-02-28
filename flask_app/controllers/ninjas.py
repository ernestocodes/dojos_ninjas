from flask import redirect, request, render_template
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    print(request.form)
    ninja_id = Ninja.save(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')

@app.route('/ninja/new')
def ninja_new():
    return render_template('new_ninja.html', dojos=Dojo.get_all())