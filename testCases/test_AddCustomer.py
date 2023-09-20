import pytest
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
from selenium import webdriver
from pageObjects.loginPage import Login

class Test_003_AddCutomer:

    

    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # from LogGen class calling logger method

    @pytest.mark.sanity
    def test_addCustom(self,setUp):
        self.logger.info("*********** Test_003_AddCustomer************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        #creating obj of page obj class to access the methods 
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login successful*************")

        self.logger.info("**** Starting Add Custoemr Test*******")


    