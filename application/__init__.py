from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SECRET_KEY'] = "shhhhhh" #this is the only way I don't get an arror from Jenkins!!!!
db = SQLAlchemy(app)

from application import routes