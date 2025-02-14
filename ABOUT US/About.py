import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

about=driver.find_element(By.XPATH,"//a[normalize-space()='About us']").click()
time.sleep(2)
table=driver.find_element(By.CLASS_NAME,"vjs-poster").click()
time.sleep(10)
close_btn=driver.find_element(By.XPATH,"//*[@id='videoModal']/div/div/div[3]/button").click()
time.sleep(2)