import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

lists=driver.find_elements(By.CLASS_NAME,"col-lg-3")
for i in lists:
    print(i.text)
time.sleep(2)