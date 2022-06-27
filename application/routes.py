from application import app, db
from application.models import Teams, Catches
from application.forms import TeamsForm
from flask import redirect, request, url_for, render_template

#@app.before_first_request
#def create_tables():
 #   db.create_all()

@app.route('/')
def index():
    teams = Teams.query.all()
    print(teams)
    return render_template("team.html",teams=team)   


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add_team', methods=['GET','POST'])
def team():
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
            return redirect(url_for('team'))
    return render_template('add_team.html', form=form)


@app.route('/fee_paid/<int:id>')
def fee_paid(id):
    team = Teams.query.get(id)
    team.fee = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/fee_not_paid/<int:id>')
def fee_not_paid(id):
    team = Teams.query.get(id)
    team.fee = False
    db.session.commit()
    return redirect(url_for('index'))
