# CITS5505_Agile_Web_Application
Repo for collaborating on the CITS5508 Project 2 to build a responsive tutorial web application

## Contributors:
- Akhil Eaga (22859584)
- Arjun Panicker (22954837)

# Front-End Technologies:
- HTML
- CSS
- JavaScript
- Boostrap
- jQuery
- Flexbox

# Back-End Technologies
- Flask
- Jinja
- SQLAlchemy
- Python 
- DOM
- AJAX

A full list of all the modules and libraries used for the developement of this project is available in the requirements.txt file available within this repo. 

For this project we took a simple and straightforward approach of keeping all the routes, forms and datamodels all in one place to speed up the development and debugging process.

The HTML files are kept in a folder named "templates" with each page named after the section/feature of the app that it represents. The CSS files, JS files and the images are kept in placed in their respective folders under the static directory. The app.py which is the main script and the templates folder and static folder are all in the same level of hierarchy.

# Launching the application:
- For the app to run, it needs an instance of the database. 
- To instantiate the database, the "setupdatabase.py" script should be run once
- Then the application can be launched by executing the app.py file using the "python app.py" for windows and an equivalent command for MacOS.


# Features:
## Admin features:
- Admin login
- Addition of more admins
- Deletion of all data from the database
- Removal of an individual user

## User features:
- User signup and login
- User dasboard
- Access to learning materials through the Exercises page
- User Assessments
- Feedback on the assessment taken
- Ability to view the result of the latest test
- Access to some anonymised statistics to encourage viewer to subscriber conversion.


# Testing:
- Unit tests and selenium tests are performed to make sure the features are working as expected.
- Scripts for the tests can be found in the respective directories within the repo.


# Unique Features:
- The app has been designed the pique the user's attention and interest
- The app is made interactive with the use of flash messages and instant feedback to keep the user engaged
- The app is responsive to multiple device sizes due to the usage of Boostrap containers and flexbox. 


# Design and Development:
- The design process of the application used agile methodology keeping a working version of the app at any stage. 
- It was writtten in parts to keep the code manageable and maintainable at all stages of the development
- Additional features can be added with relative ease due to the simple architecture used for the design of the app
- Significant importance was given to styling the web app to give a overall consistent yet familiar and distinctive feel to gain user's trust


# P.S:
Please download the repo and give it a try.

Feedback and feature suggestions can be sent to akhil.bitsian2013@gmail.com


Thank and regards,
Akhil Eaga
Arjun Panicker



