import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_login:
    # baseUrl = "https://admin-demo.nopcommerce.com/login"
    # username = "admin@yourstore.com"
    # password = "admin"

    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # from LogGen class calling logger method


    
    @pytest.mark.regression
    def test_HomePageTitle(self,setUp):


        self.logger.info("************Test_Login*****************************")
        self.logger.info("*********Verifying Homepage title********************")
        self.driver = setUp  # as we have created in conftest file
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()

        if act_title == "Your store Login":
            assert True
            self.driver.close()
            self.logger.info("********Passed *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" +"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("********Failed*********************")
            assert False
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setUp):

        self.logger.info("*********Verifying Login test********************")
        self.driver = setUp
        self.driver.get(self.baseUrl)

        #creating obj of page obj class to access the methods 
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_login = " Dashboard..............."
        self.driver.close()

        if act_login ==" Dashboard...............":
            assert True
            self.logger.info("****************login test passed***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" +"test_login.png")
            self.logger.error("****************login test passed***********")
            self.driver.close()
            assert False

