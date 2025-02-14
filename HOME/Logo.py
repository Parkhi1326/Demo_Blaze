import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

logo=driver.find_element(By.ID,"nava")
print(logo.is_displayed())
time.sleep(2)