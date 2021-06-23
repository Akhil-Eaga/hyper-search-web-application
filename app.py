# importing necessary python and flask libraries
import os
import sys
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import json

# base directory - the directory where "this" file resides in the host computer
basedir = os.path.abspath(os.path.dirname(__file__))

# app initialization and configuration settings
app = Flask(__name__)
app.config["SECRET_KEY"] = "jkshdfkafkanvjjgbajlgbsldfgjlfngbjhlsbfgjsbgjlsbdfgjklsbdfgjklsjklgjkl"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# database initialization, connection and the login manager configuration
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
# overwriting the default login view from "login" to "admin_login"
# this is written in this way to be able to quickly find, remove and edit admin related fucntionality
login_manager.login_view = "admin_login"

# User Database model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    username = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(90))
    attempt = db.Column(db.Integer)
    correct = db.Column(db.Integer)
    wrong = db.Column(db.Integer)
    score = db.Column(db.Float)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.attempt = 0
        self.correct = 0
        self.wrong = 0
        self.score = 0.0

# Admin Database model
class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(90))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

# method to load the user upon input of successful login credentials
@login_manager.user_loader
def load_user(user_id):
    # this is used for user login but not for admin login
    if User.query.get(int(user_id)):
        return User.query.get(int(user_id))
    else:
        print("No user found, looking for admin..")
        return Admin.query.get(int(user_id))

###########################################################################################
##########################              FORMS          ####################################
###########################################################################################

# login form used to create the login form fields and data validation
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=50, message = "Username should be 4 to 50 characters long")])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=90, message = "Password should be atleast 8 characters long")])
    remember = BooleanField("Keep me signed in")

# registration form to create the form fields and data validation
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired("Please enter your email address"), Email("Invalid email address"), Length(max=50, message = "Max email address length is 50 characters")])
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=50, message = "Username should be 4 to 50 characters long")])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=90, message = "Password should be atleast 8 characters long")])


# admin login form used to create form fields for the admin login page
class AdminLoginForm(FlaskForm):
    username = StringField("Admin name", validators=[InputRequired(), Length(min=4, max=50, message = "Admin name should be 4 to 50 characters long")])
    password = PasswordField("Admin password", validators=[InputRequired(), Length(min=8, max=90, message = "Admin Password should be atleast 8 characters long")])
    remember = BooleanField("Keep me signed in")


# new admin addition form
class AdminAdditionForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=50, message = "Admin name should be 4 to 50 characters long")])
    email = StringField("Email", validators=[InputRequired("Please enter your email address"), Email("Invalid email address"), Length(max=50, message = "Max email address length is 50 characters")])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=90, message = "Admin Password should be atleast 8 characters long")])

###########################################################################################
##########################              ROUTES         ####################################
###########################################################################################

# index route or home page route
@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return render_template("index.html", page_title="Home Page")

# route to the stats page
@app.route('/stats')
def stats():
    # Number of users
    user_count = User.query.count()
    # Number of users who attempted the test
    unattempted_user_count = User.query.filter(User.attempt == 0).count()
    # Number of users who completed the test is the sum of zero and non zero scorers
    zero_score_users = User.query.filter(User.attempt != 0).filter_by(score = 0).count()
    nonzero_score_users = User.query.filter(User.attempt != 0).filter(User.score != 0).count()

    return render_template('stats.html', page_title = "Stats", user_count = user_count, unattempted_user_count = unattempted_user_count, zero_score_users = zero_score_users, nonzero_score_users = nonzero_score_users)

# --------------- LOGIN/LOGOUT ROUTES------------- #

# login route to access login form
@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for("dashboard"))
            else:
                flash("Wrong password. Please try again.")
                return redirect(url_for('login'))
        else:
            flash("Account doesn't exist. Please register before logging in.")
            NonExistentUser = True
            return redirect(url_for('login'))
    else:
        if(len(list(form.errors.values())) > 0):
            flash(list(form.errors.values())[0][0])
    return render_template("login.html", page_title="Login", form=form)


# logout route - can be accessed by only logged in users and logs the user out when accessed
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are logged out")
    return redirect(url_for('index'))

# signup route to access the signup page
@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        usernamecheck = User.query.filter_by(username = form.username.data).first()
        useremailcheck = User.query.filter_by(email=form.email.data).first()
        if not useremailcheck and not usernamecheck:
            # sha256 method generates a password that is 80 characters long but is adding some extra characters when hosted on heroku
            # this is the reason why the password field was made 90 (80 +10 chars for better hosting on heroku) characters long
            hashed_password = generate_password_hash(form.password.data, method = "sha256")
            new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
        else:
            flash("User account already exists")
            return redirect(url_for('signup'))
        
        # flashing the success message to the user
        flash("Your account is successfully created ! Please Login to continue.")
        return redirect(url_for('signup'))
    else:
        if(len(list(form.errors.values())) > 0):
            flash(list(form.errors.values())[0][0])

    return render_template("signup.html", page_title="Signup", form=form)


