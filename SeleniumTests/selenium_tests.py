# Generated by Selenium IDE
# modified by Arjun Panicker
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestApp():
  def setup_method(self, method,path):
    self.driver = webdriver.Chrome(path)
    self.vars = {}
    self.driver.set_window_size(1900, 1080)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_adminFetchUserDetails(self):
    self.driver.get("http://127.0.0.1:5000/")
    
    self.driver.find_element(By.LINK_TEXT, "Admin Login").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("admin1")
    self.driver.find_element(By.ID, "password").send_keys("adminadmin")
    self.driver.find_element(By.ID, "remember").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".container > h1").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".container > h1").text == "Welcome to admin dashboard"
    self.driver.find_element(By.CSS_SELECTOR, ".column-content > .btn-primary").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".user-info > h1").text == "User Information List"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".close-button-container > .btn")
    assert len(elements) > 0
  
  def test_adminLogin(self):
    self.driver.get("http://127.0.0.1:5000/")
    
    self.driver.find_element(By.LINK_TEXT, "Admin Login").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("admin1")
    self.driver.find_element(By.ID, "password").send_keys("adminadmin")
    self.driver.find_element(By.ID, "remember").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".container > h1").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".container > h1").text == "Welcome to admin dashboard"
  
  def test_adminLogout(self):
    self.driver.get("http://127.0.0.1:5000/")
    
    self.driver.find_element(By.LINK_TEXT, "Admin Login").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("admin1")
    self.driver.find_element(By.ID, "password").send_keys("adminadmin")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".btn").text == "Get started"
  
  def test_existingUserConflict(self):
    self.driver.get("http://127.0.0.1:5000/")
    
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("user@username.com")
    self.driver.find_element(By.ID, "username").send_keys("myusername")
    self.driver.find_element(By.ID, "password").send_keys("mypassword")
    self.driver.find_element(By.ID, "password").send_keys("mypassword")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    text = self.driver.find_element(By.CSS_SELECTOR, "h1").text
    assert text != "Welcome, Myusername"
  
  def test_existingUserWrongPassword(self):
    self.driver.get("http://127.0.0.1:5000")
    
    self.driver.find_element(By.LINK_TEXT, "User Login").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("myusername")
    self.driver.find_element(By.ID, "password").send_keys("wrongpassowrd")
    self.driver.find_element(By.ID, "remember").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".btn").text == "Sign in"
    text = self.driver.find_element(By.CSS_SELECTOR, "h1").text
    assert text != "Welcome, Myusername"
  
  def test_newUsershortpassword(self):
    self.driver.get("http://127.0.0.1:5000/")
    
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("username2@gmail.com")
    self.driver.find_element(By.ID, "username").send_keys("username2")
    self.driver.find_element(By.ID, "password").send_keys("short")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".btn").text == "Register"
    self.driver.find_element(By.CSS_SELECTOR, ".signuppage-form-container").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".errors > li")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".errors > li").text == "Password should be atleast 8 characters long"
    text = self.driver.find_element(By.CSS_SELECTOR, "h1").text
    assert text != "Welcome, Myusername"
  
  def test_userExcerices(self):
    self.driver.get("http://127.0.0.1:5000/")
    
    self.driver.find_element(By.LINK_TEXT, "User Login").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("myusername")
    self.driver.find_element(By.ID, "password").send_keys("mypassword")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Jump into learning").click()
    self.driver.find_element(By.CSS_SELECTOR, ".intro-slide .img-center").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-prev-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-indicators > li:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-indicators > li:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-indicators > li:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(7)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(10)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(11)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(12)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(11)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(10)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(7)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-indicators > li:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-indicators > li:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-indicators > li:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-indicators > li:nth-child(1)").click()/home/arjun/Desktop/chromedriver
    self.driver.find_element(By.NAME, "q").send_keys()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".intro-slide .gSearch-btn").click()
    self.vars["win2827"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win2827"])
    elements = self.driver.find_elements(By.NAME, "q")
    assert len(elements) > 0
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".carousel-control-next-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(11)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(12)").click()
    self.driver.find_element(By.LINK_TEXT, "Take the quiz").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".carousel-control-next-icon")
    assert len(elements) == 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".button-container:nth-child(6) > .btn:nth-child(1)")
    assert len(elements) > 0
  
  def test_userLoginSuccess(self):
    self.driver.get("http://127.0.0.1:5000/")
    
    self.driver.find_element(By.LINK_TEXT, "User Login").click()
    self.driver.find_element(By.ID, "username").send_keys("myusername")
    self.driver.find_element(By.ID, "password").send_keys("mypassword")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Welcome, Myusername"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".start-learning-link-container")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Jump into learning")
    assert len(elements) > 0
  
  def test_userLogoutSuccess(self):
    self.driver.get("http://127.0.0.1:5000/")
    
    self.driver.find_element(By.LINK_TEXT, "User Login").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("myusername")
    self.driver.find_element(By.ID, "password").send_keys("mypassword")
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Myusername\'s Dashboard").click()
    self.driver.find_element(By.LINK_TEXT, "Exercises").click()
    self.driver.find_element(By.LINK_TEXT, "Quiz").click()
    self.driver.find_element(By.LINK_TEXT, "HyperSearch").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".btn").text == "Get started"
  
  def test_userQuiz(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1920, 1080)
    self.driver.find_element(By.LINK_TEXT, "User Login").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("myusername")
    self.driver.find_element(By.ID, "password").send_keys("mypassword")
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    
    self.driver.find_element(By.LINK_TEXT, "Quiz").click()
    time.sleep(0.8)
    self.driver.find_element(By.CSS_SELECTOR, ".button-container:nth-child(6) > .btn:nth-child(1)").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "0").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "next-btn").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "2").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "next-btn").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "0").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "next-btn").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "2").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "next-btn").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "0").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "next-btn").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "2").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "next-btn").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "1").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "next-btn").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "2").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "next-btn").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "0").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "next-btn").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "2").click()
    time.sleep(0.8)
    self.driver.find_element(By.ID, "next-btn").click()
    time.sleep(0.8)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".result-box .btn:nth-child(2)")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".result-box .btn:nth-child(2)").text == "Dashboard"
  


  
if __name__ == '__main__':
    app = TestApp()
    
    path = input("Enter path of chrome driver: ")
    #start
    app.setup_method("",path)
    
    #admin tests
    app.test_adminFetchUserDetails()
    app.test_adminLogin()
    app.test_adminLogout()
    
    #existing user in database
    app.test_existingUserConflict()
    app.test_existingUserWrongPassword()
    app.test_existingUserWrongPassword()
    app.test_newUsershortpassword()
    
    #current user tests
    app.test_userExcerices()
    app.test_userLoginSuccess()
    app.test_userLogoutSuccess()
    app.test_userQuiz()    
    
    #quit
    app.teardown_method("")