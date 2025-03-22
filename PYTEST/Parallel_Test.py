from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
class TestClass:
    @pytest.mark.parametrize("username,passwd",[("Admin","admin123"),("Parkhi","admin123"),("Admin","Admin"),("Parkhi","Parkhi@123")])
    def test_login(self,username,passwd):
        driver=webdriver.Chrome()
        driver.get("https://www.demoblaze.com/index.html")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.find_element(By.ID, "login2").click()
        driver.find_element(By.ID,"loginusername").send_keys(username)
        driver.find_element(By.ID,"loginpassword").send_keys(passwd)
        driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()

        try:
            text=driver.find_element(By.ID,"nava").text
            assert text=="PRODUCT STORE"
        except:
            driver.close()
            assert False
            #last case passed rest cases failed