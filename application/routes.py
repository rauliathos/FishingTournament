from webbrowser import get
from application import app, db
from application.models import Teams, Catches
from application.forms import TeamsForm, CatchesForm
from flask import redirect, url_for, render_template, request
import datetime

#@app.before_first_request
#def create_tables():
 #   db.create_all()

@app.route('/' )
def homepage():
    tms = Teams.query.all()
    cth = Catches.query.all()
    return render_template('team.html', tms=tms, cth=cth)   

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add_team', methods=['GET','POST'])
def add_team():
    form = TeamsForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            teamData = Teams(
                team = form.team.data,
                email = form.email.data,
                fee = form.fee.data
            )
            db.session.add(teamData)
            db.session.commit()
            print(teamData)
            return redirect(url_for('homepage'))
    return render_template('add_team.html', form=form)


@app.route('/add_catch', methods=['GET','POST'])
def add_catch():
    form = CatchesForm()
    form.team.choices= [(teams.team, teams.team) for teams in Teams.query.all()]
 
    if request.method == 'POST':
        if form.validate_on_submit():
            catchData = Catches(
                team = form.team.data, #change it to id
                species = form.species.data,
                weight= form.weight.data,
                total =  get.weight.data, #Calculate Button to calc the total
                rank =  form.rank.data
            )
            db.session.add(catchData)
            db.session.commit()
            #print(catchData)
            return redirect(url_for('homepage'))
    return render_template('add_catch.html', form=form)

@app.route('/fee_paid/<int:id>')
def fee_paid(id):
    team = Teams.query.get(id)
    team.fee = True
    db.session.commit()
    return redirect(url_for('homepage'))

@app.route('/fee_not_paid/<int:id>')
def fee_not_paid(id):
    team = Teams.query.get(id)
    team.fee = False
    db.session.commit()
    return redirect(url_for('homepage'))

@app.route('/update_team/<int:id>', methods= ['GET', 'POST'])
def update(id):
    form = TeamsForm()
    team = Teams.query.get(id)
    if form.validate_on_submit():
        team.team = form.team.data
        db.session.commit()
        return redirect(url_for('homepage'))
    elif request.method == 'GET':
        form.team.data = team.team
    return render_template('update.html', form=form)



@app.route('/delete/<int:id>')
def delete(id):
    team = Teams.query.get(id)
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for('homepage'))
  