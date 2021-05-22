from re import S
import unittest
from unittest import mock

from werkzeug.wrappers import response
from app import *
from flask_testing import TestCase

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config["SECRET_KEY"] = "mysecretkey"
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "test.db")
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.app = app.test_client(self)
        db.create_all()
        User1 = User(username="myusername1",email="test1@test1.com",password="testpassword1")
        User2 = User(username="myusername2",email="test1@test2.com",password="testpassword2")
        User3 = User(username="myusername3",email="test1@test3.com",password="testpassword3")
        admin = Admin(username="admin",email="admin@admin.com",password="adminadmin")
        db.session.add(User1)
        db.session.add(User2)
        db.session.add(User3)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        # check if html loads properly
    def test_html_response(self):
        response1 = app.test_client(self).get("/index",content_type ='html/index')
        response2 = app.test_client(self).get("/login",content_type ='html/login')
        response3 = app.test_client(self).get("/quiz",content_type ='html/quiz')
        response4 = app.test_client(self).get("/admin_dashboard",content_type ='html/admin_dashboard')
        response6 = app.test_client(self).get("/admin_login",content_type ='html/admin_login')
        response7 = app.test_client(self).get("/dashboard",content_type ='html/dashboard')
        response8 = app.test_client(self).get("/error",content_type ='html/error')
        response9 = app.test_client(self).get("/excercises",content_type ='html/excercises')
        response10 = app.test_client(self).get("/signup",content_type ='html/signup')

        # 302 redirect, #200 success
        self.assertEqual(response1.status_code,200)
        self.assertEqual(response2.status_code,200)
        self.assertEqual(response3.status_code,302)
        self.assertEqual(response4.status_code,302)
        self.assertEqual(response6.status_code,200)
        self.assertEqual(response7.status_code,302)
        self.assertEqual(response8.status_code,200)
        self.assertEqual(response9.status_code,200)
        self.assertEqual(response10.status_code,200)

        # test user load function.
    def test_load_user(self):
        user1 = User.query.get(1)
        self.assertEqual(load_user(1), user1)

    
if __name__ == '__main__':
    unittest.main()
