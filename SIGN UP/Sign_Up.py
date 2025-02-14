import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

sign_up=driver.find_element(By.ID,"signin2").click()
name=driver.find_element(By.ID,"sign-username").send_keys("Parkhi")
password=driver.find_element(By.ID,"sign-password").send_keys("Parkhi@123")
time.sleep(2)
sign_up=driver.find_element(By.XPATH,"//button[normalize-space()='Sign up']").click()
# close=driver.find_element(By.XPATH,"//*[text()='Close']").click()
time.sleep(2)

alert=driver.switch_to.alert
alert.accept()
time.sleep(2)