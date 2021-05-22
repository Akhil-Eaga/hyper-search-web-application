# This should be run only once and before running the app.py script

# This script imports the db, User and Admin classes from the app.py script
from app import db, User, Admin
from werkzeug.security import generate_password_hash, check_password_hash


# creates the database in the host computer in the specified location (specified in app.py not in this script)
db.create_all()


# below code creates a default admin to access all admin level features
admin1 = Admin(username = "admin", email = "admin@admin.com", password = generate_password_hash("password"))
db.session.add(admin1)
db.session.commit()