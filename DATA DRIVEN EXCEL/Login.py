import os
import time
import openpyxl

from selenium.webdriver.common.by import By
import XLUtils
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.implicitly_wait(5)
driver.maximize_window()

file=os.getcwd()+r"\Login.xlsx"
rows=XLUtils.getRowCount(file,"Sheet1")
login=driver.find_element(By.ID,"login2").click()
time.sleep(2)

for r in range(2,rows+1):
    username=XLUtils.readData(file,"Sheet1",r,1)
    password=XLUtils.readData(file,"Sheet1",r,2)

    driver.find_element(By.ID,"loginusername").clear()
    driver.find_element(By.ID,"loginusername").send_keys(username)
    driver.find_element(By.ID,"loginpassword").clear()
    driver.find_element(By.ID,"loginpassword").send_keys(password)

    login=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
    time.sleep(2)

    try:
        alert=driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        XLUtils.writeData(file,"Sheet1",r,4,"Fail")
        XLUtils.fillRedColor(file,"Sheet1",r,4)
    except:
        XLUtils.writeData(file,"Sheet1",r,4,"Pass")
        XLUtils.fillGreenColor(file,"Sheet1",r,4)