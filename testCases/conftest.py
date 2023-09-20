from selenium import webdriver
import pytest
from html import parser,__all__


# for common elements in  test cases we create conftest file and mention in fixture
@pytest.fixture()
def setUp(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser.........!!")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser.........!!")
    else:
        driver = webdriver.Ie()
        print("As no broser is provide , running on default browser ,IE")
    return driver

def pytest_addoption(parser): # this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this method will return the  Browser value to setup method
    return request.config.getoption("--browser")

    #----------HTML REPORTS=============================

# its a hook for adding environment info to html rports
def pytest_configure(config):
    config._metadata['Project Name'] == 'nop commerce'
    config._metadata['Module Name'] == 'Customers'
    config._metadata['Tester'] == 'SOhil'

# It is hook for delete /Modify Environment info to HTML Report

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
