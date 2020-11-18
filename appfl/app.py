from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from appfl.config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

#app.register_blueprint(posts, url_prefix='/blog')