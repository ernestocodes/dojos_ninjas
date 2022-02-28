from flask import Flask, redirect, render_template, request
from dojo import Dojo
from ninja import Ninja

app=Flask(__name__)

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

@app.route('/dojo/<int:id>')
def show(id):
    data = {
        'id' : id
    }
    dojo=Dojo.get_dojo_with_ninjas(data)
    return render_template('show_dojo.html', dojo=dojo)

@app.route('/ninja/new')
def ninja_new():
    return render_template('new_ninja.html', dojos=Dojo.get_all())

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/dojos')

if __name__ =="__main__":
    app.run(debug=True)