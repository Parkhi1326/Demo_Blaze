import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

home=driver.find_element(By.XPATH,"//*[text()='Home ']").click()
time.sleep(2)