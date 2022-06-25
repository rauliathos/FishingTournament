from application import app, db
from application.models import Angler, Catches
from application.forms import AnglerForm
from flask import redirect, request, url_for, render_template

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    angler = Angler.query.all()
    catches = Catches.query.all()
    return render_template('layout.html', angler=angler, catches=catches)   
@app.route('/home')
def home():
    return render_template('home.html') 

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add_angler', methods=['GET','POST'])
def add_angler():
    form = AnglerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            anglerData = Angler(
                team = form.team.data,
                email = form.email.data,
                fee = form.fee.data
            )
            db.session.add(anglerData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addangler.html', form=form)

