import sys

sys.path.insert(1, '/home/ltpl/Desktop/selenium/page_object_model/locators')
from locator import Locators

class LoginPage():
    
    def __init__(self,driver):
        self.driver = driver
    
        self.username_id = Locators.username_id,
        self.password_id =Locators.password_id,
        self.login_id = Locators.login_id,
    
    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)
    
    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_id).click()
        