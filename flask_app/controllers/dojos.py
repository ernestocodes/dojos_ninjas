from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('dojos')

@app.route('/dojos')
def dojos():
    return render_template('new_dojo.html', dojos=Dojo.get_all())

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show(id):
    data = {
        'id' : id
    }
    dojo=Dojo.get_dojo_with_ninjas(data)
    return render_template('show_dojo.html', dojo=dojo)



