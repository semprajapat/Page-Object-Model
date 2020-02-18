from selenium import webdriver
import sys
import unittest
# from pages.loginPage import LoginPage
# from pages.homePage import HomePage

sys.path.insert(1, '/home/ltpl/Desktop/selenium/page_object_model/pages')
from loginPage import LoginPage
from homePage import HomePage

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        path = "../geckodriver"
        self.driver = webdriver.Firefox(executable_path =path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password('admin123')
        login.click_login()
        home = HomePage(driver)
        home.click_welcome()

    def tearDown(self):
        self.driver.close()
        print("test completed")


if __name__ == '__main__':
    unittest.main()