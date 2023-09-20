import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.excelUtilitiesfile import excelUtilitiesfile 
import time


class Test_001_login_ddt:

    baseUrl = ReadConfig.getApplicationUrl()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen() # from LogGen class calling logger method

    
    def test_login_ddt(self,setUp):

        self.logger.info("*********Verifying Login DDT--1  test********************")
        self.driver = setUp
        self.driver.get(self.baseUrl)

        #creating obj of page obj class to access the methods 
        self.lp = Login(self.driver)

        self.rows = excelUtilitiesfile.getRowCount(self.path,"Sheet1")
        print("Number of rows in excel ",self.rows)

        for r in range(2, self.rows+1):
            self.user = excelUtilitiesfile.readData(self.path,"Sheet1",r,1)
            self.password= excelUtilitiesfile.readData(self.path,"Sheet1",r,2)
            self.exp= excelUtilitiesfile.readData(self.path,"Sheet1",r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.slee(5)

            act_title = self.driver.title
            exp_tile= "Dashboard / nopCommerce administration"

            if act_title == exp_tile:
                if self.exp =="Pass":
                    self.logger.info("*** Passed")
                    self.lp.clickLogout();



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

