from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-ever-know'

bootstrap = Bootstrap(app)

#leave at bottom to avoid circular import with routes
from app import routes