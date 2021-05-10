import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# base directory - the directory where this file resides in the host computer
basedir = os.path.abspath(os.path.dirname(__file__))

# app initialization and configuration settings
app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "database.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# database initialization, connection and the login manager configuration
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Database model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique = True)
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(80))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# FORMS

# login form used to create the login form fields and data validation
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField("Remember me")

# Email("This field requires a valid email address"),
# registrattion form to create the form fields and data validation
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired("Please enter your email address"), Email("This field requires a valid email address"), Length(max=50)])
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=80)])

# ROUTES

# index route or home page route
@app.route('/')
def index():
    return render_template("index.html", page_title="Home Page")

# login route to access login form
@app.route('/login', methods=["GET", "POST"])
def login():
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
            return redirect(url_for('login'))
            
    return render_template("login.html", page_title="Login", form=form)

# signup route to access the signup page
@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        usernamecheck = User.query.filter_by(username = form.username.data).first()
        useremailcheck = User.query.filter_by(email=form.email.data).first()
        if not useremailcheck and not usernamecheck:
            # sha256 method generates a password that is 80 characters long
            # this is the reason why the password field was made 80 characters long
            hashed_password = generate_password_hash(form.password.data, method = "sha256")
            new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
        else:
            flash("User account already exists")
            return redirect(url_for('signup'))
        
        # flashing the success message to the user
        flash("Your account is successfully created !")
        return redirect(url_for('signup'))

    return render_template("signup.html", page_title="Signup", form=form)


# dashboard route - can be accessed only after logging in
# this view is protected and cannot be accessed without logging in
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", page_title = "Dashboard", name = current_user.username.lower().capitalize())


# logout route - can be accessed by only logged in users and logs the user out when accessed
@app.route('/logout')
@login_required
def logout():
    # ---------------- before logging out the user save the quiz data into the database ------------------
    logout_user()
    flash("You are logged out")
    return redirect(url_for('index'))

@app.route("/exercises")
@login_required
def exercises():
    return render_template("exercises.html", page_title = "Exercises", name = current_user.username.lower().capitalize())

@app.route('/quiz')
@login_required
def quiz():
    return render_template("quiz.html", page_title = "Quiz", name = current_user.username.lower().capitalize())

@app.route('/<page_name>')
def error(page_name):
    return render_template("error.html", page_title = "Error",  page_name = page_name)
# running the app.py script
if __name__ == "__main__":
    app.run(debug=True)
