from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import SelectField,DecimalField, IntegerField, StringField, BooleanField, SubmitField
class TeamsForm(FlaskForm):
    team = StringField("Team")
    email = StringField("Email")
    fee = BooleanField("Fee", default=False)
    submit = SubmitField("Submit")
    
class CatchesForm(FlaskForm):
    fishes =["Cod", "Red Cod","Whiting","Mackerel",
             "Dab", "Coalfish", "Plaice","Ling",
             "Bass", "Flounder", "Eel", "Pollack"]
    
    team = SelectField('Team', choices=[])
    species=SelectField('Species', choices=fishes)
    weight=DecimalField('weight')
    submit = SubmitField("Submit")
    
    
# class ResultsForm(FlaskForm):
    