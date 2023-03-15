from app import app
from flask import render_template
from app.forms import TaskForm

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])

def index():
    form = TaskForm()
    return render_template('index.html', form=form)