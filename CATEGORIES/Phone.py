import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

phone=driver.find_element(By.XPATH,"//*[text()='Phones']").click()
time.sleep(2)
samsung=driver.find_element(By.XPATH,"//*[text()='Samsung galaxy s7']").click()
time.sleep(2)
add=driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()
time.sleep(2)

alert=driver.switch_to.alert
alert.accept()
time.sleep(2)