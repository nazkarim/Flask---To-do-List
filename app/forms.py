from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    task = StringField('Add Task', validators=[DataRequired()])
    due_date = DateField('Due date', validators=[DataRequired()])
    submit = SubmitField('Save')