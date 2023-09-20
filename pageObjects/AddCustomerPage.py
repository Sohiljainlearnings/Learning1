import time
from selenium import webdriver
from selenium.webdriver.support import select
import pytest



class AddCustomer():

    


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomer_menu_item_xpath).click()