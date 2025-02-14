import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

cart=driver.find_element(By.XPATH,"//*[text()='Cart']").click()
place_order=driver.find_element(By.XPATH,"//*[text()='Place Order']").click()
time.sleep(2)

name=driver.find_element(By.ID,"name").send_keys("Parkhi")
country=driver.find_element(By.ID,"country").send_keys("India")
city=driver.find_element(By.ID,"city").send_keys("Kurukshetra")
credit_card=driver.find_element(By.ID,"card").send_keys("123456789")
month=driver.find_element(By.ID,"month").send_keys("02")
year=driver.find_element(By.ID,"year").send_keys("2024")
purchase=driver.find_element(By.XPATH,"//*[text()='Purchase']").click()
time.sleep(2)