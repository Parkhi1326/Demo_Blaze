import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

monitor=driver.find_element(By.XPATH,"//*[text()='Monitors']").click()

asus=driver.find_element(By.XPATH,"//*[text()='ASUS Full HD']").click()
time.sleep(2)
add=driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()
time.sleep(2)
alert=driver.switch_to.alert
alert.accept()
time.sleep(2)

driver.back()
driver.back()
apple=driver.find_element(By.XPATH,"//*[text()='Apple monitor 24']").click()
time.sleep(2)
add=driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()
time.sleep(2)

alert=driver.switch_to.alert
alert.accept()
time.sleep(2)