from one import create_app

app = create_app()

if __name__ == '__main__': ## call the script directly
	app.run(debug=True)

"""
-- Windows10 CMDz --
set FLASK_APP=one.py
set FLASK_DEBUG=1

[!!]
* circular import
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on ==> no need to restart the server

db set up:
from _file name_ import db
db.create_all()
from _flname_ import User, Post
user_1 = User(username='Richiewww', email='admin@admin.com', password='admin')  ### watch-out for invalid input like repeats
db.session.add(user_1)
db.session.commit()
User.query.all()
User.query.filter_by(username='Corey').all()/.first()
user = User.query.filter_by(username='Corey').all()/.first()
user.id



===
db.drop_all()
db.create_all()


>>> from yourapp import create_app
>>> app = create_app()
>>> app.app_context().push()
"""