# This should be run only once and before running the app.py script

# This script imports the db and User classes from the app.py script

from app import db, User

# creates the database in the host computer in the specified location (specified in app.py not in this script)
db.create_all()