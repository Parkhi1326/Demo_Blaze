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
rows=XLUtils.getRowCount(file,"Sheet2")
sign_up=driver.find_element(By.ID,"signin2").click()
time.sleep(2)

for r in range(2,rows+1):
    username=XLUtils.readData(file,"Sheet2",r,1)
    password=XLUtils.readData(file,"Sheet2",r,2)

    driver.find_element(By.ID,"sign-username").clear()
    driver.find_element(By.ID,"sign-username").send_keys(username)
    driver.find_element(By.ID,"sign-password").clear()
    driver.find_element(By.ID,"sign-password").send_keys(password)

    sign_up = driver.find_element(By.XPATH, "//button[normalize-space()='Sign up']").click()
    time.sleep(2)

    try:
        alert=driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        XLUtils.writeData(file,"Sheet2",r,4,"Fail")
        XLUtils.fillRedColor(file,"Sheet2",r,4)
    except:
        XLUtils.writeData(file,"Sheet2",r,4,"Pass")
        XLUtils.fillGreenColor(file,"Sheet2",r,4)