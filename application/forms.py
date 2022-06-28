from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, StringField, BooleanField, SubmitField

class TeamsForm(FlaskForm):
    team = StringField("Team")
    email = StringField("Email")
    fee = BooleanField("Fee", default=False)
    submit = SubmitField("Submit")
    
class CatchesForm(FlaskForm):
    team = SelectField('Team', choices=[])
    species=StringField('Species')
    weight=IntegerField('weight')
    total = IntegerField('total')
    rank = IntegerField('rank')
    submit = SubmitField("Submit")