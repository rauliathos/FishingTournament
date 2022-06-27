from application import app, db
from application.models import Teams, Catches
from application.forms import TeamsForm
from flask import redirect, url_for, render_template, request
import datetime

#@app.before_first_request
#def create_tables():
 #   db.create_all()

@app.route('/' )
def homepage():
    tms = Teams.query.all()
    print(Teams)
    return render_template('team.html', tms=tms)   

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
            
            return redirect(url_for('homepage'))
    return render_template('add_team.html', form=form)


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
  