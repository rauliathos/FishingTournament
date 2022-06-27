from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class TeamsForm(FlaskForm):
    team = StringField("Team")
    email = StringField("Email")
    fee = BooleanField("Fee", default=False)
    submit = SubmitField("Submit")