from application import db

class Angler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    fee = db.Column(db.Boolean, default=False)

class Catches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species =db.Column(db.String(40), nullable=False, unique=True)
    weight = db.Column(db.Integer, nullable=False, unique=True)
    angler = db.Column(db.String(40), db.ForeignKey('angler.team'), nullable=False)
    total = db.Column(db.Integer, nullable=False, unique=True)
    rank = db.Column(db.Integer, nullable=False, unique=True)
    
    