from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Teams, Catches
from application.forms import TeamsForm,CatchesForm
from flask import redirect, url_for, render_template, request

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        #db.drop_all()
        db.create_all()
        # Create test registree
        teamSample = Teams(team="Sample1", email="sample1@sample.com", fee= True)
        db.session.add(teamSample)
        db.session.commit()
        
        teamSample =  Teams(team="Sample2", email="sample2@sample.com", fee= False)
        db.session.add(teamSample)
        db.session.commit()
        
        
        fishes =["Cod", "Red Cod","Whiting","Mackerel",
            "Dab", "Coalfish", "Plaice","Ling",
            "Bass", "Flounder", "Eel", "Pollack"]
        catchSample= Catches(team ="Sample1", species=fishes, weight = 1.23)
        db.session.add(catchSample)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()
        
        
    