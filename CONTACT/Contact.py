import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/index.html")
driver.implicitly_wait(5)
driver.maximize_window()

contact=driver.find_element(By.XPATH,"//*[text()='Contact']").click()
time.sleep(2)
email=driver.find_element(By.ID,"recipient-email").send_keys("parkhigera@gmail.com")
time.sleep(2)
name=driver.find_element(By.ID,"recipient-name").send_keys("Parkhi")
time.sleep(2)
message=driver.find_element(By.ID,"message-text").send_keys("hello everyone")
time.sleep(2)
send=driver.find_element(By.XPATH,"//*[text()='Send message']").click()
# close=driver.find_element(By.XPATH,"//*[text()='Close']").click()
alert=driver.switch_to.alert
alert.accept()
# alert.dismiss()
time.sleep(2)