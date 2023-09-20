from selenium import webdriver


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("gmail.com")
print("Application title:",driver.title)
driver.quit()
