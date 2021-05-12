import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# base directory - the directory where "this" file resides in the host computer
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
    quiz_answers = db.Column(db.String())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.quiz_answers = ""

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# FORMS

# login form used to create the login form fields and data validation
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15, message = "Username should be 4 to 15 characters long")])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=80, message = "Password should be atleast 8 characters long")])
    remember = BooleanField("Remember me")

# registration form to create the form fields and data validation
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired("Please enter your email address"), Email("Invalid email address"), Length(max=50, message = "Max email address length is 50 characters")])
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15, message = "Username should be 4 to 15 characters long")])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=80, message = "Password should be atleast 8 characters long")])

# quiz question forms to create the form fields and data validation
class QuizForm(FlaskForm):
    # question labels
    question1_label = "1. What character do you use to search for results that relate to social media platforms?"
    question2_label = "2. How would you search the trend 'helloworld'?"
    question3_label = "3. How would you search for 'jaguar' by excluding the word 'car' from the search results ?"
    question4_label = "4. If you want to search for the exact phrase of 'agile methodology', what would your search criteria will look like?"
    question5_label = "5. Let's say you want to search for all the content posted by Rihanna, specifically on youtube.com. How would you phrase your search ?"
    question6_label = "6. Consider the situation where you want to know how popular Akhil Eaga is. So you decided to find all the sites on the web that link to Akhil's website akhileaga.com.au . How would you search for this ?"
    question7_label = "7. Your friend Arjun is a Netflix fan. So he watched all the shows on netflix. Now that he had watched all the shows on netflix, he came to you for recommendations on sites that are similar to netflix.com. You being a serious student, don't know any of similar sites. However, you decided to help Arjun. How would you search for sites similar to netflix.com ?"
    question8_label = "8. You ran into a situation where you want to search for all the pages that have either 'Microbiology' or 'Nanotechnology' in them. What special word do you use to join those two search terms ?"
    question9_label = "9. What special phrase do you add at the end of your search criteria to look for 'docx' file type ?"
    question10_label = "10. You went to your friend's house for a party and listened to song which you liked it very much. But after coming home you forgot the second word of the song. You only remember the first word 'supermarket'. How would you search for the song ?"

    
    # questions
    question1 = StringField(question1_label, validators=[InputRequired("Please answer this question"), Length(min=1, max=1, message ="Please input only one character for question 1")])
    
    question2 = StringField(question2_label, validators=[InputRequired("Please answer this question"), Length(min=11, max=11, message ="Please input exactly 11 characters for question 2")])

    question3 = StringField(question3_label, validators=[InputRequired("Please answer this question"), Length(min=11, max=11, message ="Please input exactly 11 characters for question 3")])

    question4 = StringField(question4_label, validators=[InputRequired("Please answer this question"), Length(min=19, max=19, message ="Please input exactly 19 characters for question 4")])

    question5 = StringField(question5_label, validators=[InputRequired("Please answer this question"), Length(min=24, max=24, message ="Please input exactly 24 characters for question 5")])

    question6 = StringField(question6_label, validators=[InputRequired("Please answer this question"), Length(min=21, max=21, message ="Please input exactly 21 characters for question 6")])

    question7 = StringField(question7_label, validators=[InputRequired("Please answer this question"), Length(min=19, max=19, message ="Please input exactly 19 characters for question 7")])

    question8 = StringField(question8_label, validators=[InputRequired("Please answer this question"), Length(min=2, max=2, message ="Please input exactly 2 characters for question 8")])

    question9 = StringField(question9_label, validators=[InputRequired("Please answer this question"), Length(min=13, max=13, message ="Please input exactly 13 characters for question 9")])
    
    question10 = StringField(question10_label, validators=[InputRequired("Please answer this question"), Length(min=13, max=13, message ="Please input exactly 13 characters for question 10")])


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
    else:
        if(len(list(form.errors.values())) > 0):
            flash(list(form.errors.values())[0][0])
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
    else:
        if(len(list(form.errors.values())) > 0):
            flash(list(form.errors.values())[0][0])
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

@app.route('/quiz', methods=["GET", "POST"])
@login_required
def quiz():
    form = QuizForm()
    if form.validate_on_submit():
        answers = [form.question1.data, form.question2.data, form.question3.data, form.question4.data, form.question5.data, form.question6.data, form.question7.data, form.question8.data, form.question9.data, form.question10.data]
        
        # __sep__ is used as the separator to join the answers into a string
        answers = "__sep__".join(answers)
        # user = User.query.filter_by(username = current_user.username).first()
        user = User.query.get(current_user.id)
        user.quiz_answers = answers
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('feedback'))
    else:
        if(len(list(form.errors.values())) > 0):
            flash(list(form.errors.values())[0][0])
    
    return render_template("quiz.html", form = form, page_title = "Quiz", name = current_user.username.lower().capitalize(), quiz_progress = current_user.quiz_answers.split("__sep__"))

@app.route('/feedback')
@login_required
def feedback():
    # question labels
    question1_label = "1. What character do you use to search for results that relate to social media platforms?"
    question2_label = "2. How would you search the trend 'helloworld'?"
    question3_label = "3. How would you search for 'jaguar' by excluding the word 'car' from the search results ?"
    question4_label = "4. If you want to search for the exact phrase of 'agile methodology', what would your search criteria will look like?"
    question5_label = "5. Let's say you want to search for all the content posted by Rihanna, specifically on youtube.com. How would you phrase your search ?"
    question6_label = "6. Consider the situation where you want to know how popular Akhil Eaga is. So you decided to find all the sites on the web that link to Akhil's website akhileaga.com.au . How would you search for this ?"
    question7_label = "7. Your friend Arjun is a Netflix fan. So he watched all the shows on netflix. Now that he had watched all the shows on netflix, he came to you for recommendations on sites that are similar to netflix.com. You being a serious student, don't know any of similar sites. However, you decided to help Arjun. How would you search for sites similar to netflix.com ?"
    question8_label = "8. You ran into a situation where you want to search for all the pages that have either 'Microbiology' or 'Nanotechnology' in them. What special word do you use to join those two search terms ?"
    question9_label = "9. What special phrase do you add at the end of your search criteria to look for 'docx' file type ?"
    question10_label = "10. You went to your friend's house for a party and listened to song which you liked it very much. But after coming home you forgot the second word of the song. You only remember the first word 'supermarket'. How would you search for the song ?"

    question_labels = [question1_label, question2_label, question3_label, question4_label, question5_label, question6_label, question7_label, question8_label, question9_label, question10_label]

    user_answers = User.query.get(current_user.id).quiz_answers
    user_answers = user_answers.lower().split("__sep__")
    actual_answers = ["@", "#helloworld", "jaguar -car", '"agile methodology"', "rihanna site:youtube.com", "link:akhileaga.com.au", "related:netflix.com", "or", "filetype:docx", "supermarket *"]

    score = 0
    boolean_score = []
    for index in range(len(user_answers)):
        if user_answers[index] == actual_answers[index]:
            score = score + 1
            boolean_score.append("Correct")
        else:
            boolean_score.append("Wrong")

    return render_template("feedback.html", page_title = "Feedback", name = current_user.username.lower().capitalize(), user_answers = user_answers, actual_answers = actual_answers, score = score, boolean_score = boolean_score, question_labels = question_labels)

@app.route('/<page_name>')
def error(page_name):
    return render_template("error.html", page_title = "Error",  page_name = page_name)

# running the app.py script
if __name__ == "__main__":
    app.run(debug=True)
