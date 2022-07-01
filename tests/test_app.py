from modulefinder import Module
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
        test_team = Teams(team="Sample1", email="sample1@sample.com", fee= True)
        db.session.add(test_team)
        db.session.commit()
        
        test_team =  Teams(team="Sample2", email="sample2@sample.com", fee= False)
        db.session.add(test_team)
        db.session.commit()
        
        
        
        test_catch= Catches(team ="Sample1", species="Cod", weight = 1.23)
        db.session.add(test_catch)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()
        
        
class TestViews(TestBase):

    def test_homepage(self):
        response = self.client.get(url_for("homepage"))
        self.assertEqual(response.status_code, 200)
        
    def test_all_catches(self):
        response = self.client.get(url_for("all_catches"))
        self.assertEqual(response.status_code, 200)
        
    def test_about(self):
        response = self.client.get(url_for("about"))
        self.assertEqual(response.status_code, 200)
        
    def test_add_team(self):
        response = self.client.get(url_for("add_team"))
        data = dict(team="Sample1", email="sample1@sample.com", fee= True)
        self.assertEqual(response.status_code, 200)
        
    def test_add_catch(self):
        response = self.client.get(url_for("add_catch"))
        self.assertEqual(response.status_code, 200)
        
    def test_update_team(self):
        response = self.client.get(url_for("update", id=1))
        self.assertEqual(response.status_code, 200)
    
    def test_update_catch(self):
        response = self.client.get(url_for("update_catch", id=1))
        self.assertEqual(response.status_code, 200)        
        
               
    def test_fee_paid(self):
        response = self.client.get(url_for("fee_paid", id=1))
        self.assertEqual(response.status_code, 302)

    def test_fee_not_paid(self):
        response = self.client.get(url_for("fee_not_paid", id=2))
        self.assertEqual(response.status_code, 302)


    def test_delete_team(self):
        response = self.client.get(url_for("delete", id=2))
        self.assertEqual(response.status_code, 302)

    def test_delete_catch(self):
        response = self.client.get(url_for("delete_catch", id=1))
        self.assertEqual(response.status_code, 302)
        
        
class TestCreate(TestBase):
    def test_add_team(self):
        response = self.client.post(
            url_for('add_team'),
            data = dict(team="Sample3", email="sample3@sample.com", fee= False)  
            )
        assert Teams.query.filter_by(team="Sample3").first().id ==3
       
    def test_add_catch(self):
        response = self.client.post(
            url_for('add_catch'),
            data = dict(team ="Sample1", species="Mackerel", weight = 4.23)  
            )
        assert Catches.query.filter_by(species="Mackerel").first().id ==2
       
       
class TestUpdate(TestBase):
    
    def test_update_team(self):
        response = self.client.post(
            url_for('update', id=2),
              data = dict(team="SampleUpdated", email="sample3@sample.com", fee= False)  
            )
        assert Teams.query.filter_by(team="SampleUpdated").first().id ==2
       
       
    def test_update_catch(self):
        response = self.client.post(
            url_for('update_catch',id=1),
            data = dict(team ="Sample1", species="Cod", weight = 1.23)  
            )
        assert Catches.query.filter_by(team ="Sample1").first().id ==1

class TestDelete(TestBase):
    def test_delete_team(self):
        response = self.client.get(
            url_for('delete', id=2),
            follow_redirects=True
        )
        assert 'Sample2' not in response.data.decode()
                  
           
           
    def test_delete_catch(self):
        response = self.client.get(
            url_for('delete_catch', id=1),
           follow_redirects=True
        
    
        )
        
        assert 'Cod' not in response.data.decode()
 