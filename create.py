from application import db
from application.models import Teams, Catches





db.drop_all()
db.create_all()

#dummyTeam = Teams(team='Cold Blood',email='coldblood@fishery.uk', fee=False) # Extra: this section populates the table with an example entry
#db.session.add(dummyTeam)
#db.session.commit()



