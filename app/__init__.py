from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_moment import Moment


app = Flask(__name__)

app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
moment = Moment(app)

#leave at bottom to avoid circular import with routes
from app import routes, models