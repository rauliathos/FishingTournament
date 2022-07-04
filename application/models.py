from application import db

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    fee = db.Column(db.Boolean, default=False)
    catch = db.relationship('Catches',  backref='teamsRef')

class Catches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team= db.Column(db.String(40), db.ForeignKey('teams.team'), nullable=False)
    species =db.Column(db.String(40), nullable=False)
    weight = db.Column(db.Float, nullable=False)
  
# class Results(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     team_name = db.Column(db.String(40), nullable=False, unique=True)
#     total = db.Column(db.Float, nullable=False)
    
    