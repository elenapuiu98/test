from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#open Chrome
driver = webdriver.Chrome()
#open Sensix page
driver.get("https://dev-app.sensix.io/")
#assert that the correct page has been opened
assert "Sensix" in driver.title
#input email address
email = driver.find_element_by_id("email")
email.clear()
email.send_keys("puiubiancaelena@gmail.com")
#input password
password = driver.find_element_by_id("password")
password.clear()
password.send_keys("temp4elena")
password.send_keys(Keys.RETURN)
#find the "Workspace" dropdown
driver.implicitly_wait(3)  # seconds
#workspace=driver.find_elements_by_css_selector("div[class='Iconstyle__Container-wbc9rb-0 bevhRj'] ["
#                                               "style='display:block']").click()
workspace=driver.find_elements_by_xpath("//div[@class='DropdownTogglestyle__Toggle-v1w2zb-0 losrgG']")
driver.implicitly_wait(3)
workspace.click()
