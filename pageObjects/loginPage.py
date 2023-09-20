from selenium import webdriver
from webdriver_manager import drivers

class Login:
    textbox_username_id = "Email"
    textbox_password_name = "Password"
    button_login_xpath= "//button[@type='submit']"
    link_logout_linkedText = "Logout"

    def __init__(self,driver):       
        self.driver = driver # class variable

    #action methods

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys("admin@yourstore.com")

    def setPassword(self,password):
        self.driver.find_element_by_Name(self.textbox_password_name).send_keys("admin")

    def clickLogin(self):
        self.driver.find_element_by_Xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_Xpath(self.link_logout_linkedText).click()