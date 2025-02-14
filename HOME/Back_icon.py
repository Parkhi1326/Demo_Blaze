import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

back=driver.find_element(By.CLASS_NAME,"carousel-control-prev-icon").click()
time.sleep(2)