# dashboard route - can be accessed only after logging in
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", page_title = "Dashboard", name = current_user.username.lower().capitalize())

###########################################################################################
##########################          ADMIN ROUTES       ####################################
###########################################################################################

# admin login route
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()

    if form.validate_on_submit():
        print("Entered form validation")
        admin = Admin.query.filter_by(username = form.username.data).first()
        if admin:
            print("Entered the admin if condition")
            if check_password_hash(admin.password, form.password.data):
                login_user(admin, remember=form.remember.data)
                print("Current admin info : ", current_user.username)
                return redirect(url_for("admin_dashboard"))
            else:
                flash("Wrong password. Please try again.")
                return redirect(url_for('admin_login'))
        else:
            flash("Admin account doesn't exist. Please contact help center.")
            return redirect(url_for('admin_login'))
    else:
        if(len(list(form.errors.values())) > 0):
            flash(list(form.errors.values())[0][0])
    return render_template("admin_login.html", page_title="Admin Login", form=form)


# admin_dashboard route - can be accessed only after loggin in with admin creds
@app.route("/admin_dashboard", methods = ['GET', 'POST'])
@login_required
def admin_dashboard():
    form = AdminAdditionForm()

    if form.validate_on_submit():
        adminUsernameCheck = Admin.query.filter_by(username = form.username.data).first()
        adminEmailCheck = Admin.query.filter_by(email = form.email.data).first()
        if not adminUsernameCheck and not adminEmailCheck:
            hashed_password = generate_password_hash(form.password.data, method = "sha256")
            new_admin = Admin(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_admin)
            db.session.commit()
            flash("New admin has been added to the database")
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Not a unique admin name or admin email")
            return redirect(url_for('admin_dashboard')) 
    else:
        if(len(list(form.errors.values())) > 0):
            flash(list(form.errors.values())[0][0])
            return redirect(url_for('admin_dashboard'))

    # passing user info
    data = User.query.all()
    userlist = []
    
    for users in data:
        userlist.append([users.username, users.email, users.attempt, users.score])
    return render_template("admin_dashboard.html", page_title = "Admin Dashboard", userlist=userlist, form = form)


@app.route("/admin_delete_user", methods = ['GET', 'POST'])
@login_required
def admin_delete_user():
    if request.method == 'POST':
        print("printing username")
        del_username = list(request.form.keys())[0]
        print(del_username)
        print("deleting " + del_username)
        selectedUser = User.query.filter_by(username = del_username).first()
        db.session.delete(selectedUser)
        db.session.commit()
        print("redirecting")
    return redirect(url_for('admin_dashboard'))


@app.route("/admin_delete_database", methods = ['GET', 'POST'])
@login_required
def admin_delete_database():
    if request.method == 'POST':
        if  list(request.form.keys())[0] == 'delete-db':
            userdata = User.query.all()
            for eachUser in userdata:
                db.session.delete(eachUser)
        db.session.commit()
    return redirect(url_for('admin_dashboard'))



# ROUTING FOR ADMIN HTML
@app.route('/admin_logout')
@login_required
def admin_logout():
    logout_user()
    flash("Admin is logged out")
    return redirect(url_for('index'))


# ROUTING FOR EXERCISE HTML
@app.route("/exercises")
@login_required
def exercises():
    return render_template("exercises.html", page_title = "Exercises", name = current_user.username.lower().capitalize())


# ROUTING FOR QUIZ HTML
@app.route('/quiz', methods=["GET", "POST"])
@login_required
def quiz():
    user = User.query.get(current_user.id)
    if request.method =="POST":        
        print("Saving Results to DB")
        for key in request.form.keys():
            data = key
        results = json.loads(data)['output']
        user.attempt += 1
        user.correct = results[2]
        user.wrong = results[3]
        user.score = round(user.correct/results[0],2)
        db.session.add(user)
        db.session.commit()
        resp_dic={'msg':"Results Saved."}
        resp = jsonify(resp_dic)      
        return resp        
    else:

        return render_template("quiz.html",name = current_user.username.lower().capitalize(),page_title = "Quiz", TotalAttempt= user.attempt, pWrong = user.wrong , pCorrect= user.correct, pScore = user.score)



@app.route('/<page_name>')
def error(page_name):
    return render_template("error.html", page_title = "Error",  page_name = page_name)

###########################
# running the app.py script
###########################

if __name__ == "__main__":
    app.run(debug=True)
