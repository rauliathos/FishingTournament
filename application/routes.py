
from application import app, db
from application.models import Teams, Catches
from application.forms import TeamsForm, CatchesForm
from flask import redirect, url_for, render_template, request



@app.route('/' )
def homepage():
    tms = Teams.query.all()
    return render_template('team.html', tms=tms)  
 
@app.route('/all_catches')
def all_catches():
    cth = Catches.query.all()
    return render_template('catch.html', cth=cth)

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
    for teams in Teams.query.all():
        if teams.fee == True:
            form.team.choices += [teams.team]
    
    if request.method == 'POST':
        if form.validate_on_submit():
            catchData = Catches(
                team = form.team.data, #change it to id
                species = form.species.data,
                weight= form.weight.data,
               # total =  get.weight.data, #Calculate Button to calc the total
                #rank =  form.rank.data
            )
            db.session.add(catchData)
            db.session.commit()
            #print(catchData)
            return redirect(url_for('all_catches'))
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
        team.email = form.email.data
        db.session.commit()
        return redirect(url_for('homepage'))
    elif request.method == 'GET':
        form.team.data = team.team
        form.email.data=team.email
    return render_template('update.html', form=form)


@app.route('/update_catch/<int:id>', methods= ['GET', 'POST'])
def update_catch(id):
    form = CatchesForm()
    catch = Catches.query.get(id)
    for teams in Teams.query.all():
        if teams.fee == True:
            form.team.choices += [teams.team]
           
        
    if form.validate_on_submit():
        catch.team = form.team.data
        catch.species = form.species.data
        catch.weight = form.weight.data
        db.session.commit()
        return redirect(url_for('all_catches'))
    elif request.method == 'GET':
        form.team.data = catch.team
        form.species.data=catch.species
        form.weight.data= catch.weight
    return render_template('update_catch.html', form=form)
   

@app.route('/delete/<int:id>')
def delete(id):
    team = Teams.query.get(id)
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for('homepage'))


@app.route('/delete_catch/<int:id>')
def delete_catch(id):
    catch = Catches.query.get(id)
    db.session.delete(catch)
    db.session.commit()
    return redirect(url_for('all_catches'))


# @app.route('/total')
# def total():
#     xxx=[]
#     total=0
    
    
#     for catch in Catches.query.all():
#         xxx+=[catch.team]
#     for i in xxx:
#         if xxx.count(i)>1:
            
#             total+=catch.weight
#             print(f'TOTAL={total}')
#         print(f'i={i}')
        
#         print(f'xxx={xxx[0]}') #xxx=['aaaa', 'pais', 'dana', 'aaaa']
#         print(f'xxx={xxx[1]}') #xxx=['aaaa', 'pais', 'dana', 'aaaa']
#         print(f'xxx={xxx[2]}') #xxx=['aaaa', 'pais', 'dana', 'aaaa']
#         print(f'xxx={xxx[3]}') #xxx=['aaaa', 'pais', 'dana', 'aaaa']
#         print(f'catch={catch}')
#         print(catch.team)
#         print(catch.weight)