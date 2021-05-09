# this script should be run before running the app.py script
from app import db, User

db.create_all()