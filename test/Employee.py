from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\k_sur\Downloads\chromedriver.exe")

driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.switch_to.frame("f3")
driver.switch_to.frame("f4")

# to switch the parent frame
driver.switch_to.parent_frame()
driver.switch_to.parent_frame()
driver.switch_to.parent_frame()

# redirect to web page
driver.switch_to.default_content()
