from run import db, Fighter

# Create all the tables
db.create_all()

# create fighters
conor = Fighter(name='Priti')
floyd = Fighter(name='Pushkaraj')

# add fighters to session
db.session.add(conor)
db.session.add(floyd)

# commit the fighters to database
db.session.commit()
