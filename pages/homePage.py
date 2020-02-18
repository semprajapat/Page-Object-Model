import sys

sys.path.insert(1, '/home/ltpl/Desktop/selenium/page_object_model/locators')
from locator import Locators

class HomePage():
    
    def __init__(self,driver):
        self.driver = driver,
        self.welcome_link_id = Locators.welcome_link_id,
        self.logout_link_id = Locators.logout_link_id

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click() 

    def click_logout(self):
        self.driver.find_element_by_id(self.logout_link_id).click()