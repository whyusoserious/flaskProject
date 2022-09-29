import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# root = sys.path[1]
# conf = os.path.join(root, 'instance/config.py')

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://admin:admin@localhost/public'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config.from_pyfile(conf)

db = SQLAlchemy(app)

from app import api