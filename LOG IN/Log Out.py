import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

log_in=driver.find_element(By.ID,"login2").click()
username=driver.find_element(By.ID,"loginusername").send_keys("Parkhi")
time.sleep(2)
password=driver.find_element(By.ID,"loginpassword").send_keys("Parkhi@123")
time.sleep(2)
login=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
time.sleep(5)

logout=driver.find_element(By.XPATH,"//a[@id='logout2']").click()
time.sleep(5)