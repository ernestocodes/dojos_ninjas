from flask import redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/dojos')