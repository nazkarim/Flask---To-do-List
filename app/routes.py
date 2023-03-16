from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import TaskForm
from app.models import Tasks

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])

def index():
    form = TaskForm()
    if form.validate_on_submit():
        task = form.task.data
        due_date = form.due_date.data

        task_item = Tasks(task=task,due_date=due_date)

        db.session.add(task_item)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))

    tasks = Tasks.query.all()
    return render_template('index.html', form=form, task=tasks)